---
name: documentation
description: Developer documentation including API references, guides, and getting started content
sasmp_version: "1.3.0"
bonded_agent: 04-technical-writer
bond_type: PRIMARY_BOND
---

# Developer Documentation

Create **comprehensive, usable documentation** that helps developers succeed.

## Documentation Types

| Type | Purpose | Example |
|------|---------|---------|
| **Quickstart** | First 5 minutes | "Hello World in 5 min" |
| **Tutorial** | Learn by doing | "Build your first app" |
| **How-to** | Solve specific task | "How to authenticate" |
| **Concept** | Understand system | "How caching works" |
| **Reference** | Look up details | "API endpoint list" |

## Information Architecture

```
Docs Site
├── Getting Started
│   ├── Quickstart
│   ├── Installation
│   └── First API Call
├── Guides
│   ├── Authentication
│   ├── Error Handling
│   └── Best Practices
├── API Reference
│   ├── Endpoints
│   ├── Parameters
│   └── Response Codes
├── SDKs
│   ├── Python
│   ├── JavaScript
│   └── Go
└── Resources
    ├── FAQ
    ├── Changelog
    └── Migration Guides
```

## Writing Standards

### Structure Every Page
```markdown
# Page Title

Brief intro (what this covers, who it's for)

## Prerequisites
What they need before starting

## Main Content
Step-by-step or organized sections

## Next Steps
What to do after this
```

### Code Samples
- Complete, working examples
- Multiple language options
- Copy button on code blocks
- Show expected output

## Docs-as-Code

```
Write (MD) → Review (PR) → Build (CI) → Deploy (CD)
    ↓          ↓            ↓            ↓
  Local     GitHub       Docusaurus   Vercel/
  Editor    Review       Build        Netlify
```

## Quality Metrics

| Metric | Target |
|--------|--------|
| Time to first success | <10 min |
| Doc search success rate | >80% |
| Support ticket deflection | 60%+ |
| User satisfaction | >4.0/5.0 |

See `assets/` for documentation templates.
