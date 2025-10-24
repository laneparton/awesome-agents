---
title: "Meta AI for Efficient Incident Response"
company: "Meta"
author: "Diana Hsu, Michael Neu, Mohamed Farrag, Rahul Kindi"
source: "https://engineering.fb.com/2024/06/24/data-infrastructure/leveraging-ai-for-efficient-incident-response/"
date: "2024-06-24"
category: "development"
tags: ["incident-response", "root-cause-analysis", "fine-tuning", "llama", "heuristic-retrieval", "production", "system-reliability"]
description: "Two-stage incident response system achieving 42% accuracy identifying root cause in top 5 suggestions through heuristic filtering (thousands→hundreds changes) + fine-tuned Llama 2 (7B) election-based ranking (hundreds→5)"

# Problem Classification
problemPattern: "root-cause-analysis"
problemComplexity: "complex"

# Architecture
architecture:
  type: "pipeline"
  pattern: "two-stage-retrieval-ranking"
  rationale: "Heuristic retrieval (code ownership, runtime graphs) maintains high recall while reducing thousands→hundreds changes; fine-tuned Llama 2 (7B) with election-based ranking handles context limits by processing max 20 changes per batch, aggregating across requests until 5 candidates remain; two-stage approach balances recall and precision"
  components: ["heuristic-retriever", "llama2-7b-ranker", "election-aggregator", "logprob-ranker", "confidence-measurement"]

# What Made It Work
breakthroughInsight: "Fine-tuning on ~5,000 historical investigations with sparse information (matching what's known at investigation start) was biggest performance lever, not pre-trained models; election-based ranking processes 20 changes at a time and aggregates results to handle context limits while reasoning across large candidate sets; using logprobs to rank relevancy and training model to produce ranked lists dramatically improved output"

criticalConstraints:
  - "monolithic-repository-scale"
  - "thousands-of-code-changes"
  - "unique-investigations"
  - "context-building-overhead"
  - "cross-team-dependencies"
  - "time-sensitive-mitigation"
  - "context-window-limits"

antiPatterns:
  - "pre-trained-only-models: Biggest performance lever was fine-tuning on ~5,000 historical Meta investigations - pre-trained models lack domain-specific context for Meta infrastructure and terminology"
  - "dense-training-information: Training on comprehensive information degrades real-world performance - intentionally sparse training data (matching investigation start conditions) makes model perform better in practice"
  - "full-context-ranking: Processing all candidates in one prompt exceeds context limits and degrades reasoning - election-based approach with max 20 changes per batch and aggregation enables effective ranking"
  - "direct-llm-without-retrieval: Processing thousands of changes directly wastes tokens and degrades accuracy - heuristic filtering (ownership, code graphs) maintains recall while reducing search space"

# Tech Stack
techStack:
  framework: "custom-pipeline"
  llmProvider: "Llama-2-7B-fine-tuned"
  knowledgeRetrieval: "heuristic-retrieval"
  otherTools: ["CPT", "SFT", "logprobs-ranking", "election-aggregation", "code-ownership-analysis", "runtime-code-graphs"]

# Scale
scale:
  volume: "Production deployment at Meta scale for web monorepo investigations"
  latency: "42% accuracy root cause in top 5 suggestions, significant time savings in investigation process"
---

# Meta AI for Efficient Incident Response

**Source**: [Meta Engineering Blog - Leveraging AI for efficient incident response](https://engineering.fb.com/2024/06/24/data-infrastructure/leveraging-ai-for-efficient-incident-response/)
**Authors**: Diana Hsu, Michael Neu, Mohamed Farrag, Rahul Kindi
**Date**: June 24, 2024
**Category**: Development & Engineering

## Problem

Investigation is a critical part of ensuring system reliability at Meta and a prerequisite to mitigating issues quickly. However, investigating anomalies presents significant challenges:

**Investigation Challenges:**
- **Every investigation is unique**: Identifying the root cause is necessary to mitigate properly
- **Monolithic repository scalability**: Accumulating number of changes across many teams makes investigations complex
- **Context building overhead**: Responders need to build context on what is broken, which systems are involved, and who might be impacted
- **Large search space**: Thousands of potential code changes to review
- **Time-consuming process**: Complex and lengthy investigations delay mitigation

The challenge was particularly acute for systems dependent on monolithic repositories where the volume of changes and cross-team dependencies create a massive search space for root cause identification.

## Solution

Meta developed an **AI-assisted root cause analysis system** that streamlines investigations through a combination of heuristic-based retrieval and large language model (LLM)-based ranking to speed up root cause identification.

### Two-Stage Approach

#### Stage 1: Heuristics-Based Retriever

Reduces the search space from **thousands of changes to a few hundred** without significant reduction in accuracy using:
- Code and directory ownership analysis
- Runtime code graph exploration of impacted systems
- Other novel heuristics specific to Meta's infrastructure

**Purpose**: Intelligent filtering to maintain high recall while dramatically reducing the search space.

#### Stage 2: LLM-Based Ranker

Once the search space is reduced to a few hundred changes, the system uses a **fine-tuned Llama 2 (7B) model** to further reduce to the **top 5 most likely root causes**.

**Ranking Through Election:**
- Structures prompts to contain maximum of 20 changes at a time
- Asks LLM to identify top 5 changes from each batch
- Aggregates outputs across LLM requests
- Repeats process until only 5 candidates remain

**Key Innovation**: This election-based approach accommodates context window limitations while enabling the model to reason across different changes effectively.

### Training Process

The biggest lever to achieving high accuracy was **fine-tuning a Llama 2 (7B) model** using historical investigations with known root causes.

#### Continued Pre-Training (CPT)
- Used limited and approved internal wikis, Q&As, and code
- Exposed model to Meta-specific artifacts and terminology
- Built foundation for understanding Meta's infrastructure

#### Supervised Fine-Tuning (SFT)
- Mixed Llama 2's original SFT data with internal context
- Created dedicated investigation root cause analysis (RCA) SFT dataset
- Taught model to follow RCA instructions

**RCA SFT Dataset:**
- ~5,000 instruction-tuning examples
- Details of 2-20 changes from retriever
- Known root cause included
- Information available at investigation start (title, observed impact)
- Intentionally limited information density to match real-world scenarios

**Advanced Fine-Tuning for Ranked Lists:**
- Gathered model's log probabilities (logprobs) for each possible culprit
- Ranked search space based on relevancy to given investigation
- Created fine-tuning examples where model yields ranked list of potential code changes
- Expected root cause appears first in ranked output
- Re-ran SFT with this augmented dataset to enable proper ranking behavior

## Impact

### Accuracy Metrics
- **42% accuracy** in identifying root causes for investigations at their creation time (related to web monorepo)
- Root cause appears in **top 5 suggested code changes** for 42% of backtested investigations
- Based on exhaustive backtesting with historical investigations and information available at their start

### Time Savings
- Significantly reduced effort and time needed to root cause an investigation
- Streamlined onboarding of engineers to investigations
- Accelerated root cause isolation process

### Operational Impact
- Production deployment at Meta scale
- Integrated into internal investigation tools
- Used alongside existing tools like Hawkeye (end-to-end ML workflow debugging)

## Key Insights

1. **Two-Stage Retrieval Works**: Combining heuristic-based filtering (thousands → hundreds) with LLM-based ranking (hundreds → top 5) provides optimal balance of recall and precision.

2. **Election-Based Ranking Handles Context Limits**: Processing 20 changes at a time and aggregating results enables reasoning across large candidate sets despite context window limitations.

3. **Fine-Tuning is Critical**: The biggest performance lever was fine-tuning on ~5,000 historical investigations with known root causes, not just using pre-trained models.

4. **Limited Information Training Matches Reality**: Training on intentionally sparse information (what's known at investigation start) makes the model perform better in real-world scenarios.

5. **Log Probabilities Enable Ranking**: Using logprobs to rank relevancy and training the model to produce ranked lists significantly improved output quality.

6. **Closed Feedback Loops for Trust**: Ensuring responders can independently reproduce results validates AI suggestions and prevents misleading recommendations.

7. **Precision Over Reach**: Using confidence measurement methodologies to detect low confidence answers—sacrificing reach in favor of precision—maintains trust.

8. **Domain-Specific Training Matters**: Continued pre-training on internal wikis, Q&As, and code exposed the model to Meta-specific context, improving performance on Meta infrastructure.

## Risk Mitigation

The team identified key risks and implemented mitigations:

**Risk: Wrong Root Cause Suggestions**
- **Mitigation**: Prioritize closed feedback loops and explainability
- Ensure responders can independently reproduce results
- Validate AI-generated results before acting

**Risk: Low Confidence Answers**
- **Mitigation**: Confidence measurement methodologies
- Avoid recommending low-confidence results
- Sacrifice reach in favor of precision

**Risk: Over-Reliance on AI**
- **Mitigation**: AI assists but doesn't replace human judgment
- Responders maintain control of investigation process
- AI suggestions are starting points, not final answers

## What's Next

### Autonomous Workflows
- Expanding AI capabilities to autonomously execute full workflows
- AI systems validate their own results
- Reduced need for human intervention in routine investigations

### Proactive Incident Detection
- Detect potential incidents prior to code push
- Proactively mitigate risks before they arise
- Shift from reactive investigation to preventive detection

### Broader Integration
- Expand beyond web monorepo to other systems
- Integrate deeper into existing investigation tooling
- Scale AI-assisted investigation across Meta's infrastructure

## Technical Stack

- **LLM**: Fine-tuned Llama 2 (7B) model
- **Training Data**: ~5,000 instruction-tuning examples from historical investigations
- **Training Process**: Continued pre-training (CPT) + supervised fine-tuning (SFT)
- **Ranking Algorithm**: Election-based ranking with max 20 changes per prompt
- **Retrieval**: Novel heuristics-based retrieval (code ownership, runtime code graph analysis)
- **Integration**: Internal investigation tooling, Hawkeye debugging system

## Training Dataset Composition

**RCA SFT Dataset Structure:**
- Investigation title and observed impact
- 2-20 code changes from retriever
- Known root cause (for training)
- Change metadata (author, timestamp, affected files, etc.)
- Ranked list format with logprobs

**Fine-Tuning Data Sources:**
- Llama 2's original SFT data (base instruction-following)
- Internal context (wikis, Q&As, code)
- Historical RCA investigations (~5,000 examples)
- Ranked list examples (augmented dataset)

---

**Tags**: AI-Assisted Investigation, Root Cause Analysis, LLM, Llama, Fine-Tuning, Incident Response, System Reliability, Heuristic Retrieval, Production System, Meta Infrastructure

**Related Examples**:
- Other AI-assisted development and debugging tools
- LLM-based code analysis systems
- Incident response automation platforms
