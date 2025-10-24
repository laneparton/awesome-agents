---
title: "Google Security Incident Response with Generative AI"
company: "Google"
author: "Lambert Rosique, Jan Keller, Diana Kramer, Alexandra Bowen, Andrew Cho"
source: "https://security.googleblog.com/2024/04/accelerating-incident-response-using.html"
date: "2024-04"
category: "Development & Engineering"
tags: ["incident-response", "document-generation", "prompt-engineering", "production", "workflow-automation"]
description: "51% time savings in incident summary writing through LLM-generated summaries that outperformed human-written equivalents by 10%"

# Problem Classification
problemPattern: "workflow-automation"
problemComplexity: "moderate"

# Architecture
architecture:
  type: "single-agent"
  pattern: "ai-assisted-writing"
  rationale: "LLM generates initial draft summaries that humans review and refine before publishing - balancing AI efficiency with human accountability to mitigate hallucination risks while maintaining quality standards"
  components: ["structured-input-processor", "llm-summarizer", "human-review-interface"]

# What Made It Work
breakthroughInsight: "Iterative prompt engineering with structured input tags and human-crafted examples was critical - final prompt with 2 curated summary examples and self-explanatory tags (<Title>, <Impact>, <Mitigation History>) produced outstanding summaries without hallucinations"

criticalConstraints:
  - "privacy-sensitive-data"
  - "no-data-storage-allowed"
  - "accuracy-critical"
  - "multiple-audience-types"

antiPatterns:
  - "simple-task-prompts: produced inconsistent, overly long summaries missing key facts"
  - "prompt-without-examples: struggled with format adherence and latest update prioritization"

# Tech Stack
techStack:
  framework: "custom"
  llmProvider: "not-specified"
  knowledgeRetrieval: "structured-incident-data"
  otherTools: ["input-tagging-system", "no-logging-infrastructure"]

# Scale
scale:
  volume: "production deployment for Google security incident response"
  latency: "real-time summary generation integrated into incident workflow"
---

# Google Security Incident Response with Generative AI

## The Problem

Google's security and privacy incident response teams needed to write thorough summaries for different audiences—executives, leads, and partner teams—during active incident management. This tedious, time-consuming process heavily depended on target audience and incident complexity, with writing requirements that created bottlenecks during critical security events.

**The Manual Process:**
- Security teams manually drafted incident summaries from scratch for each audience
- Reviewed complex, unstructured incident data (logs, images, links, stats, timelines, code)
- Synthesized information to address main incident response steps (coordination, resolution)
- Ensured compliance with regulatory requirements and internal best practices
- Nearly 1 hour spent writing thorough summaries for standard incidents
- Multiple hours required for complex executive communications
- Repeated similar work across different stakeholder groups

**Key Pain Points:**
- Time-intensive summary writing diverted responders from more critical incident management tasks
- Inconsistent quality depending on writer's familiarity with best practices (passive voice, tense, terminology)
- Different audience needs required multiple tailored communications per incident
- Difficult to extract key points from messy, unstructured incident data
- Communication delays could impact regulatory compliance and executive decision-making
- Native and non-native English speakers produced varying quality levels

## The Solution

Google built an LLM-powered tool integrated into their incident workflow that generates draft summaries from structured incident data. The system uses carefully engineered prompts with human-crafted examples to produce summaries that security teams review and refine before publishing, maintaining human accountability while dramatically reducing writing time.

**Impact**:
- **51% time savings** per incident summary when using LLM generation versus manual writing
- **53% time reduction** for complex executive communications
- **10% higher quality ratings** for LLM-written summaries compared to human-written equivalents
- **Consistent coverage** of all key points across both simple and complex incidents
- Successfully deployed across Google's security incident response workflow at production scale

## How It Works

**Key Capabilities:**
- **Structured Input Processing** - Transforms messy incident data (logs, code, free-form text) into tagged format using self-explanatory tags like <Title>, <Actions Taken>, <Impact>, <Mitigation History>
- **Context-Aware Summarization** - LLM generates concise summaries focused on coordination and resolution steps, following organizational best practices
- **Privacy-Preserving Architecture** - Zero-logging infrastructure ensures no incident data stored; LLM doesn't use input/output for retraining
- **Human-in-the-Loop Review** - "Generate Summary" button pre-populates draft that humans can accept, modify, or discard
- **Multi-Audience Support** - Evolved from basic summaries to complex executive communications with multiple sections

**Process Flow:**
1. Incident responder gathers facts from monitoring, detection tools, and triage process
2. Input processor structures messy data by replacing long code/log sections with self-closing tags (<Code Section/>, <Logs/>)
3. Structured incident data tagged with descriptive elements (<Title>, <Impact>, <Comment>)
4. System checks input size - only calls LLM if >200 tokens to prevent hallucinations on small inputs
5. LLM receives engineered prompt with task, guidelines, and 2 human-crafted summary examples
6. Model generates draft summary following organizational format and best practices
7. Draft appears in UI via "Generate Summary" button pre-populating text field
8. Human reviewer accepts summary as-is, makes manual edits, or discards and starts fresh
9. Finalized summary published to appropriate stakeholders (executives, leads, partner teams)

**Prompt Engineering Evolution:** Team iterated through 3 major prompt versions. Version 1 (simple task) produced overly long, inconsistent summaries. Version 2 (elaborate instructions) improved but still struggled with format adherence and latest updates. Final prompt introduced <Good Summary> tag with 2 human-crafted examples, immediately starting output generation without task repetition. This produced "outstanding summaries" with correct structure, complete coverage, and minimal hallucinations.

**Privacy Architecture:** Built infrastructure ensuring no confidential data storage - logging disabled across entire pipeline (UI, LLM, output processing). LLM explicitly configured not to use inputs/outputs for retraining. System monitored through metrics and indicators rather than data logging, meeting strict requirements for sensitive security incident information.

## Key Insight

**Iterative prompt engineering with structured inputs and curated examples is critical for production quality** - The breakthrough came from combining self-explanatory XML-style tags that mirrored incident templates with 2 human-crafted summary examples in the final prompt. This taught the model both the structure (what to include) and quality standards (how to write it) while the <Good Summary> tag eliminated unnecessary preambles.

**Why This Matters:**
- Simple task prompts fail for complex, structured outputs - need explicit examples showing desired format
- Structured input tags (<Title>, <Impact>) create clear semantic boundaries that LLMs can reference in prompts
- Few-shot examples (2-3 high-quality summaries) dramatically outperform lengthy guidelines alone
- Input size thresholds prevent hallucinations - blocking LLM calls for <200 token inputs eliminated edge case failures
- Human review remains essential for accuracy-critical applications despite LLM quality improvements
- Privacy-preserving architectures enable AI deployment on sensitive data through zero-logging and no-retraining configurations

**Critical Design Principles:**
- Start with simple prompts and iterate based on observed failures
- Structure unstructured data before LLM processing using domain-specific tags
- Include concrete examples of desired output format, not just instructions
- Build in programmatic safeguards (size thresholds) to prevent known failure modes
- Always maintain human accountability through review loops for high-stakes content
- Design zero-logging infrastructure for sensitive data from the start

## Links

- [Accelerating Incident Response Using Generative AI](https://security.googleblog.com/2024/04/accelerating-incident-response-using.html) - Original security blog post
- [Google Incident Response Program](https://cloud.google.com/security/incident-response) - Overview of response process
