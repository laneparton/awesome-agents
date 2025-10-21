---
title: "Tender RFP Analysis Agent for Construction Sector"
company: "SoftIQ"
author: "Adam Marszowski and team"
source: "https://www.llamaindex.ai/blog/case-study-tender-rfp-agent-for-construction-sector-with-softiq"
date: "2025-01"
category: "research"
tags: ["document-analysis", "multimodal", "web-research"]
description: "Reduced tender analysis from hours/days to <10 minutes, enabling 6-10x productivity increase"

# Problem Classification
problemPattern: "document-processing-at-scale"
problemComplexity: "complex"

# Architecture
architecture:
  type: "single-agent"
  pattern: "workflow-based"
  rationale: "Chain of thought reasoning following domain-specific workflows ensures outputs match industry expectations and encode expert knowledge"
  components: ["semantic-chunker", "multimodal-parser", "workflow-engine"]

# What Made It Work
breakthroughInsight: "Semantic chunking that preserves hierarchical document structure was critical - simple text extraction lost essential context for nested tender requirements"

criticalConstraints:
  - "non-standardized-document-formats"
  - "multimodal-content-blueprints-diagrams"
  - "domain-workflow-compliance"
  - "100-page-documents"

antiPatterns:
  - "flat-chunking: lost hierarchical relationships in nested tender documents"
  - "text-only-parsing: missed critical information in blueprints and diagrams"
  - "keyword-based-search: highly inaccurate for finding relevant tenders"

# Tech Stack
techStack:
  framework: "LlamaIndex"
  llmProvider: "OpenAI"
  knowledgeRetrieval: "semantic-chunking"
  otherTools: ["LlamaParse"]

# Scale
scale:
  volume: "tens of thousands of documents, millions of pages"
  latency: "< 10 minutes per tender"
---

# Tender RFP Analysis Agent for Construction Sector

## The Problem

Poland's public sector construction tender market represents $7 billion annually with over 17,000 contracts awarded in 2024. Construction companies face massive inefficiencies in identifying and analyzing relevant tender opportunities from thousands of lengthy, unstructured documents.

**The Manual Process:**
- Keyword-based search to find potentially relevant tenders (highly inaccurate)
- Manual review of non-standardized tender documents: 2 hours to several days per tender
- Documents often exceed 100 pages with complex technical specifications
- Manual extraction of key information, terms, and requirements
- Risk assessment and compliance checking against company capabilities
- Generation of detailed internal reports with executive summaries

**Key Pain Points:**
- Keyword matching results in reviewing many irrelevant tenders, wasting time
- Thousands of unstructured documents uploaded to Poland's public tenders platform
- Multimodal content (blueprints, technical diagrams) difficult to analyze
- Non-standardized formats across different government entities
- Specific business workflows and reporting requirements must be followed
- Manual process limits companies to analyzing 3 tenders per day per employee

## The Solution

SoftIQ built Przetargi.io, a SaaS application with an AI agent that automates tender analysis for the construction industry. The agent processes lengthy tender documents, extracts relevant information, and generates comprehensive 20-30 page reports with executive summaries, risk assessments, and recommendations.

**Impact**: Reduced average tender analysis time to under 10 minutes. One pilot client increased throughput from 3 tenders per day per employee to 20-30 tenders per day per employee—a 6-10x productivity gain. Improved accuracy in identifying relevant tenders compared to keyword-based approaches.

## How It Works

**Key Capabilities:**
- **Advanced Document Ingestion** - Processes lengthy, unstructured tender documents at scale
- **Semantic Chunking** - Preserves hierarchical document structure and layout information
- **Multimodal Parsing** - Extracts information from blueprints and technical diagrams
- **Workflow-Based Reasoning** - Chain of thought reasoning following specific business processes
- **Automated Report Generation** - Produces 20-30 page reports matching industry expectations

**Process Flow:**
1. Monitor Poland's public tender platform for new construction-sector RFPs
2. Ingest and parse tender documents (often 100+ pages with mixed content)
3. Use semantic chunking to break down documents while preserving hierarchical structure
4. Extract multimodal information including text, tables, blueprints, and diagrams
5. Apply chain of thought reasoning following construction industry workflows:
   - Identify key requirements and specifications
   - Match against company capabilities
   - Assess compliance requirements
   - Evaluate risk factors
   - Determine strategic fit
6. Generate comprehensive report with:
   - Executive summary
   - Detailed requirements breakdown
   - Risk assessment
   - Strategic recommendations
7. Present analysis to decision-makers for bid/no-bid decisions

**Technical Architecture:** Built using agentic workflows where each section of the RFP report follows a specific business process. This ensures outputs mimic the structure and depth of manual analysis previously performed by experienced construction professionals.

## Key Insight

**The breakthrough was semantic chunking that preserves hierarchical document structure, combined with chain of thought reasoning that follows industry-specific workflows.** Simply extracting text wasn't sufficient—the agent needed to understand document layout, section relationships, and follow established business processes.

**Why This Matters:**
- Construction tenders contain deeply nested hierarchical information (project scope → phases → tasks → specifications)
- Losing document structure during chunking meant losing critical context for analysis
- Multimodal parsing enables understanding blueprints and technical diagrams alongside text
- Chain of thought reasoning ensures reports match the format and depth that industry professionals expect
- Workflow-based approach allows encoding domain expertise into the agent's analysis process

**Scale Achievement:** The system handles workloads of tens of thousands of documents spanning millions of pages—essential for monitoring Poland's entire public tender marketplace in real-time.

**Development Velocity:** Rapid development with production deployment saved an estimated 2 months compared to building document processing infrastructure from scratch.

## Links

- [Original Case Study](https://www.llamaindex.ai/blog/case-study-tender-rfp-agent-for-construction-sector-with-softiq) - Full SoftIQ story
- [Przetargi.io](https://przetargi.io/) - The production application
- [SoftIQ](https://softiq.pl/) - Company website
