---
title: "Fullscript Automated Security Investigation Agent"
company: "Fullscript"
author: "Fullscript Engineering Team, led by Sahar Rahmani"
source: "https://n8n.io/case-studies/fullscript/"
date: "2025-01"
category: "productivity"
tags: ["security", "workflow-automation"]
description: "Reduced security investigations by 97% (weeks to 30 minutes), saving 3,600+ hours/year"

# Problem Classification
problemPattern: "workflow-automation"
problemComplexity: "complex"

# Architecture
architecture:
  type: "single-agent"
  pattern: "workflow-based"
  rationale: "Slack-based orchestration was critical - investigations became 'just a Slack message' instead of weeks of coordination, with AI handling analysis while maintaining human oversight"
  components: ["slack-bot-orchestration", "ai-analysis", "automated-reporting", "multi-system-data-collection"]

# What Made It Work
breakthroughInsight: "Complex, regulation-heavy workflows automated in 2 days during hackathon using low-code orchestration - Slack interface made weeks-long investigations become 'just a Slack message'"

criticalConstraints:
  - "healthcare-compliance"
  - "multi-system-data-aggregation"
  - "audit-trail-required"
  - "highly-regulated-industry"

antiPatterns:
  - "traditional-development: would have taken months vs 2-day hackathon build"

# Tech Stack
techStack:
  framework: "n8n"
  llmProvider: "OpenAI"
  knowledgeRetrieval: "workflow-automation"
  otherTools: ["Slack", "Google Docs"]

# Scale
scale:
  volume: "3,600+ hours saved annually"
  latency: "weeks to 30 minutes"
---

# Fullscript Automated Security Investigation Agent

## The Problem

Fullscript, a healthcare platform serving licensed practitioners across North America, operates in a highly regulated industry where they must verify that practitioners using their accounts can prove their identity to prevent hacking and malicious usage. Security investigations were taking weeks or even months to complete, creating massive delays in threat response.

**The Manual Process:**
- Security team manually investigates each flagged account to verify practitioner identity
- Gather data from multiple systems and sources manually
- Coordinate with various stakeholders for additional information
- Review and analyze all data points to determine legitimacy
- Document findings and make recommendation for next steps
- **Total time per investigation: weeks to months**
- **Annual impact: 3,600+ hours** of engineering time consumed

**Key Pain Points:**
- Investigations "could never be made easy" and took weeks to complete
- Manual coordination across multiple teams and data sources
- Complex data parsing and analysis required for each case
- Delayed threat response due to investigation backlog
- Resource-intensive process preventing team from focusing on strategic work
- Operating in highly regulated healthcare industry with strict compliance requirements

## The Solution

At a company-wide hackathon, the engineering team built an automated security investigation workflow in just 2 days that reduced investigation time from weeks to 30 minutes. The Platform Account Investigations workflow automatically triggers when suspicious activity is detected, orchestrates data collection via Slack bot, uses AI to analyze findings, and generates comprehensive audit reports with recommended next steps.

**Impact**:
- **97% reduction** in investigation time (weeks → 30 minutes)
- **3,600 hours saved annually** on security investigations
- **Built in 2 days** at hackathon (vs months of traditional development)
- Investigations now "just a Slack message" instead of weeks-long process

## How It Works

**Key Capabilities:**
- **Automated data collection** - Parses all available account data and user history across systems
- **Slack-based orchestration** - Security bot handles data verification and stakeholder coordination
- **AI-powered analysis** - Agent summarizes findings and determines if further investigation required
- **Automated reporting** - Generates comprehensive Google Docs audit reports with suggested next steps
- **Compliance-ready** - Built for highly regulated healthcare industry requirements

**Process Flow:**
1. Security monitoring system detects suspicious account activity requiring identity verification
2. Workflow automatically triggers Platform Account Investigations agent
3. Slack security bot initiates automated data collection from all relevant systems
4. Bot parses account data, user history, and activity patterns
5. Slack bot gathers additional feedback from relevant stakeholders as needed
6. AI agent analyzes all collected data and determines risk level
7. Agent decides if report requires further manual analysis or can be closed
8. Comprehensive audit report automatically generated in Google Docs
9. Report includes summary of findings, risk assessment, and suggested next steps
10. **Investigation completed in ~30 minutes instead of weeks**

**Development Time:** Built in just 2 days during organization-wide hackathon by the engineering team. Traditional development approach would have taken months for a workflow this complex.

**Technical Architecture:** Workflow automation platform with Slack integration for human-in-the-loop coordination, AI agent for analysis and summarization, automated data collection from multiple internal systems, and Google Docs generation for audit trail and compliance documentation.

## Key Insight

**Complex, regulation-heavy workflows can be automated in days using AI agents when the right orchestration tools are available.** The engineering team built in 2 days what would have traditionally taken months—proving that low-code workflow platforms don't mean low capability when dealing with sophisticated use cases.

**Why This Matters:**
- **Speed of implementation**: Hackathon project to production workflow demonstrates rapid development velocity
- **Complexity handled**: Healthcare compliance, multi-system data aggregation, and AI analysis in single workflow
- **Dramatic ROI**: 97% time reduction and 3,600 hours saved annually from 2-day build effort
- **Human-in-the-loop design**: Slack bot enables stakeholder input while automating data collection and analysis
- **Compliance-ready automation**: Proves AI agents can work in highly regulated industries with proper audit trails

**Why It Worked:** The Slack-based interface was crucial—investigations that previously required weeks of coordination became "just a Slack message." The AI agent handled the complex analysis while maintaining human oversight through the bot interface, and automated Google Docs reporting ensured compliance and audit readiness.

## Links

- [Original Case Study](https://n8n.io/case-studies/fullscript/) - n8n case study with quotes from Director of Internal AI
- [Fullscript](https://fullscript.com/) - Healthcare platform serving licensed practitioners
