#!/usr/bin/env python3
"""DevRel metrics calculator."""
import json

def calculate_metrics():
    return {
        "awareness": ["website_traffic", "social_followers", "newsletter_subs"],
        "engagement": ["api_calls", "github_stars", "community_activity"],
        "adoption": ["signups", "active_users", "time_to_first_value"],
        "retention": ["churn_rate", "nps_score", "repeat_usage"],
        "advocacy": ["referrals", "testimonials", "user_content"]
    }

if __name__ == "__main__":
    print(json.dumps(calculate_metrics(), indent=2))
