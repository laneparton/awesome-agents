---
title: "Walmart Ghotok - Ensemble AI for Product Categorization"
company: "Walmart"
author: "Adnan Hassan, Tanay Kumar Saha"
source: "https://medium.com/walmartglobaltech/using-predictive-and-gen-ai-to-improve-product-categorization-at-walmart-dc9821c6a481"
date: "2024-07"
category: "data-analysis"
tags: ["ensemble-models", "classification", "chain-of-thought", "production", "semantic-search", "predictive-ai", "caching"]
description: "Ensemble AI system combining predictive AI filtering with GenAI semantic validation to categorize 400M+ SKUs across complex many-to-many product hierarchies with sub-millisecond latency"

# Problem Classification
problemPattern: "data-classification"
problemComplexity: "complex"

# Architecture
architecture:
  type: "ensemble"
  pattern: "multi-stage-filtering"
  rationale: "Two-stage ensemble leverages predictive AI for cost-efficient broad filtering (millions→thousands of candidates) while using GenAI's semantic comprehension for precise refinement, optimizing for both cost and accuracy at scale"
  components: ["predictive-ai-ensemble", "genai-false-positive-filter", "two-tier-lru-cache", "exception-handler"]

# What Made It Work
breakthroughInsight: "GenAI as validator not generator - using billion-parameter GenAI models to filter false positives from predictive AI (rather than generate mappings) leverages semantic comprehension while avoiding hallucination, and cost-optimizes by only applying expensive GenAI to thousands instead of millions of candidates"

criticalConstraints:
  - "400m-skus-scale"
  - "many-to-many-relationships"
  - "real-time-latency-required"
  - "cost-optimization-essential"
  - "limited-human-labels"
  - "noisy-engagement-data"

antiPatterns:
  - "single-model-approach: Neither pure predictive AI nor pure GenAI alone achieved satisfactory false positive rates - ensemble combining both paradigms proved essential"
  - "engagement-data-reliance: Customer click data is noisy (curiosity clicks, accidental clicks) and doesn't provide reliable ground truth for product categorization"
  - "node-name-only-context: Using just category node names without full root-to-leaf path context significantly degraded relevance assessment quality"
  - "genai-for-all-candidates: Running GenAI inference on millions of candidates is prohibitively expensive - predictive AI pre-filtering essential for cost optimization"

# Tech Stack
techStack:
  framework: "custom-ensemble"
  llmProvider: "GenAI-based"
  knowledgeRetrieval: "semantic-comprehension"
  otherTools: ["predictive-ai-models", "two-tier-lru-cache", "chain-of-thought", "symbol-tuning"]

# Scale
scale:
  volume: "400M+ SKUs, millions of category-product type mappings in production"
  latency: "sub-millisecond cache access, real-time filtering"
---

# Walmart Ghotok - Ensemble AI for Product Categorization

**Company**: Walmart
**Domain**: Data Analysis
**Published**: July 2024

## Problem

With over 400 million SKUs on Walmart.com, the company must streamline the online shopping process to enhance customer satisfaction. Just as physical Walmart stores have organized departments and aisles, the digital platform needs to mirror this experience by properly categorizing products.

The challenge is mapping products to the correct categories and product types across a complex hierarchy. For example, a screwdriver should be classified under "Screwdriver Tool" for electronics use, but under "Oral Care Accessories" for dental instruments. Given the massive scale and many-to-many relationships between categories and product types, items are sometimes mistakenly categorized, leading customers to see less relevant products.

### The Manual Process

The categorization system involves:
1. Fetching items based on their category placement
2. Identifying relevant product types for each category
3. Filtering items based on product type matches

With several thousand categories, each connecting to hundreds of potential product types, this creates millions of potential mappings that need to be validated and maintained.

## Solution

Walmart developed **Ghotok** (named after a Bengali matchmaker), an ensemble AI system that combines predictive and generative AI models to understand the many-to-many relationships between product categories and product types.

### How Ghotok Works

**Three-Stage Ensemble Approach:**

1. **Predictive AI Stage**: Train multiple predictive AI models on domain-specific features using human-labeled data, optimizing for precision, recall, F1, TPR, and FPR metrics

2. **Candidate Reduction**: For each predictive model, learn confidence thresholds by fixing a certain FPR and filter out candidates that don't meet this threshold - reducing millions of candidate pairs to thousands

3. **Generative AI Refinement**: Apply generative AI models with chain-of-thought prompting to the reduced candidate set, using their semantic comprehension to eliminate false positives from predictive AI results

**Key Technical Innovations:**

- **Chain-of-thought reasoning**: Enables the model to trace a logical path from prompt to output, improving adherence to system prompts and output quality

- **Symbol tuning**: Instructing GenAI to give higher importance to leaf nodes during relevance assessment, using full path representation (root-to-node) rather than just context node names

- **Two-tier LRU caching**: L1 and L2 cache system storing Category→Set<ProductType> mappings for sub-millisecond access times to handle millions of entries

- **Exception handling tool**: ML and human intervention system for swift resolution of edge cases in production

### Impact

- **Production deployment** across Walmart.com's 400M+ SKU catalog
- **Reduced false positive rate** to satisfactory levels through ensemble approach
- **Cost optimization**: Avoids expensive GenAI inference on all million+ candidates by using predictive AI for initial filtering
- **Real-time performance**: Two-tier caching enables millisecond-level response times despite processing millions of mappings

## Key Insights

### 1. Ensemble Over Single Model
Rather than choosing either predictive or generative AI, Walmart found that combining multiple models from both paradigms produced the best results. The ensemble approach leverages the speed and efficiency of predictive AI for broad filtering, while using GenAI's semantic understanding for precise refinement.

### 2. GenAI as False Positive Filter
Hallucination in GenAI wasn't a concern because Walmart specifically utilized GenAI's semantic comprehension (from billion-parameter models) to eliminate false positives generated by predictive AI models (million-parameter models). This role reversal - using GenAI to validate rather than generate - proved highly effective.

### 3. Limited Human Labels, No Engagement Data
The system avoids relying on customer engagement data (which is noisy as customers may click items by mistake or curiosity). Instead, it leverages a limited amount of high-quality human-labeled data, making the model effective for both frequently and rarely visited parts of the product hierarchy.

### 4. Full Path Context Matters
Using the entire category path (root-to-node) as a string, rather than just node names, and instructing the model to prioritize leaf nodes significantly improved relevance assessment quality.

## Technical Architecture

```
Product Catalog (400M+ SKUs)
         ↓
[Stage 1: Predictive AI Models]
  - Train on domain features
  - Multiple model ensemble
  - Learn confidence thresholds
         ↓
Millions → Thousands of candidates
         ↓
[Stage 2: Generative AI Filtering]
  - Chain-of-thought prompting
  - Symbol tuning (leaf node focus)
  - Semantic relevance check
         ↓
High-confidence Category↔ProductType mappings
         ↓
[Two-Tier LRU Cache]
  L1 Cache (fast, small)
     ↓
  L2 Cache (larger, slightly slower)
     ↓
  Primary Storage (if cache miss)
         ↓
Millisecond-level filtering in production
```

## References

- **Primary Source**: [Using Predictive and Gen AI to Improve Product Categorization at Walmart](https://medium.com/walmartglobaltech/using-predictive-and-gen-ai-to-improve-product-categorization-at-walmart-dc9821c6a481)
- **Authors**: Adnan Hassan, Tanay Kumar Saha
- **Date**: July 2024

## Tags

`ensemble-models` `classification` `chain-of-thought` `production` `semantic-search` `llm` `predictive-ai` `caching`
