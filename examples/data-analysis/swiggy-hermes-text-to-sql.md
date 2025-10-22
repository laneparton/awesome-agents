---
title: "Swiggy Hermes - Charter-Based Text-to-SQL with Multi-Stage RAG"
company: "Swiggy"
author: "Amaresh Marripudi, Rutvik Reddy - Swiggy Data Science Team"
source: "https://bytes.swiggy.com/hermes-a-text-to-sql-solution-at-swiggy-81573fb4fb6e"
date: "2024-07"
category: "data-analysis"
tags: ["rag", "text-to-sql", "workflow-automation", "knowledge-retrieval", "production", "developer-productivity"]
description: "Charter-based multi-stage RAG system delivering SQL queries in <2 minutes via Slack, serving hundreds of users across product, DS, and analyst teams"
problem_type: "Data-driven decisions requiring specific numbers from SQL queries, with users lacking table knowledge, access, or SQL skills"
architecture_pattern: "multi-stage-rag-with-domain-charters"
key_components: ["charter-compartmentalization", "knowledge-base", "multi-stage-retrieval", "query-validation", "slack-integration"]
breakthrough_insight: "Compartmentalizing by business charters (Swiggy Food, Instamart, etc.) with charter-specific metadata dramatically improved performance vs kitchen-sink approach treating all data uniformly"
anti_patterns_avoided: ["monolithic-metadata", "generic-cross-domain-models", "no-query-validation", "ignoring-metadata-quality"]
tech_stack:
  llms: ["GPT-4o", "GPT-3.5 (V1)"]
  frameworks: ["Databricks", "AWS Lambda"]
  infrastructure: ["Slack", "Snowflake", "Vector embeddings"]
  methods: ["RAG", "Few-shot prompting", "Vector similarity search"]
scale_metrics:
  users: "Hundreds of users"
  queries_processed: "Several thousand queries"
  turnaround_time: "<2 minutes average"
  user_types: "Product managers, data scientists, analysts"
---

# Swiggy Hermes - Charter-Based Text-to-SQL with Multi-Stage RAG

## The Problem

As a data-driven company, Swiggy teams needed to access specific numbers and quantities for business and product decisions. Questions like "How many customers were impacted by a telco outage and missed receiving order-specific updates last month?" or "What is the P95 of customer claims in a certain cohort of restaurants in a particular region?" required SQL queries. Without Hermes, users faced multiple time-consuming paths: hope to find an existing dashboard, write the query themselves (requiring table knowledge, access permissions, and SQL skills), or request an analyst to pull the data - all taking anywhere from minutes to days. This bottleneck meant important questions went unasked or were answered with proxy (or worse, incorrect) information.

**The Manual Process:**
- Search for existing dashboards or reports hoping to find the answer
- If writing SQL: identify relevant databases and tables from hundreds available
- Obtain necessary access permissions to query the data
- Learn SQL syntax and write the query correctly
- Debug and iterate when queries fail or return incorrect results
- Alternative: Submit request to analyst and wait for their availability (can take days)
- Many important questions simply not asked due to friction

**Key Pain Points:**
- **Data accessibility barrier** - Non-technical teams dependent on analysts for data access
- **Decision-making delays** - Time-to-insight ranging from minutes to days
- **SQL knowledge requirement** - Product managers and business teams lacked SQL skills
- **Table discovery challenge** - Hundreds of tables across multiple business domains (Food, Instamart, Genie, etc.)
- **Context complexity** - Metrics and tables for Food Marketplace similar but distinct from Instamart, requiring domain-specific understanding
- **Questions going unasked** - Friction led to self-regulation or settling for proxy/incorrect information

## The Solution

Swiggy built Hermes, a generative AI workflow that allows users to ask questions in natural language via Slack and receive both generated SQL queries and results from automatic execution. The system evolved from V1 (simple RAG) to V2 (charter-based multi-stage RAG) addressing the complexity of Swiggy's data landscape through compartmentalization by business domain.

**Impact**: Hundreds of users across product managers, data scientists, and analysts processing several thousand queries with average turnaround time <2 minutes. Charter-based compartmentalization (Swiggy Food, Instamart, etc.) with charter-specific metadata dramatically improved performance vs. kitchen-sink approach. First-shot acceptance rate increased significantly as implementation improved and users became familiar with the system.

## How It Works

**Key Capabilities:**
- **Charter Compartmentalization** - Separate metadata and models for each business unit (Swiggy Food, Instamart, Genie, etc.) addressing distinct business needs and data sources
- **Knowledge Base** - Charter-specific metadata including metrics, tables, columns, reference SQL queries
- **Multi-Stage Retrieval** - Metrics retrieval → Table/column retrieval → Few-shot SQL retrieval → Structured prompt creation
- **Query Validation** - Generated SQL validated by running on database, errors relayed back to LLM for correction with retries
- **Slack Integration** - Users ask questions and receive SQL + results directly in Slack without breaking workflow
- **Automated Onboarding** - Cron ensures queries for all metrics accurately generated and sent for QA validation when new charter onboarded

**Process Flow (V2 Multi-Stage RAG):**
1. **User Question via Slack** - User types natural language prompt (e.g., "What was the average rating last week in Bangalore for orders delivered 5 mins earlier than promised?")
2. **Charter Identification** - Determine which business charter (Food, Instamart, etc.) based on user context
3. **Metrics Retrieval** - Leverage knowledge base to fetch relevant metrics using embedding-based vector lookup, retrieve associated queries and historical SQL examples
4. **Table & Column Retrieval** - Identify necessary tables and columns using metadata descriptions, combine LLM querying, filtering, and vector-based lookup; for large tables make multiple LLM calls to avoid token limits
5. **Column Matching** - Match column descriptions with user questions and metrics using vector search to ensure all relevant columns identified
6. **Few-Shot SQL Retrieval** - Vector-based retrieval of ground-truth/verified reference queries for key metrics
7. **Structured Prompt Creation** - Compile gathered information into structured prompt, query database for data snapshots, send to LLM for SQL generation
8. **Query Validation** - Run generated SQL on database; if errors occur, relay back to LLM for correction with set number of retries
9. **Results Delivery** - Once executable SQL obtained, run query and deliver SQL + results to user in Slack; if retries fail, share query with modification notes
10. **Feedback Collection** - Collect accuracy feedback from users directly in Slack bot for evaluation and improvement

**Technical Architecture:** Three-layer system with (1) Slack UI for natural language input, (2) AWS Lambda middleware for request processing and formatting, and (3) Databricks pipeline where charter-specific GenAI model (GPT-4o) fetches metadata from knowledge base, performs multi-stage retrieval, generates SQL, validates execution, and returns results. Charter compartmentalization enables modular product lifecycle management - onboard new charters, test outputs, and continuously adjust knowledge base independently.

**Evolution from V1 to V2:**
- **V1**: Simple RAG with user-provided metadata, GPT-3.5, straightforward vector search
- **V1 Problems**: Performance declined with query complexity; kitchen-sink approach treating all business domains uniformly didn't work; massive volume of tables/columns/metrics required Swiggy-specific context
- **V2 Solution**: Charter-based compartmentalization, knowledge base with charter-specific metadata, multi-stage retrieval pipeline, GPT-4o, query validation with retries

**Metadata Importance:**
- **Contextual understanding**: Table names, column names, descriptions help model map natural language to database structures
- **Disambiguation**: Clarifies whether 'sales' refers to table or column, which business domain
- **Accuracy**: Comprehensive metadata improves query precision, reduces errors and manual corrections
- **Scalability**: Standardized metadata enables scaling across different charters without extensive reconfiguration

## Key Insight

**Compartmentalizing by business charters (Swiggy Food, Instamart, etc.) with charter-specific metadata dramatically improved performance vs kitchen-sink approach treating all data uniformly.** The sheer volume of data, tables, and columns combined with necessity to incorporate Swiggy-specific context (Food Marketplace metrics differ from Instamart but are similar) meant treating all business needs and data as the same did not work. Charter-based approach validated that table metadata generated through data governance efforts was crucial to overall performance, and that overall performance heavily depends on complexity of use cases and quality of metadata in the knowledge base.

**Why This Matters:**
- **Domain specificity trumps generalization** - Business units have distinct needs and data models requiring separate treatment
- **Metadata quality is the bottleneck** - Performance heavily depends on quality of charter-specific metadata, not just model sophistication
- **Modular lifecycle management** - Charter compartmentalization enables independent onboarding, testing, and iteration per business unit
- **User adoption through clarity** - Clear, straightforward prompts from users provide better instructions to model vs. ambiguous prompts

**User Adoption Patterns:**
- **Product Managers & Business Teams**: Sizing numbers for initiatives, post-release validations, quick metric check-ins across dimensions (cities, time slots, customer segments)
- **Data Scientists**: Independent deep dives into discrepancies (predicted vs actual delivery times), gathering examples for RCAs (orders with delays), detailed investigations (specific geographies)
- **Analysts**: Answering specific questions during analysis, streamlining validation process, tracking trends, analyzing metric distributions

**Upcoming Improvements:**
- **Historical query knowledge base**: Leverage corpus of historical queries as few-shot examples
- **Query explanation layer**: Provide logic behind query construction to drive user confidence and improve future queries
- **ReAct agent**: Enhance column retrieval and summarization to reduce noise in final prompt, improving accuracy

## Links

- [Original Blog Post](https://bytes.swiggy.com/hermes-a-text-to-sql-solution-at-swiggy-81573fb4fb6e) - Technical deep dive into Hermes V1 and V2 architecture
- [Hermes V3 Follow-up](https://bytes.swiggy.com/hermes-v3-building-swiggys-conversational-ai-analyst-6c5e6b8e0a3e) - Subsequent iteration building conversational AI analyst capabilities
