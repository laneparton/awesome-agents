---
title: "Text-to-SQL AI Agent"
company: "Salesforce"
author: "Salesforce Engineering Team"
source: "https://www.salesforce.com/blog/text-to-sql-agent/"
date: "2025-01"
category: "data-analysis"
tags: ["workflow-automation", "knowledge-retrieval", "rag", "enterprise", "production"]
description: "Reduced data query time from days to minutes through Slack-integrated Text-to-SQL agent with RAG-powered query generation"

# Problem Classification
problemPattern: "workflow-automation"
problemComplexity: "complex"

# Architecture
architecture:
  type: "single-agent"
  pattern: "rag-query-generation"
  rationale: "RAG architecture enriches natural language queries with business context from knowledge bases and metadata catalogs, enabling accurate SQL generation for non-technical users"
  components: ["slack-integration", "knowledge-base", "metadata-catalog", "llm-gateway", "query-validator", "execution-engine"]

# What Made It Work
breakthroughInsight: "Shipping with 50% accuracy and prioritizing feedback loops over perfectionism - combined with generating 10 query candidates and using consensus algorithms (Cosine Similarity + Levenshtein Distance) to identify the most likely correct query"

criticalConstraints:
  - "non-technical-users-cant-write-sql"
  - "engineers-as-data-gatekeepers"
  - "organizational-jargon-changes-frequently"
  - "llm-non-determinism"

antiPatterns:
  - "siloed-tool-development: Streamlit prototype failed due to adoption friction; Slack integration drove immediate usage"
  - "black-box-reasoning: System must provide SQL explanations and ask clarifying questions for user trust"
  - "perfectionism-paralysis: Shipped at ~50% accuracy to prioritize feedback loops over flawless launch"

# Tech Stack
techStack:
  framework: ["Bolt", "Slack SDK"]
  llmProvider: "Einstein Gateway"
  knowledgeRetrieval: "RAG"
  otherTools: ["Fack (knowledge base)", "Horizon Data Platform (metadata)", "Trino", "Iceberg"]

# Scale
scale:
  volume: "Internal Salesforce usage - reduced technologist query time from dozens of hours weekly"
  latency: "minutes vs days for query responses"
---

# Text-to-SQL AI Agent

## The Problem

Non-technical Salesforce employees needed data insights but couldn't write SQL queries, creating a bottleneck where engineers and data scientists became gatekeepers to organizational data. Technologists spent dozens of hours weekly writing custom queries for business users who waited days for answers.

**The Manual Process:**
- Non-technical users identify data questions for their work
- Submit query requests to engineering or data science teams
- Engineers translate business questions into SQL queries
- Users wait days for query results
- Dozens of technologist hours consumed weekly on query-writing
- Data access limited to those with SQL expertise

**Key Pain Points:**
- Engineers and data scientists become bottlenecks for data access
- Non-technical teams can't self-serve data insights
- Days-long turnaround time for simple queries
- Organizational knowledge (jargon, business terms) not encoded in schemas
- SQL expertise requirement limits data democratization

## The Solution

A Slack-integrated AI agent that translates natural language questions into SQL queries using RAG to incorporate business context and organizational terminology. Users ask questions directly in Slack and receive query explanations with optional execution results.

**Impact**: Reduced data query time from days to minutes, cutting technologist query-writing time from dozens of hours weekly to near-zero while democratizing data access for non-technical users.

## How It Works

**Key Capabilities:**
- **Natural Language Interface** - Slack integration using Bolt framework enables queries in users' existing workflow
- **RAG-Powered Context** - Enriches queries with business terminology from Fack knowledge base and schema metadata from Horizon Data Platform
- **Consensus Validation** - Generates 10 SQL query candidates and uses Cosine Similarity + Levenshtein Distance to identify most likely correct query
- **Transparent Reasoning** - Returns SQL explanations and asks clarifying questions instead of black-box answers
- **Rapid Knowledge Updates** - Knowledge base deployments complete in ~15 minutes with automated regression testing

**Process Flow:**
1. User asks question in Slack (e.g., "What was my service cost last month?")
2. Python microservice receives message via Bolt (Slack's Python framework)
3. RAG system retrieves relevant context:
   - Business terminology and SQL patterns from Fack knowledge base
   - Table schemas, sample records, and access patterns from Horizon Data Platform
4. LLM generates 10 SQL query candidates through Einstein Gateway
5. Consensus algorithms (Cosine Similarity + Levenshtein Distance) identify most likely correct query
6. System runs EXPLAIN query to validate syntax before execution
7. Returns query explanation to user with optional execution results and data analysis
8. User can ask clarifying questions or refine the query

**Technical Architecture:** Built on Slack Bolt framework with RAG architecture combining Fack (open-source knowledge base) and Horizon Data Platform (Salesforce's internal dbt-equivalent for metadata). Queries execute on Trino engine with Iceberg data lake backend, all orchestrated through Einstein Gateway for LLM access.

## Key Insight

**Ship with imperfect accuracy and prioritize feedback loops over perfectionism.** The team launched with approximately 50% accuracy, recognizing that real-world usage would reveal failure modes faster than extended development cycles.

**Why This Matters:**
- Early Streamlit prototype failed due to adoption friction; Slack integration drove immediate usage because it met users where they work
- Transparency through SQL explanations and clarifying questions built trust more than confident black-box outputs
- Generating 10 candidates and using consensus algorithms addresses LLM non-determinism without requiring perfect first-pass accuracy
- Knowledge base agility (~15 minute deployment cycles) enables continuous improvement as organizational terminology evolves
- Shipping early with clear limitations beats holding for perfection

**Non-Determinism Solution:** LLMs produce different queries for identical inputs. By generating 10 candidates and identifying consensus through similarity algorithms, the system significantly improves reliability despite underlying non-determinism.

**Adoption Strategy:** Integration with existing workflows (Slack) proved critical - an earlier standalone Streamlit prototype failed to gain traction because users had to leave their work context to use it.

## Links

- [Original Article](https://www.salesforce.com/blog/text-to-sql-agent/) - How We Built a Text-To-SQL AI Agent
- [Fack GitHub](https://github.com/salesforce/fack) - Salesforce's open-source knowledge base tool
