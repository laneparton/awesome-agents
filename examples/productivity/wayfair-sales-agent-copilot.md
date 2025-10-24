---
title: "Wayfair Sales Agent Co-Pilot"
company: "Wayfair"
author: "Bradley West, Ashequl Qadir"
source: "https://www.aboutwayfair.com/careers/tech-blog/agent-co-pilot-wayfairs-gen-ai-assistant-for-digital-sales-agents"
date: "2024-06"
category: "Productivity & Automation"
tags: ["customer-support", "real-time-assistance", "contextual-recommendations", "production", "conversation-analysis"]
description: "10% reduction in average handle time through AI-powered real-time chat response recommendations for sales agents"
problemPattern: "workflow-automation"
problemComplexity: "moderate"

# Architecture
architecture:
  type: "single-agent"
  pattern: "copilot-assistant"
  rationale: "Copilot works side-by-side with human agents rather than replacing them, analyzing full conversation context to surface contextually relevant response suggestions that agents can accept or modify"
  components: ["prompt-constructor", "primary-llm", "qa-llm", "agent-interface"]

# What Made It Work
breakthroughInsight: "Leveraging full conversation history rather than single-turn interactions - analyzing entire conversation context for relevance rather than rule-based responses distinguishes effective AI copilots from traditional chatbots"

criticalConstraints:
  - "real-time-response-requirements"
  - "production-scale"
  - "accuracy-critical-for-agent-trust"
  - "multi-source-context-integration"

antiPatterns:
  - "rule-based-chatbots: couldn't handle conversational nuance and context"
  - "single-turn-responses: missed critical conversation history"

# Tech Stack
techStack:
  framework: "custom"
  llmProvider: "not-specified"
  knowledgeRetrieval: "product-data-policies-conversation-history"
  otherTools: ["qa-llm-quality-assessment", "levenshtein-distance-tracking"]

# Scale
scale:
  volume: "production deployment for digital sales agents"
  latency: "real-time suggestions during live customer conversations"
---

# Wayfair Sales Agent Co-Pilot

## The Problem

Digital sales agents at Wayfair needed to quickly access product information, policies, and conversation context while handling live customer chats. Manually hunting down information across multiple systems created delays, reduced response quality, and slowed customer service delivery.

**The Manual Process:**
- Agents manually searched for product data across internal systems during conversations
- Reviewed policy documentation while customers waited
- Recalled conversation history without systematic support
- Formulated responses from scratch for each customer inquiry
- Switched between multiple tools and knowledge sources during each interaction

**Key Pain Points:**
- Time-consuming information retrieval interrupted conversation flow
- Inconsistent response quality depending on agent knowledge and memory
- Cognitive load from juggling conversation management with information search
- Slower average handle time (AHT) reduced overall team productivity
- No systematic way to surface contextually relevant information in real-time

## The Solution

Wayfair built Agent Co-Pilot, a generative AI system that works side-by-side with digital sales agents by providing real-time chat response recommendations during customer conversations. The system analyzes full conversation history, product data, and policies to surface contextually relevant suggestions that agents can accept, modify, or reject.

**Impact**:
- **10% reduction in average handle time (AHT)** enabling faster customer service delivery
- **Improved order conversion rates** through higher quality, contextually relevant responses
- **High adoption rates** at both contact-level and response-level (specific metrics tracked)
- **Maintained response quality** with agents retaining full control over final messaging
- Tracked edit distance (Levenshtein Distance) showing minimal modifications needed to AI suggestions

## How It Works

**Key Capabilities:**
- **Full Conversation Context Analysis** - System analyzes entire conversation history rather than single-turn interactions, distinguishing it from rule-based chatbots
- **Multi-Source Prompt Construction** - Assembles prompts from five elements: task description, guidelines, policies, product information, and conversation history
- **Token-by-Token Generation** - Primary LLM generates response suggestions iteratively with contextual awareness
- **Quality Assessment** - Secondary QA LLM evaluates suggestion quality before surfacing to agents
- **Agent-in-the-Loop** - Agents review suggestions and maintain full control, accepting, modifying, or rejecting recommendations

**Process Flow:**
1. Customer sends message in live chat conversation
2. System assembles contextual prompt from task description, guidelines, policies, product data, and full conversation history
3. Primary LLM generates token-by-token response prediction based on assembled context
4. QA LLM assesses quality of generated response suggestion
5. Approved suggestion surfaces to agent interface in real-time
6. Agent reviews suggestion and chooses to accept, modify, or reject
7. Agent sends final response (original suggestion or modified version) to customer
8. System tracks adoption metrics and edit distance for continuous improvement

**Technical Architecture:** Built on a prompt construction system that integrates five critical context sources: task description defining the copilot's role, operational guidelines for response best practices, company policies relevant to the conversation, product information specific to items being discussed, and complete conversation history. The primary LLM performs token-by-token generation, with each token selection informed by cumulative context. A secondary QA LLM validates response quality before surfacing suggestions to agents.

**Evaluation Approach:** Team tracks multiple metrics beyond handle time reduction: order conversion rate to measure business impact, adoption rate at both contact-level (how often agents engage with suggestions) and response-level (how often they use suggestions), and Levenshtein Distance to quantify how much agents modify AI suggestions. This multi-dimensional evaluation ensures the system improves both efficiency and effectiveness.

## Key Insight

**Full conversation context is critical for effective copilot systems** - The breakthrough was analyzing entire conversation history for relevance rather than treating each customer message as an isolated interaction. This contextual analysis distinguishes AI copilots from traditional rule-based chatbots, enabling suggestions that genuinely understand conversation flow and customer intent.

**Why This Matters:**
- Single-turn interaction models miss critical conversational context that informs appropriate responses
- Rule-based systems cannot handle the nuance and complexity of real customer conversations
- Agent trust depends on suggestion quality - poor recommendations lead to low adoption
- Multi-source context integration (policies + products + conversation) provides richer foundation than any single data source
- Quality assessment through QA LLM adds validation layer that improves agent confidence
- Measuring edit distance reveals how much agents trust AI suggestions vs. treating them as rough drafts

**Critical Design Principles:**
- Keep humans in the loop - agents maintain final control over all customer communications
- Analyze full conversation context rather than isolated messages
- Integrate multiple knowledge sources (policies, products, history) into unified prompts
- Track multi-dimensional metrics (speed, conversion, adoption, quality) not just efficiency gains
- Use secondary validation (QA LLM) to ensure suggestion quality before surfacing to agents

## Links

- [Agent Co-Pilot: Wayfair's Gen AI Assistant for Digital Sales Agents](https://www.aboutwayfair.com/careers/tech-blog/agent-co-pilot-wayfairs-gen-ai-assistant-for-digital-sales-agents) - Original engineering blog post
