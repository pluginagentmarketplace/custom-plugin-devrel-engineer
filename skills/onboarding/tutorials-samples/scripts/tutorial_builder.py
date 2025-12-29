#!/usr/bin/env python3
"""Interactive tutorial builder."""
import json

def build_tutorial(topic=""):
    return {
        "topic": topic,
        "format": ["text_guide", "video", "interactive_sandbox"],
        "structure": ["intro", "prerequisites", "step_by_step", "verification", "next_steps"],
        "engagement": ["checkpoints", "quizzes", "achievements"]
    }

if __name__ == "__main__":
    print(json.dumps(build_tutorial("Getting Started with API"), indent=2))
