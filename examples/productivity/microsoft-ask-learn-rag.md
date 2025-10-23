---
title: "Microsoft Ask Learn - Advanced RAG Knowledge Service"
company: "Microsoft"
author: "Sarah Luck (Principal PM Manager), Bob Tabor (Software Developer), Microsoft Skilling Organization"
source: "https://devblogs.microsoft.com/engineering-at-microsoft/how-we-built-ask-learn-the-rag-based-knowledge-service/"
date: "2024-04"
category: "productivity"
tags: ["rag", "knowledge-retrieval", "production", "enterprise", "semantic-search"]
description: "Advanced RAG system powering Microsoft Q&A Assist and Copilot for Azure, reducing community response wait time from hours to instant answers with documentation-grounded responses"
---

# Microsoft Ask Learn - Advanced RAG Knowledge Service

## The Problem

Microsoft Q&A users typically waited hours for community responses to technical questions, often receiving only clarifying questions rather than actual answers. The team needed to provide interim answers via generative AI based on Microsoft Learn documentation to improve the question-answering experience while users waited for community expertise.

**The Manual Process:**
- Users post technical questions on Microsoft Q&A platform
- Wait hours (or longer) for community members to respond
- Frequently receive clarifying questions instead of solutions
- Must search through Microsoft Learn documentation manually
- No immediate access to documentation-based answers
- Quality varies significantly based on community availability and expertise

**Key Pain Points:**
- Hours-long wait times for any response, let alone quality answers
- Community responses often ask for clarification rather than providing solutions
- Users unable to get immediate help from existing documentation
- Microsoft Learn documentation not surfaced automatically in Q&A context
- No consistent quality baseline for responses
- Technical questions require up to 30 minutes of manual review for quality assurance

## The Solution

Microsoft built "Ask Learn," an Advanced RAG (Retrieval-Augmented Generation) system that goes beyond naive RAG with extensive pre- and post-processing. The service powers Microsoft Q&A Assist and Microsoft Copilot for Azure, providing instant documentation-grounded answers while users wait for community responses.

**Impact**: Launched May 2023, now powers both Microsoft Q&A Assist and Microsoft Copilot for Azure (announced November 2023). Developed in "just a few short, intense months" by cross-functional team. Enables three critical functions: direct Q&A, grounding data for multi-handler orchestration, and fallback assistance. Team performs root cause analysis on each response (up to 30 minutes per response) to ensure quality.

## How It Works

**Key Capabilities:**
- **Advanced RAG Processing** - Extensive pre-retrieval (query rewriting, expansion, clarification) and post-retrieval (re-ranking, filtering, compression) beyond naive RAG
- **Vector Similarity Search** - Microsoft Learn documentation chunked, embedded, and stored in vector database with cosine similarity retrieval
- **Service-Oriented Architecture** - High-level orchestration layer coordinating specialized services for chunking, embeddings, evaluation, and safety
- **Knowledge Service** - Manages vector embeddings with continuous updates as documentation changes
- **Golden Dataset Benchmarking** - Curated question-answer pairs for performance testing and validation
- **Safety Measures** - Harms evaluation tools and red-teaming for jailbreak detection

**Process Flow:**
1. User submits technical question on Microsoft Q&A or Copilot for Azure
2. Pre-retrieval processing rewrites, expands, and clarifies the query
3. Vector similarity search finds relevant Microsoft Learn documentation chunks using cosine similarity
4. Post-retrieval processing re-ranks, filters, and compresses retrieved chunks
5. Azure OpenAI APIs generate answer grounded in retrieved documentation
6. Response returned instantly to user while community response still pending
7. Continuous evaluation and root cause analysis (up to 30 minutes per response) ensures quality

**Technical Architecture:** .NET service-oriented architecture with orchestration layer coordinating specialized components. Knowledge Service manages vector embeddings and continuous documentation updates. Custom Python evaluation notebooks later migrated to evaluation flows in Prompt flow. Azure OpenAI APIs (initially direct, later migrated to Azure SDK preview packages) power generation.

**Development Journey:** Built in "just a few short, intense months" by cross-functional v-team including technical writers, engineers, and data scientists. Launched May 2023 for Microsoft Q&A Assist, expanded to power Microsoft Copilot for Azure (November 2023). Team emphasizes quality through rigorous root cause analysis on each response.

## Key Insight

**Advanced RAG with extensive pre- and post-processing delivers production-quality answers that naive RAG cannot achieve.** By investing in query rewriting, re-ranking, filtering, and compression around the core retrieval step, Microsoft enables instant documentation-grounded answers that reduce wait times from hours to seconds.

**Why This Matters:**
- Naive RAG (embed → retrieve → generate) insufficient for production quality at Microsoft's scale
- Pre-retrieval processing (query rewriting, expansion, clarification) improves retrieval relevance
- Post-retrieval processing (re-ranking, filtering, compression) ensures LLM receives optimal context
- Service-oriented architecture with orchestration layer enables continuous improvement
- Root cause analysis (up to 30 minutes per response) drives quality assurance and iteration

**Production Validation:**
- Powers both Microsoft Q&A Assist (May 2023) and Microsoft Copilot for Azure (November 2023)
- Three critical use cases: direct Q&A, grounding data for orchestration, fallback assistance
- Cross-functional v-team collaboration (technical writers, engineers, data scientists) essential
- Continuous evaluation through "golden dataset" benchmarks and safety red-teaming

## Links

- [Original Article](https://devblogs.microsoft.com/engineering-at-microsoft/how-we-built-ask-learn-the-rag-based-knowledge-service/) - Detailed technical deep dive into building Advanced RAG knowledge service at Microsoft scale
