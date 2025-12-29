#!/usr/bin/env python3
"""Community moderation helper."""
import json

def get_guidelines():
    return {
        "rules": ["be_respectful", "stay_on_topic", "no_spam", "no_harassment"],
        "actions": ["warn", "mute", "ban", "escalate"],
        "escalation_path": ["moderator", "lead_moderator", "community_manager"]
    }

if __name__ == "__main__":
    print(json.dumps(get_guidelines(), indent=2))
