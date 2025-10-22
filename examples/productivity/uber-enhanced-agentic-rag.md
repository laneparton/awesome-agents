---
title: "Uber Enhanced Agentic-RAG - Genie On-Call Copilot"
company: "Uber"
author: "Arnab Chakraborty, Paarth Chothani, Christopher Settles, Adi Raghavendra - Uber Engineering Security and AI Teams"
source: "https://www.uber.com/blog/enhanced-agentic-rag/"
date: "2025-05"
category: "productivity"
tags: ["workflow-automation", "rag", "knowledge-retrieval", "document-analysis", "production"]
description: "Enhanced agentic RAG achieving 27% relative increase in acceptable answers and 60% reduction in incorrect advice through enriched document processing and LLM-powered agents"
problem_type: "On-call support copilot providing incomplete, inaccurate responses failing to retrieve relevant information from knowledge base at SME quality standards"
architecture_pattern: "enhanced-agentic-rag-with-enriched-processing"
key_components: ["enriched-document-processing", "query-optimizer-agent", "source-identifier-agent", "hybrid-retrieval", "post-processor-agent", "llm-as-judge"]
breakthrough_insight: "Enriched document processing with LLM-powered table formatting and metadata enrichment (summaries, FAQs, keywords) combined with agentic pre/post retrieval steps dramatically improves accuracy beyond traditional RAG"
anti_patterns_avoided: ["traditional-pdf-loaders-losing-formatting", "simple-semantic-similarity-only", "single-retrieval-method", "manual-sme-evaluation-bottleneck"]
tech_stack:
  llms: ["LLMs for agents and answer generation"]
  frameworks: ["Langfx (Uber internal LangChain service)", "LangGraph", "Michelangelo"]
  infrastructure: ["Vector store", "BM25 retriever", "Offline feature store", "Google Docs API"]
  methods: ["RAG", "Custom document loaders", "LLM-powered enrichment", "Hybrid retrieval (vector + BM25)", "LLM-as-Judge evaluation"]
scale_metrics:
  improvement: "27% relative increase in acceptable answers"
  error_reduction: "60% relative reduction in incorrect advice"
  deployment: "Multiple security and privacy help channels"
  evaluation_speedup: "Weeks to minutes for experiment evaluation"
---

# Uber Enhanced Agentic-RAG - Genie On-Call Copilot

## The Problem

Genie is Uber's internal on-call copilot designed to provide real-time support for thousands of queries across multiple Slack help channels, enabling users to receive prompt responses with proper citations from Uber's internal documentation. While Genie's configurable framework allowed domain teams to deploy an LLM-powered Slack bot overnight with full RAG pipeline integration, delivering highly precise and relevant responses to domain-specific queries remained a significant challenge. When tested against a golden set of 100+ curated queries for engineering security and privacy with 40+ policy documents, response quality didn't meet SME standards—many answers were incomplete, inaccurate, or failed to retrieve relevant information in correct detail from the knowledge base.

**The Manual Process:**
- On-call engineers and SMEs manually responding to common ad-hoc queries in Slack
- Effort required to address repetitive questions across multiple help channels
- SMEs spending significant time providing guidance on security and privacy policies
- Manual review of every chatbot response taking weeks to evaluate experiments
- Traditional RAG approach with basic PDF loaders losing table formatting and structure
- Chunking and retrieval challenges due to poor text extraction quality

**Key Pain Points:**
- **Accuracy gaps** - Incomplete or inaccurate answers failing SME quality standards for critical security/privacy guidance
- **Retrieval challenges** - Ambiguous queries or context-lacking questions hinder accurate document retrieval
- **Formatting loss** - Traditional PDF loaders fail to capture structured text, bullet points, and complex tables correctly
- **Context fragmentation** - Table cells become isolated stand-alone text, disconnecting from row/column context
- **Semantic search limitations** - Simple semantic similarity leads to retrieving irrelevant context with subtle distinctions across documents
- **Evaluation bottleneck** - Manual SME assessment requiring significant bandwidth, often taking weeks per experiment
- **Marginal improvements** - Experiments yielding slight accuracy gains before plateauing with no clear enhancement path

## The Solution

Uber developed Enhanced Agentic RAG (EAg-RAG) transitioning from PDFs to Google Docs with HTML formatting, implementing custom document loaders with LLM-powered table enrichment, and introducing LLM-powered agents in pre-retrieval and post-processing steps. The system enriches metadata with document summaries, FAQs, and keywords; uses dual-agent pre-processing (Query Optimizer and Source Identifier); implements hybrid retrieval combining vector search with BM25; and employs Post-Processor agent for de-duplication and structural organization. LLM-as-Judge framework automates evaluation reducing experiment assessment from weeks to minutes.

**Impact**: 27% relative increase in acceptable answers, 60% relative reduction in incorrect advice, measurable reduction in support load for on-call engineers and SMEs allowing focus on complex high-value tasks, evaluation time reduced from weeks to minutes enabling faster iterations, now deployed across multiple security and privacy help channels.

## How It Works

**Key Capabilities:**
- **Enriched Document Processing** - Custom Google Docs loader using Python API extracting paragraphs, tables, table of contents recursively with LLM-powered table formatting converting to markdown and enriching metadata
- **Metadata Enrichment** - Document summaries, FAQs, keywords added to chunks; table-aware chunking using metadata identifiers keeping tables intact with two-line summaries and keywords for semantic search relevancy
- **Agentic Pre-Processing** - Query Optimizer refines ambiguous queries and breaks complex queries into simpler ones; Source Identifier narrows document subset using document list artifact (titles, summaries, FAQs)
- **Hybrid Retrieval** - Vector search for semantic similarity + BM25 retriever using enriched metadata (summaries, FAQs, keywords) with union of results
- **Post-Processing Agent** - De-duplicates retrieved chunks and structures context based on positional order within original documents
- **LLM-as-Judge Automation** - Evaluates chatbot responses using user query, SME response, evaluation instructions, additional retrieved documents; scores 0-5 with reasoning for feedback

**Process Flow:**
1. **Document Processing (Offline)** - Custom Google Docs loader extracts content using Python API recursively
2. **Table Enrichment** - LLM converts extracted table contents to markdown-formatted tables with metadata identifiers distinguishing table-containing chunks
3. **Content Enrichment** - LLM generates document summaries, FAQs, keywords added to chunk metadata; table chunks get two-line summaries and keywords for improved semantic search
4. **Indexing and Storage** - Chunks indexed and embeddings generated, stored in vector store; artifacts (document lists, FAQs) saved in offline feature store
5. **Query Reception** - User asks question via Slack on-call channel
6. **Pre-Processing - Query Optimizer** - Refines query if lacking context or ambiguous, breaks down complex queries into multiple simpler queries using document list artifact as context
7. **Pre-Processing - Source Identifier** - Processes optimized query to narrow document subset most likely containing relevant answers using few-shot examples and document list
8. **Hybrid Retrieval** - Vector search fetches semantically similar chunks restricted to identified documents; BM25 retriever fetches chunks using enriched metadata; union of results returned
9. **Post-Processing Agent** - De-duplicates retrieved chunks, structures context by positional order in original documents
10. **Answer Generation** - Original query + optimized auxiliary queries + post-processed context passed to LLM with specific instructions for answer construction
11. **Response Delivery** - Generated answer with proper citations shared via Slack interface
12. **Automated Evaluation (Testing)** - LLM-as-Judge scores response 0-5 using SME response, query, evaluation instructions, retrieved documents as context; provides reasoning for feedback

**Enriched Processing Details:**
- **Problem with Traditional Loaders**: SimpleDirectoryLoader (LlamaIndex), PyPDFLoader (LangChain) lose formatting; complex tables spanning 5+ pages with nested cells become fragmented; cells isolated without row/column context; chunking splits tables incorrectly; semantic search can't fetch correct values
- **HTML to Markdown Challenges**: html2text and Markdownify from LangChain show improvements but still formatting issues with tables
- **Custom Solution**: Google Docs with HTML formatting + custom Python API loader + LLM-powered markdown conversion for tables + metadata identifiers for table-aware chunking = preserved structure and context

**Agentic RAG Components:**
- **Query Optimizer**: Refines ambiguous queries, breaks complex queries into simpler ones for better retrieval
- **Source Identifier**: Uses document list (titles, summaries, FAQs) with few-shot examples to narrow document subset
- **Hybrid Retrieval**: Vector search (semantic) + BM25 (keyword-based with enriched metadata) union
- **Post-Processor**: De-duplication + structural organization by positional order in source documents

**LLM-as-Judge Framework:**
- **Stage 1 (One-time)**: SMEs provide high-quality responses or feedback on chatbot answers
- **Stage 2 (Batch)**: Chatbot generates responses using current version
- **Stage 3 (Evaluation)**: LLM evaluates using query, SME response, evaluation instructions, additional documents from latest RAG pipeline as context (C)
- **Output**: 0-5 scale score + reasoning for evaluation + feedback for future experiments
- **Benefit**: Reduces evaluation time from weeks to minutes, enables rapid iteration

**Technical Stack:**
- Built on Langfx (Uber internal LangChain-based service) within Michelangelo
- LangGraph for agent development and workflow orchestration
- Sequential flow currently, expandable to complex agentic frameworks
- Configurable components within Michelangelo Genie framework for cross-domain adoption

## Key Insight

**Enriched document processing with LLM-powered table formatting and metadata enrichment (summaries, FAQs, keywords) combined with agentic pre/post retrieval steps dramatically improves accuracy beyond traditional RAG.** Traditional PDF loaders lose critical structure (tables, formatting) fragmenting context, while simple semantic similarity retrieves irrelevant content when documents have subtle distinctions. By preserving structure through custom loaders with LLM-enrichment and adding intelligent agents to optimize queries, identify sources, and structure context, the system bridges the gap between basic RAG and SME-quality precision.

**Why This Matters:**
- **Data quality foundation** - Model quality depends on data quality; enriched processing ensures high-quality inputs for RAG pipeline
- **Context preservation** - Table-aware chunking with metadata identifiers keeps complex structures intact, preventing fragmentation during retrieval
- **Semantic search enhancement** - Summaries, FAQs, keywords in metadata improve relevancy beyond basic embedding similarity
- **Query refinement** - Ambiguous or complex queries optimized before retrieval prevents poor retrieval results
- **Source targeting** - Identifying relevant document subset before search reduces noise from irrelevant documents with similar language
- **Hybrid retrieval power** - Combining vector (semantic) + BM25 (keyword/metadata) captures both conceptual and literal matches
- **Evaluation acceleration** - LLM-as-Judge reduces weeks to minutes, unblocking rapid experimentation and iteration
- **Modular agent architecture** - Agentic approach allows seamless integration/testing of incremental improvements vs monolithic RAG

**Development Breakthrough:**
Overcoming two critical challenges: (1) Manual SME evaluation bottleneck taking weeks, and (2) Marginal accuracy gains plateauing with no clear path forward. LLM-as-Judge automation + agentic RAG framework solved both—fast evaluation enabled rapid iteration, modular agents allowed testing incremental improvements independently.

**Future Enhancements:**
- Multi-modal content extraction and enrichment (images)
- Iterative Chain-of-RAG for multi-hop reasoning queries
- Self-critique agent after answer generation to refine responses and reduce hallucinations
- Tool-based approach where LLM agents choose tools based on query type/complexity
- Foundation for building agentic RAG systems for Q&A automation across Uber

## Links

- [Original Blog Post](https://www.uber.com/blog/enhanced-agentic-rag/) - Technical deep dive into Enhanced Agentic-RAG architecture for Genie on-call copilot
- [Michelangelo Platform](https://www.uber.com/blog/michelangelo-machine-learning-platform/) - Uber's ML platform including Langfx and Genie framework
- [LangGraph](https://www.langchain.com/langgraph) - Framework for building agentic AI workflows
