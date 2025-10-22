---
title: "Pinterest Text-to-SQL in Querybook"
company: "Pinterest"
author: "Adam Obeng, J.C. Zhong, Charlie Gu - Pinterest Data Platform Team"
source: "https://medium.com/pinterest-engineering/how-we-built-text-to-sql-at-pinterest-30bad30dabff"
date: "2024-04"
category: "data-analysis"
tags: ["rag", "text-to-sql", "semantic-search", "knowledge-retrieval", "production", "developer-productivity"]
description: "RAG-enhanced Text-to-SQL achieving 40%+ first-shot acceptance rate and 35% task completion speed improvement through table metadata optimization"
problem_type: "Data analysts struggling to find correct tables among hundreds of thousands and translate analytical problems into efficient SQL"
architecture_pattern: "rag-enhanced-text-to-sql"
key_components: ["vector-table-search", "llm-table-summarization", "metadata-enrichment", "streaming-response", "offline-vector-indexing"]
breakthrough_insight: "Table documentation quality trumps model sophistication - weighting embeddings toward table metadata increased search hit rate from 40% to 90%, proving data governance is the bottleneck for Text-to-SQL performance"
anti_patterns_avoided: ["generic-embeddings-only", "ignoring-table-documentation", "synchronous-response-generation", "benchmark-only-evaluation"]
tech_stack:
  llms: ["GPT (unspecified version)"]
  frameworks: ["LangChain"]
  infrastructure: ["OpenSearch (vector store)", "WebSocket", "Querybook (open source)"]
  methods: ["RAG", "Partial JSON parsing", "Embedding similarity search"]
scale_metrics:
  tables_in_warehouse: "Hundreds of thousands"
  first_shot_acceptance: "20% → 40%+"
  task_speed_improvement: "35%"
  top_tier_tables_indexed: "Tiered subset"
  metadata_hit_rate_improvement: "40% → 90%"
---

# Pinterest Text-to-SQL in Querybook

## The Problem

Writing queries to solve analytical problems is the core task for Pinterest's data users, yet finding the right data and translating analytical problems into correct and efficient SQL code proved challenging in a fast-paced environment. With hundreds of thousands of tables spread across different domains, data analysts spent significant time hunting for the correct tables before even beginning to write queries, while also struggling to encode complex business logic correctly.

**The Manual Process:**
- Browse through hundreds of thousands of tables in the data warehouse to find relevant datasets
- Manually read table schemas, column descriptions, and sample queries to understand table purpose
- Translate analytical questions into SQL code, encoding domain-specific logic and extraction conditions
- Debug and iterate on queries when initial attempts fail or return incorrect results
- Repeat process for each new analytical task across different business domains

**Key Pain Points:**
- **Table discovery challenge** - Finding the right tables among hundreds of thousands was overwhelming for analysts
- **Domain knowledge barrier** - Understanding which tables contained relevant data required deep institutional knowledge
- **SQL translation difficulty** - Converting natural language analytical questions into correct SQL syntax and logic was time-consuming
- **Efficiency concerns** - Writing performant queries on large datasets required optimization expertise
- **Fast-paced environment** - Business needs demanded quick answers, but data exploration took hours or days

## The Solution

Pinterest built a Text-to-SQL feature integrated into Querybook (their open-source big data SQL query tool) using LLMs enhanced with RAG for intelligent table discovery. The system evolved from simple schema-based generation to a two-stage architecture that first finds relevant tables via vector similarity search, then generates optimized SQL queries.

**Impact**: First-shot acceptance rate increased from 20% to above 40% as the implementation improved and users became familiar with the feature. Real-world data showed 35% improvement in task completion speed for writing SQL queries using AI assistance (compared to 50%+ in controlled research experiments). Table documentation weighting in embeddings proved critical - search hit rate jumped from 40% without documentation to 90% with proper metadata weighting, demonstrating that data governance quality is the primary performance bottleneck.

## How It Works

**Key Capabilities:**
- **Metadata-Enriched Table Schemas** - Includes table/column descriptions, low-cardinality column values for precise filtering, and column pruning for context window management
- **Streaming Response Generation** - WebSocket-based streaming with LangChain partial JSON parsing to avoid 10+ second wait times
- **RAG-Based Table Discovery** - Offline vector indexing of table summaries and historical queries, with similarity search and LLM re-selection
- **Table/Query Summarization** - LLM-generated summaries of table purpose and use cases from schemas + sample queries
- **Tiered Table Indexing** - Only top-tier tables indexed to promote high-quality datasets

**Process Flow (V2 with RAG):**
1. **Offline Vector Index Creation** - Background job generates embeddings for: (a) LLM-generated table summaries (from schema + sample queries), (b) LLM-generated query summaries (purpose + tables used)
2. **User Question** - Analyst asks analytical question (e.g., "How many active users are on the web platform?")
3. **Table Search (if not specified)** - Question converted to embeddings, similarity search against vector index returns top N candidate tables
4. **LLM Table Re-selection** - GPT evaluates top N table summaries against question, selects most relevant K tables
5. **User Validation** - Top K tables returned to user for confirmation or modification
6. **Schema Retrieval** - Fetch table schemas from metadata store including: table/column names/descriptions, column types, low-cardinality column unique values
7. **Prompt Construction** - Compile question + SQL dialect + table schemas into Text-to-SQL prompt
8. **SQL Generation** - LLM generates query with streaming response via WebSocket (partial JSON parsing)
9. **Display to User** - Structured response (SQL + explanation) displayed in real-time

**Technical Architecture:** Two-tier system with (1) offline indexing pipeline running scheduled jobs to generate and store table/query summaries in OpenSearch vector store with embedding-based similarity search, and (2) real-time generation pipeline using LangChain for streaming LLM responses with WebSocket transport and partial JSON parsing to handle structured outputs during streaming.

**Metadata Optimization Techniques:**
- **Low-cardinality value injection**: Include unique values for frequently-filtered columns (e.g., `platform` values: 'WEB', 'MOBILE', 'TABLET') to prevent incorrect WHERE clauses
- **Column pruning**: Tag and exclude certain columns from schemas to stay within context window limits
- **Reduced schema version**: Fallback to minimal schema (table name, column name, type only) for extremely large tables
- **Documentation weighting**: Embeddings weighted heavily toward table documentation increased hit rate 40% → 90%

## Key Insight

**Table documentation quality trumps model sophistication - weighting embeddings toward table metadata increased search hit rate from 40% to 90%, proving data governance is the primary bottleneck for Text-to-SQL performance.** While benchmark datasets like Spider suggest Text-to-SQL is a solved problem with off-the-shelf LLMs, real-world deployment at Pinterest revealed that table discovery (finding the right tables among hundreds of thousands) and metadata quality (ensuring descriptions accurately reflect table purpose and column meanings) are far more critical than prompt engineering or model selection for production systems.

**Why This Matters:**
- **Real-world differs from benchmarks** - Spider dataset uses small number of pre-specified, well-normalized tables; production systems face hundreds of thousands of denormalized tables requiring discovery as core challenge
- **Data governance is the foundation** - Investment in table descriptions, column documentation, and business terminology standardization directly drives Text-to-SQL performance
- **Embeddings need structure** - Generic embedding similarity alone yielded 40% hit rate; weighting toward curated metadata achieved 90%, showing human-created documentation outweighs pure semantic similarity
- **Iterative user behavior is normal** - 20-40% first-shot acceptance is reasonable; most queries require multiple iterations whether human or AI-generated

**Evaluation Challenges:** Team noted that existing benchmarks (Spider, etc.) treat small numbers of well-labeled tables as given, failing to capture the table discovery challenge central to real-world Text-to-SQL. They advocate for more realistic benchmarks including larger denormalized table sets and treating table search as core evaluation criteria.

**Future Improvements Identified:**
- Metadata enhancement: Include tiering, tags, domains in vector index for refined filtering
- Scheduled/real-time index updates: Currently manual; automation needed for new tables/queries
- Similarity scoring strategy: Current aggregation is basic; fine-tuning could improve relevance
- Query validation: No validation currently; constrained beam search could catch errors
- User feedback loops: UI for collecting feedback to improve vector index and metadata

## Links

- [Original Blog Post](https://medium.com/pinterest-engineering/how-we-built-text-to-sql-at-pinterest-30bad30dabff) - Technical deep dive into Text-to-SQL implementation
- [Querybook (Open Source)](https://github.com/pinterest/querybook) - Pinterest's open-source big data SQL query tool where Text-to-SQL is deployed
- [Table Summarization Prompt](https://gist.github.com/pnxenopoulos/81e6fa76bf1b8ec8afaab34b6a72f5a9) - Actual prompt used for LLM table summarization
- [Query Summarization Prompt](https://gist.github.com/pnxenopoulos/b2d5a0e3c653f11b0a12ee30eafd3be0) - Actual prompt used for query summarization
- [Text-to-SQL Prompt](https://gist.github.com/pnxenopoulos/41a51cd0095569da07a5e6b0c18a827f) - Actual prompt used for SQL generation
- [Spider Benchmark Reference](https://yale-lily.github.io/spider) - Academic benchmark showing gap between research and production reality
