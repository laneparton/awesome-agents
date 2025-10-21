# Add Agent Example Checklist

Use this checklist to ensure quality and completeness when adding a new example.

## Content Quality

- [ ] Example is from a real, production implementation (not theoretical)
- [ ] Source URL is valid and credible
- [ ] Includes concrete metrics and numbers
- [ ] Focuses on agentic solution and architecture
- [ ] NOT focused on tool/framework marketing
- [ ] Explains WHY the solution worked (key insights and breakthroughs)
- [ ] Proper attribution to original author/team
- [ ] Date is accurate (when published/implemented)

## Format Compliance

- [ ] Frontmatter (YAML) includes all required fields:
  - [ ] title
  - [ ] company
  - [ ] author
  - [ ] source (with working link)
  - [ ] date (YYYY-MM format)
  - [ ] category
  - [ ] tags (4-7 tags from tag-taxonomy.md)
  - [ ] description (one-line impact summary)
- [ ] Tags follow taxonomy guidelines:
  - [ ] 4-7 tags selected from tag-taxonomy.md
  - [ ] NO category name as tag
  - [ ] NO tool/framework names as tags
  - [ ] NO company names as tags
  - [ ] Tags from multiple categories (architecture + capabilities + domain)
- [ ] All required sections present:
  - [ ] Title
  - [ ] The Problem (with Manual Process and Key Pain Points)
  - [ ] The Solution (with Impact callout)
  - [ ] How It Works (with Key Technologies/Capabilities and Process Flow)
  - [ ] Key Insight (with Why This Matters)
  - [ ] Links
- [ ] Consistent formatting with existing examples
- [ ] Markdown syntax is valid
- [ ] All links work and point to original sources

## Repository Updates

- [ ] Main README updated with new example in correct category
- [ ] Category README updated with new example
- [ ] Example file in correct category folder
- [ ] Filename follows naming convention: `{company-name}-{descriptive-slug}.md`
- [ ] Category choice is appropriate for the primary use case

## Git Workflow

- [ ] Started from main branch (`git checkout main`)
- [ ] New branch created with descriptive name
- [ ] Branch name follows convention: `add-{company-name}-{short-description}`
- [ ] Commit message follows template structure
- [ ] Only relevant files committed:
  - [ ] New example file
  - [ ] Main README.md
  - [ ] Category README.md
- [ ] No unrelated changes included
- [ ] Branch pushed to remote
- [ ] PR created with detailed description using template

## PR Quality

- [ ] PR title starts with "Add:"
- [ ] PR includes summary of example
- [ ] PR lists key highlights (metrics, scale, approach)
- [ ] PR explains why example is valuable
- [ ] PR includes technical highlights
- [ ] PR links to original source
- [ ] PR mentions focus on agentic solution vs. tool promotion
- [ ] Test plan checklist included and completed

## Final Review

- [ ] Read the example file end-to-end for clarity
- [ ] Verify all numbers and metrics are accurate
- [ ] Check that technical explanations make sense
- [ ] Ensure tone is neutral and educational (not promotional)
- [ ] Confirm attribution is correct
- [ ] Test all links in the example file
- [ ] Preview markdown rendering (if possible)

## Common Issues to Avoid

- [ ] NOT too tool-focused (focus on agent capabilities, not tool features)
- [ ] NOT vague or generic (include specific numbers and details)
- [ ] NOT missing attribution (always credit original authors)
- [ ] NOT theoretical (must be real implementation)
- [ ] NOT missing metrics (quantify impact wherever possible)
- [ ] NOT wrong category (choose based on primary use case)
- [ ] NOT messy git history (one clean commit per example)
