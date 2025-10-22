---
title: "Plaid AI Agents for Product Experiences - AI Annotator and Fix My Connection"
company: "Plaid"
author: "Raghu Chetlapalli and Ali Vira - Plaid Product Management"
source: "https://plaid.com/blog/ai-agents-june-2025/"
date: "2025-06"
category: "development"
tags: ["workflow-automation", "production", "developer-productivity", "platform-engineering"]
description: "AI Annotator achieving >95% human alignment for data labeling and Fix My Connection enabling 2M+ logins with 90% reduction in repair time"
problem_type: "Data labeling scalability bottleneck limiting model improvements and costly manual bank integration maintenance causing user disruptions"
architecture_pattern: "dual-agent-system-for-data-and-infrastructure"
key_components: ["ai-annotator-llm-labeling", "human-oversight-selective", "fix-my-connection-proactive-detection", "automated-script-generation", "centralized-annotation-platform"]
breakthrough_insight: "LLM-powered automation for both data generation (labeling) and integration maintenance (repairs) scales capabilities beyond manual processes while maintaining quality through selective human oversight for edge cases"
anti_patterns_avoided: ["manual-bulk-labeling", "reactive-integration-fixes", "siloed-labeling-efforts", "complete-human-dependency"]
tech_stack:
  llms: ["LLMs for annotation and script generation"]
  frameworks: ["Internally hosted annotation platform"]
  infrastructure: ["Centralized labeling environment", "Proactive monitoring system", "Automated repair system"]
  methods: ["AI-assisted label generation", "Human-in-the-loop validation", "Proactive issue detection", "Automated script generation"]
scale_metrics:
  ai_annotator_alignment: ">95% human alignment"
  ai_annotator_impact: "Fraction of cost and time vs manual"
  fix_my_connection_logins: "2 million+ successful user-permissioned logins enabled"
  fix_my_connection_speedup: "90% reduction in average time to fix degradation"
  coverage: "Thousands of bank integrations monitored in parallel"
---

# Plaid AI Agents for Product Experiences - AI Annotator and Fix My Connection

## The Problem

Plaid faces two critical scalability challenges in delivering reliable financial data connectivity. First, high-quality labeled data is essential for machine learning models to deliver reliable results, especially for complex tasks like categorizing financial transactions. Despite processing millions of transactions daily, manual labeling struggled to keep pace with demand across Personal Finance, Credit, Payments and other use cases—limiting the ability to train, benchmark, and materially improve models. Second, reliable access to thousands of smaller banks and credit unions is critical for customers who depend on seamless connectivity to reach every user and drive conversions. However, manually building and maintaining these connections at scale is challenging and costly, and when institutions update their login experiences, users face interruptions impacting conversions, satisfaction, and growth potential.

**The Manual Process:**
- **Data Labeling**: Manual annotation of transactions for model training across multiple use cases and teams
- **Bulk Labeling Burden**: Human reviewers spending extensive time on repetitive labeling tasks rather than edge cases
- **Siloed Efforts**: Each team independently managing labeling needs without shared infrastructure
- **Integration Maintenance**: Manual monitoring and repair of thousands of bank integrations
- **Reactive Fixes**: Responding to connection issues after users experience disruptions
- **Script Writing**: Engineers manually analyzing breaking changes and writing repair scripts
- **Limited Coverage**: Manual process unable to scale across thousands of integrations in parallel

**Key Pain Points:**
- **Labeling bottleneck** - Manual processes unable to generate sufficient labeled data to keep pace with demand for model improvements
- **Cost and time constraints** - Bulk labeling requiring significant human effort and time investment at scale
- **Quality inconsistency** - Variability in human labeling across different reviewers and time periods
- **Training limitations** - Insufficient labeled data constraining ability to train, benchmark, and improve models
- **Integration fragility** - Bank login experience updates causing user-facing interruptions and conversion drops
- **Slow manual repairs** - Engineers spending significant time detecting issues, analyzing changes, and writing fix scripts
- **Scalability limits** - Manual monitoring and repair unable to cover thousands of institutions effectively
- **User impact** - Connection downtime affecting user satisfaction, conversions, and customer lifetime value

## The Solution

Plaid developed two AI-powered agents to address these challenges: AI Annotator automates large-scale labeling of anonymized transactions using LLMs while enabling targeted human validation for edge cases and quality spot-checks, deployed as centralized infrastructure where internal teams can annotate, review, and scale labeled datasets. Fix My Connection proactively detects connection quality issues before user disruption spreads, uses intelligent agents to analyze bank integrations for breaking changes and automatically generate repair scripts, and operates at scale monitoring thousands of integrations in parallel unlike traditional manual flows.

**Impact**: AI Annotator produces high-quality labels with >95% human alignment at fraction of cost and time, directly enabling improved categorization models and insights. Fix My Connection has enabled 2 million+ successful user-permissioned logins and reduced average time to fix degradation by 90%, resolving issues faster while improving connection reliability and helping customers drive better business outcomes.

## How It Works

**AI Annotator Capabilities:**
- **AI-Assisted Label Generation** - LLMs create likely transaction labels with high precision and consistency across large-scale anonymized transaction data
- **Human Oversight** - Initially involves human reviewers primarily to generate "golden data-set" for benchmarking, then selectively engages for edge cases or quality spot-checks rather than bulk labeling
- **Centralized Infrastructure** - Single environment where internal teams can annotate, review, and scale labeled datasets to support multiple initiatives
- **Quality Validation** - Selective human validation for edge cases and quality assurance while LLMs handle bulk labeling
- **Multi-Use Case Support** - Serves Personal Finance, Credit, Payments and other use cases from shared platform

**Fix My Connection Capabilities:**
- **Proactive Issue Detection** - Automations spot connection quality issues before user disruption spreads widely
- **Instant Script Generation** - Intelligent agents analyze bank integrations for potential breaking changes, automatically generating scripts to repair them
- **Built to Scale** - System monitors and acts across thousands of integrations in parallel, unlike traditional manual flows
- **Automated Repairs** - Reduces manual engineering effort while minimizing downtime and user impact
- **Coverage Expansion** - Rapidly creates new integrations beyond just repairing existing ones

**Process Flow (AI Annotator):**
1. **Transaction Data** - Millions of daily transactions require labeling for model training across multiple use cases
2. **LLM Processing** - AI Annotator uses LLMs to automatically generate likely labels with high precision
3. **Initial Golden Dataset** - Human reviewers generate benchmark "golden data-set" for quality validation
4. **Bulk Labeling** - LLMs handle large-scale labeling at fraction of manual cost and time
5. **Selective Validation** - Human oversight focused on edge cases and quality spot-checks rather than bulk work
6. **Dataset Scaling** - Centralized platform enables internal teams to annotate, review, and scale datasets
7. **Model Training** - Labeled data feeds into categorization models and insights generation
8. **Continuous Improvement** - Feedback loops refine annotation quality over time

**Process Flow (Fix My Connection):**
1. **Proactive Monitoring** - System continuously monitors connection quality across thousands of bank integrations
2. **Issue Detection** - Automations detect potential problems before widespread user disruption occurs
3. **Breaking Change Analysis** - Intelligent agents analyze bank integrations to identify login experience updates or breaking changes
4. **Script Generation** - Agents automatically generate repair scripts to fix detected issues
5. **Automated Repair** - Scripts deploy to restore connectivity without manual intervention
6. **Parallel Execution** - System operates across thousands of integrations simultaneously
7. **Success Validation** - Monitors restored connections to ensure fixes work correctly
8. **New Integration Creation** - Expanding capability from repairs to proactively creating new integrations

**Technical Architecture:**
- **AI Annotator**: Internally hosted platform with LLM-powered labeling, selective human validation interface, centralized data management, benchmarking against golden datasets
- **Fix My Connection**: Proactive monitoring layer, intelligent analysis agents, automated script generation and deployment, parallel processing across thousands of integrations

## Key Insight

**LLM-powered automation for both data generation (labeling) and integration maintenance (repairs) scales capabilities beyond manual processes while maintaining quality through selective human oversight for edge cases.** By automating bulk labeling with LLMs achieving >95% human alignment and proactively detecting/repairing bank integration issues before users are impacted, Plaid removes scalability bottlenecks in critical product operations—manual processes couldn't generate sufficient labeled data or maintain thousands of connections, but AI agents operating at scale with targeted human validation enable continuous model improvement and reliable connectivity.

**Why This Matters:**
- **Scalability breakthrough** - Manual labeling and integration maintenance hit hard limits; AI agents scale to millions of transactions and thousands of institutions in parallel
- **Quality preservation** - >95% human alignment proves LLMs can match manual labeling quality while selective human oversight catches edge cases
- **Cost efficiency** - Fraction of cost and time vs manual processes frees resources for higher-value work
- **Human-in-the-loop optimization** - Strategic use of humans for golden datasets, edge cases, and quality checks rather than bulk work maximizes expertise impact
- **Proactive vs reactive** - Detecting and fixing issues before user impact dramatically improves experience vs waiting for disruption
- **Continuous improvement enabler** - More labeled data directly enables training, benchmarking, and improving models that were previously data-constrained
- **Customer outcome impact** - 2M+ successful logins and 90% faster fixes translate to better conversions, satisfaction, and lifetime value

**AI Annotator Innovation:**
- Centralized platform serves multiple use cases (Personal Finance, Credit, Payments) from shared infrastructure
- Golden dataset approach establishes quality benchmarks upfront
- Selective human engagement focused on value-add (edge cases, quality) not bulk labeling
- Feedback loops continuously improve annotation over time

**Fix My Connection Innovation:**
- Proactive detection before widespread disruption vs reactive manual monitoring
- Automated script generation from breaking change analysis vs manual engineering
- Parallel operation across thousands of integrations vs sequential manual process
- Expanding from repairs to new integration creation accelerates coverage growth

**Future Enhancements:**
- **AI Annotator**: Expanding to income identification, client vertical detection, business finance classification; incorporating richer knowledge sources and contextual signals; voting mechanisms across multiple LLMs; enhanced feedback loops
- **Fix My Connection**: Creating new integrations proactively (not just repairs); new AI-driven capabilities for more products and features from financial institutions; unlocking richer financial scenarios regardless of where users bank

## Links

- [Original Blog Post](https://plaid.com/blog/ai-agents-june-2025/) - Overview of AI Annotator and Fix My Connection agents improving Plaid's platform
- [Plaid MCP Server](https://plaid.com/blog/mcp-server/) - Model Context Protocol server for AI-powered troubleshooting and analysis
- [Plaid Blog](https://plaid.com/blog/) - Latest updates on Plaid's platform and AI innovations
