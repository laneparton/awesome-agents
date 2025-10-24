---
title: "Thomson Reuters Customer Support RAG System"
company: "Thomson Reuters"
author: "Keshav Unni"
source: "https://medium.com/tr-labs-ml-engineering-blog/better-customer-support-using-retrieval-augmented-generation-rag-at-thomson-reuters-4d140a6044c3"
date: "2023-08"
category: "productivity"
tags: ["rag", "customer-support", "semantic-search", "production", "embeddings", "vector-database", "knowledge-retrieval"]
description: "RAG system with GPT-4 and Milvus vector database reducing customer support resolution times by grounding responses in up-to-date knowledge base articles with provenance, eliminating hallucinations"

# Problem Classification
problemPattern: "knowledge-retrieval"
problemComplexity: "medium"

# Architecture
architecture:
  type: "single-agent"
  pattern: "rag"
  rationale: "RAG combines parametric (LLM generalization) and non-parametric (vector DB knowledge) components to solve three critical support issues: hallucinations, lack of provenance, and stale knowledge - enabling accurate domain-specific responses with source citations and flexible knowledge updates without retraining"
  components: ["sentence-transformer-embeddings", "milvus-vector-database", "gpt4-generation", "similarity-search", "chunking-processor"]

# What Made It Work
breakthroughInsight: "RAG solves fundamental LLM limitations for support by introducing non-parametric retrieval component: eliminates hallucinations through grounding in actual KB articles, provides provenance with source citations, and enables knowledge updates without expensive LLM retraining - dense embeddings capture semantic relationships that keyword matching misses"

criticalConstraints:
  - "hundreds-thousands-kb-articles"
  - "expert-customer-base"
  - "specialized-legal-tax-products"
  - "rapidly-changing-product-information"
  - "cognitive-overload-agents"
  - "rising-support-expectations"

antiPatterns:
  - "pure-llm-without-retrieval: Generates plausible but incorrect generic advice without product-specific grounding, lacks source citations, and can't access current product information - produces hallucinations"
  - "sparse-keyword-retrieval: Traditional keyword matching misses fine-grained semantic relationships between queries and relevant knowledge, underperforms compared to dense vector embeddings for document retrieval"
  - "fixed-parametric-knowledge: LLMs trained on static data become stale quickly as products evolve - non-parametric vector DB allows knowledge updates without expensive retraining"

# Tech Stack
techStack:
  framework: "custom-rag"
  llmProvider: "GPT-4"
  knowledgeRetrieval: "dense-vector-retrieval"
  otherTools: ["Milvus", "sentence-transformers", "all-MiniLM-L6-v2", "cosine-similarity"]

# Scale
scale:
  volume: "Hundreds of thousands of KB articles across legal and tax products"
  latency: "Reduced resolution times with fast dense retrieval"
---

# Thomson Reuters Customer Support RAG System

**Company**: Thomson Reuters
**Domain**: Productivity & Automation
**Published**: August 2023

## Problem

Customer support agents at Thomson Reuters face significant cognitive overload when assisting customers with specialized legal and tax products like Westlaw, Practical Law, and Checkpoint. The challenges include:

### Finding Signal in the Noise
- Agents must quickly navigate CRM systems and hundreds of thousands of knowledge base articles
- When one agent finds a resolution, it's often not available to others in a structured manner
- Heavily reliant on person-to-person knowledge transfer
- Agents constantly in state of cognitive overload from information fragmentation

### Domain Expertise Requirements
Thomson Reuters customers are already experts in highly specialized fields (attorneys, executives, government officials). Support agents need to quickly make sense of an ever-changing set of information across complex products to assist these sophisticated users.

### Rising Customer Expectations
- **78% of customers** say their support experiences determine whether to continue buying
- **58% of customers** state their service expectations are higher than they were a year prior
- What constitutes great customer support today likely won't be good enough next year
- Need to continuously invest to keep up with evolving expectations

## Solution

Thomson Reuters Labs implemented a **Retrieval Augmented Generation (RAG)** system powered by GPT-4 to supercharge customer support executives with better access to domain knowledge.

### How It Works

**Processing and Indexing Flow:**

1. **Data Sources**: Knowledge base articles, CRM tools, and resolved ticket data
2. **Chunking**: Process text files into manageable chunks for embedding
3. **Embedding Generation**: Use pre-trained models (sentence transformers like all-MiniLM-L6-v2) to convert chunks into dense vector representations
4. **Vector Database Storage**: Store embeddings in Milvus (open-source vector database) for efficient similarity search

**Retrieval Flow:**

1. **Query Encoding**: User question is converted into dense vector embedding
2. **Similarity Search**: Compute cosine similarity or Euclidean distance between query vector and document vectors
3. **Context Retrieval**: Documents with highest similarity scores are retrieved as relevant context
4. **LLM Generation**: Most relevant context concatenated with prompts and sent to GPT-4 API
5. **Response**: GPT-4 generates accurate, domain-specific answer grounded in retrieved knowledge

### Impact

- **Reduced resolution times** for customer support queries
- **Provenance**: System provides sources and references, unlike pure LLM responses
- **Reduced hallucinations**: Grounding responses in actual knowledge base prevents fabricated answers
- **Better accuracy**: Concrete example shows RAG providing specific product steps vs generic advice

**Example Comparison:**

*Without RAG*: Generic troubleshooting advice that "looks like it makes sense" but isn't the accurate resolution

*With RAG*: Precise steps within the actual product:
1. Go to the Organizer
2. Click on General Information
3. Open Basic Return Information
4. Click on Paid Preparer Information
5. Correct any fields in the Third Party Designee section

This accuracy matches the actual resolution process within Thomson Reuters products with the most recent information.

## Key Insights

### 1. RAG Solves LLM Limitations for Support

Traditional LLMs face three critical issues in support scenarios:
- **Hallucinations**: Generating plausible but incorrect information
- **No provenance**: Can't cite sources or provide references
- **Stale knowledge**: Fixed parametric knowledge from training, not adaptable to new information

RAG addresses all three by introducing a non-parametric component that retrieves up-to-date, verifiable information before generation.

### 2. Dense Retrieval Captures Semantic Relationships

Unlike traditional sparse retrieval (keyword matching), dense vector representations:
- Capture fine-grained semantic relationships between text snippets
- Measure semantic similarity in embedding space
- Achieve better performance in document retrieval, passage ranking, and question-answering
- Handle large-scale collections with fast retrieval times

### 3. Knowledge Update Without Retraining

The non-parametric approach allows for flexible knowledge maintenance:
- Update knowledge base post-training without expensive LLM retraining
- Adapt to evolving data in real-world applications
- More economical means to introduce new information
- Critical for support where product information changes frequently

### 4. Balancing Parametric and Non-Parametric

The power comes from combining both approaches:
- **Parametric (LLM)**: Generalization abilities, language understanding, response generation
- **Non-parametric (Vector DB)**: Up-to-date knowledge, domain-specific information, verifiable sources
- Together: Accurate, contextual, provenance-backed responses

## Technical Architecture

```
Knowledge Sources
(KB Articles, CRM, Tickets)
         ↓
   [Processing Flow]
- Chunk text into segments
- Generate embeddings (sentence transformers)
- Store in Milvus vector database
         ↓
   [Retrieval Flow]
User Query → Embed Query
         ↓
Dense Retrieval (Similarity Search)
  - Cosine similarity / Euclidean distance
  - Return top-K most relevant documents
         ↓
Context + Prompt → GPT-4 API
         ↓
Accurate, Grounded Response
  - Domain-specific
  - With provenance
  - Reduced hallucinations
```

## References

- **Primary Source**: [Better Customer Support Using RAG at Thomson Reuters](https://medium.com/tr-labs-ml-engineering-blog/better-customer-support-using-retrieval-augmented-generation-rag-at-thomson-reuters-4d140a6044c3)
- **Author**: Keshav Unni (Thomson Reuters Labs)
- **Date**: August 2023
- **Research**: [RAG: Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401) (2021)

## Tags

`rag` `customer-support` `semantic-search` `production` `embeddings` `vector-database` `llm` `knowledge-retrieval`
