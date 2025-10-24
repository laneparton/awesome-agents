---
title: "Grab LLM-Powered Data Classification"
company: "Grab"
author: "Hualin Liu, Stefan Jaro, and Grab Data Engineering Team"
source: "https://engineering.grab.com/llm-powered-data-classification"
date: "2024-07"
category: "development"
tags: ["workflow-automation", "production", "enterprise", "structured-output", "platform-engineering", "data-governance"]
description: "20K+ data entities scanned in first month with 360 man-days saved annually using GPT-3.5 powered column-level data tagging for governance at petabyte scale"

# Problem Classification
problemPattern: "data-classification"
problemComplexity: "complex"

# Architecture
architecture:
  type: "single-agent"
  pattern: "orchestration-service"
  rationale: "Column-level classification vs schema-level prevents over-classification (half of schemas marked Tier 1 due to single sensitive table); Gemini orchestration service with message queue batching, rate limiting (240K tokens/minute), and context chunking (4K token limits) enables petabyte-scale automation; JSON structured output with DTOs ensures consistent downstream integration"
  components: ["gemini-orchestration-service", "message-queue-batching", "gpt35-classifier", "rate-limiter", "context-chunker", "kafka-integration", "weekly-review-loop"]

# What Made It Work
breakthroughInsight: "Column-level vs schema-level classification eliminates over-restriction - half of schemas were marked Tier 1 because single sensitive table justified maximum classification, unnecessarily locking down non-sensitive data; automated LLM tagging enables granular governance at petabyte scale where manual classification infeasible (2 minutes per entity × 20K+ entities); structured JSON output with explicit 'None' tags for ambiguous cases + few-shot learning ensures reliable predictions; 80% user satisfaction with <1 tag changed on average validates LLM aligns with data owner expectations"

criticalConstraints:
  - "petabyte-scale-data"
  - "20k-plus-entities"
  - "manual-classification-infeasible"
  - "schema-level-over-classification"
  - "inconsistent-policy-interpretation"
  - "4k-token-context-limits"
  - "240k-tokens-per-minute-quota"
  - "cost-efficiency-required"

antiPatterns:
  - "schema-level-classification: Half of schemas marked Tier 1 due to single sensitive table, unnecessarily restricting non-sensitive data - column-level granularity essential for petabyte-scale governance"
  - "manual-column-level-at-scale: 2 minutes per entity × 20K+ entities = 360 man-days annually - infeasible without automation at petabyte scale"
  - "unstructured-llm-output: Free-form responses create downstream integration issues - JSON structured output with DTOs ensures consistent format for governance systems"
  - "no-review-feedback-loop: LLM predictions improve through iteration - weekly user review with corrections feeds back to improve future accuracy"

# Tech Stack
techStack:
  framework: "custom-orchestration"
  llmProvider: "GPT-3.5-Azure-OpenAI"
  knowledgeRetrieval: "schema-context"
  otherTools: ["message-queue", "Kafka", "JSON-DTOs", "few-shot-learning", "rate-limiting", "context-chunking"]

# Scale
scale:
  volume: "20,000+ data entities scanned first month, 300-400 daily throughput, petabyte-scale data infrastructure"
  latency: "2 minutes manual → seconds automated per entity, 360 man-days saved annually, 80% user satisfaction, <1 tag changed on average, extremely affordable cost"
---

# Grab LLM-Powered Data Classification

## The Problem

Grab faced a data governance challenge at petabyte scale. Initial schema-level classification using four sensitivity tiers created a bottleneck where half of all schemas were marked as "Tier 1" (most restrictive) because a single sensitive table justified maximum classification, unnecessarily locking down non-sensitive data.

**The Manual Process:**
- Manual classification at schema level with four sensitivity tiers
- Each schema classified based on most sensitive table within it
- Developers manually interpret data policies to classify new tables/columns
- Volume of data entities made manual table-level and column-level classification infeasible
- Estimated 2 minutes per manual classification across thousands of entities
- Governance team reviewing and correcting classification errors

**Key Pain Points:**
- Over-classification: Half of schemas marked Tier 1 due to single sensitive table
- Non-sensitive data locked down unnecessarily by schema-level classification
- Petabyte scale made manual column-level classification impossible
- Inconsistent policy interpretation by developers led to classification errors
- No scalable way to tag columns with appropriate sensitivity labels
- Data access bottlenecks from overly conservative classification

## The Solution

Grab built "Gemini," an orchestration service using GPT-3.5 to automate column-level data tagging at scale. The system analyzes database table and column names with schema information to assign appropriate sensitivity tags, reducing manual effort from 2 minutes to seconds per entity.

**Impact**: Scanned over 20,000 data entities within the first month (300-400 daily), saving an estimated 360 man-days annually. 80% of surveyed data owners reported the system helped their tagging efforts, with users changing less than one tag on average during weekly reviews. Cost described as "extremely affordable" for current load.

## How It Works

**Key Capabilities:**
- **Column-Level Tagging** - Analyzes each column and assigns specific sensitivity tags (e.g., `<Personal.ID>`, `<Personal.Name>`, `<Personal.Contact_Info>`)
- **JSON Structured Output** - Returns predictions in JSON format with explicit "None" tags for ambiguous cases
- **Few-Shot Learning** - Uses example-based prompting to guide classification decisions
- **Schema Enforcement** - DTOs ensure consistent output structure for downstream systems
- **Weekly User Review** - Data owners verify predictions to iteratively improve accuracy
- **Kafka Integration** - Sends tag predictions to downstream governance systems

**Process Flow:**
1. Database table and column names with schema information sent to Gemini orchestration service
2. Message queue aggregates requests into mini-batches at fixed intervals
3. GPT-3.5 analyzes each column against data sensitivity policies
4. LLM assigns appropriate tags based on column name, type, and schema context
5. JSON-formatted predictions sent to Kafka for downstream governance systems
6. Users review predictions weekly and make corrections
7. Corrections feed back into system to improve future accuracy

**Technical Architecture:** Gemini orchestration service handles message queue aggregation, rate limiting (respects 240K tokens/minute Azure OpenAI quota), and dual classification engines. Context management handles 4,000-token limits by breaking large requests into chunks. Third-party service runs concurrently with GPT-3.5 during evaluation phase.

**Development Journey:** Originally developed October 2023 in partnership with Singapore's Infocomm Media Development Authority, concluded partnership March 2024 and published learnings July 2024. Estimated 2 minutes per manual classification replaced by automated seconds-long processing.

## Key Insight

**Automating data governance classification with LLMs enables granular column-level tagging at petabyte scale, eliminating over-classification and unlocking access to non-sensitive data.** By moving from schema-level to column-level classification, Grab reduced unnecessary data restrictions while maintaining security and compliance requirements.

**Why This Matters:**
- Schema-level classification creates access bottlenecks by over-restricting non-sensitive data
- Manual column-level classification infeasible at petabyte scale (20K+ entities)
- Inconsistent human interpretation of data policies leads to classification errors
- Automated tagging enables granular governance without manual bottlenecks
- 80% user satisfaction shows LLM classifications align with data owner expectations

**Scale Achievement:**
- Scanned 20,000+ data entities in first month (300-400 daily throughput)
- Estimated 360 man-days saved annually (2 minutes per entity × volume)
- Users change "less than one tag on average" during weekly review
- Cost extremely affordable for current load on Azure OpenAI

## Links

- [Original Article](https://engineering.grab.com/llm-powered-data-classification) - Detailed technical implementation of LLM-powered automated data classification at Grab's petabyte scale
