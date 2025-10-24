---
title: "Vimeo Customer Support with Generative AI"
company: "Vimeo"
author: "Jon Ruddell, Principal Engineer, Office of the CTO"
source: "https://medium.com/vimeo-engineering-blog/from-idea-to-reality-elevating-our-customer-support-through-generative-ai-101a2c5ea680"
date: "2023-08"
category: "productivity"
tags: ["rag", "knowledge-retrieval", "customer-support", "production"]
description: "RAG-powered help desk chat prototype integrating Zendesk articles with LangChain, comparing Google Vertex AI Bison and OpenAI models for customer support automation"

# Problem Classification
problemPattern: "customer-support"
problemComplexity: "medium"

# Architecture
architecture:
  type: "single-agent"
  pattern: "conversational-retrieval-rag"
  rationale: "RAG architecture combining organization-specific knowledge base (Zendesk Help Center) with LLMs enables precise, contextualized support responses impossible with LLMs alone; conversational retrieval pattern uses chat history to reformulate followup questions as standalone queries improving retrieval accuracy; vector store with HNSWLib enables semantic matching beyond keyword-based search limitations; automatic webhook-based updates keep index synchronized with article changes; source attribution links responses to authoritative articles building trust"
  components: ["vector-store-indexing", "conversational-retrieval-chain", "standalone-question-generation", "similarity-search", "contextual-response-generation", "source-attribution", "automatic-webhook-updates"]

# What Made It Work
breakthroughInsight: "RAG architecture combining organization-specific knowledge bases with LLMs enables precise, contextualized support responses impossible with LLMs alone - by indexing Vimeo's Help Center into vector store and using conversational retrieval patterns, prototype demonstrated how AI can provide immediate, actionable answers grounded in existing documentation rather than hallucinated information; generic LLMs (commercial or open-source) lack context for company-specific needs, but RAG bridges this gap by retrieving relevant internal documentation before generation"

criticalConstraints:
  - "help-center-search-irrelevance"
  - "third-party-chatbot-limitations"
  - "ticket-wait-times"
  - "repetitive-query-volumes"
  - "company-specific-knowledge-gap"
  - "exhaustive-qa-testing-impossible"
  - "api-reliability-variation"
  - "training-data-privacy-concerns"

antiPatterns:
  - "llm-only-without-rag: Generic LLMs (commercial or open-source) lack context for company-specific support needs and hallucinate plausible but incorrect information - RAG retrieval of internal documentation before generation essential for accurate, grounded responses"
  - "keyword-search-only: Traditional Help Center search returning irrelevant results (e.g., 'domain restrict embed' returns nothing) - vector similarity search enables semantic matching beyond exact keyword requirements"
  - "ignoring-conversation-history: Treating each question independently fails on followup queries lacking context - conversational retrieval reformulating question + history into standalone query dramatically improves retrieval for multi-turn interactions"
  - "no-source-attribution: Answers without links to original articles reduce trust and prevent users from exploring related content - metadata (title, URL, tags) attached to enable verification and deeper learning"

# Tech Stack
techStack:
  framework: "LangChain"
  llmProvider: "Google-Vertex-AI-Chat-Bison"
  knowledgeRetrieval: "rag-conversational-retrieval"
  otherTools: ["HNSWLib-vector-store", "OpenAI-embeddings", "Zendesk-API", "webhook-automation", "temperature-0", "safety-filters", "moderation-endpoints"]

# Scale
scale:
  volume: "Zendesk Help Center articles scraped, chunked, embedded, and indexed, automatic webhook updates on article changes, tested with multiple LLM providers (Google Vertex AI Chat Bison, OpenAI ChatGPT 3.5 Turbo, ChatGPT 4, Azure OpenAI)"
  latency: "Immediate responses vs ticket wait times, Google Vertex AI selected for: concise bullet-point answers, faster response (fewer characters), better prompt following, cost savings, seamless GCP authentication, all-at-once response vs streaming"
---

# Vimeo Customer Support with Generative AI

## The Problem

Vimeo customers with questions or issues faced multiple friction points in the existing support system. Traditional support channels struggled with overwhelming query volumes, delayed response times, and lack of personalized solutions, leading to customer frustration and missed business opportunities.

**The Manual Process:**
- Customers opening tickets with Vimeo support team (long wait times)
- Searching manually through Vimeo Help Center articles
- Interacting with third-party chatbot that parses existing help content
- Help Center search often returning irrelevant results
- No immediate access to precise, contextual answers
- Support teams manually responding to high volumes of repetitive queries

**Key Pain Points:**
- Delayed responses and long ticket wait times
- Help Center search returning irrelevant articles at a glance
- Third-party chatbot unable to handle specific queries effectively
- Customers frustrated by lack of immediate, accurate solutions
- Support inefficiency affecting customer satisfaction and retention
- Example: Searching "domain restrict embed" returns no relevant information

## The Solution

Vimeo built an AI help desk chat prototype leveraging RAG (Retrieval-Augmented Generation) to combine generative AI with existing Help Center content. The system provides immediate, accurate, and contextually relevant responses by indexing Zendesk articles in a vector store and using LangChain to orchestrate LLM interactions.

**Impact**: Prototype demonstrated AI's potential to dramatically improve customer support efficiency. Enables customers to receive immediate, precise, and actionable answers to specific queries. System tested with multiple LLM providers (Google Vertex AI Chat Bison, OpenAI ChatGPT 3.5 Turbo, ChatGPT 4, Azure OpenAI), ultimately selecting Google Vertex AI for concise responses, cost effectiveness, and seamless GCP authentication.

## How It Works

**Key Capabilities:**
- **Vector Store Indexing** - Zendesk Help Center articles scraped, split into chunks, converted to embeddings, and indexed in HNSWLib vector store
- **Conversational Retrieval** - LangChain's ConversationalRetrievalQAChain orchestrates multi-step LLM interactions
- **Standalone Question Generation** - Chat history + new question reformulated as standalone query for better retrieval
- **Similarity Search** - Question embedding matched against vector store to retrieve relevant article chunks
- **Contextual Response Generation** - LLM generates final answer using standalone question + relevant document chunks
- **Source Attribution** - Metadata (title, URL, tags) attached to enable linking back to original articles
- **Automatic Updates** - Zendesk webhooks trigger indexing updates when articles added/modified/removed

**Process Flow:**
1. User submits question through chat interface
2. System loads chat history from database
3. LLM rephrases question + history into standalone question (fixes misspellings, adds context)
4. Standalone question converted to embedding representation
5. Vector store queried for articles with similar content
6. Relevant document chunks returned with metadata
7. Standalone question + relevant docs sent to LLM
8. LLM generates final answer with actionable instructions
9. Response displayed with links to source articles

**Technical Architecture:** RAG system using Zendesk Help Center API for article scraping, HNSWLib for local vector storage, OpenAI embeddings, and LangChain for LLM orchestration. Compared Google Vertex AI Chat Bison, OpenAI ChatGPT 3.5 Turbo/4, and Azure OpenAI. Selected Google Vertex AI Chat Bison for: concise bullet-point responses (follows prompts better), faster response generation (fewer characters), cost savings, seamless GCP Workload Identity authentication (no API keys), and all-at-once response vs. streaming.

**Development Journey:** Built as AI exploration project using support content as testbed. Primary focus was demonstrating broader AI capabilities, not revolutionizing customer support. Prototype tested multiple LLM providers with rigorous comparison of performance, pricing, response quality, and streaming behavior.

## Key Insight

**RAG architecture combining organization-specific knowledge bases with LLMs enables precise, contextualized support responses impossible with LLMs alone.** By indexing Vimeo's Help Center into a vector store and using conversational retrieval patterns, the prototype demonstrated how AI can provide immediate, actionable answers grounded in existing documentation rather than hallucinated information.

**Why This Matters:**
- Generic LLMs (commercial or open-source) lack context for company-specific needs
- RAG bridges this gap by retrieving relevant internal documentation before generation
- Conversational retrieval uses chat history to improve followup question understanding
- Vector search enables semantic matching beyond keyword-based search limitations
- Source attribution builds trust by linking responses back to authoritative articles
- LLM provider comparison reveals meaningful tradeoffs (conciseness, latency, cost, streaming)

**LLM Provider Comparison Lessons:**
- **Google Vertex AI Chat Bison**: Concise bullet-point answers, faster response (fewer chars), better prompt following, seamless GCP auth, all-at-once responses
- **OpenAI ChatGPT 3.5 Turbo**: Longer paragraph responses, streaming available, slower under heavy API load
- **OpenAI ChatGPT 4**: Stronger answers than 3.5 Turbo but dramatically slower and 2x+ cost
- **Azure OpenAI**: Same performance as public API, higher cost, but better reliability/security/privacy for enterprises
- **Training data surprise**: ChatGPT contained old copy of Vimeo Help Center from late 2021 in training data!

**Quality Assurance Challenges:**
- Temperature set to 0 for consistent responses
- Prompt instructions direct AI to refuse non-Vimeo questions
- Safety filters (Vertex AI) and moderation endpoints (OpenAI) flag harmful prompts
- Unlimited possible questions make exhaustive QA testing impossible

## Links

- [Original Article](https://medium.com/vimeo-engineering-blog/from-idea-to-reality-elevating-our-customer-support-through-generative-ai-101a2c5ea680) - Comprehensive technical walkthrough of Vimeo's AI help desk chat prototype including architecture, LLM comparisons, and implementation code
