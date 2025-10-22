---
title: "Dropbox Dash - RAG and Multi-Step AI Agents for Business Knowledge Management"
company: "Dropbox"
author: "Ranjitha Gurunath Kulkarni and James Johnson - Dropbox Engineering"
source: "https://dropbox.tech/machine-learning/building-dash-rag-multi-step-ai-agents-business-users"
date: "2025-04"
category: "research"
tags: ["workflow-automation", "agent-framework", "rag", "knowledge-retrieval", "code-generation", "multimodal", "production"]
description: "Multi-step AI agents using custom Python DSL achieve <2 second response time for 95% of queries, enabling autonomous task execution across fragmented business data"
problem_type: "Information scattered across multiple applications making document discovery tedious, hindering collaboration, productivity, and creating security risks"
architecture_pattern: "multi-step-orchestration-with-dsl-code-generation"
key_components: ["rag-retrieval", "llm-planning", "dsl-execution", "static-analysis", "security-controls"]
breakthrough_insight: "Two-stage approach where LLMs generate code in custom DSL allows agents to 'show their work', enabling deterministic testing, clearer debugging, and enhanced security through static analysis"
anti_patterns_avoided: ["purely-semantic-retrieval", "purely-lexical-retrieval", "full-featured-interpreter-security-risks", "non-deterministic-testing"]
tech_stack:
  llms: ["Multiple LLMs (model-agnostic)"]
  frameworks: ["Custom Python DSL", "Custom Python interpreter"]
  infrastructure: ["Traditional IR with reranking", "Embedding models", "Vector search"]
  methods: ["RAG", "On-the-fly chunking", "Static analysis", "Runtime type enforcement"]
scale_metrics:
  latency: "<1-2 seconds for 95% of queries"
  capabilities: "Multi-step autonomous task execution"
  data_coverage: "Multiple apps, diverse data types and modalities"
---

# Dropbox Dash - RAG and Multi-Step AI Agents for Business Knowledge Management

## The Problem

Knowledge workers face significant challenges managing their digital workflows. Information is scattered across multiple applications and formats—emails, documents, meeting notes, task management data—making it tedious and time-consuming to find the right document, message, or piece of information. This fragmentation creates collaboration barriers, productivity losses, and potential security issues when sensitive information surfaces unintentionally.

**The Manual Process:**
- Search for information across multiple disconnected applications
- Context switch between different tools and services to locate relevant data
- Manually synthesize information from various sources to answer complex questions
- Struggle with diverse data types (text, images, presentations, videos) each requiring different search approaches
- Navigate access permissions and security controls across different systems
- Repeat searches when information needs updating or verification

**Key Pain Points:**
- **Information fragmentation** - Relevant data spread across multiple apps, not in single location
- **Time-consuming discovery** - Finding specific documents or information requires extensive searching
- **Context switching overhead** - Constantly moving between applications disrupts workflow efficiency
- **Data diversity complexity** - Different data types (emails, docs, videos) each have unique structures requiring different approaches
- **Security risks** - Difficult to ensure employees and partners see only appropriate content
- **Collaboration barriers** - Fragmented information prevents effective team collaboration and knowledge sharing

## The Solution

Dropbox built Dash, a universal search and knowledge management product combining RAG with multi-step AI agents to help knowledge workers organize their digital lives. The system allows users to find, organize, share, and secure content across apps through AI-powered search with advanced filtering, granular access controls, and autonomous multi-step task execution. The agents use a two-stage approach (planning and execution) where LLMs generate code in a custom Python-like domain-specific language (DSL), enabling autonomous breakdown of complex queries into actionable steps.

**Impact**: <1-2 seconds latency for 95% of queries, autonomous execution of complex multi-step tasks requiring domain knowledge and contextual information, comprehensive coverage across diverse data types and modalities (text, images, audio, video), enhanced security through granular access controls and static code analysis.

## How It Works

**Key Capabilities:**
- **RAG-Powered Search** - Traditional information retrieval combined with on-the-fly chunking and embedding-based reranking, maintaining <2 second latency for 95% of queries
- **Multi-Step Orchestration** - AI agents autonomously break down complex queries into individual steps using LLM-generated code in custom Python DSL
- **Two-Stage Execution** - Planning stage (LLM generates high-level DSL code statements) followed by execution stage (validation via static analysis, detection of missing functionality, LLM implements gaps)
- **Security Controls** - Custom Python interpreter with minimal required functionality, static analysis passes, runtime type enforcement, and security reviews
- **Multimodal Support** - Processes text, images, audio, and video data across fragmented business applications
- **Access Control Integration** - Granular permissions ensure employees and external partners see only appropriate content

**Process Flow (Multi-Step Agent Example):**
1. **User Query** - User asks complex question like "Show me the notes for tomorrow's all-hands meeting"
2. **Planning Stage** - LLM interprets query and generates Python-like DSL code expressing logic: resolve "tomorrow" to concrete dates, identify meeting matching "all-hands" in time window, retrieve attached documents
3. **Code Validation** - Static analysis examines generated code to identify security risks, missing functionality, or correctness errors without executing
4. **Missing Functionality Detection** - If missing capabilities identified, LLM called second time to implement the missing code
5. **Execution Stage** - Interpreter executes validated code step-by-step with runtime type enforcement
6. **Step-by-Step Results** - Each code statement executes: time window retrieval returns concrete dates, meeting identification searches calendar, document retrieval fetches notes
7. **Response Generation** - Final response (list of documents) returned to user with type guarantees
8. **Feedback Loop** - Code execution path enables "showing the work" for debugging and evaluation

**RAG Architecture:** Traditional lexical-based IR system combined with on-the-fly document chunking at query time (pulling only relevant sections) and reranking using larger embedding models to place most relevant chunks at top. This hybrid approach balances speed and relevance, achieving high-quality results in <2 seconds for 95% of queries while keeping costs manageable.

**Custom DSL Design:** LLM generates simple code statements in Python-like syntax using `XXXX_helper` objects as building blocks. Two-stage code generation allows agents to be clear and focused with overall plan while remaining adaptable to new query types and variations. Static analysis and "dry runs" integrated into interpreter alongside runtime type enforcement ensure safety and correctness.

**Model Selection:** Model-agnostic approach tested multiple open-source and closed-source LLMs on public datasets (Google's Natural Questions, MuSiQue multi-hop questions, Microsoft's Machine Reading Comprehension) using hand-tuned metrics: LLM judge for answer correctness, LLM judge for completeness, source precision/recall/F1 metrics for retrieval accuracy. This flexibility allows choosing models customers are comfortable with and adapting to rapid LLM developments.

## Key Insight

**Two-stage approach where LLMs generate code in a custom Python-like DSL allows agents to "show their work", enabling deterministic testing, clearer debugging, and enhanced security through static analysis.** By expressing logic as code statements rather than opaque LLM reasoning, the system can examine plans without executing them, identify exactly which step failed, test components independently, and enforce type guarantees at runtime—making LLM integration reliable enough for business-critical knowledge management.

**Why This Matters:**
- **Deterministic testing** - Code representation enables testing specific steps (e.g., "Does resolving 'tomorrow' always return correct time window?") rather than evaluating approximate text similarity
- **Clear failure modes** - Instead of "Can't answer this question", system reports "Error on step 3 when fetching attached documents to meeting..." with exact failure location
- **Security controls** - Static analysis can examine code for risks before execution; minimal interpreter feature set eliminates entire classes of security vulnerabilities present in full-featured interpreters
- **Type safety** - Runtime type enforcement guarantees returned data matches expected types (e.g., list of documents will always be list of documents), preventing downstream errors
- **Adaptability** - Two-stage generation (high-level plan → implementation of missing pieces) allows handling new query variations without retraining
- **Model evolution resilience** - Code-based approach provides more stable interface as new LLM versions release compared to opaque prompt-response patterns

**Development Trade-Offs:**
- **Latency vs. quality** - Advanced embedding models and reranking improve accuracy but add latency; system achieves balance by using efficient larger models and staying under 2 seconds for 95% of queries
- **Data freshness vs. scalability** - Periodic data syncs plus webhooks maintain reasonable freshness without throttling throughput from constant re-indexing
- **Budget vs. user experience** - High-quality retrieval (advanced embeddings, reranking, large-chunked indexes) requires more compute; system keeps costs manageable through efficient model selection and traditional IR foundations

**Future Directions:**
- Multi-turn conversations for more natural dialogue
- Self-reflective agents evaluating their own performance and adapting to new information
- Continuous fine-tuning to align with specific business needs
- Multi-language support for global teams

## Links

- [Original Blog Post](https://dropbox.tech/machine-learning/building-dash-rag-multi-step-ai-agents-business-users) - Technical deep dive into RAG implementation and multi-step AI agent architecture for Dropbox Dash
- [Dropbox Dash Product](https://www.dropbox.com/dash) - Universal search and knowledge management product
- [Dropbox AI Principles](https://www.dropbox.com/ai-principles) - Company's approach to building trustworthy AI
