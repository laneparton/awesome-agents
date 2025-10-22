---
title: "Dropbox Dash - RAG and Multi-Step AI Agents"
company: "Dropbox"
author: "Dropbox ML Team"
source: "https://dropbox.tech/machine-learning/building-dash-rag-multi-step-ai-agents-business-users"
date: "2025-01"
category: "research"
tags: ["rag", "multi-agent", "knowledge-retrieval", "semantic-search", "code-generation", "enterprise", "production"]
description: "Hybrid RAG + multi-step agent system achieving sub-2-second response for 95%+ of queries with custom DSL interpreter for security"

# Problem Classification
problemPattern: "content-discovery"
problemComplexity: "complex"

# Architecture
architecture:
  type: "hybrid"
  pattern: "rag-plus-agent"
  rationale: "Two-pronged approach: RAG for factual document synthesis, multi-step agents for complex task orchestration using custom Python DSL with static analysis for security"
  components: ["hybrid-retrieval", "reranker", "custom-interpreter", "planning-llm", "execution-engine", "helper-objects"]

# What Made It Work
breakthroughInsight: "Custom minimal Python DSL interpreter with static analysis eliminates security risks while code-as-logic enables deterministic testing and clear error diagnosis - 'Error on step 3' vs vague failures"

criticalConstraints:
  - "data-fragmentation-across-apps"
  - "modality-diversity"
  - "latency-budget-1-2-seconds"
  - "security-risks-sensitive-data"
  - "model-variability"

antiPatterns:
  - "assuming-retrieval-equivalence: not all retrieval methods offer same latency-quality trade-offs"
  - "identical-prompts-across-llms: different LLM families respond differently to identical prompts"
  - "full-featured-interpreters: security risks inherent to general-purpose code execution"

# Tech Stack
techStack:
  framework: "Custom"
  llmProvider: "Model-agnostic"
  knowledgeRetrieval: "Hybrid lexical IR + semantic embeddings"
  otherTools: ["custom-Python-DSL", "static-analysis", "reranking", "on-the-fly-chunking"]

# Scale
scale:
  volume: "Production Dropbox Dash users"
  latency: "Sub-2-seconds for 95%+ of queries"
---

# Dropbox Dash - RAG and Multi-Step AI Agents

## The Problem

Knowledge workers faced critical challenges managing scattered digital workflows across multiple disconnected applications and formats. Data fragmentation required constant context-switching between tools, data diversity (emails, documents, notes, tasks) came with varying structures, multiple modalities (text, images, audio, video) needed unified processing, and sensitive information risked unintended exposure across applications.

**The Manual Process:**
- Manually search across disconnected applications for relevant information
- Context-switch between email, documents, notes, calendars, tasks
- Synthesize information from diverse formats and modalities
- Repeat search across multiple tools for comprehensive answers
- Risk exposing sensitive data through insecure sharing
- Manually trace relationships between related items (meetings, documents, notes)

**Key Pain Points:**
- Data fragmentation across disconnected apps creates inefficiency
- Context-switching disrupts workflow and productivity
- No unified search across diverse data types and modalities
- Manual synthesis of information from multiple sources
- Security risks from scattered sensitive information
- Multi-step tasks require manual orchestration

## The Solution

Dropbox Dash deploys a hybrid approach: RAG for factual information retrieval and document synthesis, plus multi-step AI agents for complex task orchestration. Agents use a custom Python DSL with static analysis for security, executing multi-step workflows through LLM-generated code validated before runtime.

**Impact**: Achieved sub-2-second response times for over 95% of queries while unifying access to scattered information across applications with secure multi-step task orchestration.

## How It Works

**Key Capabilities:**
- **Hybrid Retrieval** - Traditional lexical IR combined with embedding-based reranking for quality and speed
- **Two-Pronged Architecture** - RAG for factual queries, multi-step agents for complex task orchestration
- **Custom DSL Interpreter** - Minimal Python interpreter built in-house focused on essential features only
- **Static Analysis Security** - Validates generated code before execution, identifying security risks without runtime
- **Code as Explainability** - Agent logic expressed as code enables deterministic testing and clear error diagnosis
- **Helper Objects** - Domain-specific building blocks (time_helper, meetings_helper, documents_helper)

**Process Flow:**

*For Simple Factual Queries (RAG):*
1. User submits query
2. Hybrid retrieval: lexical IR + semantic embeddings
3. On-the-fly chunking of relevant documents
4. Reranking results for quality
5. LLM synthesizes response from retrieved documents
6. Return answer in under 2 seconds (95%+ of cases)

*For Complex Multi-Step Tasks (AI Agents):*
1. User submits complex query (e.g., "Show me notes for tomorrow's all-hands")
2. **Planning Stage**: LLM interprets query and generates code in custom Python DSL
   - Example breakdown: resolve date → find meeting → retrieve attached documents
   - Code uses helper objects: `time_helper.get_time_window_for_tomorrow()`
3. **Static Analysis**: Custom interpreter validates code for:
   - Security risks
   - Missing functionality
   - Type correctness
4. **Execution Stage**: Validated code executes through custom interpreter
   - `meetings_helper.find_meeting(title="all-hands", time_window=time_window)`
   - `meetings_helper.get_attached_documents(meeting=meeting)`
5. Results returned with step-by-step traceability
6. Errors reported with specific step identification ("Error on step 3")

**Technical Architecture:** Custom minimal Python interpreter focused only on essential features eliminates security risks of full-featured interpreters. LLM-generated DSL code undergoes static analysis before execution. Hybrid retrieval combines lexical IR with embedding-based reranking for latency-quality balance. Model-agnostic LLM integration allows flexibility across providers. Helper objects provide domain-specific primitives for time, meetings, documents operations.

## Key Insight

**Code as agent logic with static analysis enables security, testability, and explainability.** Custom minimal Python DSL interpreter eliminates security risks while expressing agent plans as code provides deterministic testing and clear error diagnosis.

**Why This Matters:**
- Full-featured interpreters introduce major security risks; minimal custom interpreter focuses only on essential features
- Code representation enables static analysis to catch issues before execution
- Deterministic testing possible with code vs black-box agent behavior
- Clear error messages ("Error on step 3") vs vague failures
- Helper objects encapsulate domain logic as reusable building blocks
- Different LLMs require different prompts—model selection and optimization critical

**Hybrid Retrieval Wins**: Traditional lexical IR + embedding reranking achieved "high-quality results in under 2 seconds for over 95% of queries" while managing costs better than pure embedding approaches.

**Latency-Quality Trade-offs**: Larger models may provide more precise results but introduce delays misaligned with user expectations—staying under 1-2 seconds prevents abandonment.

**Evaluation Strategy**: Tested across multiple public datasets (Google Natural Questions, MuSiQue, Microsoft MRC) with custom metrics for LLM correctness, completeness, source precision/recall.

## Links

- [Original Article](https://dropbox.tech/machine-learning/building-dash-rag-multi-step-ai-agents-business-users) - Building Dash: How RAG and AI Agents Help Us Meet the Needs of Businesses
