---
title: "eBay Mercury - Agentic AI Platform for LLM-Powered Recommendation Experiences"
company: "eBay"
author: "Nazmul Chowdhury, Jonathan Galsurkar, Minnie Li, Yuri M. Brovman - eBay Recommendations Team"
source: "https://www.linkedin.com/pulse/mercury-agentic-ai-platform-llm-powered-experiences-ebay-chowdhury-kka8e/"
date: "2025-04"
category: "data-analysis"
tags: ["agent-framework", "rag", "knowledge-retrieval", "semantic-search", "production", "enterprise"]
description: "Agentic framework serving hundreds of millions of customers across 2 billion+ listings with hundreds of ms latency through plug-and-play agent components"

# Problem Classification
problemPattern: "recommendation-system"
problemComplexity: "complex"

# Architecture
architecture:
  type: "multi-agent"
  pattern: "plug-and-play-agent-framework"
  rationale: "Agent abstraction decoupling input/output contracts from implementation allows multiple variations honoring same interface but differing in complexity/models/optimization; plug-and-play components enable strong inter-agent compatibility and reusability; NRT distributed queue-based execution platform smooths traffic peaks for consistent GPU utilization; Listing Matching Engine bridges LLM text outputs to 2B+ live inventory through hybrid exact-match and semantic search; OOP engineering standards enable complex systems built from simple well-defined parts"
  components: ["agent-abstraction", "chain-orchestration", "rag-integration", "listing-matching-engine", "nrt-execution-platform", "text-to-listing-retrieval", "content-moderation", "guardrails"]

# What Made It Work
breakthroughInsight: "Agent abstraction decoupling input/output from implementation allows multiple variations honoring same contract but differing in complexity/models/optimization - maintaining strong inter-agent compatibility and reusability for rapid development; if solution works in developer's local environment for single instance, platform automatically scales to eBay's industrial needs serving hundreds of millions across billions of listings; NRT distributed queue-based messaging smooths user activity peaks/valleys for consistent controllable throughput and better GPU utilization"

criticalConstraints:
  - "hundreds-millions-customers-scale"
  - "2-billion-plus-listings"
  - "hundreds-ms-latency-requirements"
  - "unstructured-listing-data-volume"
  - "cost-efficiency-llm-inference"
  - "dynamic-inventory-access"
  - "reusability-across-use-cases"
  - "model-provider-flexibility"

antiPatterns:
  - "monolithic-agent-coupling: Tightly coupling agents to specific models or implementation details prevents independent evolution and optimization - agent contracts with defined inputs/outputs allow swapping implementations while maintaining downstream compatibility"
  - "synchronous-user-dependent-processing: Processing tied to user activity patterns creates GPU utilization peaks/valleys and unpredictable costs - NRT distributed queue-based platform smooths traffic for consistent controllable throughput across all use cases"
  - "llm-only-inventory-access: LLMs lack access to current insights into eBay's dynamic 2B+ item inventory - Listing Matching Engine essential to bridge LLM text outputs to live listings through hybrid exact-match and semantic retrieval"
  - "custom-infrastructure-per-use-case: Building separate infrastructure for each recommendation experience doesn't scale - reusable plug-and-play components with defined contracts enable rapid development where each new use case improves the entire system"

# Tech Stack
techStack:
  framework: "Mercury-agentic-framework"
  llmProvider: "multiple-providers-fine-tuned-models"
  knowledgeRetrieval: "rag-with-multiple-sources"
  otherTools: ["Chains", "LangGraph-patterns", "NRT-execution-platform", "distributed-queue-messaging", "vector-databases", "Common-Crawl", "Google-Search-API", "KNN-search", "BERT-embeddings", "content-moderation"]

# Scale
scale:
  volume: "Hundreds of millions of customers, 2 billion+ active listings, industrial scale deployment across numerous experiences, multiple LLM providers and fine-tuned models (Llama, Mistral, Lillium)"
  latency: "As low as hundreds of ms for recommendations, resilient self-healing distributed processing with automated retry, consistent controllable throughput via on-the-fly configuration"
---

# eBay Mercury - Agentic AI Platform for LLM-Powered Recommendation Experiences

## The Problem

eBay operates a global e-commerce platform with over two billion active listings where users can sell and buy virtually anything. This vast and diverse ecosystem generates an immense amount of unstructured data from listings, user interactions, and marketplace dynamics. Making sense of this data to provide personalized recommendations at scale presents significant challenges. While Large Language Models (LLMs) offer transformative potential for enhancing recommendations, scaling these applications to serve hundreds of millions of customers across billions of item listings across numerous experiences is both technically challenging and prohibitively costly with traditional approaches.

**The Manual Process:**
- Previous recommendation systems required extensive feature engineering from unstructured listing data
- Separate models and infrastructure needed for each recommendation use case
- Scaling LLM applications required custom implementation for each new experience
- Model selection, prompt engineering, and deployment processes duplicated across teams
- Each use case built from scratch without reusable components
- Extensive development time to productionize LLM-powered features

**Key Pain Points:**
- **Scale complexity** - Serving hundreds of millions of customers across billions of listings requires industrial-scale infrastructure
- **Cost challenges** - LLM inference costs prohibitive without optimization and batching strategies
- **Latency requirements** - User-facing experiences demand responses in hundreds of milliseconds, challenging with LLM processing
- **Unstructured data volume** - Vast amounts of listing data, user interactions, and marketplace context to process
- **Reusability gaps** - Each new recommendation experience built from scratch without shared components
- **Model coupling** - Solutions tightly coupled to specific models preventing optimization and adaptation
- **Inventory dynamics** - LLMs lack access to current insights into eBay's dynamic inventory requiring external bridging

## The Solution

eBay developed Mercury, an internal agentic framework and execution platform designed to facilitate creation of LLM-powered experiences at scale. Mercury structures LLM work as "Agents" with defined contracts, enabling plug-and-play architecture where components can be combined, swapped, or upgraded independently. The framework integrates RAG with multiple data sources (Common Crawl, Google Search, user/listing information, external partners) and includes a custom Listing Matching Engine that bridges LLM text outputs to eBay's 2 billion+ live item inventory through text-to-listing retrieval. A distributed queue-based NRT (near-real-time) execution platform smooths traffic peaks/valleys for efficient GPU utilization and consistent throughput.

**Impact**: Hundreds of millions of customers served across 2 billion+ active listings, latency as low as hundreds of ms, industrial scale deployment across numerous experiences, rapid development through reusable components, consistent and controllable throughput via NRT platform, resilient self-healing distributed processing.

## How It Works

**Key Capabilities:**
- **Agent Abstraction** - Unit of LLM work encapsulating prompt + input transformations + output translations with defined contracts, allowing multiple implementations honoring same interface but differing in complexity/models/optimization
- **Plug-and-Play Architecture** - Components designed for strong inter-agent compatibility and reusability, enabling complex systems built from simple well-defined parts following OOP engineering standards
- **RAG Integration** - Access to vast relevant current information (structured and unstructured) including Common Crawl, Google searches for real-time trending data, external partner signals, user/listing information
- **Listing Matching Engine** - Bridges gap between LLM text outputs and eBay's dynamic 2 billion+ item inventory through text-to-listing retrieval combining exact match and semantic search
- **NRT Execution Platform** - Distributed queue-based message passing system smoothing traffic peaks/valleys for consistent GPU utilization, resilient self-healing with automated retry, on-the-fly throughput/priority control
- **AI Safety Controls** - Content moderation models, LLM safety mechanisms, internal prompt injection detection models

**Process Flow (Recommendations Use Case):**
1. **User Context** - User shopping mission, previous interactions, preferences captured
2. **Agent Invocation** - Recommendation agent called with user context and available data sources
3. **RAG Retrieval** - Agent accesses relevant information via multiple sources (Common Crawl for trending topics, Google search for recent releases, user history, external partner data) with latency/relevancy/cost tradeoffs per use case
4. **Query Expansion** - LLM generates expanded set of product queries and recommendations based on learned knowledge or RAG understanding of topic
5. **Text-to-Listing Retrieval** - Listing Matching Engine processes LLM output through multiple retrieval mechanisms:
   - Exact match retrieval via eBay search engine for specific queries
   - Semantic similarity using text embeddings + KNN search on vector databases with BERT-based and custom deep learning models
6. **Anomaly Detection and Filtering** - Category/price validation, title alignment checking, hard filters (NSFW, condition, location, user preferences)
7. **Personalized Ranking** - Tailored to user's previous interactions, shopping behaviors, preferences with round-robin presentation for fair visibility
8. **Quality Optimization** - Optional N-step refinement or threshold-based optimization with query caching
9. **Results Delivery** - Highly relevant product recommendations delivered to user
10. **Monitoring and Observability** - Comprehensive monitoring for reliability, debugging, performance tracking

**Agent Architecture:** Agents in simplest form encapsulate instruction (prompt) + transformation layers for input data formatting + output translation to expected structure. Input/output abstractions decoupled from implementation allow multiple agent variations with different complexity levels, models, or quality vs. latency optimizations while maintaining same contract. Chains link sequences of steps enabling more intricate behaviors while presenting as single agent with consistent interface—engineers focus only on inputs/outputs without concerning themselves with underlying workings.

**Advanced Orchestration:** OOP concepts within agents accommodate complex behaviors through Chains. Agents configured as trees or graphs support autonomous operations (LangGraph patterns). Foundation for future self-assembling large network of agents using self-discovery and defined contracts where more capable AI plugs in to use lesser agents as tools for specialized tasks.

**NRT Platform Design:** Distributed queue-based message passing alleviates dependence on user activity pattern peaks/valleys throughout day. Smooths curve for consistent controllable throughput across all use cases or per use case via on-the-fly configuration. Resilient, self-healing, low maintenance—failed tasks automatically retried later. Parallel processing aperture controlled on-the-fly. Service disruptions trigger auto-resume when recovered.

**Core Principles:**
- **Built To Last** - Defined unbreakable agent contracts, prompts treated as code (PRs, reviews, unit/functional testing)
- **Ease of Use** - Simplified interfaces drive complex behavior, accessible for teams across eBay
- **Scalability** - Drop-in execution layer with online and NRT processing, scales from developer local environment to eBay industrial needs in days not months
- **Intercompatibility and Reusability** - Seamless component integration, each new use case creates or improves components making entire system better
- **Options In Models** - Connected to multiple generative models across providers, support for internal fine-tuned models and external platforms
- **Knowledge Is Power** - Integrated with many internal/external data sources (structured and unstructured)
- **Observability and Metrics** - Built-in comprehensive monitoring, debugging, performance tracking
- **Safety** - Various external and internal safety measures including content moderation and prompt injection detection

## Key Insight

**Agent abstraction decoupling input/output contracts from internal implementation allows multiple agent variations honoring the same interface but differing in complexity, models, or optimization strategies.** This plug-and-play architecture maintains strong inter-agent compatibility and reusability, enabling teams to build complex recommendation systems by combining simple well-defined components that can be individually upgraded or swapped out—drastically accelerating development while ensuring robustness through OOP engineering standards.

**Why This Matters:**
- **Rapid iteration** - Teams quickly develop and iterate solutions using simplified interfaces to drive complex behavior without rebuilding infrastructure
- **Model flexibility** - Same agent contract supports multiple LLM providers, fine-tuned models, or optimization strategies without changing downstream consumers
- **Scalability guarantee** - If solution works in developer's local environment for single instance, platform scales to eBay's industrial needs automatically
- **Component reuse** - Every new use case creates or improves components, making entire system better and building larger library for next use case
- **Independent evolution** - Components upgraded or swapped independently without breaking dependent systems due to contract guarantees
- **Cost efficiency** - NRT platform with distributed queuing smooths traffic peaks for better GPU utilization versus synchronous user-activity-dependent processing

**Listing Matching Engine Innovation:**
- **Inventory bridge** - LLMs lack access to current eBay inventory insights; engine dynamically connects LLM-generated product ideas to 2 billion+ live listings
- **Hybrid retrieval** - Combines exact match precision for specific searches with semantic similarity for broad/exploratory suggestions
- **Quality controls** - Anomaly detection ensures relevance through category/price validation, title alignment, customizable filtering
- **Personalization** - Rankings tailored to individual user interactions and preferences while maintaining fair visibility via round-robin

**Development Acceleration:**
- Components plug-and-play with defined contracts
- Prompts treated as code with PR reviews and testing
- Drop-in execution layer eliminates infrastructure work
- Comprehensive observability built-in
- Safety mechanisms integrated by default

**Future Vision:**
Self-assembling large network of agents using self-discovery and existing contracts where more capable future AI can autonomously plug into network and use specialized agents as tools—creating truly autonomous system that leverages distributed specialized capabilities.

## Links

- [Original LinkedIn Article](https://www.linkedin.com/pulse/mercury-agentic-ai-platform-llm-powered-experiences-ebay-chowdhury-kka8e/) - Technical overview of Mercury agentic platform and recommendation architecture
- [eBay Recommendations Research](https://tech.ebayinc.com/) - Previous work on recommendation systems at eBay
- [eBay AI Responsibility](https://www.ebayinc.com/company/our-approach-to-ai/) - eBay's approach to responsible and safe AI use
