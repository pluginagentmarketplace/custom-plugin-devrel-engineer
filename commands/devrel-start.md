---
description: Start a DevRel task - content creation, community management, or event planning
allowed-tools: Read, Write, Edit, WebSearch
sasmp_version: "1.4.0"
version: "2.0.0"
---

# DevRel Start Command

Help the user start a DevRel task. Ask what type of task:

1. **Content Creation** - Blog post, video, documentation
2. **Community Management** - Discord/Slack setup, moderation
3. **Event Planning** - Meetup, conference, webinar
4. **Advocacy** - Speaking proposal, feedback collection
5. **Metrics** - Dashboard setup, reporting

Based on their choice, guide them through the initial steps using the relevant skills.

## Input Validation

```yaml
input:
  required: []
  optional:
    - task_type: enum[content, community, event, advocacy, metrics]
  validation:
    - task_type must be one of the allowed values if provided
```

## Workflow

```
Start → Select Task Type → Load Skills → Guide Setup → Confirm
  ↓           ↓                ↓             ↓           ↓
Prompt     Validate         Import       Step-by-step  Summary
```

## Exit Codes

| Code | Meaning | Action |
|------|---------|--------|
| 0 | Success | Task started successfully |
| 1 | Invalid task type | Show available options |
| 2 | Missing dependencies | Install required tools |

## Usage

```
/devrel-start
/devrel-start content
/devrel-start community
```

## Troubleshooting

### Common Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| Unknown task type | Invalid input | Use one of: content, community, event, advocacy, metrics |
| Skill not found | Missing skill file | Verify skills/ directory structure |
| Permission denied | File access issue | Check file permissions |

### Debug Checklist

```
□ Task type valid?
□ Required skills available?
□ User context understood?
□ Dependencies met?
```
