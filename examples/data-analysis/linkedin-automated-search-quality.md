---
title: "LinkedIn Automated GenAI-Driven Search Quality Evaluation"
company: "LinkedIn"
author: "Xueying Lu, Ali Hooshmand, Fan Dong, Raghavan Muthuregunathan"
source: "https://www.linkedin.com/blog/engineering/ai/automated-genai-driven-search-quality-evaluation"
date: "2024-12"
category: "data-analysis"
tags: ["workflow-automation", "production", "enterprise", "structured-output"]
description: "20% reduction in low-quality typeahead suggestions with automated evaluation reducing assessment time from days/weeks to hours using GPT-powered quality scoring"
---

# LinkedIn Automated GenAI-Driven Search Quality Evaluation

## The Problem

LinkedIn historically relied on human evaluators to assess typeahead suggestion quality across 1 billion+ members. As the platform scaled, manual evaluation became a critical bottleneck preventing rapid iteration on search features and quality improvements.

**The Manual Process:**
- Human evaluators manually reviewed typeahead suggestions for quality
- Evaluation cycles took days or even weeks to complete
- Assessment needed to cover diverse suggestion types (People, Company, Jobs, plain text)
- Quality evaluation couldn't keep pace with platform growth
- Slow feedback loops prevented rapid experimentation with search improvements

**Key Pain Points:**
- Manual evaluation unsustainable at scale with 1B+ members
- Days/weeks turnaround time blocked rapid iteration on search features
- Typeahead quality directly impacted member experience but couldn't be assessed quickly
- Need to evaluate suggestions at multiple positions (top-1, top-3, top-5, top-10)
- Traditional approaches couldn't handle velocity required for modern search development

## The Solution

LinkedIn built the GenAI Typeahead Quality Evaluator using OpenAI's GPT-3.5 Turbo served through Azure to automate search quality assessment at scale. The system generates quality scores across diverse suggestion types with clear binary evaluation (high/low quality).

**Impact**: 20% reduction in low-quality suggestions (from 66.70% to 73.50% quality at top-10) with evaluation speed improved from days/weeks to just a few hours. Representative experiment showed +6.8% absolute improvement in TyahQuality@10 and +4% absolute improvement at top-1.

## How It Works

**Key Capabilities:**
- **Binary Quality Classification** - Clear high/low quality guidelines for People, Company, Jobs, and plain text suggestions
- **Specialized Prompt Templates** - Structured prompts with Identity, Task Guidelines, Examples, Input, and Output sections
- **Chain-of-Thought Reasoning** - Improves evaluation accuracy through step-by-step reasoning
- **Position-Aware Evaluation** - Measures quality at top-1, top-3, top-5, and top-10 positions recognizing ranked surface constraints
- **Golden Test Set** - Samples 200 queries per intent category plus bypass/abandoned sessions

**Process Flow:**
1. Request generation creates {query, member ID} pairs across intent categories
2. Typeahead backend called to generate suggestions for each test query
3. Prompt generation builds specialized evaluation prompts based on suggestion type
4. Batch GPT API calls process evaluations at scale
5. Quality scores calculated at multiple positions (top-1, top-3, top-5, top-10)
6. Results aggregated to measure overall typeahead quality

**Technical Architecture:** Pipeline executes request generation → typeahead backend calls → prompt generation → batch GPT API calls → quality score calculation. GPT-3.5 Turbo served through Azure provides fast, cost-effective evaluation at LinkedIn's scale.

## Key Insight

**Automating quality evaluation with LLMs enables continuous, rapid iteration on search improvements that would be impossible with manual review.** By reducing evaluation time from days/weeks to hours, LinkedIn can experiment with search enhancements and measure impact quickly, dramatically accelerating search quality improvements.

**Why This Matters:**
- Manual evaluation at scale is fundamentally unsustainable for platforms serving billions
- Slow feedback loops prevent experimentation and innovation in search quality
- GPT-powered evaluation provides consistent, fast assessment enabling continuous improvement
- Representative experiment validated approach: 20% reduction in low-quality suggestions with +6.8% absolute quality improvement
- Pattern applicable to any quality evaluation bottleneck blocking rapid iteration

**Validation Results:**
A representative experiment expanding plain text suggestions demonstrated measurable improvements:
- TyahQuality@10: 66.70% → 73.50% (+6.8% absolute, 20% reduction in low-quality)
- TyahQuality@1: 73.20% → 77.20% (+4% absolute improvement)

## Links

- [Original Article](https://www.linkedin.com/blog/engineering/ai/automated-genai-driven-search-quality-evaluation) - Detailed technical implementation of GenAI-driven automated search quality evaluation at LinkedIn scale
