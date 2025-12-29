#!/usr/bin/env python3
"""Measure community health metrics."""
import json

def assess_health():
    return {
        "metrics": {
            "active_members": "Monthly active contributors",
            "response_time": "Average time to first response",
            "resolution_rate": "Issues resolved within SLA",
            "sentiment": "Community sentiment score"
        },
        "health_indicators": ["growth_rate", "retention", "engagement", "diversity"]
    }

if __name__ == "__main__":
    print(json.dumps(assess_health(), indent=2))
