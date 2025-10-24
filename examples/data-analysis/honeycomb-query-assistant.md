---
title: "Honeycomb Natural Language Query Assistant"
company: "Honeycomb"
author: "Phillip Carter, Honeycomb Engineering"
source: "https://www.honeycomb.io/blog/hard-stuff-nobody-talks-about-llm"
date: "2023-05"
category: "data-analysis"
tags: ["production", "enterprise", "workflow-automation", "text-to-query", "few-shot-prompting"]
description: "Production LLM feature converting natural language to executable Honeycomb queries, addressing real-world challenges of latency, context limits, prompt injection, and enterprise compliance"

# Problem Classification
problemPattern: "text-to-query"
problemComplexity: "medium"

# Architecture
architecture:
  type: "single-agent"
  pattern: "single-pass-generation"
  rationale: "Single-pass LLM prompting avoids compounding accuracy issues (90% accuracy compounds to 59% over 5 chains); extensive context (syntax docs, domain knowledge, schema, few-shot examples) provides all needed information upfront; schema constrained to 7-day active fields for large customers handles context limits; integrated with standard Query Builder (not chat UI) reduces prompt injection surface; 'engines for features' approach treats LLM as tool powering specific workflow"
  components: ["few-shot-prompter", "schema-constrainer", "output-validator", "query-builder-integration"]

# What Made It Work
breakthroughInsight: "Single-pass generation essential to avoid accuracy degradation - 90% accuracy compounds to 59% over 5 chains, so chaining multiple LLM calls fails; few-shot prompting outperformed zero-shot and chain-of-thought; accepting 'good enough' outputs (flexible interpretation like user typing 'slow') serves users better than rigid correctness; LLMs are engines for features not standalone products; schema filtering by 7-day activity handles context limits for 5,000+ field customers"

criticalConstraints:
  - "query-syntax-barrier"
  - "context-window-limits-5000-plus-fields"
  - "latency-2-15-seconds"
  - "prompt-injection-risk"
  - "enterprise-compliance-healthcare"
  - "no-chat-ui-standard-builder-only"
  - "single-pass-accuracy-requirements"

antiPatterns:
  - "chaining-llm-calls: 90% accuracy per call compounds to 59% over 5 chains - single-pass generation essential to avoid compounding accuracy degradation"
  - "zero-shot-or-chain-of-thought: Few-shot prompting with examples outperformed both zero-shot and chain-of-thought variants for query generation"
  - "chat-ui-interface: Chat interface increases prompt injection surface area - standard Query Builder integration provides safety and familiar UX"
  - "full-schema-context: Context limits fail with 5,000+ field customers - constraining to fields with 7-day activity essential for large schemas"
  - "perfect-correctness-requirement: Rigid correctness rejects useful vague inputs (user types 'slow') - accepting 'good enough' flexible interpretation serves users better"

# Tech Stack
techStack:
  framework: "custom"
  llmProvider: "LLM-based"
  knowledgeRetrieval: "schema-aware"
  otherTools: ["few-shot-prompting", "output-validation", "7-day-schema-filtering", "Query-Builder-integration"]

# Scale
scale:
  volume: "Production feature deployed to Honeycomb customers"
  latency: "2-15+ seconds per query generation, single-pass to avoid accuracy degradation"
---

# Honeycomb Natural Language Query Assistant

## The Problem

Honeycomb users needed to express data queries in the platform's native query language, requiring knowledge of specific syntax, operators, filters, and clause structure. This created a barrier to ad-hoc data exploration and slowed down troubleshooting workflows.

**The Manual Process:**
- Users manually constructing queries using Query Builder UI
- Learning and remembering Honeycomb's query syntax and operators
- Understanding visualization types (HEATMAP, COUNT, etc.) and when to use them
- Manually filtering data and structuring query clauses
- Trial-and-error iteration to build correct queries
- Referring to documentation for syntax and operators

**Key Pain Points:**
- Query language syntax barrier slows data exploration
- Users must learn platform-specific operators and structure
- Manual query construction interrupts troubleshooting flow
- Complex queries require significant syntax knowledge
- No natural way to ask questions like "Which service has the highest latency?"
- Context switching between problem investigation and query building

## The Solution

Honeycomb built Query Assistant, a production LLM feature that converts natural language requests into executable Honeycomb queries. Users ask questions naturally and receive valid queries as output, which they can refine using the standard Query Builder.

**Impact**: Production feature deployed to Honeycomb customers. Represents "engine for features" approach where LLMs power specific workflows rather than standalone products. Results are "best effort" answers users can refine, balancing usefulness with correctness.

## How It Works

**Key Capabilities:**
- **Natural Language Input** - Users ask questions like "Which service has the highest latency?"
- **Query Syntax Generation** - LLM outputs valid Honeycomb query syntax
- **Schema-Aware** - Incorporates user's data schema (constrained to fields with data in past 7 days for customers with 5,000+ fields)
- **Few-Shot Prompting** - Uses example-based prompting (outperformed zero-shot and chain-of-thought variants)
- **Standard UI Integration** - Executes through Honeycomb's query engine, returns results via standard UI (not chat interface)
- **Single-Pass Processing** - Avoids chaining multiple LLM calls to prevent compounding accuracy issues

**Process Flow:**
1. User enters natural language query request
2. System feeds LLM context including query syntax documentation, domain knowledge about trace data, user's data schema, few-shot examples, and existing query if applicable
3. LLM generates Honeycomb query syntax
4. System parses and validates LLM output
5. Query executes through Honeycomb's standard engine
6. Results returned through standard UI for refinement via Query Builder
7. No chat interface—single query generation per request

**Technical Architecture:** Single-pass LLM prompting with extensive context (syntax docs, domain knowledge, schema, examples). Schema constrained to fields receiving data in past 7 days for large customers. Output parsing and validation ensures syntactically correct queries. Integrated with standard Query Builder rather than chat UI to reduce prompt injection surface.

**Development Journey:** Shipped quickly with effective few-shot prompting approach. Explicitly chose single-pass over chaining approaches after learning 90% accuracy compounds to 59% over 5 chains. Accepted "something rather than nothing" philosophy—trading perfect correctness for user-helpful outputs.

## Key Insight

**Deploying LLMs as "engines for features" rather than standalone products requires solving latency, security, compliance, and accepting imperfect-but-useful outputs.** Real-world production deployment goes far beyond model selection, demanding architectural decisions around prompt engineering, data privacy, and user experience that balance theoretical correctness with practical usefulness.

**Why This Matters:**
- LLMs are tools to power features, not products themselves
- Single-pass prompting avoids compounding accuracy issues (90%^5 = 59%)
- Context window limits require schema filtering strategies (7-day activity constraint)
- Latency (2-15+ seconds) demands careful UX decisions about when to invoke LLMs
- Prompt injection has no complete solution—mitigation layers (validation, rate limiting, no chat UI) reduce risk
- Enterprise compliance (healthcare, contractual obligations) constrains provider selection
- Accepting "good enough" outputs (flexible interpretation of vague inputs) serves users better than rigid correctness

**Production Challenges Solved:**
- **Context limits**: Constrain schema to fields with recent activity; exploring embeddings for relevancy
- **Latency**: 2-15+ seconds per call; avoid chaining to prevent accuracy degradation
- **Prompt engineering**: Few-shot outperformed zero-shot and chain-of-thought
- **Correctness vs. usefulness**: Accept broad inputs (user types "slow") even if imprecise
- **Security**: Mitigation layers (non-destructive outputs, input/output truncation, rate limiting, no chat UI)
- **Compliance**: Only OpenAI met audit requirements; updated ToS; flagged BAA customers for review

## Links

- [Original Article](https://www.honeycomb.io/blog/hard-stuff-nobody-talks-about-llm) - Comprehensive technical deep-dive into real-world challenges of building production LLM features at Honeycomb
