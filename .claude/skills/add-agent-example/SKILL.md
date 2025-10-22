---
name: add-agent-example
description: Add a new real-world agent case study to the awesome-agent-examples repository. Use when the user wants to add a new agent example, case study, or contribute an implementation to the repository. Handles research, file creation, git workflow, and PR creation. (project)
---

# Add Agent Example

Add new real-world agent case studies to the awesome-agent-examples repository following the established format and workflow.

## When to Use This Skill

Trigger this skill when the user:
- Provides a blog post, tweet, or case study URL about an agent implementation
- Asks to "add this example to the repo" or "create a PR for [case study]"
- Wants to contribute a new real-world agent implementation
- Mentions adding an agent case study or example

## Core Workflow

Follow these steps to add a new example:

### 1. Research and Extract Details

Fetch the source URL and extract:
- **Problem**: Manual process, time/effort, pain points
- **Solution**: What the agent does (high-level)
- **Impact**: Real-world results and metrics (focus on actual deployment)
- **How It Works**: Architecture, technologies, process flow
- **Key Insight**: What made it work, technical breakthroughs
- **Author/Team**: Who built it
- **Date**: When published/implemented (YYYY-MM format)

**Focus**: Real-world agents solving actual problems, NOT theoretical use cases or tool marketing.

### 2. Determine Category

Choose the appropriate category based on primary use case:
- `finance` - Finance & Investment
- `productivity` - Productivity & Automation
- `development` - Development & Engineering
- `research` - Research & Analysis
- `content-creation` - Content Creation
- `data-analysis` - Data Analysis

### 3. Create Git Branch

```bash
git checkout main
git checkout -b add-{company-name}-{short-description}
```

Example: `add-bertelsmann-content-search`

### 4. Create Example File

Create `examples/{category}/{company-name}-{descriptive-slug}.md` using the template in `references/example-template.md`.

**Key guidelines**:
- Select 4-7 tags from `references/tag-taxonomy.md` (NO category names, tool names, or company names)
- Focus on agentic solution and architecture, not tool promotion
- Include specific metrics and implementation details
- Explain WHY the approach worked

### 5. Update READMEs

**Main README** (`README.md`):
```markdown
**Problem: [Specific pain point]**
→ [Example Name](examples/category/filename.md) by [Author]
*[One-line impact with metrics]*
```

**Category README** (`examples/{category}/README.md`):
```markdown
- [Example Name](filename.md) - [Brief impact description]
```

### 6. Commit Changes

Stage only relevant files:
```bash
git add README.md examples/{category}/filename.md examples/{category}/README.md
git commit -m "[message from references/commit-message.txt]"
```

### 7. Push and Create PR

```bash
git push -u origin [branch-name]
gh pr create --title "[PR title]" --body "[description from references/pr-description.md]"
```

Return the PR URL to the user.

## Quality Standards

Before finalizing, verify:
- Example is from a real implementation (production or serious prototype)
- Source URL is valid and credible
- Focuses on agentic solution, not tool marketing
- Includes concrete implementation details
- Explains technical approach and why it worked
- Proper attribution to original authors
- All required sections present (see template)
- Markdown formatting is correct
- Links work and point to original sources

## Common Issues

**Can't access source URL**: Ask user for content directly or use WebSearch for related information

**Too tool-focused**: Reframe to focus on agent architecture and capabilities rather than specific tools

**Missing metrics**: Metrics are valuable but NOT required - focus on real-world implementation and technical architecture

**Unclear category**: Choose based on primary use case; if it spans multiple, pick most relevant and mention others in tags

## Bundled Resources

- `references/example-template.md` - Full example file structure and format
- `references/tag-taxonomy.md` - Canonical list of allowed tags with selection rules
- `references/commit-message.txt` - Commit message format and example
- `references/pr-description.md` - PR body template and example
- `references/quality-checklist.md` - Comprehensive quality checklist for final review

## Example Execution

**User input**: "Add this case study: https://blog.example.com/agent-case-study"

**Execution**:
1. Fetch and analyze the blog post
2. Extract problem, solution, impact, insights, author, date
3. Determine category (e.g., `research`)
4. Create branch: `add-example-company-agent`
5. Write example file following template at `examples/research/example-company-agent.md`
6. Update main README and category README with formatted entries
7. Commit with structured message
8. Push branch and create PR
9. Return PR URL to user
