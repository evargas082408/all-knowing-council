"""Validate and tally a complete council stage. Python 3, standard library only."""

import argparse
import json
import sys
from pathlib import Path


JURORS = {f"J{i:02d}" for i in range(1, 51)}
IDEAS = {f"I{i:02d}" for i in range(1, 11)}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def strings(value):
    return isinstance(value, list) and all(nonempty(item) for item in value)


def tally(data):
    require(isinstance(data, dict), "Stage must be a JSON object.")
    phase = data.get("phase")
    require(phase in ("rank", "accept"), "phase must be rank or accept.")
    version = data.get("proposal_version")
    require(nonempty(version), "Missing proposal_version.")
    ballots = data.get("ballots")
    require(isinstance(ballots, list) and len(ballots) == 50,
            "Exactly 50 ballots are required.")
    seen = set()
    for ballot in ballots:
        require(isinstance(ballot, dict), "Each ballot must be an object.")
        juror = ballot.get("juror_id")
        require(isinstance(juror, str) and juror in JURORS,
                f"Invalid juror ID: {juror!r}.")
        require(juror not in seen, f"Duplicate juror: {juror}.")
        seen.add(juror)
        require(ballot.get("proposal_version") == version,
                f"{juror}: stale or missing proposal_version.")
    require(seen == JURORS, "All J01-J50 must participate.")

    if phase == "rank":
        ids = data.get("idea_ids")
        require(isinstance(ids, list) and len(ids) == 10
                and all(isinstance(item, str) for item in ids)
                and set(ids) == IDEAS, "idea_ids must contain I01-I10 exactly once.")
        scores = {idea: {"idea_id": idea, "credits": 0,
                         "rank_points": 0, "first_place_count": 0}
                  for idea in sorted(IDEAS)}
        for ballot in ballots:
            juror = ballot["juror_id"]
            ranking = ballot.get("ranking")
            require(isinstance(ranking, list) and len(ranking) == 10
                    and all(isinstance(item, str) for item in ranking)
                    and set(ranking) == IDEAS,
                    f"{juror}: rank all I01-I10 exactly once.")
            credits = ballot.get("credits")
            require(isinstance(credits, dict) and set(credits) == IDEAS,
                    f"{juror}: provide credit values for every idea.")
            require(all(type(value) is int and 0 <= value <= 4
                        for value in credits.values()),
                    f"{juror}: credits must be integers between zero and four.")
            require(sum(credits.values()) == 4,
                    f"{juror}: allocate exactly four credits.")
            evaluations = ballot.get("evaluations")
            require(isinstance(evaluations, dict) and set(evaluations) == IDEAS
                    and all(nonempty(value) for value in evaluations.values()),
                    f"{juror}: give a reasoned evaluation for every idea.")
            require(strings(ballot.get("objections")),
                    f"{juror}: objections must be a list of nonempty strings (may be empty).")
            for index, idea in enumerate(ranking):
                scores[idea]["credits"] += credits[idea]
                scores[idea]["rank_points"] += 10 - index
                if index == 0:
                    scores[idea]["first_place_count"] += 1
        ordered = sorted(scores.values(), key=lambda score: (
            -score["credits"], -score["rank_points"],
            -score["first_place_count"], score["idea_id"]))
        return {"phase": phase, "proposal_version": version,
                "juror_count": 50, "total_credits": 200, "ranked_ideas": ordered}

    yes = []
    no = []
    for ballot in ballots:
        juror = ballot["juror_id"]
        vote = ballot.get("vote")
        require(vote in ("yes", "no"), f"{juror}: vote must be yes or no.")
        require(nonempty(ballot.get("rationale")), f"{juror}: give a rationale.")
        objections = ballot.get("blocking_objections")
        require(strings(objections), f"{juror}: blocking_objections must be a list.")
        if vote == "yes":
            require(not objections, f"{juror}: a yes cannot have blocking objections.")
            yes.append(juror)
        else:
            require(bool(objections), f"{juror}: a no requires a blocking objection.")
            no.append({"juror_id": juror, "rationale": ballot["rationale"],
                       "blocking_objections": objections})
    return {"phase": phase, "proposal_version": version, "juror_count": 50,
            "yes_count": len(yes), "no_count": len(no),
            "unanimous": len(yes) == 50, "audit_required": len(yes) == 50,
            "yes_jurors": sorted(yes), "dissent": sorted(no, key=lambda b: b["juror_id"])}


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f"Duplicate JSON key: {key}.")
        result[key] = value
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ballots", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.ballots.read_text(encoding="utf-8-sig"),
                          object_pairs_hook=unique_object)
        result = tally(data)
    except (OSError, ValueError, TypeError) as exc:
        print(json.dumps({"valid": False, "error": str(exc)}), file=sys.stderr)
        return 2
    print(json.dumps({"valid": True, **result}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
