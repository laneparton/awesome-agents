---
title: "Manus - Context Engineering for Production AI Agents"
company: "Manus"
author: "Manus Engineering Team"
source: "https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus"
date: "2025-01"
category: "development"
tags: ["agent-framework", "developer-productivity", "production", "enterprise"]
description: "Production AI agent framework achieving 10x cost savings through KV-cache optimization and context engineering, tested across millions of users"

# Problem Classification
problemPattern: "framework-platform-building"
problemComplexity: "complex"

# Architecture
architecture:
  type: "single-agent"
  pattern: "context-engineered-agent"
  rationale: "Chose in-context learning over fine-tuning to enable rapid iteration (hours vs weeks) with strategic context structuring, KV-cache optimization, and state machine tool masking"
  components: ["context-manager", "state-machine", "file-system-memory", "kv-cache-optimizer", "action-space-controller"]

# What Made It Work
breakthroughInsight: "KV-cache hit rate is the single most important production metric - cached tokens cost $0.30/MTok vs $3/MTok uncached (10x difference), with typical 100:1 input-to-output ratio heavily favoring prefill optimization"

criticalConstraints:
  - "rapid-iteration-required"
  - "cost-at-scale-critical"
  - "model-agnostic-desired"
  - "long-context-degradation"
  - "cache-stability-essential"

antiPatterns:
  - "dynamic-timestamps: precise timestamps in system prompts break KV-cache"
  - "tool-removal: dynamically adding/removing tools mid-task invalidates cache"
  - "aggressive-compression: losing observation details harms error recovery"
  - "uniform-context: repetitive patterns enable few-shot overfitting"
  - "hiding-errors: error recovery is clearest indicator of agentic behavior"

# Tech Stack
techStack:
  framework: "Custom"
  llmProvider: ["Claude Sonnet", "vLLM"]
  knowledgeRetrieval: "file-system-as-memory"
  otherTools: ["Hermes Function-Calling", "prefix-caching", "state-machines"]

# Scale
scale:
  volume: "Tested across millions of users"
  latency: "Average task requires ~50 tool calls"
---

# Manus - Context Engineering for Production AI Agents

## The Problem

Building production AI agents required choosing between training custom agentic models (weeks of iteration cycles) or leveraging in-context learning capabilities of frontier models (hours of iteration). The challenge was achieving rapid development velocity while maintaining production-grade performance, cost efficiency, and model agnosticism at scale.

**The Manual Process:**
- Fine-tune custom models for agentic behavior
- Wait weeks for training and evaluation cycles
- Lock into specific model architectures
- Rebuild for each new model generation
- High costs without cache optimization
- Debug issues through retraining cycles

**Key Pain Points:**
- Model fine-tuning requires weeks per iteration
- Vendor lock-in to specific model families
- KV-cache invalidation causes 10x cost increases
- Long contexts degrade model performance
- Lost-in-the-middle issues with complex tasks
- Few-shot brittleness from repetitive context patterns
- Tool management breaks caching when dynamic

## The Solution

Manus adopted context engineering over fine-tuning, strategically structuring prompts and context to guide agent behavior while optimizing KV-cache hit rates as the primary production metric. The system uses state machines for tool masking, file systems for persistent memory, and attention manipulation for task focus.

**Impact**: Achieved 10x cost savings through KV-cache optimization ($0.30/MTok cached vs $3/MTok uncached) with rapid iteration cycles (hours instead of weeks), tested across millions of users with average tasks requiring ~50 tool calls.

## How It Works

**Key Capabilities:**
- **KV-Cache Optimization** - Stable prompt prefixes and append-only context maximize cache hit rates for 10x cost reduction
- **State Machine Tool Masking** - Context-aware state machine masks token logits during decoding to constrain action selection without modifying tool definitions (preserving cache)
- **File System as Memory** - Treats file system as unlimited, persistent context directly operable by agents
- **Attention Manipulation** - Agents maintain todo.md files updated throughout execution, "reciting objectives" at context end to combat lost-in-the-middle
- **Error Preservation** - Retains failed actions and error traces in context for genuine error recovery
- **Context Diversity** - Introduces structured variation in actions/observations to prevent few-shot brittleness

**Process Flow:**
1. Agent receives task with stable prompt prefix (no dynamic timestamps)
2. Model selects action from available tools (state machine masks unavailable options)
3. Action executes and observation appends to context (deterministic serialization)
4. Agent updates todo.md file with current objectives and progress
5. File system stores persistent state accessible across iterations
6. Failed actions and error traces preserved in context for learning
7. Small structured variations introduced to prevent pattern overfitting
8. KV-cache reuses prefill computation across iterations (10x cost savings)
9. Iteration continues until task completion (~50 tool calls average)
10. Session IDs route requests across distributed workers maintaining context

**Technical Architecture:** vLLM with prefix caching enabled for self-hosted inference. Hermes Function-Calling format for constrained response generation. State machines manage context-aware tool availability through logit masking without cache invalidation. File system serves as persistent, unlimited memory layer. Append-only context with deterministic serialization ensures cache stability.

**Framework Evolution:** Rebuilt four times as better patterns emerged from production usage across millions of users. Current design prioritizes cache stability over dynamic flexibility.

## Key Insight

**KV-cache hit rate is the single most important production metric for cost and performance.** With typical 100:1 input-to-output ratios, cached tokens at $0.30/MTok versus $3/MTok uncached create 10x cost difference, making prefill optimization critical.

**Why This Matters:**
- Prompt prefix stability (no timestamps, no tool modifications) is non-negotiable for cache hits
- Append-only context with deterministic serialization preserves cache across iterations
- Tool masking via logit manipulation beats dynamic tool removal for cache preservation
- File system as memory provides unlimited context without invalidating cache
- Error preservation enables true agentic behavior and learning from mistakes
- Context diversity prevents few-shot brittleness where agents blindly follow patterns
- Long contexts degrade performance despite large context windows—compression strategies needed

**Action Space Management**: Rather than dynamically adding/removing tools (which breaks cache), use state machines to mask token logits during decoding, constraining action selection without modifying tool definitions.

**Lost-in-the-Middle Solution**: Agents maintain and update todo.md files throughout execution, placing current objectives at the end of context to combat attention degradation in long contexts.

**Production vs Research Trade-offs**: Chose in-context learning over fine-tuning despite potential performance gaps, valuing rapid iteration (hours vs weeks) and model agnosticism for production systems.

## Links

- [Original Article](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus) - Context Engineering for AI Agents: Lessons from Building Manus
