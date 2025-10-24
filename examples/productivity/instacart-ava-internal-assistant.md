---
title: "Instacart Ava - Company-Wide Internal AI Assistant"
company: "Instacart"
author: "Zain Adil, Sr. Director Developer Infra & Productivity"
source: "https://tech.instacart.com/scaling-productivity-with-ava-instacarts-internal-ai-assistant-ed7f02558d84"
date: "2023-09"
category: "productivity"
tags: ["developer-productivity", "workflow-automation", "knowledge-retrieval", "enterprise", "production"]
description: "50% of Instacart employees using monthly, 900+ weekly, with Prompt Exchange for template sharing and Slack integration reducing context grind from 5-10 minutes to seconds"

# Problem Classification
problemPattern: "developer-productivity"
problemComplexity: "moderate"

# Architecture
architecture:
  type: "single-agent"
  pattern: "organizational-infrastructure-platform"
  rationale: "Democratizing AI through organizational infrastructure (Prompt Exchange, Slack integration, conversation sharing) rather than individual access dramatically increases adoption and impact; Prompt Exchange enables domain experts to encode expertise into shareable templates reducing barrier to entry for non-technical users; Slack integration meets users where they work eliminating 5-10 minute context grind; unfurled conversation links increase organic awareness; GPT-4 32K context handles longer conversations while automatic model upgrades and code-copying shortcuts improve ergonomics"
  components: ["web-interface", "prompt-exchange", "slack-integration", "conversation-sharing", "fast-breakdown-template", "support-sidekick", "automatic-model-selection"]

# What Made It Work
breakthroughInsight: "Democratizing AI through organizational infrastructure rather than individual access dramatically increases adoption and impact - building company-specific features (Prompt Exchange, Slack integration, conversation sharing) proved more valuable than raw AI capabilities, enabling knowledge sharing and reducing friction; individual AI tool access doesn't enable organizational learning or best practice sharing; template sharing allows domain experts to encode expertise for others to leverage; unfurled conversation links increase product awareness and adoption organically"

criticalConstraints:
  - "company-wide-scale"
  - "individual-chatgpt-accounts-fragmented"
  - "no-prompt-sharing-mechanism"
  - "context-switching-friction"
  - "5-10-minute-thread-summary-time"
  - "non-technical-user-adoption"
  - "data-privacy-security-guarantees"
  - "internal-documentation-integration"

antiPatterns:
  - "individual-access-only: Providing individual ChatGPT accounts without organizational infrastructure prevents knowledge sharing and best practice distribution - company-specific features (Prompt Exchange, conversation sharing) enable organizational learning exponentially more valuable than isolated access"
  - "blank-text-box-barrier: Starting with empty interface creates barrier to entry for non-technical users unfamiliar with prompt engineering - Prompt Exchange template library allows browsing and reusing proven prompts reducing friction dramatically"
  - "external-context-switching: Requiring users to navigate to external websites and paste context repeatedly introduces 5-10 minute overhead - Slack integration with @Ava mentions enables instant thread summarization meeting users where they work"
  - "siloed-prompt-development: Teams independently creating similar prompts duplicates effort and prevents cross-functional learning - Prompt Exchange with starring and sharing enables domain experts to encode expertise for organization-wide leverage"

# Tech Stack
techStack:
  framework: "custom-web-platform"
  llmProvider: "OpenAI-GPT-4-GPT-3.5"
  knowledgeRetrieval: "prompt-templates"
  otherTools: ["Slack-bot-integration", "conversation-search", "automatic-model-upgrades", "code-copying-shortcuts", "unfurled-links", "Support-Sidekick-RAG"]

# Scale
scale:
  volume: "50% of Instacart employees using monthly, 900+ using weekly, Prompt Exchange user-created template library, company-wide adoption across engineering, Ops, Recruiting, Marketing, HR"
  latency: "20+ minutes per session average, significant code generation usage, thread summarization reduces 5-10 minute context grind to seconds, 80% development time on UI vs 20% on AI/prompts"
---

# Instacart Ava - Company-Wide Internal AI Assistant

## The Problem

During a company hackathon, Instacart's engineering team realized they could produce nearly twice as many features using ChatGPT. However, accessing GPT-4 required individual accounts and lacked company-specific context, prompt templates, or integration with internal workflows.

**The Manual Process:**
- Engineers manually using ChatGPT for brainstorming, coding, debugging, and generating tests
- No shared prompt templates or best practices across organization
- Employees navigating to external websites and pasting context repeatedly
- Support teams manually searching through documentation to answer internal questions
- No way to quickly summarize long Slack threads or email chains
- Teams across departments (Ops, Recruiting, Marketing, HR) unable to access GPT-4

**Key Pain Points:**
- Friction of context-switching to external ChatGPT interface
- No company-wide sharing of effective prompts and workflows
- Teams duplicating effort creating similar prompts independently
- 5-10 minute context grind reading through long Slack threads
- Missing integration with company data and documentation

## The Solution

Instacart built Ava, an internal AI assistant powered by OpenAI's GPT-4 and GPT-3.5 models with custom data privacy, security, and quota guarantees. Started as an engineering tool, expanded company-wide with prompt templates, conversation sharing, and Slack integration.

**Impact**: Over 50% of Instacart employees using monthly, 900+ using weekly. Users spending 20+ minutes per session with significant code generation. Thread summarization reduces context grind from 5-10 minutes to seconds.

## How It Works

**Key Capabilities:**
- **Web Interface with Enhanced Features** - ChatGPT-like interface plus conversation search, automatic model upgrades, and code-copying shortcuts
- **Prompt Exchange** - User-created template library allowing employees to create, share, and star prompts across organization
- **Slack Integration** - Native bot for summarizing threads and channels with @Ava mentions
- **Fast Breakdown Template** - Summarizes conversations with facts, open questions, and action items
- **Support Sidekick** - Automated help desk that analyzes questions, generates search terms, retrieves relevant docs, and provides hyperlinked answers

**Process Flow:**
1. User accesses Ava via web interface or Slack
2. Can start fresh conversation or browse Prompt Exchange for templates
3. Ava processes queries using GPT-4 (32K context) or GPT-3.5 based on conversation size
4. In Slack, typing "@Ava summarize" triggers Fast Breakdown on thread or channel
5. Support Sidekick triggered by emoji reaction: analyzes question → generates search → retrieves docs → returns hyperlinked steps
6. Conversations can be saved, shared via unfurled Slack links for visibility
7. All responses can be copied with single-click for code or text

**Development Journey**: Started at company hackathon for engineers, quickly expanded due to high adoption. Team prioritized ergonomic features over developer-centric ones when scaling to non-engineering users. 80% of development time spent on UI, 20% on AI/prompts.

## Key Insight

**Democratizing AI through organizational infrastructure rather than individual access dramatically increases adoption and impact.** Building company-specific features (Prompt Exchange, Slack integration, conversation sharing) proved more valuable than raw AI capabilities, enabling knowledge sharing and reducing friction.

**Why This Matters:**
- Individual AI tool access doesn't enable organizational learning or best practice sharing
- Starting with blank text box creates barrier to entry for non-technical users
- Slack integration meets users where they already work vs requiring context switch
- Template sharing allows domain experts to encode expertise for others to leverage
- Unfurled conversation links increase product awareness and adoption organically

**Evolution Strategy**: Initially launched for engineers with keyboard shortcuts and code-focused features. When expanding company-wide, shifted to prompt templates, conversation search, and Slack integration. Leveling up with knowledge retrieval and code execution to access Instacart's internal data for complex task accomplishment.

## Links

- [Original Article](https://tech.instacart.com/scaling-productivity-with-ava-instacarts-internal-ai-assistant-ed7f02558d84) - Detailed journey from hackathon project to company-wide internal AI assistant
