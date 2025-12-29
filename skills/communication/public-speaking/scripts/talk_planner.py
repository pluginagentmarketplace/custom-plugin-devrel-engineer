#!/usr/bin/env python3
"""Plan and prepare technical talks."""
import json

def plan_talk(title="", duration=30):
    return {
        "title": title,
        "duration_minutes": duration,
        "sections": {
            "intro": int(duration * 0.15),
            "main_content": int(duration * 0.65),
            "demo": int(duration * 0.10),
            "qa": int(duration * 0.10)
        },
        "checklist": ["outline", "slides", "demo", "rehearsal", "backup_plan"]
    }

if __name__ == "__main__":
    print(json.dumps(plan_talk("API Best Practices", 45), indent=2))
