#!/usr/bin/env python3
"""Social media content scheduler."""
import json

def create_schedule():
    return {
        "platforms": {
            "twitter": {"posts_per_day": 3, "best_times": ["9am", "12pm", "5pm"]},
            "linkedin": {"posts_per_week": 5, "best_days": ["tue", "wed", "thu"]},
            "youtube": {"videos_per_month": 4}
        },
        "content_mix": {"educational": 40, "engagement": 30, "promotional": 20, "personal": 10}
    }

if __name__ == "__main__":
    print(json.dumps(create_schedule(), indent=2))
