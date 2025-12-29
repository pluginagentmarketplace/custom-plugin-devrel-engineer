#!/usr/bin/env python3
"""Lint and improve technical documentation."""
import json
import re

def lint_doc(text=""):
    issues = []
    if len(text) > 0:
        if not text.strip().startswith("#"):
            issues.append("Missing title (start with #)")
        if "TODO" in text:
            issues.append("Contains TODO items")
        if len(re.findall(r'\b(very|really|basically)\b', text.lower())) > 0:
            issues.append("Contains filler words")
    return {"issues": issues, "word_count": len(text.split())}

if __name__ == "__main__":
    print(json.dumps(lint_doc("# Sample Doc\nThis is basically very good."), indent=2))
