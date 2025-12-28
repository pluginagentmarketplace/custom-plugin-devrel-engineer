---
name: tutorials-samples
description: Creating tutorials, code samples, and example applications for developer onboarding
sasmp_version: "1.3.0"
bonded_agent: 04-technical-writer
bond_type: SECONDARY_BOND
---

# Tutorials & Code Samples

Create **effective tutorials and sample code** that accelerate developer learning.

## Tutorial Types

| Type | Goal | Length |
|------|------|--------|
| Quickstart | First success | 5-10 min |
| Walkthrough | Build something | 30-60 min |
| Deep dive | Master topic | 1-2 hours |
| Workshop | Hands-on practice | 2-4 hours |

## Tutorial Structure

```
1. Introduction
   - What you'll build
   - What you'll learn
   - Prerequisites

2. Setup
   - Environment preparation
   - Dependencies installation
   - Configuration

3. Steps (3-7 steps)
   - Clear numbered instructions
   - Code with explanations
   - Expected results

4. Conclusion
   - What you accomplished
   - Next steps
   - Related resources
```

## Code Sample Best Practices

### DO
```javascript
// Good: Complete, runnable example
const client = new APIClient({ apiKey: process.env.API_KEY });

async function getUser(userId) {
  try {
    const user = await client.users.get(userId);
    console.log(`User: ${user.name}`);
    return user;
  } catch (error) {
    console.error(`Failed to get user: ${error.message}`);
    throw error;
  }
}

getUser('user_123');
```

### DON'T
```javascript
// Bad: Incomplete, unclear
client.users.get(id).then(u => console.log(u));
```

## Sample Application Patterns

| Pattern | Use Case |
|---------|----------|
| **Minimal** | Single feature demo |
| **Full-stack** | Complete application |
| **Use-case** | Specific scenario |
| **Clone** | Production starter |

## Repository Structure

```
sample-app/
├── README.md        # Quick start
├── .env.example     # Environment template
├── src/             # Source code
├── docs/            # Additional docs
└── tests/           # Example tests
```

## Quality Checklist

- [ ] Works on clone/download
- [ ] Clear README instructions
- [ ] Environment variables documented
- [ ] Error handling included
- [ ] Comments explain "why"

See `assets/` for sample templates.
