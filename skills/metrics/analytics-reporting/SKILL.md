---
name: analytics-reporting
description: DevRel metrics, analytics dashboards, and program reporting
sasmp_version: "1.3.0"
bonded_agent: 07-metrics-analyst
bond_type: PRIMARY_BOND
---

# DevRel Analytics & Reporting

Measure **program impact** with data-driven metrics and reporting.

## Key Metrics Framework

### AAARRRP Model for DevRel

| Stage | Metrics |
|-------|---------|
| **Awareness** | Impressions, reach, brand mentions |
| **Acquisition** | Signups, registrations, first visits |
| **Activation** | First API call, tutorial completion |
| **Retention** | MAU, DAU, repeat usage |
| **Revenue** | Conversions, upgrades, pipeline |
| **Referral** | NPS, word-of-mouth, shares |
| **Product** | Feature adoption, feedback quality |

## Metrics by Category

### Community Metrics
```yaml
growth:
  - total_members
  - new_members_per_week
  - member_retention_30d

engagement:
  - daily_active_users
  - messages_per_day
  - questions_answered
  - response_time_avg
```

### Content Metrics
```yaml
reach:
  - page_views
  - unique_visitors
  - social_impressions

engagement:
  - time_on_page
  - scroll_depth
  - shares_and_saves

conversion:
  - cta_clicks
  - signups_from_content
  - doc_to_api_calls
```

### Event Metrics
```yaml
attendance:
  - registrations
  - show_up_rate
  - session_attendance

satisfaction:
  - nps_score
  - session_ratings
  - feedback_sentiment

business:
  - leads_generated
  - pipeline_influenced
```

## Dashboard Structure

```
Executive Dashboard
├── North Star Metric (primary KPI)
├── Funnel Overview
├── Weekly Trends
└── Key Highlights

Detailed Dashboards
├── Community Health
├── Content Performance
├── Event Analysis
└── Developer Journey
```

## Reporting Cadence

| Report | Frequency | Audience |
|--------|-----------|----------|
| Weekly pulse | Weekly | DevRel team |
| Monthly review | Monthly | Leadership |
| Quarterly OKR | Quarterly | Executives |
| Annual summary | Yearly | Company-wide |

## Attribution Challenges

Common issues:
- Multi-touch attribution
- Long sales cycles
- Indirect influence
- Data silos

Solutions:
- UTM parameters
- Developer surveys
- CRM integration
- Cohort analysis

See `assets/` for dashboard templates.
