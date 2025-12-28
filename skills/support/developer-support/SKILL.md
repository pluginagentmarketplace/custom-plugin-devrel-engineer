---
name: developer-support
description: Developer support systems including forums, office hours, and FAQ management
sasmp_version: "1.3.0"
bonded_agent: 06-developer-advocate
bond_type: SECONDARY_BOND
---

# Developer Support

Build **effective support systems** that help developers succeed and scale.

## Support Channels

| Channel | Response Time | Best For |
|---------|---------------|----------|
| Docs/FAQ | Instant | Self-service |
| Forum/Discord | 4-24 hours | Community Q&A |
| Office Hours | Scheduled | Complex issues |
| Support Tickets | 24-48 hours | Bugs/urgent |
| Live Chat | Minutes | Quick questions |

## Support Tier Model

```
Tier 0: Self-Service
├── Documentation
├── FAQ
├── Knowledge Base
└── Search

Tier 1: Community
├── Forums
├── Discord/Slack
└── Stack Overflow

Tier 2: DevRel Team
├── Office Hours
├── Direct Outreach
└── Webinars

Tier 3: Engineering
├── Bug Reports
├── Feature Requests
└── Architecture Reviews
```

## Office Hours Best Practices

### Format
- Weekly or bi-weekly
- 30-60 minutes
- Open Q&A or themed topics
- Record for those who can't attend

### Running Sessions
1. **Start on time** - Respect schedules
2. **Screen share** - Show, don't just tell
3. **Take notes** - Action items to follow up
4. **Be honest** - "I'll find out" is OK

## FAQ Management

### Creating Effective FAQs
```markdown
Q: How do I authenticate with the API?

A: You can authenticate using API keys or OAuth 2.0:

**API Keys** (simplest)
```code
curl -H "Authorization: Bearer YOUR_API_KEY" ...
```

**OAuth 2.0** (for user data)
[See our OAuth guide →](/docs/oauth)

Related: [Authentication errors](/docs/errors#auth)
```

### FAQ Sources
- Support tickets (recurring issues)
- Community questions
- Search queries (what people look for)
- User feedback

## Support Metrics

| Metric | Target |
|--------|--------|
| Response time (community) | <24 hours |
| Resolution rate | >80% |
| CSAT score | >4.0/5 |
| Ticket deflection | >60% |

See `assets/` for support templates.
