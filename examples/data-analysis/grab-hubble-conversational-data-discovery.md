---
title: "Grab Hubble - Conversational Data Discovery with LLMs"
company: "Grab"
author: "Shreyas Parbat, Amanda Ng, Yucheng Zeng, Vinnson Lee, Feng Cheng, Varun Torka"
source: "https://engineering.grab.com/hubble-data-discovery"
date: "2024-09-26"
category: "data-analysis"
tags: ["data-discovery", "documentation-generation", "semantic-search", "elasticsearch", "enterprise-search", "slack-integration", "production"]
description: "Three-stage systematic approach reducing data discovery from days to seconds: enhanced Elasticsearch (82%→94% CTR), GPT-4 doc generation (20%→90% coverage), LLM chatbot (HubbleIQ) - documentation foundation essential before LLM discovery works"

# Problem Classification
problemPattern: "knowledge-retrieval"
problemComplexity: "complex"

# Architecture
architecture:
  type: "multi-stage-system"
  pattern: "incremental-capability-building"
  rationale: "Three-step systematic approach builds foundation before advanced capabilities - enhanced Elasticsearch addresses 75% exact/partial searches, GPT-4 documentation generation creates context store (20%→90% coverage) essential for LLM effectiveness, HubbleIQ chatbot on Glean leverages existing enterprise search for faster go-to-market; four distinct search categories require different technical solutions"
  components: ["enhanced-elasticsearch", "gpt4-doc-generator", "hubbleiq-llm-chatbot", "glean-integration", "slack-bot", "context-store"]

# What Made It Work
breakthroughInsight: "Documentation is foundation for LLM discovery - without high-quality docs (increased from 20%→90% coverage), LLM chatbot cannot work effectively; four distinct search categories (exact, partial, inexact, semantic) require different solutions - keyword search handles 75%, LLM handles semantic; incremental approach (Elasticsearch→Docs→LLM) validated each step before next; leveraging existing Glean tool accelerated go-to-market vs building from scratch"

criticalConstraints:
  - "200k-plus-tables-scale"
  - "18-percent-search-abandonment"
  - "low-documentation-coverage"
  - "tribal-knowledge-dependency"
  - "multi-day-discovery-time"
  - "four-search-category-types"
  - "existing-tool-integration"

antiPatterns:
  - "llm-without-documentation: LLM-based discovery cannot work without high-quality documentation coverage - team had to solve documentation problem first (20%→90%) before chatbot would be effective"
  - "one-search-solution-all-categories: Four distinct search categories (exact, partial, inexact, semantic) require different technical solutions - Elasticsearch for 75%, LLM for semantic; single approach can't serve all effectively"
  - "build-from-scratch: Building custom enterprise search from scratch would delay go-to-market - leveraging existing Glean tool significantly accelerated deployment"
  - "keyword-only-search: Elasticsearch without semantic capability couldn't accept user context, leading to 18% search abandonment for semantic queries"

# Tech Stack
techStack:
  framework: "custom-multi-stage"
  llmProvider: "GPT-4"
  knowledgeRetrieval: "hybrid-search"
  otherTools: ["Datahub", "Elasticsearch", "Glean", "Glean-Apps", "Slack", "clickstream-analysis"]

# Scale
scale:
  volume: "200,000+ tables in data lake, production deployment at Grab scale, all-time high monthly active users"
  latency: "Discovery time reduced from multiple days to seconds, CTR 82%→94%, docs coverage 20%→90%, 73% found discovery easy (17pp increase), 95% found AI docs useful"
---

# Grab Hubble - Conversational Data Discovery with LLMs

**Source**: [Grab Engineering Blog - Enabling conversational data discovery with LLMs at Grab](https://engineering.grab.com/hubble-data-discovery)
**Authors**: Shreyas Parbat, Amanda Ng, Yucheng Zeng, Vinnson Lee, Feng Cheng, Varun Torka
**Date**: September 26, 2024
**Category**: Data Analysis

## Problem

At Grab, finding the right data among a massive repository was a significant challenge that hampered productivity across the organization.

**The Data Discovery Challenge:**
- **Over 200,000 tables** in data lake, plus numerous Kafka streams, production databases, and ML features
- Hubble (internal data discovery tool built on Datahub) primarily used as a reference tool, not for true discovery
- **Reliance on Elasticsearch**: Performed well for keyword searches but couldn't accept user-provided context (no semantic search capability)
- **Only 82% click-through rate**: 18% of users abandoned searches without clicking on any dataset, indicating search results weren't meeting needs
- **Low documentation coverage**: Only 20% of most frequently queried tables (P80 tables) had existing documentation
- **Heavy reliance on tribal knowledge**: Data consumers constantly asked colleagues via Slack to find datasets
- **Survey results**: **51% of data consumers took multiple days** to find the dataset they required

## Solution

The Hubble team implemented a systematic three-step approach to revolutionize data discovery using AI and LLMs.

### Vision and Goals

**Vision**: Remove humans from the data discovery loop by automating the entire process using LLM-powered products. Reduce time taken from multiple days to mere seconds.

**Three Core Goals**:
1. **Build HubbleIQ**: LLM-based chatbot serving as equivalent of Lead Data Analyst for data discovery, accessible via Slack
2. **Improve documentation coverage**: Achieve extensive high-quality documentation across datasets
3. **Enhance Elasticsearch**: Tune implementation to better meet Grab's data consumer requirements

### Step 1: Enhance Elasticsearch

Through clickstream analysis and user interviews, the team identified four categories of data search queries:

**Search Query Categories:**
1. **Exact search** (part of 75%): Query is substring of existing dataset name, with query length ≥40% of dataset's name
2. **Partial search** (part of 75%): Levenshtein distance >80 from existing dataset name, usually spelling mistakes or shorter versions
3. **Inexact search** (25%): Colloquial keywords or phrases semantically related to table/column/documentation (e.g., "city" or "taxi type")
4. **Semantic search**: Free text queries with abundant contextual information - users didn't even attempt these on Hubble, sending them via Slack instead

**Elasticsearch Optimizations Implemented:**
- Tagging and boosting P80 tables (most frequently queried)
- Boosting the most relevant schemas
- Hiding irrelevant datasets like PowerBI dataset tables
- Deboosting deprecated tables
- Improving search UI by simplifying and reducing clutter
- Adding relevant tags
- Boosting certified tables

**Result**: Click-through rate rose from 82% to **94%** (12 percentage point increase)

### Step 2: Build Context Store for HubbleIQ

To support LLM-based discovery, high-quality documentation was essential.

**Documentation Generation Engine:**
- Built using **GPT-4** to generate documentation based on table schemas and sample data
- Refined prompt through multiple iterations of feedback from data producers
- Added "generate" button on Hubble UI for easy documentation generation
- Supported Grab-wide initiative to certify tables

**Proactive Documentation:**
- Pre-populated docs for most critical tables
- Notified data producers to review generated documentation
- AI-generated docs visible with "AI-generated" tag as precaution
- Tag removed when data producers accepted or edited documentation

**Result**: Documentation coverage for P80 tables increased by **70 percentage points to ~90%**. User feedback showed **~95% of users found generated docs useful**.

### Step 3: Build and Launch HubbleIQ

With high documentation coverage in place, the team harnessed LLMs for conversational data discovery.

**Technical Implementation:**
1. **Leveraged Glean**: Used existing enterprise search tool at Grab to speed up go-to-market
2. **Integration with Glean**: Made all data lake tables with documentation available on Glean platform
3. **HubbleIQ Bot Creation**: Used Glean Apps to create bot (LLM with custom system prompt) that could access all Hubble datasets catalogued on Glean
4. **Search Integration**: For any search likely to be semantic, HubbleIQ results shown on top, followed by regular search results
5. **Slack Integration**: Recently integrated HubbleIQ with Slack for seamless discovery without breaking user flow
6. **Channel Integration**: Working with analytics teams to add bot to "ask" channels where data consumers ask contextual questions, acting as first line of defense

## Impact

### User Satisfaction
- **73% of respondents found it easy to discover datasets** (17 percentage point increase from previous survey)
- Hubble reached **all-time high in monthly active users**

### Time Savings
- Reduced data discovery from **multiple days to mere seconds** for semantic searches
- Eliminated need for constant Slack messages to colleagues

### Documentation Quality
- Documentation coverage for critical tables increased from 20% to 90%
- 95% of users found AI-generated documentation useful

### Search Effectiveness
- Click-through rate improved from 82% to 94%
- Successfully addressed all four search query categories

## Key Insights

1. **Four Distinct Search Categories**: Understanding the different types of searches (exact, partial, inexact, semantic) was crucial for building the right solutions for each category.

2. **Documentation is Foundation for LLM Discovery**: Without high-quality documentation coverage, LLM-based data discovery cannot work effectively. The team had to solve documentation first.

3. **Leverage Existing Tools**: Using Glean (existing enterprise search tool) significantly accelerated go-to-market instead of building from scratch.

4. **Meet Users Where They Are**: Integrating HubbleIQ with Slack (where data consumers already work) increased adoption and reduced friction.

5. **Incremental Approach Works**: Systematic three-step approach (Elasticsearch → Documentation → LLM chatbot) allowed team to build on each success and validate assumptions.

6. **AI-Assisted + Human Review**: Using "AI-generated" tags and requiring data producer review balanced automation with quality control.

7. **Click-Through Rate as Key Metric**: CTR served as effective proxy for search quality, allowing team to measure and improve systematically.

## Next Steps

**Documentation Generation Enhancements:**
- Enrich generator with more context for improved accuracy
- Enable auto-update of data docs from Slack threads directly from Slack
- Develop evaluator model leveraging LLMs to assess quality of both human and AI-written docs
- Implement Reflexion (agentic workflow) that uses doc evaluator outputs to iteratively regenerate docs until quality benchmark is met

**HubbleIQ Improvements:**
- Add support for metric datasets and other dataset types
- Enable follow-up questions to HubbleIQ directly on HubbleUI
- Intelligently pull additional metadata when user mentions specific dataset

## Technical Stack

- **Datahub**: Open-source data catalog platform (foundation for Hubble)
- **Elasticsearch**: Enhanced with custom parameters for better search
- **GPT-4**: Documentation generation from table schemas and sample data
- **Glean**: Enterprise search tool for LLM integration
- **Glean Apps**: Platform for creating HubbleIQ bot with custom system prompts
- **Slack**: Integration for seamless conversational data discovery

## Search Query Classification

The team's analysis of search patterns provided valuable framework for understanding data discovery needs:

| Search Type | % of Queries | Characteristics | Solution |
|------------|-------------|-----------------|----------|
| Exact | 37.5% (est.) | Substring of dataset name, ≥40% length | Vanilla Elasticsearch |
| Partial | 37.5% (est.) | Levenshtein distance >80, spelling variations | Enhanced Elasticsearch |
| Inexact | 25% | Colloquial keywords, semantic relations | Enhanced Elasticsearch + Boosting |
| Semantic | Not attempted on UI | Free text with abundant context | HubbleIQ (LLM-powered) |

---

**Tags**: Data Discovery, LLM, GPT-4, Documentation Generation, Semantic Search, Elasticsearch, Enterprise Search, Slack Integration, Datahub, Production System

**Related Examples**:
- [Swiggy Hermes - Charter-Based Text-to-SQL](swiggy-hermes-text-to-sql.md)
- [Uber QueryGPT Multi-Agent Text-to-SQL](uber-querygpt-text-to-sql.md)
- [Pinterest Text-to-SQL in Querybook](pinterest-text-to-sql-querybook.md)
