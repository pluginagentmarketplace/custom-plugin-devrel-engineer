---
name: thought-leadership
description: Building thought leadership through publishing, speaking, and industry influence
sasmp_version: "1.4.0"
version: "2.0.0"
updated: "2025-01"
bonded_agent: 01-devrel-strategist
bond_type: SECONDARY_BOND
---

# Thought Leadership

Build **industry influence** and recognition as a DevRel professional.

## Skill Contract

### Parameters
```yaml
parameters:
  required:
    - leadership_type: enum[publishing, speaking, community, advisory]
    - expertise_area: string
  optional:
    - target_audience: array[string]
    - timeline: duration
```

### Output
```yaml
output:
  strategy:
    content_plan: array[ContentItem]
    speaking_targets: array[Event]
    influence_metrics: object
```

## Thought Leadership Pillars

### 1. Publishing
- Blog posts and articles
- Guest posts on industry sites
- Technical papers and reports
- Book authorship
- Newsletter creation

### 2. Speaking
- Conference keynotes
- Podcast appearances
- Panel discussions
- Webinars and workshops
- Media interviews

### 3. Community
- Open source contributions
- Industry working groups
- Mentorship programs
- Online presence

## Content Strategy

```
Expertise Area → Point of View → Consistent Publishing
      ↓               ↓                 ↓
   Your niche    Your unique      Regular
   territory     perspective      output
```

### Finding Your Angle
| Question | Purpose |
|----------|---------|
| What do you know deeply? | Expertise |
| What frustrates you? | Opportunity |
| What do you see differently? | Differentiation |
| What do others ask you? | Value |

## Building Credibility

### The Credibility Stack
```
1. Create valuable content consistently
2. Share others' work generously
3. Engage authentically in discussions
4. Present at events
5. Get featured/quoted by others
6. Mentor others in the community
```

## Platform Presence

| Platform | Content Type | Frequency |
|----------|--------------|-----------|
| Twitter/X | Quick insights | Daily |
| LinkedIn | Long-form thinking | 2-3x/week |
| Blog | Deep dives | Weekly |
| Speaking | Events | Monthly |
| Podcast | Interviews | As invited |

## Measuring Influence

- Speaking invitations received
- Content shares and engagement
- Quote/feature requests
- Community mentions
- Follower growth quality (not just quantity)
- Inbound opportunities

## Career Impact

Thought leadership leads to:
- Better job opportunities
- Higher compensation
- Conference invitations
- Book deals
- Advisory roles
- Industry recognition

## Retry Logic

```yaml
retry_patterns:
  low_engagement:
    strategy: "Refine topic angle"
    fallback: "Test different platforms"

  rejection_from_events:
    strategy: "Improve proposal quality"
    fallback: "Start with smaller events"

  burnout:
    strategy: "Reduce frequency, batch content"
    fallback: "Focus on highest-impact activities"
```

## Failure Modes & Recovery

| Failure Mode | Detection | Recovery |
|--------------|-----------|----------|
| Content ignored | Low engagement | Adjust topic/timing |
| Speaking rejected | CFP declined | Improve abstracts |
| Credibility questioned | Negative feedback | Address directly, be humble |

## Debug Checklist

```
□ Expertise clearly defined?
□ Unique perspective identified?
□ Publishing cadence sustainable?
□ Platforms prioritized correctly?
□ Metrics being tracked?
□ Network growing authentically?
```

## Test Template

```yaml
test_thought_leadership:
  unit_tests:
    - test_content_quality:
        assert: "Provides unique value"
    - test_consistency:
        assert: "Regular publishing cadence"

  integration_tests:
    - test_influence_growth:
        assert: "Measurable increase over time"
```

## Observability

```yaml
metrics:
  - speaking_invitations: integer
  - content_published: integer
  - engagement_rate: float
  - inbound_opportunities: integer
```

See `assets/` for personal brand templates.
