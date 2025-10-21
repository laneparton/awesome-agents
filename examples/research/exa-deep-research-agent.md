---
title: "Exa Deep Research Multi-Agent System"
company: "Exa"
author: "Exa"
source: "https://blog.langchain.com/exa/"
date: "2025-06"
category: "research"
tags: ["multi-agent", "web-research", "structured-output", "langgraph", "production"]
description: "Processing hundreds of daily queries with structured research results in 15 seconds to 3 minutes"
---

# Exa Deep Research Multi-Agent System

## The Problem

Exa, known for their high-quality search API, needed to evolve beyond simple search endpoints to handle complex, deep research queries. Users needed a system that could autonomously explore the web across multiple dimensions to find and structure comprehensive information.

**The Manual Process:**
- Users had to manually formulate multiple search queries to cover different aspects of a research topic
- Results from different searches needed manual review and synthesis
- Converting search results into structured, parseable formats required significant manual effort
- Determining when to read full content vs. snippets was left to users, often leading to excessive reading or missed context
- Research could take hours to days depending on complexity and depth required

**Key Pain Points:**
- Traditional search APIs only returned raw results without deep analysis or synthesis
- Simple "answers" endpoints couldn't handle multi-faceted research requiring parallel investigation
- No way to dynamically scale research effort based on query complexity
- Unstructured outputs made API integration difficult for downstream systems
- Token costs could spiral without visibility into usage patterns

## The Solution

Exa built a production-ready deep research agent using a sophisticated multi-agent architecture that autonomously explores the web until it finds the structured information users need. The system processes hundreds of research queries daily, delivering comprehensive structured results in 15 seconds to 3 minutes depending on complexity.

**Impact**: Transformed Exa's offering from static search API to fully agentic research system handling hundreds of daily production queries with reliable structured output and predictable token costs through comprehensive observability.

## How It Works

**Key Capabilities:**
- **Dynamic Task Generation** - Planner analyzes queries and creates appropriate number of parallel research tasks based on complexity
- **Parallel Task Execution** - Independent research units execute simultaneously with specialized tools and reasoning
- **Context Engineering** - Observer maintains full visibility while individual tasks receive only cleaned outputs from other tasks
- **Smart Content Loading** - System starts with search snippets and only requests full page content when snippet-level reasoning proves insufficient
- **Structured Output** - All outputs are JSON-formatted with runtime-configurable schemas for reliable API consumption

**Process Flow:**
1. Planner agent receives research query and analyzes complexity
2. Planner dynamically generates multiple parallel tasks (number varies by query complexity)
3. Each task receives specific instructions, required JSON output format, and access to Exa API tools
4. Tasks execute independently, attempting reasoning on search snippets first
5. If snippets insufficient, tasks escalate to requesting full page content
6. Observer agent maintains full context across all planning, reasoning, outputs, and citations
7. System returns structured JSON output in specified format

**Technical Architecture:** Built entirely on LangGraph's multi-agent coordination capabilities with intentional context engineering. The Observer sees everything across all components while individual Tasks only receive final cleaned outputs, not intermediate reasoning states. This prevents context pollution while maintaining system-wide visibility. Uses function calling for structured output generation and LangSmith for comprehensive token usage tracking.

## Key Insight

**Search snippets first, full content only when necessary** - This context engineering decision significantly reduced token usage while preserving research quality. The system attempts reasoning on search snippets before escalating to full page crawls, enabled by Exa's API ability to swap between snippet and full result modes.

**Why This Matters:**
- Token cost control is critical for production agentic systems, and observability was essential for informing pricing models
- Structured JSON output at every level enables reliable API consumption, unlike unstructured research reports
- Dynamic task scaling handles both simple single-task queries and complex multi-faceted research without rigid workflow constraints
- Designing for API consumption (not end users) drove different architectural choices than consumer-facing research tools
- The architecture mirrors learnings from Anthropic's Deep Research system while adding production-specific optimizations

**Evolution Pattern:** Exa's progression from search API → answers endpoint → agentic research reflects broader industry trend of LLM applications becoming more agentic and long-running over time. As architectures grew more complex, framework adoption (LangGraph) became necessary where it wasn't before.

## Links

- [Case Study: How Exa built a Web Research Multi-Agent System](https://blog.langchain.com/exa/) - Original LangChain blog post
- [Exa Deep Research API](https://exa.ai) - Try the production API
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph) - Framework used for multi-agent coordination
