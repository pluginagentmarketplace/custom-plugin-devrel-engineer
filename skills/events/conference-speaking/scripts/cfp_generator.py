#!/usr/bin/env python3
"""Call for Papers (CFP) proposal generator."""
import json

def generate_cfp(title="", abstract=""):
    return {
        "title": title,
        "abstract": abstract[:300] if abstract else "Your compelling abstract here",
        "outline": ["Problem statement", "Solution approach", "Demo/examples", "Key takeaways"],
        "speaker_info": ["bio", "photo", "social_links", "past_talks"],
        "submission_tips": ["clear_value_prop", "specific_takeaways", "unique_angle"]
    }

if __name__ == "__main__":
    print(json.dumps(generate_cfp("Building Developer Communities"), indent=2))
