---
title: "Airtable Event-Driven Agentic Framework"
company: "Airtable"
author: "Ameya Khare and Justin Lu, Airtable Engineering Team"
source: "https://medium.com/airtable-eng/how-we-built-ai-agents-at-airtable-70838d73cc43"
date: "2025-08"
category: "productivity"
tags: ["workflow-automation", "event-driven", "production", "conversational-interface"]
description: "Powers Omni app builder and Field Agents to automate thousands of hours with event-driven state machine architecture"

# Problem Classification
problemPattern: "framework-platform-building"
problemComplexity: "complex"

# Architecture
architecture:
  type: "event-driven"
  pattern: "state-machine"
  rationale: "Custom framework provided faster iteration than existing frameworks - avoiding over-abstraction, gaining finer control over prompts, and achieving greater observability"
  components: ["context-manager", "tool-dispatcher", "decision-engine", "error-handler"]

# What Made It Work
breakthroughInsight: "Building a custom agentic framework wasn't difficult and delivered critical advantages over pre-built frameworks for production scale - finer control, better observability, and faster iteration"

criticalConstraints:
  - "production-scale-multiple-products"
  - "large-context-windows"
  - "token-cost-optimization"
  - "conversational-interface-required"

antiPatterns:
  - "pre-built-frameworks: helpful for prototypes but limited control for production optimization"
  - "loading-full-context: approaching context limits required smart trimming and filtering"

# Tech Stack
techStack:
  framework: "custom"
  llmProvider: ["OpenAI", "Anthropic"]
  knowledgeRetrieval: "context-management"

# Scale
scale:
  volume: "thousands of hours automated"
  latency: "real-time conversational"
---

# Airtable Event-Driven Agentic Framework

## The Problem

Airtable's initial AI capabilities—AI fields, AI in automations, AI-generated select options, and AI formula generation—worked well for simple use cases but were fundamentally limited. They couldn't reason through problems requiring dynamic decision making or retrieve additional data beyond what had been provided upfront. These early AI features couldn't perform complex tasks like fetching data from the internet or a base, analyzing data dynamically, or building interfaces.

**The Manual Process:**
- Users had to manually break down complex tasks into simple steps that non-agentic AI could handle
- Data retrieval required explicit upfront specification—no dynamic fetching
- Analysis tasks needed all data provided in advance, limiting scope and flexibility
- No ability to reason through multi-step workflows autonomously
- Building apps and interfaces remained entirely manual

**Key Pain Points:**
- Static AI capabilities couldn't adapt to new information or changing requirements
- No conversational interface for users to iterate with AI and provide feedback
- Simple AI features couldn't handle the complexity of real-world workflows
- Users couldn't engage naturally with AI to accomplish complex tasks
- System couldn't autonomously decide which actions were needed to complete a request

## The Solution

Airtable built a custom agentic framework as an asynchronous event-driven state machine that powers all their AI features, including Omni (conversational app builder) and Field Agents (AI-powered fields that autonomously gather insights and create content). The framework enables agents to remember context, perform predefined actions, and autonomously decide which actions are needed—capable of reasoning, planning, and orchestrating complex tasks with minimal user input.

**Impact**:
- **Relaunched Airtable as AI-native app platform** with agents automating thousands of hours of work in seconds
- **Powers multiple production products**: Omni conversational app builder and Field Agents
- **Faster iteration** compared to using existing agentic frameworks through finer control and better observability
- **15-30% reduction** in tokens, inference latency, and cost through ID aliasing optimization
- **Handles bases at scale** with smart context management and MapReduce-style summarization

## How It Works

**Key Capabilities:**
- **Event-Driven State Machine** - Consumes and processes events with specific handlers for each type
- **Contextual Memory** - Maintains guidelines (purpose/tone), session (base schema/user info), and event history
- **Tool Orchestration** - Exposes predefined actions and runs tools when requested by decision engine
- **LLM-Powered Decision Making** - "Brain" of agent decides next steps using all available context
- **Smart Context Management** - Handles large context windows through trimming, filtering, and summarization
- **MapReduce-Style Processing** - Parallelizes large dataset analysis across multiple LLM calls

**Process Flow:**
1. User sends message into interaction, triggering user message event
2. Context manager stores event and makes it accessible to all components
3. Decision engine (LLM-powered "brain") receives context and decides next action
4. If action needed, decision engine produces tool call event
5. Tool dispatcher executes requested tool with error handling for self-correction
6. Tool completion produces tool call output event sent back to decision engine
7. Decision engine analyzes output and determines if more tools needed or task complete
8. When complete, decision engine produces LLM message event with final response
9. Full cycle from initial prompt to final response completes one "interaction"

**Technical Architecture:** Built as event-driven state machine with three core components. **Context Manager** maintains all information accessible to agent: guidelines context (instructions for tone/purpose), session context (Airtable base schema and user permissions), and event context (chronological event history). **Tool Dispatcher** exposes tools (predefined actions), runs them when requested, and provides error handling with retriable/non-retriable distinction plus helpful LLM-visible error messages for self-correction. **Decision Engine** serves as LLM-backed "brain," serializing context into provider API formats (OpenAI, Anthropic), invoking inference APIs, and parsing responses to emit either tool call events or final message events.

**Handling Large Context:** For bases approaching context window limits, system uses multiple strategies. **Trimming**: truncates older tool responses (removing middle portions since LLMs weigh beginning and end more heavily), removes older messages when conversations get long. **Filtering base schema**: removes irrelevant IDs, aliases necessary IDs (15-30% token reduction), progressively removes columns from non-active tables and entire tables if needed. **Summarization**: uses MapReduce approach—divides large datasets across parallel LLM calls, each processes subset, then aggregates with summarization prompt creating "summary of summaries."

## Key Insight

**Building a custom agentic framework provided significantly faster iteration than using existing frameworks.** While pre-built agentic frameworks offer quick-start abstractions for tools, chaining, and prompt serialization, Airtable found building their own wasn't difficult and delivered critical advantages: avoiding over-abstraction of components, gaining finer control over prompts, and achieving greater observability of the system.

**Why This Matters:**
- **Custom beats off-the-shelf for production scale**: Existing frameworks helpful for prototypes but custom-built enables production optimization
- **Event-driven architecture enables complexity**: State machine pattern handles sophisticated multi-step workflows with proper error handling
- **Context engineering drives quality**: Smart management of guidelines, session, and event context critical to agent performance
- **Error handling enables self-correction**: Retriable vs non-retriable errors with LLM-visible messages allows agents to fix their own mistakes
- **MapReduce patterns work for LLMs**: Parallelizing work across multiple inference calls then aggregating mirrors distributed computing principles

**Production Learnings:**
- **ID aliasing saves 15-30%**: Shortening alphanumeric identifiers significantly reduces token usage and cost
- **Progressive context reduction**: Maintain most critical context (current table, primary columns) while pruning less relevant data
- **LLMs weight edges over middle**: When truncating, remove middle portions of text to preserve most useful information
- **Conversational interface crucial**: Users can iterate, provide feedback, and ask follow-up questions naturally

## Links

- [How we built AI agents at Airtable](https://medium.com/airtable-eng/how-we-built-ai-agents-at-airtable-70838d73cc43) - Full engineering deep dive by Ameya Khare and Justin Lu
- [Airtable Omni](https://www.airtable.com/platform/ai) - Conversational app builder powered by the framework
- [Field Agents](https://www.airtable.com/platform/ai) - AI-powered fields that autonomously create content
