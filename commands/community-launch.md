---
description: Plan and execute a developer community launch
allowed-tools: Read, Write, Edit, WebSearch
sasmp_version: "1.4.0"
version: "2.0.0"
---

# Community Launch Planner

Help plan and execute a developer community launch.

## Input Validation

```yaml
input:
  required:
    - platform: enum[discord, slack, forum, github]
  optional:
    - community_name: string
    - target_size: integer
    - launch_date: date
  validation:
    - platform must be one of the allowed values
    - target_size must be positive integer if provided
```

## Workflow

```
Define → Select → Structure → Guidelines → Launch
  ↓        ↓         ↓           ↓           ↓
Goals   Platform  Channels   CoC/Rules    Outreach
```

1. Define community goals and audience
2. Select platform (Discord, Slack, Forum)
3. Create structure and channels
4. Develop guidelines and code of conduct
5. Plan launch and initial outreach

## Output

```markdown
# Community Launch Plan

## Community Overview
- **Name:** [Community Name]
- **Platform:** [Platform]
- **Goal:** [Primary objective]
- **Audience:** [Target developers]

## Channel Structure
- #welcome-introductions
- #announcements
- #general
- #help-support
- #showcase
- [Additional channels]

## Pre-Launch Checklist
- [ ] Platform configured
- [ ] Channels created
- [ ] Guidelines written
- [ ] Code of conduct added
- [ ] Welcome message ready
- [ ] Founding members invited

## Launch Week Plan
- Day 1: [Activities]
- Day 2-3: [Activities]
- Day 4-5: [Activities]
- Day 6-7: [Activities]

## Success Metrics
- Week 1: [Target members]
- Month 1: [Target engagement]
```

## Exit Codes

| Code | Meaning | Action |
|------|---------|--------|
| 0 | Success | Launch plan generated |
| 1 | Invalid platform | Show supported platforms |
| 2 | Missing goals | Prompt for community objectives |

## Usage

```
/community-launch [platform]
/community-launch discord --name="DevAPI Community" --target=500
```

## Troubleshooting

### Common Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| Low engagement | No content ready | Pre-seed with discussions |
| Spam/trolls | No moderation | Set up automod rules |
| Ghost town | Launched too early | Build founding member group first |

### Debug Checklist

```
□ Platform configured correctly?
□ Channels logically organized?
□ Code of conduct published?
□ Moderation team assigned?
□ Welcome flow tested?
□ Founding members confirmed?
```
