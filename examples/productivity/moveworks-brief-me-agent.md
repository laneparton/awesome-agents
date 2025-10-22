---
title: "Moveworks Brief Me Agentic System"
company: "Moveworks"
author: "Moveworks Engineering Team"
source: "https://www.moveworks.com/us/en/resources/blog/how-we-built-brief-me-for-productivity"
date: "2024-10"
category: "productivity"
tags: ["workflow-automation", "knowledge-retrieval", "rag", "semantic-search", "map-reduce", "production", "enterprise"]
description: "Two-stage document intelligence system with custom MPNet embedding model achieving 97.24% action accuracy for employee productivity"
problem_type: "Information overload requiring employees to manually search across multiple enterprise systems and documents"
architecture_pattern: "two-stage-pipeline"
key_components: ["query-rewriter", "operation-planner", "custom-embedding-model", "map-reduce-generator"]
breakthrough_insight: "Decomposing complex user intent into atomic SEARCH and READ operations enables precise hybrid retrieval while maintaining query context through multi-turn GPT-4o rewriting"
anti_patterns_avoided: ["monolithic-query-processing", "generic-embedding-models", "synchronous-content-generation"]
tech_stack:
  llms: ["GPT-4o", "GPT-4o-mini"]
  embeddings: ["Custom MPNet (100M params)"]
  frameworks: ["LangChain", "Pydantic"]
  infrastructure: ["Streaming pipeline", "Map-reduce architecture"]
scale_metrics:
  training_data: "~1M query-document pairs"
  latency_p90: "<10s for source data ingestion"
  action_accuracy: "97.24%"
  resource_prediction: "97.35%"
  groundedness: "89.21%"
---

# Moveworks Brief Me Agentic System

## The Problem

Enterprise employees face constant information overload, spending hours context-switching between documents, Slack channels, emails, and company dashboards just to stay informed. Manually tracking down relevant updates, distilling key information, and synthesizing insights across disparate sources creates significant productivity drag at scale.

**The Manual Process:**
- Navigate multiple enterprise systems (Slack, email, Confluence, dashboards) to find relevant information
- Read through lengthy documents and threads to identify key updates
- Manually synthesize information from different sources into actionable insights
- Repeat daily across dozens of topics and projects
- Context-switching overhead compounds with organization size

**Key Pain Points:**
- **Information fragmentation** - Critical updates scattered across disconnected systems
- **Time waste** - Hours spent searching and reading instead of executing
- **Missing updates** - Important information gets lost in the noise
- **Synthesis overhead** - Manual effort required to connect dots across sources
- **No personalization** - Generic feeds don't align with individual roles and projects

## The Solution

Moveworks built Brief Me, a two-stage agentic document intelligence system that automatically ingests, interprets, and synthesizes information from across enterprise sources to deliver personalized summaries on demand.

**Impact**: Achieved 97.24% action accuracy and 97.35% resource prediction accuracy with <10s P90 latency for source data ingestion. The system delivers grounded summaries (89.21% groundedness score) by combining a custom-trained 100M parameter MPNet embedding model with GPT-4o-powered query understanding.

## How It Works

**Key Capabilities:**
- **Query Rewriting** - GPT-4o with multi-turn capability to understand complex user intent and maintain context across conversations
- **Operation Planning** - Decomposes queries into atomic SEARCH and READ operations for precise retrieval
- **Custom Embedding Model** - 100M parameter MPNet model trained on ~1M query-document pairs for domain-specific semantic search
- **Map-Reduce Generation** - Parallel processing pipeline with streaming splitter for efficient content synthesis
- **Hybrid Retrieval** - Combines semantic search with structured query operations

**Process Flow:**
1. **Query Understanding** - User submits natural language query (e.g., "Brief me on the Q4 launch")
2. **Query Rewriting** - GPT-4o rewrites query to resolve ambiguities and maintain multi-turn context
3. **Operation Planning** - System classifies intent and generates atomic SEARCH/READ operations
4. **Source Data Ingestion** - Online stage retrieves relevant documents from enterprise systems (P90 latency <10s)
5. **Embedding & Retrieval** - Custom MPNet model computes embeddings and retrieves top matches
6. **Content Generation** - Map-reduce pipeline synthesizes information into personalized summary
7. **Streaming Output** - Results streamed to user with source citations

**Technical Architecture:** Two-stage pipeline with (1) Online Source Data Ingestion handling real-time retrieval and embedding, and (2) Online Content Generation using map-reduce to synthesize outputs. The Operation Planner uses structured Pydantic models to ensure type-safe atomic actions while maintaining flexibility for complex queries.

**Development Approach:** Custom MPNet embedding model trained on approximately 1 million query-document pairs to capture enterprise-specific semantic relationships, significantly outperforming generic embedding models for domain-specific retrieval tasks.

## Key Insight

**Decomposing complex user intent into atomic SEARCH and READ operations enables precise hybrid retrieval while maintaining query context through multi-turn GPT-4o rewriting.** This architecture separates the concerns of understanding what the user wants (query rewriting), planning how to get it (operation planning), and actually retrieving and synthesizing the information (map-reduce generation), allowing each component to be optimized independently.

**Why This Matters:**
- **Precision vs. Flexibility** - Atomic operations provide deterministic retrieval paths while LLM rewriting handles ambiguous natural language
- **Custom embeddings pay off** - Domain-specific training on 1M query-document pairs significantly outperforms generic models for enterprise retrieval
- **Evaluation-driven development** - 97.24% action accuracy and 89.21% groundedness metrics provide concrete targets for system optimization
- **Streaming architecture enables scale** - Map-reduce pipeline with streaming splitter allows parallel processing while maintaining low latency

**Scale Achievement:** The system achieves production-grade performance with P90 latency under 10 seconds for source data ingestion while maintaining high accuracy across evaluation metrics. The two-stage architecture allows independent scaling of retrieval and generation components.

## Links

- [Original Blog Post](https://www.moveworks.com/us/en/resources/blog/how-we-built-brief-me-for-productivity) - Deep dive into the Brief Me agentic engineering system architecture
