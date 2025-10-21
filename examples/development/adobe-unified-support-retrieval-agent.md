---
title: "Adobe Unified Support Knowledge Retrieval Agent"
company: "Adobe"
author: "Adobe Developer Platform Team (Nay Doummar, Varsha Chandan Bellara, Jan Michael Ong) with AWS Generative AI Innovation Center"
source: "https://aws.amazon.com/blogs/machine-learning/adobe-enhances-developer-productivity-using-amazon-bedrock-knowledge-bases/"
date: "2025-06"
category: "development"
tags: ["developer-productivity", "knowledge-retrieval", "rag", "semantic-search", "enterprise"]
description: "20% accuracy increase with semantic search and metadata filtering, serving thousands of developers with immediate answers"
---

# Adobe Unified Support Knowledge Retrieval Agent

## The Problem

Adobe's thousands of internal developers rely on a vast, fragmented landscape of documentation—wiki pages, software guidelines, troubleshooting guides, and best practices spread across multiple systems. When setting up CI/CD pipelines in new AWS Regions, running pipelines on dev branches, troubleshooting issues, or upgrading software, developers spent excessive time hunting for the right information across disconnected sources.

**The Manual Process:**
- Search across multiple wiki pages and documentation repositories separately
- Sift through generic software guidelines to find Adobe-specific best practices
- Navigate disconnected troubleshooting guides for different domains (CI/CD, infrastructure, libraries, etc.)
- Re-ask similar questions to support teams, consuming support resources
- Context-switch between different documentation systems and formats
- **Total impact: Reduced developer productivity, increased support costs, delayed issue resolution**

**Key Pain Points:**
- No centralized place for developers to get immediate answers to questions
- Information siloed across multiple domains with no unified search
- Generic search unable to find domain-specific, Adobe-contextualized answers
- Support teams fielding repetitive questions already documented somewhere
- Developers unable to filter results by relevant domains (CI/CD, infrastructure, specific projects)
- Existing prototype struggled with scalability, resource onboarding, and retrieval precision

## The Solution

Adobe's Developer Platform team built Unified Support, a centralized AI-powered knowledge retrieval agent that provides immediate, accurate answers from across all documentation sources. Using semantic search with metadata filtering, developers can query across multiple domains and get Adobe-specific guidance in seconds, dramatically reducing time spent searching and support costs.

**Impact**:
- **20% increase** in retrieval accuracy compared to existing solution
- **Reduced support costs** through self-service knowledge retrieval
- **Thousands of Adobe developers** served with immediate answers
- **Multi-domain search** across CI/CD, infrastructure, libraries, and more with metadata filtering

## How It Works

**Key Capabilities:**
- **Semantic search** - Vector-based retrieval finds conceptually relevant answers, not just keyword matches
- **Metadata filtering** - Developers can filter by domain (project, year, type) to narrow results to relevant context
- **Multi-source ingestion** - Automatically ingests wiki pages, guidelines, troubleshooting docs from S3
- **Intelligent chunking** - 400-token fixed-size chunks with 20% overlap optimized through experimentation
- **RAG architecture** - Retrieval-augmented generation provides grounded, accurate answers

**Process Flow:**
1. Developer asks question (e.g., "How do I set up CI/CD pipeline in new AWS Region for Project A?")
2. Query automatically converted to 1,024-dimension vector embedding using Amazon Titan V2
3. Vector similarity search retrieves semantically relevant chunks from OpenSearch Serverless database
4. Optional: Metadata filter applied (e.g., `domain: "project A"`, `type: "wiki"`) to narrow results
5. Top-k most relevant document chunks retrieved and ranked by semantic similarity
6. Retrieved context presented to developer with source attribution
7. **Result: Immediate, accurate, Adobe-specific answer in seconds instead of manual searching**

**Technical Architecture:**
- **Data ingestion pipeline**: S3 buckets → chunking (400 tokens, 20% overlap) → vectorization (Amazon Titan V2) → OpenSearch Serverless vector database
- **Metadata system**: Each source document paired with `.metadata.json` file containing domain, year, type attributes
- **Retrieval API**: Amazon Bedrock Knowledge Bases Retrieve API with configurable filtering and top-k results
- **Evaluation framework**: Custom Ragas metrics for document relevance and Mean Reciprocal Rank (MRR)

**Development & Optimization:**
The team rigorously tested multiple chunking strategies:
- Fixed-size short (400 tokens, 20% overlap) - **Winner: highest accuracy**
- Fixed-size long (1,000 tokens, 20% overlap)
- Hierarchical (1,500 token parents, 300 token children)
- Semantic (400 tokens, 95% similarity threshold)

Fixed-size 400-token chunking proved simplest and most effective, consistently yielding highest MRR across different retrieval sizes (top-1 through top-5).

## Key Insight

**Metadata filtering transforms generic semantic search into domain-aware retrieval, enabling single knowledge base to serve multiple teams with precision.** The breakthrough wasn't just semantic search—it was the metadata filtering that allowed developers to navigate Adobe's complex, multi-domain information landscape and get contextually relevant answers.

**Why This Matters:**
- **Multi-tenancy through metadata**: Single knowledge base serves all domains without separate indexes per team
- **Rigorous evaluation**: Custom metrics (document relevance, MRR) provided objective framework for optimization
- **Experimentation-driven**: Tested 4 chunking strategies across multiple top-k values to find optimal configuration
- **Developer self-service**: Immediate answers reduce support ticket load and support costs
- **Adobe-specific context**: Generic documentation enhanced with company-specific best practices and guidelines

**Scalability Achievement:** From prototype to production system serving thousands of developers with seamless document ingestion, change synchronization, and flexible configuration (embedding model selection, chunk size adjustment, metadata schema).

## Links

- [Original AWS Blog Post](https://aws.amazon.com/blogs/machine-learning/adobe-enhances-developer-productivity-using-amazon-bedrock-knowledge-bases/) - Detailed technical write-up with architecture diagrams and evaluation results
- [Amazon Bedrock Knowledge Bases](https://aws.amazon.com/bedrock/knowledge-bases/) - Managed RAG service used for the solution
- [Ragas Evaluation Framework](https://docs.ragas.io/) - Open source framework extended for custom metrics
