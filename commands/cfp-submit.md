---
description: Generate a conference CFP (Call for Papers) submission
allowed-tools: Read, Write, Edit, WebSearch
sasmp_version: "1.4.0"
version: "2.0.0"
---

# CFP Submission Helper

Help the user create a compelling conference talk proposal.

## Input Validation

```yaml
input:
  required:
    - topic: string
  optional:
    - conference: string
    - talk_length: enum[lightning, standard, deep_dive]
    - audience_level: enum[beginner, intermediate, advanced]
  validation:
    - topic must be non-empty string
    - talk_length defaults to "standard" (30-45 min)
```

## Workflow

```
Input → Research → Brainstorm → Generate → Review → Output
  ↓        ↓          ↓           ↓          ↓        ↓
Topic   Context     Angles      Draft     Polish    File
```

1. Ask about the topic/area of expertise
2. Help brainstorm talk angles
3. Generate:
   - Catchy title
   - Compelling abstract
   - Detailed outline
   - Speaker bio

## Output Format

```markdown
## Talk Title
[Catchy title with benefit]

## Abstract
[2-3 paragraph description]

## Outline
1. Introduction (X min)
2. Main Point 1 (X min)
3. Main Point 2 (X min)
4. Main Point 3 (X min)
5. Conclusion (X min)

## Speaker Bio
[Professional bio]

## Why This Talk
[Why audiences will benefit]
```

## Exit Codes

| Code | Meaning | Action |
|------|---------|--------|
| 0 | Success | CFP generated and saved |
| 1 | Missing topic | Prompt for topic input |
| 2 | Generation failed | Retry with different angle |

## Usage

```
/cfp-submit [topic]
/cfp-submit "Building APIs" --conference="KubeCon" --length=standard
```

## Troubleshooting

### Common Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| Weak abstract | Too generic | Add specific outcomes/benefits |
| Title too long | Over 10 words | Shorten, focus on hook |
| Missing bio | Not provided | Create from LinkedIn/Twitter |

### Debug Checklist

```
□ Topic clearly defined?
□ Audience level specified?
□ Time constraints considered?
□ Abstract under 300 words?
□ Outline timing adds up?
```
