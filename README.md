# Awesome Agent Examples 🤖

**Real-world problems solved with AI agents**

[![GitHub stars](https://img.shields.io/github/stars/laneparton/awesome-agents?style=social)](https://github.com/laneparton/awesome-agents/stargazers)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A curated collection of real-world AI agent use cases that highlight specific problems and practical solutions. Every example is sourced from actual implementations shared by practitioners.

## Table of Contents

- [What Makes a Good Example](#what-makes-a-good-example)
- [Categories](#categories)
  - [💼 Finance & Investment](#-finance--investment)
  - [📧 Productivity & Automation](#-productivity--automation)
  - [🛠️ Development & Engineering](#️-development--engineering)
  - [🔬 Research & Analysis](#-research--analysis)
  - [✍️ Content Creation](#️-content-creation)
  - [📊 Data Analysis](#-data-analysis)
- [How to Contribute](#how-to-contribute)

## What Makes a Good Example

This repository focuses on **problem-first** examples. Each submission should clearly articulate:

- **The specific pain point** - What was the manual process? How long did it take? What made it frustrating?
- **Measurable impact** - Time saved, accuracy improved, cost reduced
- **Real-world validation** - Must link to original source (tweet, blog, video, GitHub)
- **Practical lessons** - What made the solution work? What challenges were overcome?

We're not interested in theoretical use cases or marketing content. Every example must be grounded in actual implementation.

## Categories

### 💼 Finance & Investment

**Problem: Investment analysts manually processing M&A filings for deal comparables**
→ [M&A Deal Comp Generator](examples/finance/m-and-a-deal-comp.md) by Jerry Liu
*Batch processes SEC filings and generates Excel comparables, reducing 20-50 hours of work to minutes with 95% accuracy*

**Problem: Finance teams facing fragmented data access across platforms with SQL complexity barriers**
→ [Finch - Conversational Financial Data Agent](examples/finance/uber-finch-financial-data-agent.md) by Uber FinTech Team
*Multi-agent system with semantic metadata layer eliminating analyst data request queues through Slack-native real-time financial intelligence*

**Problem: Managers overwhelmed reviewing expense approvals against ambiguous policy documents**
→ [Expense Policy Agent](examples/finance/ramp-expense-approval-agent.md) by Ramp Engineering Team
*Autonomous expense approval agent handling 65% of approvals through transparent policy-based reasoning with categorical decision framework*

---

### 📧 Productivity & Automation

**Problem: E-commerce support teams manually handling repetitive customer tickets and order management**
→ [Minimal Multi-Agent Customer Support System](examples/productivity/minimal-multi-agent-customer-support.md) by Titus Ex and Niek Hogenboom
*Multi-agent system achieving 80%+ efficiency gains, autonomously handling 90% of support tickets with integrated order management*

**Problem: Healthcare security investigations taking weeks to verify practitioner identities and prevent account fraud**
→ [Fullscript Automated Security Investigation Agent](examples/productivity/fullscript-security-investigation-agent.md) by Fullscript Engineering Team
*Built in 2 days at hackathon, reduced investigations by 97% (weeks to 30 minutes), saving 3,600+ hours/year with AI-powered workflow automation*

**Problem: Early AI features couldn't reason dynamically or handle complex multi-step workflows**
→ [Airtable Event-Driven Agentic Framework](examples/productivity/airtable-agentic-framework.md) by Airtable Engineering Team
*Powers Omni app builder and Field Agents with event-driven state machine, achieving 15-30% cost reduction and enabling conversational workflows*

**Problem: On-call support copilot providing incomplete, inaccurate responses failing to meet SME quality standards**
→ [Uber Enhanced Agentic-RAG - Genie On-Call Copilot](examples/productivity/uber-enhanced-agentic-rag.md) by Uber Engineering Security and AI Teams
*Enhanced agentic RAG achieving 27% relative increase in acceptable answers and 60% reduction in incorrect advice through enriched document processing and LLM-powered agents*

**Problem: Sales reps spending significant time on routine tasks across disconnected systems**
→ [Omega - AI Sales Agent](examples/productivity/netguru-omega-sales-agent.md) by Netguru Team
*Multi-agent system automating sales workflows in Slack with analyze-execute-review pattern, eliminating context-switching across HubSpot, Salesforce, and Drive*

---

### 🛠️ Development & Engineering

**Problem: Platform engineers overwhelmed by routine developer requests while trying to build new features**
→ [Cisco Outshift JARVIS - Agentic AI Platform Engineer](examples/development/cisco-outshift-jarvis-platform-engineer.md) by Outshift by Cisco
*10x productivity boost through distributed multi-agent system - CI/CD setup from 1 week to <1 hour, resource provisioning from half-day to seconds*

**Problem: Teams across Boeing independently building AI chatbots, duplicating 512 hours of work per agent**
→ [Unified Chatbot Framework at Jeppesen](examples/development/jeppesen-unified-chatbot-framework.md) by Jeppesen AI Team
*Reduced agent development time by 87% (512 to 64 hours), saving ~2,000 engineering hours with a shared framework powered by LlamaIndex*

**Problem: Developers spending excessive time searching across fragmented documentation for Adobe-specific guidelines**
→ [Adobe Unified Support Knowledge Retrieval Agent](examples/development/adobe-unified-support-retrieval-agent.md) by Adobe Developer Platform Team
*20% accuracy increase with semantic search and metadata filtering, serving thousands of developers with immediate answers and reduced support costs*

**Problem: Manual data labeling bottleneck and costly reactive maintenance across thousands of financial institution integrations**
→ [Plaid AI Agents for Product Operations](examples/development/plaid-ai-agents-product-ops.md) by Plaid Engineering Team
*Two specialized agents: AI Annotator achieving 95%+ human alignment for data labeling, Fix My Connection reducing repair time by 90% enabling 2M+ successful logins*

**Problem: Building production AI agents requires choosing between slow fine-tuning or rapid in-context learning**
→ [Manus - Context Engineering for Production AI Agents](examples/development/manus-context-engineering-agent.md) by Manus Engineering Team
*10x cost savings through KV-cache optimization and context engineering patterns, enabling rapid iteration (hours vs weeks) tested across millions of users*

---

### 🔬 Research & Analysis

**Problem: Complex research tasks requiring days of manual sequential searching, synthesis, and source tracking**
→ [Anthropic Multi-Agent Research System](examples/research/anthropic-multi-agent-research-system.md) by Anthropic
*90% faster research through orchestrator-worker pattern with parallel subagents, saving users days of work with 90.2% performance improvement*

**Problem: Complex web research requiring parallel investigation across multiple dimensions**
→ [Exa Deep Research Multi-Agent System](examples/research/exa-deep-research-agent.md) by Exa
*Production multi-agent system processing hundreds of daily queries, delivering structured research results in 15 seconds to 3 minutes with dynamic task scaling*

**Problem: Media company creatives searching for content across dozens of isolated systems, spending hours instead of creating**
→ [Multi-Agent Content Discovery at Bertelsmann](examples/research/bertelsmann-content-search.md) by Bertelsmann AI Hub
*Reduced content discovery from hours to seconds with intelligent multi-agent orchestration across books, TV/film, news, and web sources*

**Problem: Construction companies manually analyzing 100+ page tender documents, taking hours to days per tender**
→ [Tender RFP Analysis Agent for Construction](examples/research/softiq-tender-rfp-agent.md) by SoftIQ
*Reduced tender analysis from hours/days to <10 minutes, enabling 6-10x productivity increase with semantic chunking and workflow-based reasoning*

**Problem: Knowledge workers managing scattered data across disconnected apps with constant context-switching**
→ [Dropbox Dash - RAG and Multi-Step AI Agents](examples/research/dropbox-dash-rag-multi-step-agent.md) by Dropbox ML Team
*Hybrid RAG + multi-step agent system achieving sub-2-second responses for 95%+ of queries with custom DSL interpreter for secure task orchestration*

---

### ✍️ Content Creation

*Examples coming soon - [contribute yours!](CONTRIBUTING.md)*

---

### 📊 Data Analysis

**Problem: Manual product catalog management across regions with inconsistent vendor data formats**
→ [Delivery Hero Agentic Product Knowledge Base](examples/data-analysis/delivery-hero-product-knowledge-base.md) by Delivery Hero QC
*Automates extraction of 22 product attributes and title standardization with predefined agents, improving efficiency and data quality through knowledge distillation*

**Problem: Scaling LLM applications to serve hundreds of millions of customers across billions of item listings cost-effectively**
→ [eBay Mercury - Agentic AI Platform](examples/data-analysis/ebay-mercury-agentic-platform.md) by eBay Recommendations Team
*Agentic framework serving hundreds of millions of customers across 2 billion+ listings with hundreds of ms latency through plug-and-play agent components*

**Problem: Non-technical users can't access data insights without SQL expertise, creating engineer bottlenecks**
→ [Text-to-SQL AI Agent](examples/data-analysis/salesforce-text-to-sql-agent.md) by Salesforce Engineering Team
*Reduced data query time from days to minutes through Slack-integrated agent with RAG-powered SQL generation and consensus validation*

---

### 💡 Uncategorized

**Additional Resources:**
→ [Real-World Gen AI Use Cases with Technical Blueprints](https://cloud.google.com/blog/products/ai-machine-learning/real-world-gen-ai-use-cases-with-technical-blueprints) by Google Cloud
→ [ML System Design: 650 Case Studies](https://www.evidentlyai.com/ml-system-design) - A similar curated list of real-world AI implementations

---

## How to Contribute

We're actively looking for real-world agent examples! Have you built an agent that solves a specific problem? Know of an impressive implementation shared online?

**Two ways to contribute:**

1. **Submit via Issue** - Use our [example submission template](.github/ISSUE_TEMPLATE/example-submission.md)
2. **Submit via Pull Request** - Follow the guidelines in [CONTRIBUTING.md](CONTRIBUTING.md)

All contributions must link to original sources and focus on real-world problems and solutions.

---

**Maintained by the community** | [Contribute](CONTRIBUTING.md) | [MIT License](LICENSE)
