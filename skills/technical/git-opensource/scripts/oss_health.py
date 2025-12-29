#!/usr/bin/env python3
"""Open source project health checker."""
import json

def check_health():
    return {
        "files": ["README", "CONTRIBUTING", "LICENSE", "CODE_OF_CONDUCT", "CHANGELOG"],
        "metrics": ["stars", "forks", "issues", "prs", "contributors"],
        "community_health": ["response_time", "pr_merge_time", "issue_close_rate"],
        "governance": ["maintainers", "codeowners", "release_process"]
    }

if __name__ == "__main__":
    print(json.dumps(check_health(), indent=2))
