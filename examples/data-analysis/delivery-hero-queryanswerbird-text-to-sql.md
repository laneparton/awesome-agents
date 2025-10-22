---
title: "Delivery Hero QueryAnswerBird AI Data Analyst - Text-to-SQL"
company: "Delivery Hero (Woowa Brothers)"
author: "BADA Team (Baemin Advanced Data Analytics)"
source: "https://deliveryhero.jobs/blog/introducing-the-ai-data-analyst-queryanswerbird-part-1-utilization-of-rag-and-text-to-sql/"
date: "2024-07"
category: "data-analysis"
tags: ["multi-agent", "rag", "text-to-sql", "workflow-automation", "knowledge-retrieval", "production", "enterprise"]
description: "Multi-chain RAG architecture with Router Supervisor generating production-quality SQL queries in 30-60 seconds through domain-enriched metadata and ReAct prompting"
problem_type: "95% of employees using data but >50% unable to write SQL or validate query reliability across business domains"
architecture_pattern: "multi-chain-rag-with-router-supervisor"
key_components: ["router-supervisor", "vector-store-pipeline", "react-prompt-engineering", "llmops-infrastructure", "slack-interface"]
breakthrough_insight: "Enriching table metadata with business terminology, few-shot examples, and multi-stage retrieval algorithms transforms generic GPT-4 into domain-expert Text-to-SQL capable of production use"
anti_patterns_avoided: ["simple-prompt-only", "generic-metadata", "single-retriever", "no-evaluation-framework"]
tech_stack:
  llms: ["GPT-4o", "GPT-3.5"]
  frameworks: ["LangChain", "LangServe"]
  infrastructure: ["VectorDB", "Microsoft Azure OpenAI", "Slack API"]
  methods: ["RAG", "ReAct", "Chain-of-Thought", "Few-shot learning"]
scale_metrics:
  response_time: "30-60 seconds"
  ab_tests_conducted: "500+"
  development_timeline: "6 months (task force)"
  hackathon_result: "1st place winner"
---

# Delivery Hero QueryAnswerBird AI Data Analyst - Text-to-SQL

## The Problem

At Woowa Brothers (Delivery Hero), internal surveys revealed that 95% of employees were using data for their work, yet more than half faced critical barriers. They wanted to use SQL for data extraction but lacked time to learn it properly, struggled to generate queries that correctly reflected complex business logic and extraction conditions, and were deeply concerned about data reliability. Business terminology varied across services and organizations, creating confusion and miscommunication.

**The Manual Process:**
- Data analysts manually writing SQL queries for stakeholders across dozens of business domains
- Employees spending hours trying to learn SQL syntax while needing to focus on core work
- Repeated back-and-forth communication to clarify business requirements and data definitions
- Manual validation of query correctness and data extraction reliability
- Fragmented knowledge of table structures, column meanings, and business policies

**Key Pain Points:**
- **SQL knowledge barrier** - Technical skill required to access data prevented business users from self-service analytics
- **Business logic complexity** - Queries needed to encode domain-specific rules that only experienced analysts understood
- **Data reliability concerns** - No systematic way to validate whether extracted data matched business intent
- **Terminology inconsistency** - Same business concepts defined differently across teams, leading to incorrect queries
- **Analyst bottleneck** - Data teams overwhelmed with repetitive query requests instead of strategic analysis

## The Solution

The BADA team developed QueryAnswerBird (QAB), an LLM-based agentic AI data analyst accessible via Slack that automatically generates, interprets, and validates SQL queries while incorporating deep domain knowledge through multi-chain RAG architecture and sophisticated prompt engineering.

**Impact**: Delivers production-quality SQL queries in 30-60 seconds that employees can directly reference for their work. Won 1st place at Woowa Hackathon 2023 and was promoted to a 6-month task force with full LLMOps infrastructure. Conducted 500+ A/B tests through internal leaderboard to continuously improve performance. New employees report significant help in understanding their work domains through query generation and interpretation features.

## How It Works

**Key Capabilities:**
- **Router Supervisor** - Categorizes incoming questions in real-time and routes to specialized chains (query generation, interpretation, validation, table exploration, log guides)
- **Domain-Enriched Metadata** - Automatically collects table DDL, column descriptions, business terminology glossary, and few-shot SQL examples from data analysts
- **Multi-Stage Retrieval** - Sophisticated search algorithms refine questions, extract business terms, retrieve relevant metadata, and select similar few-shot examples
- **ReAct Prompting** - Combines chain-of-thought reasoning with dynamic data search/selection for step-by-step query generation
- **LLMOps Infrastructure** - A/B testing, leaderboard, GPT caching, feedback loops, monitoring dashboards, and CI/CD deployment

**Process Flow:**
1. **Question Input** - User asks natural language question in Slack (e.g., "Show me daily order counts by region for last week")
2. **Router Classification** - Router Supervisor chain identifies question type and routes to appropriate multi-chain
3. **Question Refinement** - If question is ambiguous/short, system extracts relevant business terms and refines the query
4. **Context Retrieval** - Multi-stage search extracts: (a) relevant business terminology, (b) table/column metadata, (c) table DDL, (d) few-shot SQL examples
5. **Query Generation** - ReAct-based prompt performs step-by-step reasoning while dynamically searching and selecting data
6. **Validation** - System validates query syntax and provides error description if issues detected
7. **Response Delivery** - Slack bot returns generated query with interpretation, validation status, and satisfaction feedback buttons
8. **Feedback Loop** - User evaluations (satisfied/unsatisfied) feed into GPT cache, expanding standardized knowledge to other users

**Technical Architecture:** Three-layer system with (1) unstructured data pipeline collecting and vectorizing metadata into VectorDB with embedding index by data area, (2) RAG-based multi-chain structure where Router Supervisor routes to specialized chains executing custom retrievers, and (3) LLMOps layer providing experiment environment, leaderboard, API load balancing, caching, and monitoring for production deployment.

**Development Approach:** Task force ran two-week sprints with task rotation to help members discover strengths and build diverse skillsets. Built custom evaluation metrics and data benchmarking public leaderboards (YALE Spider, Alibaba BIRD, RAGAS Score) but tailored to internal domain-specific problems. Automated testing system allowed anyone to evaluate performance across dozens of metrics, with gamified leaderboard encouraging 500+ A/B tests.

## Key Insight

**Enriching table metadata with business terminology, few-shot examples from domain experts, and multi-stage retrieval algorithms transforms generic GPT-4 into a domain-expert Text-to-SQL system capable of production use.** Simply using GPT-4 alone produces queries that lack company context, ignore data policies, and suffer from hallucinations, but the combination of (1) augmented documentation with detailed column descriptions and business glossaries, (2) sophisticated search algorithms that refine questions and select relevant examples, and (3) ReAct prompting that reasons step-by-step while dynamically retrieving context enables query quality that employees trust for actual work.

**Why This Matters:**
- **"Garbage in, garbage out" for LLMs** - Foundation model performance is capped by input quality; enriched metadata is more important than model sophistication
- **Domain knowledge > generic capability** - GPT-4 can write SQL syntactically, but production queries require business logic, policies, and terminology that must be injected through RAG
- **Multi-stage retrieval prevents hallucination** - Refining questions, extracting terms, filtering metadata, and selecting examples at different stages reduces irrelevant context that causes errors
- **Evaluation-driven development works** - Custom metrics, automated testing, and gamified leaderboards enabled 500+ experiments to systematically improve a complex multi-chain system

**Known Challenges:** Initial user feedback indicated room for improvement in accuracy of business logic understanding and question interpretation. Team is conducting ongoing tasks to enhance performance through various methods and tests based on question histories. Data discovery questions (exploring tables, understanding columns) emerged as significant use case beyond query generation, leading to Part 2 expansion of capabilities.

## Links

- [Original Blog Post - Part 1](https://deliveryhero.jobs/blog/introducing-the-ai-data-analyst-queryanswerbird-part-1-utilization-of-rag-and-text-to-sql/) - Detailed technical breakdown of Text-to-SQL architecture and development process
- [Cited Paper: Data Ambiguity Strikes Back](https://neurips.cc/virtual/2023/poster/73502) - NeurIPS 2023 paper on improving GPT Text-to-SQL through documentation (referenced in metadata enrichment approach)
- [Cited Paper: ReAct](https://arxiv.org/abs/2210.03629) - ICLR 2023 paper on synergizing reasoning and acting in LLMs (foundation for prompt engineering approach)
