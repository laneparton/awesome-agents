---
title: "Anthropic Multi-Agent Research System"
company: "Anthropic"
author: "Jeremy Hadfield, Barry Zhang, Kenneth Lien, Florian Scholz, Jeremy Fox, Daniel Ford and Anthropic Apps Engineering Team"
source: "https://www.anthropic.com/engineering/multi-agent-research-system"
date: "2025-06"
category: "research"
tags: ["multi-agent", "web-research", "parallel-execution", "production"]
description: "90% faster complex research through orchestrator-worker pattern with 3-5 parallel subagents, saving users days of work"

# Problem Classification
problemPattern: "multi-source-research"
problemComplexity: "complex"

# Architecture
architecture:
  type: "multi-agent"
  pattern: "coordinator-workers"
  rationale: "Orchestrator-worker pattern enables parallel execution (3-5 subagents simultaneously) with dynamic scaling based on query complexity - critical for reducing research time from days to minutes"
  components: ["lead-researcher-orchestrator", "specialized-subagents", "citation-agent", "memory-persistence", "adaptive-planning"]

# What Made It Work
breakthroughInsight: "Token efficiency is 80% of performance variance - model selection (Sonnet 4 → Opus 4) yielded larger gains than doubling token budget, and parallel execution reduced research time by ~90%"

criticalConstraints:
  - "context-limits-200k-tokens"
  - "production-scale"
  - "complex-multi-faceted-queries"
  - "citation-management-required"

antiPatterns:
  - "single-agent-sequential: couldn't handle parallel nature of deep research effectively"
  - "fixed-workflows: needed dynamic scaling based on query complexity"

# Tech Stack
techStack:
  framework: "custom"
  llmProvider: "Anthropic"
  knowledgeRetrieval: "multi-source-web"
  otherTools: ["extended-thinking", "interleaved-thinking"]

# Scale
scale:
  volume: "production Claude Research feature"
  latency: "~90% reduction in research time for complex queries"
---

# Anthropic Multi-Agent Research System

## The Problem

Research tasks involve open-ended exploration where the required steps are "very difficult to predict in advance." Manual research requires sequential searching, following multiple independent leads simultaneously, and synthesizing vast amounts of information—a time-consuming, path-dependent process that could take days for complex queries.

**The Manual Process:**
- Manually formulate multiple search queries to cover different research angles
- Execute searches sequentially, waiting for each to complete before starting the next
- Review and evaluate results from each search independently
- Synthesize findings across multiple sources and research threads
- Track citations and sources manually throughout the process
- Complex research tasks like "identify all board members of Information Technology S&P 500 companies" required hours to days of manual work

**Key Pain Points:**
- Sequential searching created bottlenecks when multiple research threads needed exploration
- Single-agent approaches couldn't handle the parallel nature of deep research effectively
- Context limits (200k+ tokens) made it difficult to maintain full research state across long sessions
- No systematic way to scale research effort based on query complexity
- Difficult to balance breadth (exploring many angles) with depth (thorough investigation of promising leads)

## The Solution

Anthropic built a production multi-agent research system using an orchestrator-worker pattern where a lead agent coordinates specialized subagents operating in parallel. The system performs dynamic, multi-step web searches, adapts to new findings, and analyzes results to formulate high-quality answers—now powering Claude's Research feature.

**Impact**:
- **90.2% performance improvement** over single-agent Claude Opus 4 on internal research evaluations
- **~90% reduction in research time** for complex queries through parallelization (3-5 subagents running simultaneously)
- Users reported **"saving up to days of work"** and discovering business opportunities they would have otherwise missed
- Successfully handles complex multi-faceted queries in production at scale

## How It Works

**Key Capabilities:**
- **Orchestrator-Worker Architecture** - Lead researcher analyzes queries, develops strategy, and spawns specialized subagents while maintaining overall context
- **Parallel Execution** - 3-5 subagents execute simultaneously, each independently exploring different research angles with 3+ tool calls in parallel
- **Adaptive Planning** - System uses extended thinking for strategic planning and interleaved thinking for real-time reasoning refinement
- **Memory Persistence** - Critical context maintained across sessions as research approaches 200k+ token limits
- **Citation Management** - Dedicated citation agent identifies sources and ensures proper attribution across all findings

**Process Flow:**
1. Lead Researcher agent receives query and performs extended thinking to analyze complexity
2. Lead agent develops research strategy and determines appropriate number of subagents to spawn
3. Specialized subagents launch in parallel (typically 3-5), each with specific research objectives and task boundaries
4. Each subagent independently performs web searches using interleaved thinking for adaptive refinement
5. Subagents evaluate results and determine whether findings meet their objectives or require further exploration
6. Completed findings are compressed and returned to lead agent with relevant context
7. Citation agent processes all sources and ensures proper attribution
8. Lead agent synthesizes findings from all subagents into comprehensive final answer
9. Full execution history persisted to memory for context continuity

**Technical Architecture:** Built on orchestrator-worker pattern with context engineering at its core. The Lead Researcher maintains full system state and delegates to specialized workers. Subagents use interleaved thinking as a "controllable scratchpad" for reasoning. System scales from simple queries (1 agent, 3-10 tool calls) to complex research (10+ subagents). Tool design treated as "critically important as human-computer interfaces" with broad-to-narrow search progression. Production deployment uses "rainbow deployments" to avoid disrupting running agents during updates.

**Development Approach:** Team built internal simulations to observe agent failure modes, using the principle "think like your agents" to debug behaviors. Prompting focused on teaching orchestrators detailed delegation with specific objectives and clear task boundaries. Production implementation required resumable execution, graceful error handling, and full tracing to handle compounding errors in stateful systems.

## Key Insight

**Token efficiency is 80% of performance variance** - Analysis revealed three factors explained 95% of performance: token usage (80% contribution), tool call count, and model choice. Surprisingly, upgrading from Claude Sonnet 4 to newer models yielded larger performance gains than doubling the token budget.

**Why This Matters:**
- Model selection has outsized impact compared to simply increasing token budgets for agentic systems
- Extended and interleaved thinking modes act as "controllable scratchpads" that can be tuned for specific reasoning needs
- Teaching orchestrators how to delegate is fundamentally different from teaching single agents to execute—requires explicit guidance on objectives and boundaries
- Tool design quality directly impacts agent effectiveness, similar to how UI/UX design affects human productivity
- Production agentic systems require different infrastructure than request-response systems: resumability, error handling, tracing, and deployment strategies that don't disrupt running agents

**Critical Prompting Principles:**
- Build agent simulations to observe failure modes before production deployment
- Scale effort to query complexity dynamically rather than using fixed workflows
- Start searches broad, then progressively narrow based on findings
- Provide specific objectives and clear task boundaries when delegating to subagents

## Links

- [Building a Multi-Agent Research System](https://www.anthropic.com/engineering/multi-agent-research-system) - Original engineering deep dive
- [Claude Research Feature](https://www.anthropic.com/claude/research) - Try the production implementation
