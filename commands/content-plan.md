---
description: Create a content calendar and plan for DevRel activities
allowed-tools: Read, Write, Edit
sasmp_version: "1.4.0"
version: "2.0.0"
---

# Content Planning Command

Generate a content plan for DevRel activities.

## Input Validation

```yaml
input:
  required:
    - period: enum[week, month, quarter]
  optional:
    - platforms: array[blog, video, social, events]
    - focus_areas: array[string]
    - launches: array[object]
  validation:
    - period must be one of: week, month, quarter
    - platforms defaults to all if not specified
```

## Workflow

```
Input → Analyze → Generate → Schedule → Output
  ↓        ↓         ↓          ↓         ↓
Period  Context   Topics      Dates     Calendar
```

1. Ask about:
   - Time period (week/month/quarter)
   - Focus areas (blog, video, social, events)
   - Key product/feature launches
   - Target audience

2. Generate:
   - Content calendar with dates
   - Topic ideas for each slot
   - Platform distribution plan
   - Key metrics to track

## Output Format

```markdown
# Content Plan: [Period]

## Weekly Schedule
| Day | Platform | Content Type | Topic |
|-----|----------|--------------|-------|
| Mon | Twitter  | Thread       | ...   |
| Tue | Blog     | Tutorial     | ...   |
| Wed | LinkedIn | Insight      | ...   |
| Thu | YouTube  | Video        | ...   |
| Fri | Twitter  | Community    | ...   |

## Content Ideas
### Blog Posts
- [Topic 1]
- [Topic 2]

### Videos
- [Topic 1]
- [Topic 2]

## Key Dates
- [Event/Launch dates]

## Success Metrics
- [Metric 1]: [Target]
- [Metric 2]: [Target]
```

## Exit Codes

| Code | Meaning | Action |
|------|---------|--------|
| 0 | Success | Plan generated |
| 1 | Invalid period | Show valid options |
| 2 | No focus areas | Prompt for input |

## Usage

```
/content-plan [period]
/content-plan month --platforms="blog,video" --focus="API launch"
```

## Troubleshooting

### Common Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| Too many topics | Overambitious | Reduce to sustainable cadence |
| No dates | Missing context | Add key dates/launches |
| Vague metrics | Unclear goals | Define specific KPIs |

### Debug Checklist

```
□ Period realistic?
□ Platforms prioritized?
□ Launch dates included?
□ Metrics measurable?
□ Team capacity considered?
```
