#!/usr/bin/env python3
"""Video production checklist generator."""
import json

def get_checklist():
    return {
        "pre_production": ["script", "storyboard", "equipment_check", "lighting"],
        "production": ["audio_test", "frame_composition", "multiple_takes"],
        "post_production": ["rough_cut", "color_grade", "audio_mix", "captions", "thumbnail"],
        "distribution": ["youtube", "twitter", "linkedin", "blog_embed"]
    }

if __name__ == "__main__":
    print(json.dumps(get_checklist(), indent=2))
