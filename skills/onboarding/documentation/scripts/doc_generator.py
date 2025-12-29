#!/usr/bin/env python3
"""Developer documentation generator."""
import json

def generate_docs():
    return {
        "structure": ["quickstart", "tutorials", "guides", "api_reference", "examples"],
        "quickstart_sections": ["prerequisites", "installation", "hello_world", "next_steps"],
        "best_practices": ["code_examples", "copy_buttons", "versioning", "feedback_loop"]
    }

if __name__ == "__main__":
    print(json.dumps(generate_docs(), indent=2))
