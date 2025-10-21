---
name: Add Agent Example
description: Add a new real-world agent case study to the awesome-agent-examples repository. Use when the user wants to add a new agent example, case study, or contribute an implementation to the repository. Handles research, file creation, git workflow, and PR creation.
allowed-tools: Read, Write, Edit, Bash, Glob, WebFetch, WebSearch
---

# Add Agent Example

This skill helps you add new real-world agent case studies to the awesome-agents repository following the established format and workflow.

## When to Use This Skill

- User provides a blog post, tweet, or case study URL about an agent implementation
- User wants to add a new example to the repository
- User asks to "create a PR for [case study URL]"
- User mentions adding a real-world agent implementation

## Workflow Overview

1. **Research**: Extract details from the source
2. **Determine Category**: Choose the appropriate category (Finance, Development, Research, etc.)
3. **Create Branch**: Make a new git branch for this example
4. **Create Example File**: Write the case study following the template
5. **Update READMEs**: Update main README and category README
6. **Commit & Push**: Commit changes with proper message
7. **Create PR**: Open pull request with detailed description

## Step-by-Step Instructions

### Step 1: Research the Source

When given a URL, extract these key details:
- **Problem**: What manual process existed? Time/effort involved? Pain points?
- **Solution**: What does the agent do? High-level description
- **Impact**: Quantifiable results (time saved, productivity gains, cost reduction)
- **How It Works**: Architecture, key technologies, process flow
- **Key Insight**: What made it work? Technical breakthroughs or lessons learned
- **Author/Team**: Who built it?
- **Date**: When was it published/implemented?

**Important**: Focus on the agentic solution and architecture, NOT on marketing the specific tools/frameworks used.

### Step 2: Determine Category

Choose the most appropriate category:
- **💼 Finance & Investment**: Trading, analysis, portfolio management, financial research
- **📧 Productivity & Automation**: Workflow automation, email, scheduling, task management
- **🛠️ Development & Engineering**: Code generation, testing, documentation, DevOps
- **🔬 Research & Analysis**: Research, data gathering, literature reviews, document analysis
- **✍️ Content Creation**: Writing, editing, social media, marketing content
- **📊 Data Analysis**: Data processing, visualization, reporting, insights

Category path: `examples/{category-slug}/`

### Step 3: Create Git Branch

Switch to main and create a new branch:

```bash
git checkout main
git checkout -b add-{company-name}-{short-description}
```

Example: `add-jeppesen-chatbot-framework`

### Step 4: Create Example File

Use the template in [templates/example-template.md](templates/example-template.md).

**Filename convention**: `{company-name}-{descriptive-slug}.md`
- Use lowercase, hyphens for spaces
- Be descriptive but concise
- Examples: `jeppesen-unified-chatbot-framework.md`, `softiq-tender-rfp-agent.md`

**File location**: `examples/{category}/{filename}.md`

**Required sections** (see template):
1. Frontmatter (YAML metadata: title, company, author, source, date, category, tags, description)
2. The Problem (with Manual Process and Key Pain Points subsections)
3. The Solution (with Impact callout)
4. How It Works (with Key Technologies and Process Flow)
5. Key Insight (with Why This Matters)
6. Links

**Tagging Guidelines**:
- **IMPORTANT**: Select 4-7 tags from [tag-taxonomy.md](tag-taxonomy.md)
- Choose tags from multiple categories (architecture + capabilities + domain)
- DO NOT include category name, tool/framework names, or company names as tags
- Focus on functional capabilities and patterns

**Writing guidelines**:
- Focus on the **agentic solution**, not tool promotion
- Include **concrete metrics** (time saved, productivity gains, scale)
- Explain **why the approach worked** (technical insights)
- Use **specific numbers** and **real-world details**
- Keep tool mentions factual, not promotional

### Step 5: Update READMEs

**Main README** (`README.md`):
Add entry to the appropriate category section:

```markdown
**Problem: [Specific pain point]**
→ [Example Name](examples/category/filename.md) by [Author]
*[One-line impact description with key metrics]*
```

**Category README** (`examples/{category}/README.md`):
Add bullet point to Examples section:

```markdown
- [Example Name](filename.md) - [Brief impact description]
```

### Step 6: Commit Changes

Stage files and commit with structured message:

```bash
git add README.md examples/{category}/filename.md examples/{category}/README.md
git commit -m "[commit message from template]"
```

See [templates/commit-message.txt](templates/commit-message.txt) for format.

### Step 7: Push and Create PR

```bash
git push -u origin [branch-name]
/opt/homebrew/bin/gh pr create --title "[PR title]" --body "[PR description]"
```

Use [templates/pr-description.md](templates/pr-description.md) for PR body.

## Quality Checklist

Before finalizing, verify:

**Content Quality**:
- [ ] Example is from a real implementation (not theoretical)
- [ ] Source URL is valid and credible
- [ ] Includes concrete metrics/numbers
- [ ] Focuses on agentic solution, not tool marketing
- [ ] Explains WHY the solution worked (key insights)
- [ ] Proper attribution to original author/team

**Format Compliance**:
- [ ] Metadata table includes all fields (Author, Source, Date, Tags)
- [ ] All required sections present
- [ ] Consistent formatting with existing examples
- [ ] Markdown syntax is valid
- [ ] Links work and point to original sources

**Repository Updates**:
- [ ] Main README updated with new example
- [ ] Category README updated
- [ ] Example file in correct category folder
- [ ] Filename follows naming convention

**Git Workflow**:
- [ ] New branch created from main
- [ ] Commit message follows template
- [ ] Only relevant files committed (example, 2 READMEs)
- [ ] Branch pushed to remote
- [ ] PR created with detailed description

## Common Issues

**Issue**: Can't access the source URL
**Solution**: Ask user to provide the content directly, or use WebSearch to find related information

**Issue**: Example is too tool-focused
**Solution**: Reframe to focus on the agent architecture, capabilities, and what made it work rather than which specific tools were used

**Issue**: Missing concrete metrics
**Solution**: Look for any quantifiable results in the source. If none exist, note "specific metrics not disclosed" but ensure the problem/solution is still compelling

**Issue**: Unclear which category fits
**Solution**: Choose based on the primary use case. If it spans multiple categories, pick the most relevant and mention others in tags

## Templates

All templates are in the `templates/` directory:
- [example-template.md](templates/example-template.md) - Full example file structure
- [commit-message.txt](templates/commit-message.txt) - Commit message format
- [pr-description.md](templates/pr-description.md) - PR body template

## Example Usage

**User**: "Add this case study to the repo: https://blog.example.com/agent-case-study"

**Skill Response**:
1. Fetch and analyze the blog post
2. Extract key details (problem, solution, impact, insights)
3. Determine category (e.g., Research & Analysis)
4. Create branch: `add-example-company-agent`
5. Write example file following template
6. Update main README and category README
7. Commit with structured message
8. Push branch
9. Create PR with detailed description
10. Provide PR URL to user

## Notes

- Always verify the source is credible before adding
- Focus on production implementations, not experiments
- Prioritize examples with measurable impact
- Maintain neutral tone (no promotional language)
- Ensure proper attribution to original authors