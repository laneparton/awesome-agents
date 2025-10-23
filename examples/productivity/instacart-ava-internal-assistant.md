---
title: "Instacart Ava - Company-Wide Internal AI Assistant"
company: "Instacart"
author: "Zain Adil, Sr. Director Developer Infra & Productivity"
source: "https://tech.instacart.com/scaling-productivity-with-ava-instacarts-internal-ai-assistant-ed7f02558d84"
date: "2023-09"
category: "productivity"
tags: ["developer-productivity", "workflow-automation", "knowledge-retrieval", "enterprise", "production"]
description: "50% of Instacart employees using monthly, 900+ weekly, with Prompt Exchange for template sharing and Slack integration reducing context grind from 5-10 minutes to seconds"
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
