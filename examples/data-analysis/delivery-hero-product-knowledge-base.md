---
title: "Delivery Hero Agentic Product Knowledge Base"
company: "Delivery Hero Quick Commerce"
author: "Mundher Al-Shabi, Data Scientist at QC"
source: "https://deliveryhero.jobs/blog/how-delivery-hero-uses-agentic-ai-for-building-a-product-knowledge-base/"
date: "2025-08"
category: "data-analysis"
tags: ["structured-data-extraction", "predefined-agents", "multimodal", "production"]
description: "Automates extraction of 22 product attributes and title standardization using predefined agentic AI with knowledge distillation"
---

# Delivery Hero Agentic Product Knowledge Base

## The Problem

Delivery Hero Quick Commerce (QC) operates in a fast-paced environment managing vast and ever-growing product catalogs across numerous platforms and geographical regions. Ensuring accurate, consistent, and detailed product information is paramount for everything from warehouse operations to customer discovery, but historically this required manual processes that simply don't scale.

**The Manual Process:**
- Manual verification of product details like brand, flavor, volume, and specific features
- Processing vendor-provided information (titles and images) by hand
- Checking and standardizing product titles across different vendor formats
- Ensuring consistency across large catalogs manually
- Time-consuming review and data entry for each product

**Key Pain Points:**
- Manual processes don't scale for large, growing catalogs across multiple regions
- Time-consuming and costly to verify product details manually
- Prone to human error leading to data inconsistencies
- Impacts inventory management accuracy
- Degrades search relevance when attributes are missing or wrong
- Reduces customer satisfaction due to inaccurate product information
- Vendors use varying title structures creating inconsistencies

## The Solution

Delivery Hero QC built a predefined agentic AI system that automates product attribute extraction and title standardization using multimodal LLMs. The system orchestrates two specialized agents in sequence: first extracting 22 predefined attributes from vendor titles and images, then generating standardized titles following Delivery Hero's format—unlocking enhanced search, smarter recommendations, and deeper analytics.

**Impact**:
- **Improved efficiency**: Reduced manual effort and accelerated catalog enrichment
- **Higher accuracy**: Ensured consistent and correct product information
- **Better data quality**: Structured attributes enable precise filtering, recommendations, and analytics
- **Enhanced customer satisfaction**: More reliable and navigable product discovery experience
- **Cost and latency reduction**: Knowledge distillation via Teacher/Student fine-tuning significantly lowered operational costs

## How It Works

**Key Capabilities:**
- **Multimodal Attribute Extraction** - First agent processes both text (vendor titles) and images to extract 22 predefined attributes (Brand, Flavor, Volume, etc.)
- **Title Standardization** - Second agent generates titles following Delivery Hero QC's standardized format using extracted attributes
- **Knowledge Distillation** - Teacher model (GPT-4o) trains smaller student model (GPT-4o-mini) for efficient production deployment
- **Confidence Scoring** - Processes output logits to quantify model confidence, flagging low-confidence predictions for human review
- **Human-in-the-Loop** - Automatically routes uncertain predictions below confidence threshold to manual verification

**Process Flow:**
1. Vendor provides product title and image in various formats
2. First LLM agent (Attribute Extraction) receives title and image as input
3. Multimodal model interprets both text and visual information
4. Agent extracts comprehensive set of 22 predefined attribute types
5. Second LLM agent (Title Generation) receives extracted attributes
6. Agent generates new product title following standardized Delivery Hero QC format
7. Confidence scoring processes output logits from both agents
8. System calculates probability scores quantifying model confidence
9. Outputs below predefined threshold flagged for human review
10. Approved outputs enrich product knowledge base with structured attributes

**Technical Architecture:** Predefined agents approach with two-step sequential orchestration. Built on multimodal LLMs capable of understanding both text and images. **Prompt Engineering**: Meticulously crafted concise, unambiguous prompts reducing token usage, lowering costs/latency, and minimizing misunderstandings. **Knowledge Distillation**: Teacher/Student paradigm where powerful GPT-4o generates high-quality training dataset with detailed prompts and examples, then fine-tunes smaller GPT-4o-mini to replicate teacher quality with shorter, efficient prompts. **Quality Control**: Confidence scoring via output logit processing establishes human-in-the-loop system for edge cases and uncertain predictions.

**Architectural Decision:** Chose predefined agents over dynamically orchestrated agents prioritizing efficiency, cost-effectiveness, predictability, and debuggability. Predefined approach offers lower and consistent latency, lower fixed costs, high predictability, and easier debugging—critical for core cataloging process running at scale. Acknowledged future potential of dynamically orchestrated agents for scenarios demanding maximum accuracy where higher latency/cost justified.

## Key Insight

**Knowledge distillation dramatically reduces operational costs while maintaining quality.** Initially, guiding the title generation LLM required numerous examples within prompts, leading to lengthy prompts that increased processing time and costs. By using a powerful teacher model to create a high-quality training dataset, then fine-tuning a smaller student model, Delivery Hero achieved the same output quality with much shorter prompts—significantly lowering operational costs and latency.

**Why This Matters:**
- **Predefined agents fit structured workflows**: Two-step task (extract, then generate) naturally maps to sequential agent orchestration
- **Trade-offs drive architecture**: Chose predictability and efficiency over flexibility since core cataloging demands consistent, reliable processing
- **Prompt engineering compounds savings**: Concise prompts reduce tokens, lower costs, decrease latency, AND improve accuracy
- **Knowledge distillation scales LLMs**: Transfer larger model capabilities to efficient smaller models for production deployment
- **Structured data unlocks value**: Extracted attributes power search filtering, recommendations, analytics, and business insights beyond simple cataloging

**Value of Structured Attributes:**
- **Enhanced Search**: Users can precisely filter (e.g., "Show me all vanilla-flavored ice creams from Ben & Jerry's")
- **Smarter Recommendations**: Suggest relevant items based on shared attributes with previously viewed/purchased products
- **Deeper Analytics**: Reveals trends in popular brands, flavors, sizes; informs merchandising strategies and data-driven decisions

## Links

- [How Delivery Hero Uses Agentic AI for Building a Product Knowledge Base](https://deliveryhero.jobs/blog/how-delivery-hero-uses-agentic-ai-for-building-a-product-knowledge-base/) - Full technical article by Mundher Al-Shabi
- [Delivery Hero Quick Commerce](https://www.deliveryhero.com/) - Company website
