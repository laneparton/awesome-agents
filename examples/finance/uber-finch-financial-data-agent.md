---
title: "Finch - Conversational Financial Data Agent"
company: "Uber"
author: "Uber FinTech Team"
source: "https://www.datatinkerer.io/p/how-uber-built-an-ai-agent-that-answers"
date: "2025-01"
category: "finance"
tags: ["workflow-automation", "rag", "knowledge-retrieval", "multi-agent", "enterprise", "production"]
description: "Slack-native multi-agent system delivering real-time financial intelligence with semantic metadata layer eliminating SQL complexity"

# Problem Classification
problemPattern: "workflow-automation"
problemComplexity: "complex"

# Architecture
architecture:
  type: "multi-agent"
  pattern: "supervisor-worker"
  rationale: "Supervisor agent routes queries to specialized sub-agents (SQL Writer) while OpenSearch metadata layer provides semantic mapping from finance terminology to structured data sources"
  components: ["supervisor-agent", "sql-writer-agent", "opensearch-metadata", "data-marts", "slack-integration", "rbac-layer"]

# What Made It Work
breakthroughInsight: "Semantic metadata layer storing natural language aliases for both column names and enumerated values in OpenSearch dramatically improved WHERE clause accuracy - solving the classic LLM-SQL precision challenge"

criticalConstraints:
  - "fragmented-data-across-platforms"
  - "finance-domain-terminology"
  - "role-based-access-control-required"
  - "predictable-latency-non-negotiable"
  - "no-new-tool-sprawl"

antiPatterns:
  - "complex-multi-table-joins: single-table data marts reduce query complexity and enable faster LLM-generated SQL"
  - "generic-chatbot-approach: live data retrieval with dynamic query planning beats static responses"

# Tech Stack
techStack:
  framework: "LangGraph"
  llmProvider: "Uber GenAI Gateway"
  knowledgeRetrieval: "RAG"
  otherTools: ["OpenSearch", "Presto", "IBM Planning Analytics", "Oracle EPM", "Google Sheets", "Slack SDK"]

# Scale
scale:
  volume: "Uber finance teams - eliminates analyst data request queues"
  latency: "real-time with progress updates via Slack callbacks"
---

# Finch - Conversational Financial Data Agent

## The Problem

Uber's finance teams faced fragmented data access across multiple platforms (Presto, IBM Planning Analytics, Oracle EPM, Google Docs). Analysts experienced significant delays hunting for the right datasets, wrestling with SQL query complexity, and waiting in queues for data specialists to fulfill requests. Context-switching between systems and latency in data retrieval created bottlenecks in financial decision-making.

**The Manual Process:**
- Analysts identify financial question requiring data
- Hunt across multiple platforms for relevant datasets
- Request help from data specialists if SQL knowledge insufficient
- Wait in queue for specialist to write and execute queries
- Context-switch between different tools and platforms
- Repeat process for each new question or dimension

**Key Pain Points:**
- Data fragmented across incompatible platforms (Presto, IBM Planning Analytics, Oracle EPM)
- SQL expertise required for self-service data access
- Internal finance terminology not mapped to database schemas
- Queue delays waiting for data specialist support
- No unified interface for financial data retrieval
- Context-switching reduces productivity and increases errors

## The Solution

Finch is a Slack-native multi-agent system that transforms natural language queries into structured data retrieval, delivering secure real-time financial intelligence. Users ask questions like "What was GB value in US&C in Q4 2024?" and Finch dynamically maps finance terminology to structured sources, generates SQL, and returns results with full transparency.

**Impact**: Eliminated analyst data request queues by enabling self-service financial insights through conversational interface, reducing friction and delays in data-driven decision-making.

## How It Works

**Key Capabilities:**
- **Multi-Agent Orchestration** - Supervisor Agent routes queries to specialized sub-agents (SQL Writer Agent)
- **Semantic Metadata Layer** - OpenSearch index stores column names, value vocabularies, and natural language aliases
- **Domain Terminology Mapping** - Internal finance terms ("US&C" → US/Canada, "GBs" → gross bookings) map to structured schemas
- **Real-Time Progress Updates** - Slack callback handlers display agent execution steps, providing transparency
- **Role-Based Access Control** - Enforces permissions pre-execution with full query auditability
- **Smart Data Organization** - Single-table data marts reduce complexity and enable faster LLM-generated SQL

**Process Flow:**
1. User asks natural language question in Slack (e.g., "What was GB value in US&C in Q4 2024?")
2. Supervisor Agent receives query and classifies intent
3. Routes to SQL Writer Agent for data retrieval
4. SQL Writer queries OpenSearch metadata index for relevant aliases and column mappings
5. Generates SQL query using finance terminology → database schema mappings
6. Validates user permissions (RBAC) before execution
7. Executes query against appropriate data source (Presto, IBM Planning Analytics, Oracle EPM)
8. Returns results with visible SQL and source attribution
9. Optionally exports to Google Sheets for larger datasets
10. Slack displays progress updates in real-time throughout execution

**Technical Architecture:** LangGraph orchestrates Supervisor and SQL Writer agents. OpenSearch provides semantic metadata layer mapping natural language finance terms to database schemas. Single-table data marts optimize for simplicity and performance. Uber GenAI Gateway abstracts LLM access. Slack SDK integration with callback handlers provides real-time progress visibility.

## Key Insight

**Semantic metadata layer with natural language aliases for columns AND values solves LLM-SQL precision challenges.** Storing finance terminology mappings in OpenSearch dramatically improved WHERE clause accuracy by providing context for both schema elements and enumerated values.

**Why This Matters:**
- Generic LLM-to-SQL struggles with ambiguous WHERE clauses; semantic layer provides necessary context
- Finance domain has specialized terminology ("US&C", "GBs") that doesn't appear in schemas
- Single-table data marts reduce query complexity, enabling faster LLM generation and easier error correction
- Real-time Slack progress updates reduce perceived latency and build user trust
- Parallel sub-task execution and prefetching frequently accessed metrics minimize database load

**Testing Strategy:** Sub-agent accuracy validation against expected outputs, routing decision verification to prevent intent collisions, end-to-end simulation of real-world queries, regression testing on historical queries before model/prompt updates.

**Competitive Differentiation:** Unlike generic chatbots or traditional BI tools, Finch retrieves live data with dynamic query planning, operates natively in Slack where teams already collaborate, and enforces enterprise security through granular RBAC—all without introducing new tool sprawl.

## Links

- [Original Article](https://www.datatinkerer.io/p/how-uber-built-an-ai-agent-that-answers) - How Uber Built an AI Agent That Answers Financial Questions in Slack
- [Uber Engineering Twitter](https://x.com/UberEng/status/1945883033921527909) - Finch announcement
