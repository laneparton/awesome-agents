---
title: "Uber QueryGPT - Multi-Agent Natural Language to SQL"
company: "Uber"
author: "Jeffrey Johnson, Callie Busch, Abhi Khune, Pradeep Chakka - Uber Data Platform Team"
source: "https://www.uber.com/en-IN/blog/query-gpt/"
date: "2024-09"
category: "data-analysis"
tags: ["multi-agent", "text-to-sql", "rag", "workflow-automation", "production", "developer-productivity"]
description: "Multi-agent system with Intent, Table, and Column Prune agents reducing SQL authoring from 10 minutes to 3 minutes with 78% user satisfaction"

# Problem Classification
problemPattern: "text-to-sql"
problemComplexity: "complex"

# Architecture
architecture:
  type: "multi-agent"
  pattern: "specialized-classifiers"
  rationale: "LLMs excel as specialized classifiers with single units of work - decomposing into Intent (domain mapping), Table Selection (human-in-loop validation), and Column Prune (token management) agents dramatically improved accuracy over monolithic; Workspaces (domain-specific collections) narrow search radius; 20+ iterations from hackathon to production optimized each agent; human-in-loop at table selection catches errors before expensive generation"
  components: ["intent-agent", "table-agent", "column-prune-agent", "workspaces", "rag-similarity-search", "human-in-the-loop-validation", "vector-database"]

# What Made It Work
breakthroughInsight: "LLMs excel as specialized classifiers when given single units of work - decomposing query generation into Intent (domain classification), Table Selection (schema identification), and Column Pruning (token reduction) agents dramatically improved accuracy over monolithic approach; Workspaces (domain-scoped collections) essential for narrowing search radius among hundreds of thousands of tables; human-in-loop validation at table selection stage catches errors before expensive generation; 20+ algorithm iterations between hackathon and production refined each specialized agent"

criticalConstraints:
  - "1.2m-monthly-queries"
  - "hundreds-thousands-tables"
  - "200-plus-column-schemas"
  - "40-60k-token-schemas"
  - "32k-early-token-limits"
  - "business-terminology-gap"
  - "domain-knowledge-required"
  - "10-minute-query-authoring"

antiPatterns:
  - "monolithic-generation: Single LLM generating SQL from all tables failed - accuracy declined as tables added; specialized agents (Intent, Table, Column) with single-unit focus dramatically improved results"
  - "simple-rag-only: Similarity search on schemas/SQL without domain organization underperformed - Workspaces (domain-specific collections) narrowing search radius essential for hundreds of thousands of tables"
  - "no-domain-organization: Without Workspaces grouping tables by business domain, search space too large for effective RAG retrieval among hundreds of thousands of tables"
  - "ignoring-token-limits: 200+ column schemas consume 40-60K tokens exceeding 32K early limits - Column Prune agent removing irrelevant columns essential for token management"
  - "no-human-validation: Errors in table selection propagate to expensive query generation - human-in-loop at table stage catches mistakes early"

# Tech Stack
techStack:
  framework: "custom-multi-agent"
  llmProvider: "GPT-4-Turbo-128K"
  knowledgeRetrieval: "rag-with-workspaces"
  otherTools: ["vector-database", "k-NN-similarity", "few-shot-prompting", "Workspaces-domain-collections", "column-pruning"]

# Scale
scale:
  volume: "1.2M monthly queries, ~300 daily active users (limited release), 36% operations contribution, 20+ algorithm iterations hackathon→production"
  latency: "10 min → 3 min per query, 78% user satisfaction reporting reduced time"
---

# Uber QueryGPT - Multi-Agent Natural Language to SQL

## The Problem

At Uber, the data platform handles approximately 1.2 million interactive queries each month, with the Operations organization alone contributing about 36% of these queries. Authoring SQL queries requires not only solid understanding of SQL syntax but deep knowledge of how Uber's internal data models represent business concepts. Each query takes around 10 minutes to author between searching for relevant datasets in the data dictionary and writing the query. With hundreds of thousands of datasets across the organization, finding the right tables and understanding their schemas creates significant productivity drag.

**The Manual Process:**
- Search through data dictionary to identify relevant datasets among hundreds of thousands of tables
- Read table schemas, understand column meanings, and map business concepts to data model
- Write SQL query with correct syntax, joins, filters, and aggregations
- Debug and iterate when queries fail or return incorrect results
- Repeat process for each analytical question across different business domains
- Average 10 minutes per query for experienced SQL users

**Key Pain Points:**
- **Data discovery challenge** - Finding the right tables among hundreds of thousands required extensive domain knowledge
- **Schema complexity** - Some Tier 1 tables span over 200 columns, consuming 40-60K tokens in LLM context
- **Business terminology gap** - Internal Uber lingo and business concepts must be correctly mapped to data model structures
- **Context requirements** - Queries often require joins across multiple tables and understanding of data relationships
- **Token limits** - Large schemas break LLM calls with early models supporting only 32K tokens

## The Solution

Uber built QueryGPT, a multi-agent system that decomposes natural language to SQL generation into specialized agents (Intent, Table Selection, Column Pruning) working with curated workspaces and RAG-based similarity search. The system evolved through 20+ algorithm iterations from hackathon prototype to production, reducing query authoring time from 10 minutes to 3 minutes.

**Impact**: Averaging ~300 daily active users in limited release with 78% reporting the generated queries reduced the time they would've spent writing from scratch. Multi-agent decomposition proved critical - giving LLMs single units of specialized work (intent classification, table selection, column pruning) dramatically improved accuracy over monolithic generation approach. System handles 1.2M monthly queries across Uber's data platform.

## How It Works

**Key Capabilities:**
- **Workspaces** - Curated collections of SQL samples and tables organized by business domain (Mobility, Ads, Core Services, Platform Engineering, IT, etc.) - includes 11 system workspaces + custom workspace creation
- **Intent Agent** - LLM classifier mapping user questions to one or more business domains/workspaces to narrow search radius for RAG
- **Table Agent** - LLM that identifies relevant tables and presents to user for ACK/edit before query generation (human-in-the-loop validation)
- **Column Prune Agent** - LLM that removes irrelevant columns from large schemas to reduce token consumption and latency
- **RAG with Similarity Search** - k-NN vector search on SQL samples and schemas to retrieve relevant few-shot examples
- **Evaluation Framework** - Golden question-to-SQL mappings with metrics tracking (intent accuracy, table overlap, run success, query similarity)

**Process Flow:**
1. **User Question** - User enters natural language prompt (e.g., "Find the number of trips completed yesterday in Seattle")
2. **Intent Agent** - LLM maps question to business domain/workspace (e.g., "Mobility" workspace for trips-related queries)
3. **Workspace Selection** - Narrow search to curated SQL samples and tables for that domain
4. **RAG Similarity Search** - k-NN search retrieves relevant SQL examples and table schemas based on question embeddings
5. **Table Agent** - LLM identifies top candidate tables, user validates or edits the list (human-in-the-loop)
6. **Column Prune Agent** - For large schemas (200+ columns), LLM prunes irrelevant columns to stay within token limits
7. **Query Generation** - Few-shot prompting with: pruned schemas + relevant SQL samples + user question + Uber business instructions
8. **Output** - Generated SQL query + explanation of how LLM generated the query
9. **Evaluation** - Track intent accuracy, table overlap, run success, output presence, qualitative similarity to golden SQL

**Technical Architecture:** Multi-agent pipeline where each agent handles specialized classification task using LLM calls. Workspaces provide domain-scoped context reducing search space. Vector database stores embeddings of SQL samples and schemas for similarity search. Human-in-the-loop validation at table selection stage catches errors before expensive query generation. Column Prune agent addresses token limit issues by reducing schema size 40-60K → manageable size.

**Evolution Journey (20+ iterations):**
- **Hackathon v1**: Simple RAG with 7 Tier 1 tables, 20 SQL samples, k-NN similarity search on schemas/queries
- **Problem**: Accuracy declined as more tables added; simple similarity search on schemas/SQL didn't work well; large schemas broke 32K token limit
- **Current Design**: Workspaces for domain organization + Intent Agent for classification + Table Agent for validation + Column Prune Agent for token management + improved RAG

**Evaluation Methodology:**
- **Vanilla Flow**: Measures baseline - input question → infer intent/datasets → generate SQL → evaluate all
- **Decoupled Flow**: Human-in-the-loop - input question + actual intent/datasets → generate SQL → enables component-level evaluation
- **Metrics**: Intent accuracy, Table Overlap Score (0-1 based on correct tables selected), Successful Run, Run Has Output (>0 records), Qualitative Query Similarity (LLM-based score 0-1)
- **Golden Set**: Manually curated question-to-SQL mappings covering variety of datasets and business domains

## Key Insight

**LLMs excel as specialized classifiers when given single units of work - decomposing query generation into Intent, Table Selection, and Column Pruning agents dramatically improved accuracy over monolithic approach.** The Intent Agent, Table Agent, and Column Prune Agent each performed excellently because they were asked to work on a single unit of specialized work rather than a broad generalized task. This pattern of breaking down complex generation into specialized agents proved more effective than trying to solve everything in one LLM call.

**Why This Matters:**
- **Specialization over generalization** - Intermediate agents that decompose user prompts into better signals for RAG improved accuracy significantly from first version
- **Token management is critical** - Column Prune agent not only solved token limit issues but also reduced cost and latency by providing smaller, more focused context
- **Domain organization scales** - Workspaces allowed targeting 1.2M monthly queries by narrowing search radius to relevant business domains
- **Human-in-the-loop catches errors early** - Table Agent validation prevents expensive query generation with wrong datasets

**Known Challenges:**
- **Hallucinations persist** - LLM sometimes generates queries with non-existent tables or columns; experimenting with validation agent for recursive fixing
- **User prompts lack context** - Questions range from detailed with keywords to 5-word queries with typos; "prompt enhancer" needed to massage questions before sending to LLM
- **High bar for accuracy** - Users expect generated queries to "just work"; important to target right personas for initial rollout
- **Non-deterministic evaluation** - Same evaluation run can produce different outcomes; focus on error patterns over long periods rather than 5% run-to-run changes

## Links

- [Original Blog Post](https://www.uber.com/en-IN/blog/query-gpt/) - Comprehensive technical deep dive into QueryGPT's architecture and evolution
