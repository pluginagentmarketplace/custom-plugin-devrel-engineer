#!/usr/bin/env python3
"""Plan and optimize blog content."""
import json

def plan_post(topic=""):
    return {
        "topic": topic,
        "structure": ["hook", "problem", "solution", "example", "cta"],
        "seo_checklist": ["keyword_research", "meta_description", "internal_links", "alt_tags"],
        "promotion": ["twitter", "linkedin", "newsletter", "hackernews"]
    }

if __name__ == "__main__":
    print(json.dumps(plan_post("GraphQL vs REST"), indent=2))
