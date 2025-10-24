---
title: "DoorDash LLM-Based Dasher Support Automation"
company: "DoorDash"
author: "Zhe Jia, Shuai Wang, Aditi Bamba, Martin Wang"
source: "https://careers.doordash.com/blog/large-language-modules-based-dasher-support-automation/"
date: "2024-09-17"
category: "productivity"
tags: ["rag", "chatbot", "customer-support", "guardrails", "quality-monitoring", "gpt4", "claude3", "prompt-engineering", "chain-of-thought", "production", "multi-language"]
description: "RAG chatbot with three-layer quality control (two-tier guardrails, LLM Judge, improvement pipeline) achieving 90% hallucination reduction and 99% compliance issue reduction while assisting thousands of Dashers daily"

# Problem Classification
problemPattern: "customer-support"
problemComplexity: "complex"

# Architecture
architecture:
  type: "single-agent"
  pattern: "rag-with-quality-controls"
  rationale: "RAG enables KB-grounded multilingual responses; three critical quality control systems essential for production: 1) two-tier guardrails (semantic similarity + LLM evaluator) prevent hallucinations before user sees them, 2) LLM Judge across 5 dimensions monitors quality and surfaces improvement areas, 3) human-AI collaboration pipeline with Promptfoo regression testing ensures continuous improvement without degradation"
  components: ["conversation-summarizer", "historical-case-retrieval", "kb-article-integration", "two-tier-guardrails", "llm-judge-5-dimensions", "quality-improvement-pipeline", "promptfoo-regression-testing"]

# What Made It Work
breakthroughInsight: "Guardrails non-negotiable for production LLMs - two-tier system (semantic similarity shallow check + LLM evaluator deep check) reduced hallucinations 90% and compliance issues 99%; LLM Judge across 5 dimensions (retrieval, accuracy, grammar, coherence, relevance) drives actionable improvements; human-AI collaboration with SME reviews transforms prototypes into robust solutions; regression prevention via Promptfoo prevents quality degradation as prompts evolve"

criticalConstraints:
  - "flow-based-system-limited-coverage"
  - "kb-access-difficult"
  - "english-only-content"
  - "human-agent-bottleneck"
  - "hallucination-risk"
  - "compliance-requirements"
  - "multilingual-support-needed"
  - "latency-vs-quality-tradeoff"

antiPatterns:
  - "llm-without-guardrails: Initial prototype had hallucinations and compliance issues - two-tier guardrail system (semantic similarity + LLM evaluator) essential for production, reducing hallucinations 90% and compliance issues 99%"
  - "no-regression-testing: As prompts and models evolve, quality can degrade - automated testing via Promptfoo like unit testing prevents regressions by blocking failing prompt changes"
  - "negative-prompting: Negative language in prompts degrades performance - clearly outline desired actions with illustrative examples instead"
  - "dense-complex-prompts: Large monolithic prompts harder to debug - breaking down into smaller parts with parallel processing improves manageability and performance"
  - "outdated-kb-content: LLM drew from outdated public data (Quora, Reddit, Twitter) - KB serves as foundational truth and must be complete, accurate, regularly updated"

# Tech Stack
techStack:
  framework: "custom-rag"
  llmProvider: "GPT-4, Claude-3"
  knowledgeRetrieval: "rag-with-historical-cases"
  otherTools: ["semantic-similarity", "LLM-Judge", "Promptfoo", "vector-store", "chain-of-thought", "sliding-window-similarity"]

# Scale
scale:
  volume: "Thousands of Dashers assisted autonomously each day in production"
  latency: "90% hallucination reduction, 99% compliance issue reduction, sub-second to tens of seconds response time with two-tier guardrails"
---

# DoorDash LLM-Based Dasher Support Automation

**Source**: [DoorDash Careers Blog - Path to high-quality LLM-based Dasher support automation](https://careers.doordash.com/blog/large-language-modules-based-dasher-support-automation/)
**Authors**: Zhe Jia, Shuai Wang, Aditi Bamba, Martin Wang
**Date**: September 17, 2024
**Category**: Productivity & Automation

## Problem

Dashers (independent contractors who do deliveries through DoorDash) sometimes need support to resolve issues they encounter during the delivery process. The existing automated support system had significant limitations:

**Support System Challenges:**
- **Flow-based limitations**: Existing automated system provides flow-based resolutions, relying heavily on pre-built resolution paths
- **Limited coverage**: Only a small subset of Dasher issues can be resolved quickly
- **Knowledge base access problems**:
  - Difficult to find the relevant article
  - Time-consuming to find useful information within any particular article
  - All articles in English only, but many Dashers prefer a different language
- **Human agent bottleneck**: Complex issues requiring human agents cause delays compared to instant automated solutions

These problems formed a perfect use case for a RAG (Retrieval Augmented Generation) system that retrieves information from knowledge base articles to generate responses that resolve Dasher issues efficiently.

## Solution

DoorDash developed an **LLM-based chatbot** using large language models (GPT-4 and Claude-3) with a RAG system, complemented by three critical quality control components to address LLM challenges.

### RAG System Architecture

The RAG process consists of several stages:

1. **Conversation Summarization**: Because issues are spread across several messages and follow-up questions, the system first condenses the entire conversation to pinpoint the core problem

2. **Historical Case Retrieval**: Using the summary, it searches historical data for the top N similar cases previously resolved with information from KB articles

3. **Article Integration**: Each identified issue corresponds to a specific article that is integrated into the prompt template

4. **Response Generation**: The enriched template allows the chatbot to generate a tailored response, leveraging:
   - Context of the conversation
   - Distilled issue summary
   - Relevant KB articles
   - Multi-language support through LLM translation capabilities

### Three Quality Control Systems

#### 1. LLM Guardrail System

An **online monitoring tool** that evaluates each output from the LLM to ensure accuracy and compliance before showing it to users.

**Two-Tier Approach:**

**Tier 1: Shallow Check (Cost-Effective)**
- Semantic similarity comparison between response and KB article segments
- Sliding window technique to measure similarities
- If response closely matches article, less likely to be hallucination
- Fast and economical first-line defense

**Tier 2: LLM-Powered Evaluator (Deep Check)**
- Triggered when shallow check fails
- Constructs prompt including initial response, relevant KB articles, and conversation history
- Evaluation model assesses whether response is grounded in provided information
- Provides rationale for further debugging
- Checks multiple aspects: groundedness, coherence, compliance

**Guardrail Checks:**
- Grounding of RAG information to prevent hallucinations
- Response coherence with previous conversations
- Filtering responses that violate company policies

**Default Strategy**: If response fails all guardrail tests, default to human agents to ensure quality user experience while maintaining high automation level

#### 2. LLM Judge for Quality Monitoring

Manual review of thousands of chat transcripts led to categorization of chatbot quality into **5 evaluation areas**:

1. **Retrieval correctness**: Did the system retrieve the right KB articles?
2. **Response accuracy**: Is the response factually correct?
3. **Grammar and language accuracy**: Are grammar and language usage correct?
4. **Coherence to context**: Does response align with conversation context?
5. **Relevance to Dasher's request**: Does response address what the Dasher actually asked?

**Monitoring Approach:**
- For each aspect, built monitors by prompting sophisticated LLM or creating rules-based regex metrics
- Overall quality determined by prompting LLM Judge with open-ended questions
- Answers processed and summarized into common issues
- High-frequency issues built into prompts or rules for further monitoring
- Continuous calibration between human review and automated system for effective coverage

#### 3. Quality Improvement Pipeline

**Human-AI Collaboration**: Human support agents act as subject matter experts, meticulously reviewing LLM responses and guiding automated process enhancements.

**Knowledge Base Improvements:**
- Thorough reviews and KB updates to eliminate misleading terminology
- Developer-friendly KB management portal for streamlined updates and expansion
- Complete and accurately phrased articles as foundational truth

**Retrieval Improvements:**
- **Query contextualization**: Simplifying queries to single concise prompt while providing context through comprehensive conversation history
- **Article retrieval**: Selecting optimal embedding model from choices within vector store to enhance retrieval accuracy

**Prompt Improvements:**
- Breaking down complex prompts into smaller, manageable parts with parallel processing
- Avoiding negative language in prompts; clearly outline desired actions with illustrative examples
- Implementing chain-of-thought prompting to encourage model to process and display reasoning
- Aids in identification and correction of logic errors and hallucinations

**Regression Prevention:**
- Open-source evaluation tool (Promptfoo) akin to unit testing in software development
- Allows rapid prompt refinement and model response evaluation
- Predefined test suite triggered by any prompt changes
- Blocks failing prompts
- Newly identified issues systematically added to test suites

## Impact

### Hallucination and Compliance Reduction
- **90% reduction in overall hallucinations**
- **99% reduction in potentially severe compliance issues**

### Scale and Automation
- **Thousands of Dashers assisted autonomously each day**
- Streamlined basic support requests
- Maximized value of human contributions
- Human support representatives focus on more complex problems

### System Transformation
- Initial prototype transformed into robust chatbot solution through quality monitoring and iterative improvement
- Created cornerstone for further advancements in automation capabilities

### Latency Trade-off
- End-to-end process includes generating response, applying guardrail, and possibly retrying
- Latency drawback noted but offset by quality improvements
- Strategic defaulting to human agents maintains user experience for edge cases

## Key Insights

1. **Guardrails are Non-Negotiable**: Two-tier guardrail system (shallow check + LLM evaluator) successfully reduces hallucinations by 90% and compliance issues by 99%.

2. **Quality Monitoring Drives Improvement**: LLM Judge across 5 dimensions (retrieval, accuracy, grammar, coherence, relevance) provides actionable feedback for system improvements.

3. **Human-AI Collaboration Works**: Subject matter experts reviewing LLM responses and guiding enhancements transforms initial prototypes into robust solutions.

4. **Knowledge Base Quality Matters**: KB serves as foundational truth, so complete and accurately phrased articles are critical for LLM response quality.

5. **Prompt Engineering Principles**: Break down complex prompts, avoid negative language, use chain-of-thought prompting, provide illustrative examples.

6. **Regression Prevention is Essential**: Automated testing (like Promptfoo) prevents quality degradation as prompts and models evolve.

7. **Default to Human for Edge Cases**: When responses fail guardrails, defaulting to human agents maintains quality user experience while preserving automation for majority of cases.

8. **Continuous Calibration Required**: Human review team calibrates against automated system to ensure effective coverage and catch edge cases.

## Challenges Addressed

### Groundedness and Relevance
**Challenge**: LLM occasionally generated responses that diverged from intended context, drawing from outdated or incorrect DoorDash information from public training data (Quora, Reddit, Twitter)

**Solution**: LLM Guardrail system with semantic similarity checks and LLM-powered evaluation

### Context Summarization Accuracy
**Challenge**: Must understand Dasher's issue from multi-turn conversations; summarization quality affects retrieval results

**Solution**: Conversation summarization system with high accuracy requirements, continuous monitoring

### Language Consistency
**Challenge**: LLMs primarily trained on English may occasionally overlook instructions to respond in different language

**Solution**: Multilingual prompting techniques; issue diminishes as LLM scales

### Consistent Action and Response
**Challenge**: LLM can perform actions through API calls, but function calls must be consistent with response text

**Solution**: Coherence checks in guardrail system

### Latency
**Challenge**: Latency varies from sub-second to tens of seconds depending on model and prompt size

**Solution**: Shallow check first layer minimizes latency for most responses; strategic defaulting for failures

## What's Next

### Expanding Automation Capabilities
- Address increasingly complex support scenarios with automated solutions
- Continue gap-narrowing between ideal experience and automated systems
- Leverage improvements in foundational models, ontology, and RAG systems

### Enhanced Model Performance
- As foundational models improve, LLM-driven solutions will become more effective
- Continuous data collection and analysis to guide enhancements
- Ensure systems remain agile and effective

### Human-AI Partnership Evolution
- While chatbot handles routine inquiries effectively, complex scenarios still require human expertise
- Expand capabilities of automated solutions with help of human customer support experts
- Maintain balance between automation efficiency and human touch for complex issues

## Technical Stack

- **LLMs**: GPT-4, Claude-3
- **RAG System**: Conversation summarization + historical case retrieval + KB article integration
- **Guardrail**: Two-tier (semantic similarity + LLM evaluator)
- **Quality Monitoring**: LLM Judge across 5 dimensions
- **Testing Tool**: Promptfoo (open-source evaluation tool)
- **Vector Store**: For article retrieval with embedding models
- **Prompt Techniques**: Chain-of-thought prompting, parallel processing

## Quality Evaluation Framework

| Dimension | Monitoring Approach | Purpose |
|-----------|-------------------|----------|
| Retrieval Correctness | LLM prompting or rules-based regex | Ensure right KB articles retrieved |
| Response Accuracy | LLM Judge with open-ended questions | Verify factual correctness |
| Grammar & Language | Rules-based and LLM evaluation | Maintain language quality |
| Coherence to Context | LLM-based coherence checks | Align with conversation flow |
| Relevance to Request | LLM Judge relevance scoring | Address actual Dasher needs |

---

**Tags**: LLM, RAG, Chatbot, Customer Support, Guardrails, Quality Monitoring, GPT-4, Claude-3, Prompt Engineering, Chain-of-Thought, Production System, Multi-Language Support

**Related Examples**:
- [Thomson Reuters Customer Support RAG](thomson-reuters-customer-support-rag.md)
- [Minimal Multi-Agent Customer Support System](minimal-multi-agent-customer-support.md)
- [Coinbase Conversational Chatbot with RAG](coinbase-conversational-chatbot-rag.md)
