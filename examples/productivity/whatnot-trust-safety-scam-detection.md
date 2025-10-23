---
title: "Whatnot Trust & Safety - GenAI Scam Detection"
company: "Whatnot"
author: "Charudatta (CD) Wad, Commerce Engineering Team"
source: "https://medium.com/whatnot-engineering/how-whatnot-utilizes-generative-ai-to-enhance-trust-and-safety-c7968eb6315e"
date: "2023-09"
category: "productivity"
tags: ["security", "production", "structured-output", "workflow-automation", "enterprise"]
description: "95% of scam attempts detected proactively within minutes with 96% precision using LLM-powered conversational analysis"
---

# Whatnot Trust & Safety - GenAI Scam Detection

## The Problem

As Whatnot grew into one of the fastest-growing livestream shopping marketplaces, scammers increasingly targeted users with sophisticated multi-message fraud patterns. Traditional rule engines operating on scalar values couldn't understand ambiguous scenarios or contextual comprehension needed to detect these evolving scam tactics.

**The Manual Process:**
- Security teams manually reviewed user reports of suspected scams
- Individual messages analyzed in isolation without conversation context
- Traditional ML models assessed single messages before publishing
- New scam patterns required manual rule updates and heuristics
- Difficult to catch scams that built trust through innocuous opening messages

**Key Pain Points:**
- Single-message analysis had low precision for scam detection
- Scammers adapted messaging to circumvent static rules
- New users particularly vulnerable to sophisticated social engineering
- Time-consuming manual investigation of reported incidents
- Reactive rather than proactive fraud prevention

## The Solution

Whatnot built an LLM-powered scam detection system that analyzes entire conversation contexts combined with user behavioral signals to proactively identify fraud attempts before users are harmed.

**Impact**: 95% of scam attempts detected proactively within minutes, achieving 96% precision with high recall. System expanded to enforce policies for off-platform transactions and harassment.

## How It Works

**Key Capabilities:**
- **Conversational Context Analysis** - LLM analyzes full message history rather than isolated messages
- **Multi-Signal Qualification** - Combines messaging patterns, account age, message frequency to flag suspicious accounts
- **Structured LLM Outputs** - Returns JSON with scam likelihood (0-1) and detailed explanation
- **Human-in-the-Loop Enforcement** - AI provides cognitive insights while humans make final decisions
- **Adaptive Pattern Recognition** - LLMs excel at adapting to new messaging patterns without manual rule updates

**Process Flow:**
1. User signals (messaging patterns, account age, frequency) qualify which conversations to analyze
2. Flagged accounts trigger LLM analysis of full conversation history
3. LLM receives known scam patterns and conversation context as input
4. LLM outputs likelihood score (0-1) and reasoning in JSON format
5. Rule engine combines LLM output with additional signals (e.g., `scam_likelihood > 0.6 AND account_age < X days`)
6. System takes temporary protective actions and notifies ops team with LLM explanation
7. OCR processes text in image attachments to catch obfuscation attempts

**Technical Architecture:** Three-phase system architecture: **Gather** (curate data from events, user data, order history, ML models), **Evaluate** (LLM insights combined with rule engine for recommended actions), **Enforce** (close/act/escalate decisions with human review for uncertain cases)

## Key Insight

**Analyzing entire conversation context rather than individual messages dramatically improves scam detection accuracy and adaptability.** LLMs proved surprisingly effective at adapting to constantly evolving scam messaging patterns without requiring manual rule updates, while providing transparent explanations that aid human investigators.

**Why This Matters:**
- Traditional ML and rule-based systems struggle with contextual understanding across multi-turn conversations
- Scammers continuously evolve tactics to evade static detection rules
- Providing reasoning alongside predictions enables effective human-AI collaboration
- Zero-shot and few-shot learning eliminates need for extensive training data per scam variant

**Human-AI Partnership Approach:** The system uses LLMs as "cognitive partners" rather than autonomous decision makers. This human-in-the-loop design ensures thoughtful collaboration where AI enhances evaluations and safety protocols while humans retain final enforcement authority, building trust in the system.

## Links

- [Original Article](https://medium.com/whatnot-engineering/how-whatnot-utilizes-generative-ai-to-enhance-trust-and-safety-c7968eb6315e) - Detailed technical breakdown of the scam detection system architecture
