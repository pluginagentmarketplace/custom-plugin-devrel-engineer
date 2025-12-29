<div align="center">

# DevRel Engineer Plugin

### Complete Developer Relations System for Claude Code

**Build developer communities with 7 specialized agents covering communication, community building, events, content creation, and career development**

[![Verified](https://img.shields.io/badge/Verified-Working-success?style=flat-square&logo=checkmarx)](https://github.com/pluginagentmarketplace/custom-plugin-devrel-engineer)
[![License](https://img.shields.io/badge/License-Custom-yellow?style=flat-square)](LICENSE)
[![Version](https://img.shields.io/badge/Version-3.1.0-blue?style=flat-square)](https://github.com/pluginagentmarketplace/custom-plugin-devrel-engineer)
[![Status](https://img.shields.io/badge/Status-Production_Ready-brightgreen?style=flat-square)](https://github.com/pluginagentmarketplace/custom-plugin-devrel-engineer)
[![Agents](https://img.shields.io/badge/Agents-7-orange?style=flat-square)](#agents-overview)
[![Skills](https://img.shields.io/badge/Skills-17-purple?style=flat-square)](#skills-reference)
[![SASMP](https://img.shields.io/badge/SASMP-v1.3.0-blueviolet?style=flat-square)](#)

[![DevRel](https://img.shields.io/badge/DevRel-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://roadmap.sh/devrel)
[![Community](https://img.shields.io/badge/Community-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.com)
[![Content](https://img.shields.io/badge/Content-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://youtube.com)
[![Events](https://img.shields.io/badge/Events-F24E1E?style=for-the-badge&logo=meetup&logoColor=white)](https://meetup.com)

[Quick Start](#quick-start) | [Agents](#agents-overview) | [Skills](#skills-reference) | [Commands](#commands)

</div>

---

## Verified Installation

> **This plugin has been tested and verified working on Claude Code.**
> Last verified: December 2025

---

## Quick Start

### Option 1: Install from GitHub (Recommended)

```bash
# Step 1: Add the marketplace from GitHub
/plugin add marketplace pluginagentmarketplace/custom-plugin-devrel-engineer

# Step 2: Install the plugin
/plugin install devrel-engineer-plugin@pluginagentmarketplace-devrel-engineer

# Step 3: Restart Claude Code to load new plugins
```

### Option 2: Clone and Load Locally

```bash
# Clone the repository
git clone https://github.com/pluginagentmarketplace/custom-plugin-devrel-engineer.git

# Navigate to the directory in Claude Code
cd custom-plugin-devrel-engineer

# Load the plugin
/plugin load .
```

After loading, restart Claude Code.

### Verify Installation

After restarting Claude Code, verify the plugin is loaded. You should see these agents available:

```
custom-plugin-devrel-engineer:01-devrel-strategist
custom-plugin-devrel-engineer:02-community-builder
custom-plugin-devrel-engineer:03-content-creator
custom-plugin-devrel-engineer:04-technical-writer
custom-plugin-devrel-engineer:05-event-manager
custom-plugin-devrel-engineer:06-developer-advocate
custom-plugin-devrel-engineer:07-metrics-analyst
```

---

## Available Skills

Once installed, these 17 skills become available:

| Skill | Invoke Command | Golden Format |
|-------|----------------|---------------|
| Public Speaking | `Skill("custom-plugin-devrel-engineer:public-speaking")` | talk-template.yaml |
| Technical Writing | `Skill("custom-plugin-devrel-engineer:technical-writing")` | writing-checklist.yaml |
| Building Community | `Skill("custom-plugin-devrel-engineer:building-community")` | community-launch-plan.yaml |
| Moderation Guidelines | `Skill("custom-plugin-devrel-engineer:moderation-guidelines")` | code-of-conduct-template.yaml |
| Event Management | `Skill("custom-plugin-devrel-engineer:event-management")` | event-checklist.yaml |
| Conference Speaking | `Skill("custom-plugin-devrel-engineer:conference-speaking")` | cfp-template.yaml |
| Blogging | `Skill("custom-plugin-devrel-engineer:blogging")` | blog-post-template.yaml |
| Video Production | `Skill("custom-plugin-devrel-engineer:video-production")` | video-checklist.yaml |
| Social Media | `Skill("custom-plugin-devrel-engineer:social-media")` | content-calendar.yaml |
| Documentation | `Skill("custom-plugin-devrel-engineer:documentation")` | docs-structure.yaml |
| Tutorials & Samples | `Skill("custom-plugin-devrel-engineer:tutorials-samples")` | sample-readme-template.yaml |
| Developer Support | `Skill("custom-plugin-devrel-engineer:developer-support")` | support-templates.yaml |
| Analytics & Reporting | `Skill("custom-plugin-devrel-engineer:analytics-reporting")` | metrics-dashboard.yaml |
| Thought Leadership | `Skill("custom-plugin-devrel-engineer:thought-leadership")` | personal-brand-guide.yaml |
| Personal Branding | `Skill("custom-plugin-devrel-engineer:personal-branding")` | networking-templates.yaml |
| APIs & SDKs | `Skill("custom-plugin-devrel-engineer:apis-sdks")` | sdk-design-patterns.yaml |
| Git & Open Source | `Skill("custom-plugin-devrel-engineer:git-opensource")` | github-templates.yaml |

---

## What This Plugin Does

This plugin provides **7 specialized agents** and **17 production-ready skills** for Developer Relations:

| Agent | Purpose |
|-------|---------|
| **DevRel Strategist** | Developer experience design, program strategy, developer marketing |
| **Community Builder** | Discord/Slack management, moderation, community growth |
| **Content Creator** | Blog posts, videos, social media, content calendars |
| **Technical Writer** | API docs, tutorials, getting started guides |
| **Event Manager** | Meetups, conferences, webinars, workshops |
| **Developer Advocate** | Public speaking, CFPs, developer feedback |
| **Metrics Analyst** | DevRel metrics, dashboards, reporting |

---

## Agents Overview

### 7 Implementation Agents

Each agent is designed to **do the work**, not just explain:

| Agent | Capabilities | Example Prompts |
|-------|--------------|-----------------|
| **DevRel Strategist** | Program design, DX optimization, OKRs | `"Design ambassador program"`, `"Create DevRel roadmap"` |
| **Community Builder** | Community launch, moderation, growth | `"Set up Discord server"`, `"Create code of conduct"` |
| **Content Creator** | Blog posts, videos, social strategy | `"Write technical blog post"`, `"Plan content calendar"` |
| **Technical Writer** | Docs, tutorials, API references | `"Write API documentation"`, `"Create getting started guide"` |
| **Event Manager** | Event planning, logistics, follow-up | `"Plan developer meetup"`, `"Create conference booth plan"` |
| **Developer Advocate** | Speaking, CFPs, developer feedback | `"Write CFP abstract"`, `"Prepare conference talk"` |
| **Metrics Analyst** | Analytics, KPIs, reporting | `"Set up DevRel metrics"`, `"Create monthly report"` |

---

## Commands

4 interactive commands for DevRel workflows:

| Command | Usage | Description |
|---------|-------|-------------|
| `/devrel-start` | `/devrel-start` | Start a DevRel task (content, community, events, advocacy) |
| `/cfp-submit` | `/cfp-submit` | Create and submit a Call for Papers |
| `/content-plan` | `/content-plan` | Plan content strategy and calendar |
| `/community-launch` | `/community-launch` | Launch and grow a developer community |

---

## Skills Reference

Each skill includes **Golden Format** content:
- `assets/` - YAML templates and configurations
- `scripts/` - Automation scripts (planned)
- `references/` - Methodology guides (planned)

### Skills Deep Dive

| Category | Skills | Focus Areas |
|----------|--------|-------------|
| **Communication** | public-speaking, technical-writing | Talks, documentation |
| **Community** | building-community, moderation-guidelines | Discord, code of conduct |
| **Events** | event-management, conference-speaking | Meetups, CFPs |
| **Content** | blogging, video-production, social-media | Posts, videos, calendars |
| **Onboarding** | documentation, tutorials-samples | Getting started guides |
| **Support** | developer-support | Issue handling, FAQs |
| **Metrics** | analytics-reporting | KPIs, dashboards |
| **Career** | thought-leadership, personal-branding | Speaking, networking |
| **Technical** | apis-sdks, git-opensource | SDK design, OSS |

---

## Usage Examples

### Example 1: Create CFP Abstract

```markdown
# Before: Manually writing conference proposals

# After (with Developer Advocate agent):
/cfp-submit

Agent generates:
- Title: "Building Developer Communities at Scale"
- Abstract: [300-word compelling abstract]
- Outline: Introduction, 3 main points, conclusion
- Bio: [100-word speaker bio]
- Technical requirements: Projector, demo laptop
```

### Example 2: Launch Community

```markdown
# Before: Starting from scratch

# After (with Community Builder agent):
/community-launch

Agent provides:
1. Discord server structure template
2. Channel organization (welcome, announcements, help, showcase)
3. Code of Conduct template
4. Moderation bot recommendations
5. Launch announcement template
6. Growth strategy for first 100 members
```

### Example 3: Content Calendar

```yaml
# Using Content Creator agent:
Skill("custom-plugin-devrel-engineer:social-media")

# Generates content-calendar.yaml:
weekly_content:
  monday: Technical blog post
  tuesday: Twitter thread (tips)
  wednesday: YouTube tutorial
  thursday: Community highlight
  friday: Newsletter
```

---

## Plugin Structure

```
custom-plugin-devrel-engineer/
├── .claude-plugin/
│   ├── plugin.json           # Plugin manifest
│   └── marketplace.json      # Marketplace config
├── agents/                   # 7 specialized agents
│   ├── 01-devrel-strategist.md
│   ├── 02-community-builder.md
│   ├── 03-content-creator.md
│   ├── 04-technical-writer.md
│   ├── 05-event-manager.md
│   ├── 06-developer-advocate.md
│   └── 07-metrics-analyst.md
├── skills/                   # 17 skills (Golden Format)
│   ├── communication/
│   │   ├── public-speaking/
│   │   └── technical-writing/
│   ├── community/
│   │   ├── building-community/
│   │   └── moderation-guidelines/
│   ├── events/
│   │   ├── event-management/
│   │   └── conference-speaking/
│   ├── content/
│   │   ├── blogging/
│   │   ├── video-production/
│   │   └── social-media/
│   ├── onboarding/
│   │   ├── documentation/
│   │   └── tutorials-samples/
│   ├── support/
│   │   └── developer-support/
│   ├── metrics/
│   │   └── analytics-reporting/
│   ├── career/
│   │   ├── thought-leadership/
│   │   └── personal-branding/
│   └── technical/
│       ├── apis-sdks/
│       └── git-opensource/
├── commands/                 # 4 slash commands
│   ├── devrel-start.md
│   ├── cfp-submit.md
│   ├── content-plan.md
│   └── community-launch.md
├── hooks/hooks.json          # 14 intelligent routing hooks
├── README.md
├── CHANGELOG.md
├── CONTRIBUTING.md
└── LICENSE
```

---

## Platform Coverage

| Category | Platforms |
|----------|-----------|
| **Community** | Discord, Slack, GitHub Discussions, Reddit |
| **Content** | Dev.to, Medium, Hashnode, YouTube, Twitch |
| **Events** | Meetup, Eventbrite, Hopin, Zoom |
| **Social** | Twitter/X, LinkedIn, Mastodon, BlueSky |
| **Docs** | GitBook, ReadTheDocs, Notion, Docusaurus |

---

## Security Notice

This plugin is designed for **authorized development and community use only**:

**USE FOR:**
- Building developer communities
- Creating technical content
- Managing developer events
- Developer advocacy
- DevRel metrics

**NEVER:**
- Share personal information
- Bypass community guidelines
- Spam or manipulate metrics
- Violate platform ToS

---

## Contributing

Contributions are welcome:

1. Fork the repository
2. Create a feature branch
3. Follow the Golden Format for new skills
4. Submit a pull request

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

---

## Metadata

| Field | Value |
|-------|-------|
| **Last Updated** | 2025-12-28 |
| **Maintenance Status** | Active |
| **SASMP Version** | 1.3.0 |
| **Support** | [Issues](../../issues) |

---

## License

Custom License - See [LICENSE](LICENSE) for details.

---

## Contributors

**Authors:**
- **Dr. Umit Kacar** - Senior AI Researcher & Engineer
- **Muhsin Elcicek** - Senior Software Architect

---

<div align="center">

**Build thriving developer communities with AI assistance!**

[![Made for DevRel](https://img.shields.io/badge/Made%20for-DevRel-blue?style=for-the-badge&logo=linkedin)](https://github.com/pluginagentmarketplace/custom-plugin-devrel-engineer)

**Built by Dr. Umit Kacar & Muhsin Elcicek**

*Based on [roadmap.sh/devrel](https://roadmap.sh/devrel)*

</div>
