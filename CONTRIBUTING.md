# Contributing to DevRel Engineer Plugin

Thank you for your interest in contributing to the DevRel Engineer Plugin!

## How to Contribute

### Reporting Issues

1. Check existing issues first
2. Provide clear description
3. Include steps to reproduce
4. Add relevant labels

### Submitting Changes

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make your changes
4. Follow the Golden Format for new skills
5. Test your changes
6. Commit with clear messages
7. Push to your fork
8. Open a Pull Request

### Golden Format for Skills

New skills must follow this structure:

```
skills/category/skill-name/
├── SKILL.md           # Main skill file with SASMP frontmatter
├── assets/            # YAML templates and configurations
│   └── template.yaml
├── scripts/           # Automation scripts (optional)
│   └── script.sh
└── references/        # Methodology guides (optional)
    └── GUIDE.md
```

### SKILL.md Requirements

```yaml
---
name: skill-name
description: Clear description
sasmp_version: "1.3.0"
bonded_agent: agent-name
bond_type: PRIMARY_BOND or SECONDARY_BOND
---
```

### Code Style

- Use clear, descriptive names
- Follow existing patterns
- Add comments for complex logic
- Include examples in documentation

### Commit Messages

- Use conventional commit format
- Start with verb: Add, Fix, Update, Remove
- Keep first line under 70 characters

### Testing

- Test all commands work
- Verify skill templates render correctly
- Check YAML syntax is valid

## Questions?

Open an issue with the `question` label.

---

**Thank you for helping improve DevRel Engineer Plugin!**

*Dr. Umit Kacar & Muhsin Elcicek*
