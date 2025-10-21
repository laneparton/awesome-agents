---
title: "Ask Astro - Dreamforce Event Agent"
company: "Salesforce"
author: "Salesforce Events Team"
source: "https://www.salesforce.com/blog/build-an-ai-agent/"
date: "2024-09"
category: "productivity"
tags: ["rag", "semantic-search", "workflow-automation", "production"]
description: "Event assistant agent built in 5 days using hybrid search and RAG, handling session recommendations and schedule management with near real-time index updates"

# Problem Classification
problemPattern: "content-discovery"
problemComplexity: "moderate"

# Architecture
architecture:
  type: "single-agent"
  pattern: "rag-hybrid-search"
  rationale: "RAG framework with hybrid search combining semantic vector search and keyword precision, augmented indexing chunking data optimally per query type, streaming ingestion for near real-time updates"
  components: ["data-cloud", "hybrid-search", "rag", "mulesoft-pipelines", "streaming-ingestion", "agentforce"]

# What Made It Work
breakthroughInsight: "Hybrid search combining semantically aware vector search with keyword precision + augmented indexing breaking records into query-optimized chunks (e.g., individual speaker names) dramatically improved retrieval accuracy"

criticalConstraints:
  - "5-day-launch-deadline"
  - "homegrown-migration-required"
  - "dreamforce-attendee-scale"
  - "speaker-name-accuracy-critical"
  - "real-time-index-updates"

antiPatterns:
  - "parallel-system-maintenance: abandoned homegrown vector DB to consolidate on Salesforce infrastructure"
  - "pure-semantic-search: needed keyword precision for speaker names"
  - "whole-record-vectorization: augmented indexing with query-optimized chunks wins"

# Tech Stack
techStack:
  framework: "Agentforce"
  llmProvider: "LLM-based"
  knowledgeRetrieval: "RAG + Hybrid Search"
  otherTools: ["Data Cloud", "MuleSoft Anypoint", "Salesforce Knowledge", "Einstein Feedback"]

# Scale
scale:
  volume: "Dreamforce attendees across 3 topics, 12 actions"
  latency: "near real-time index updates via streaming"
---

# Ask Astro - Dreamforce Event Agent

## The Problem

Salesforce needed to rapidly migrate their homegrown AI agent powering the Salesforce Events mobile app to the Agentforce platform before Dreamforce, their largest annual conference. The existing solution using OpenAI function-calling with a Heroku vector database lacked the scalability and enterprise integration needed for production deployment. They had only 5 days from project initiation to conference launch.

**The Manual Process:**
- Maintain parallel homegrown vector database infrastructure
- Manual data synchronization between systems
- Limited integration with Salesforce ecosystem
- Custom code maintenance overhead
- Slow debugging cycles without LLM-powered tools

**Key Pain Points:**
- 5-day deadline before major conference launch
- Homegrown infrastructure duplication and sync overhead
- Pure semantic search struggled with speaker name accuracy
- Whole-record vectorization missed query-specific optimization
- Manual index refresh cycles prevented real-time updates
- Parallel system maintenance created operational burden

## The Solution

Ask Astro Agent rebuilt on Salesforce-native stack using Agentforce with hybrid search combining semantic vector search and keyword precision, augmented indexing chunking data per query type, and streaming ingestion for near real-time updates. Handles session recommendations, schedule management, and FAQs for Dreamforce attendees.

**Impact**: Built production agent in 5 days with MVP completed in 1 day, consolidating onto Salesforce infrastructure with hybrid search and streaming ingestion enabling near real-time index updates.

## How It Works

**Key Capabilities:**
- **Hybrid Search** - Combines semantically aware vector search with keyword search precision
- **Augmented Indexing** - Breaks records into query-optimized chunks (e.g., individual speaker names)
- **Streaming Data Architecture** - Data Cloud native streaming with MuleSoft change-data capture for real-time sync
- **RAG Framework** - Retrieval augmented generation for event information queries
- **30-Second Debugging** - LLM-powered Agent Builder accelerates iteration cycles
- **Mobile Integration** - Bot API connects to Salesforce Events mobile app

**Process Flow:**
1. Attendee asks question via Salesforce Events mobile app (e.g., "Show me sessions on AI")
2. Query enters **Agentforce Service Agent** for orchestration
3. **Hybrid Search** executes:
   - Semantic vector search via **Data Cloud Query Service API** for concept matching
   - Keyword search for precision (e.g., exact speaker names)
   - Combines results leveraging strengths of both approaches
4. **Augmented Indexing** retrieves query-optimized chunks:
   - Speaker queries: individual chunks like "Adam Evans, SVP, AI Platform Cloud, Salesforce"
   - Session queries: chunks optimized for session attributes
   - FAQ queries: knowledge article chunks
5. **RAG framework** generates response using retrieved context
6. **Invocable Actions** handle schedule management (add/remove sessions)
7. Response delivered to attendee via mobile app
8. **Einstein Feedback** monitors production performance
9. **Streaming ingestion**: MuleSoft captures data changes → Data Cloud index updates near real-time

**Technical Architecture:** Data Cloud provides vector/hybrid search indexing with Query Service API for direct semantic access. Agentforce Service Agent orchestrates with LLM configuration via Agent Builder. MuleSoft Anypoint pipelines handle data ingestion with change-data capture for streaming updates. Salesforce Knowledge manages FAQ content. Apex classes provide custom integration layer. Einstein Feedback enables production monitoring.

**Rapid Development:** MVP completed in 1 day using CSV-based data ingestion. Production deployment required parallel workstreams: search optimization, streaming pipelines, FAQ conversion. 30-second debugging cycles via LLM-powered Agent Builder accelerated iteration.

## Key Insight

**Hybrid search combining semantic awareness with keyword precision + augmented indexing for query-specific chunks solved critical accuracy issues.** Pure semantic search struggled with speaker name queries; hybrid approach with individual speaker-name chunks dramatically improved retrieval.

**Why This Matters:**
- Pure vector search lacks precision for exact matches like speaker names
- Keyword search alone misses semantic concept matching
- Hybrid approach leverages complementary strengths: semantic breadth + keyword precision
- Augmented indexing (query-optimized chunks) beats whole-record vectorization
- Individual speaker chunks ("Adam Evans, SVP...") enable accurate name matching
- Streaming architecture via Data Cloud + MuleSoft eliminates manual refresh overhead
- 5-day timeline demonstrates rapid enterprise agent development on unified platform

**Augmented Indexing Pattern**: Breaking records into chunks optimized for specific query types (speaker names, session attributes, FAQ content) improves retrieval precision compared to vectorizing entire records.

**Migration Decision**: Abandoning parallel homegrown infrastructure to consolidate on Salesforce stack eliminated duplication, sync overhead, and maintenance burden—critical for sustainable production deployment.

**Rapid Prototyping**: CSV-based MVP in 1 day validated approach before investing in streaming pipelines, demonstrating value of incremental delivery under tight deadlines.

## Links

- [Original Article](https://www.salesforce.com/blog/build-an-ai-agent/) - How We Built the First Dreamforce Event Agent in 5 Days with Agentforce
