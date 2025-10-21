---
title: "Expense Policy Agent"
company: "Ramp"
author: "Ramp Engineering Team"
source: "https://engineering.ramp.com/post/how-to-build-agents-users-can-trust"
date: "2025-01"
category: "finance"
tags: ["workflow-automation", "structured-output", "document-analysis", "enterprise", "production"]
description: "Autonomous expense approval agent handling 65% of approvals by using transparent reasoning and graduated trust mechanisms"

# Problem Classification
problemPattern: "workflow-automation"
problemComplexity: "complex"

# Architecture
architecture:
  type: "single-agent"
  pattern: "decision-framework"
  rationale: "Categorical decision framework (Approve/Reject/Needs Review) instead of confidence scores enables meaningful policy-based decisions with clear escalation paths"
  components: ["policy-context-manager", "decision-engine", "reasoning-generator", "workflow-integration"]

# What Made It Work
breakthroughInsight: "Building trust through transparency and escape hatches - allowing agents to declare uncertainty ('not sure') and providing cited reasoning for every decision builds more trust than forced high-confidence outputs"

criticalConstraints:
  - "policy-ambiguity-high"
  - "approval-volume-justifies-automation"
  - "asymmetric-upside"
  - "user-trust-essential"

antiPatterns:
  - "confidence-scores: LLMs produce unreliable 70-80% confidence regardless of actual uncertainty, creating false precision"
  - "unchecked-user-feedback: finance teams may be lenient or incorrect, requiring expert validation for ground truth"

# Tech Stack
techStack:
  framework: "Custom"
  llmProvider: "LLM-based"
  knowledgeRetrieval: "policy-embedding"
  otherTools: ["workflow-builder", "policy-editor", "golden-dataset-evaluator"]

# Scale
scale:
  volume: "65% of expense approvals handled autonomously"
  latency: "real-time decision-making"
---

# Expense Policy Agent

## The Problem

Expense approval at scale requires managers to review hundreds or thousands of employee expenses against company policies. Policies are often written in natural language PDFs with inherent ambiguity, making automation with traditional rule-based systems infeasible. Manual review is time-consuming and inconsistent.

**The Manual Process:**
- Managers manually review each expense submission
- Cross-reference against policy documents (often PDFs)
- Interpret ambiguous policy language case-by-case
- Make approve/reject decisions with inconsistent application
- High volume creates bottlenecks and delays reimbursement

**Key Pain Points:**
- Policy documents contain ambiguous language unsuitable for simple if/then rules
- High approval volume makes manual review unsustainable
- Inconsistent policy interpretation across managers
- Employees need timely approvals, but managers are overwhelmed
- Traditional automation can't handle the nuance required

## The Solution

An LLM-powered agent that autonomously approves, rejects, or escalates expense submissions based on company policies with transparent reasoning. The agent now handles over 65% of approvals without human intervention.

**Impact**: 65% of expense approvals now handled autonomously with transparent policy-based reasoning, reducing manager workload while maintaining policy compliance.

## How It Works

**Key Capabilities:**
- **Categorical Decision Framework** - Outputs one of three predefined outcomes (Approve, Reject, Needs Review) instead of unreliable confidence scores
- **Collaborative Context Management** - Policies brought into platform and edited directly, serving as live context for agent decisions
- **Transparent Reasoning** - Every decision includes cited explanations referencing specific policy sections
- **Autonomy Sliders** - Users control agent authority through workflow builder, combining deterministic rules with agentic decisions
- **Escape Hatches** - Agent can declare uncertainty and escalate to existing human review processes

**Process Flow:**
1. Employee submits expense through Ramp platform
2. Agent retrieves relevant expense policies (embedded in platform, not external PDFs)
3. LLM analyzes expense against policy context
4. Decision engine selects one of three outcomes:
   - **Approve**: Clear policy alignment
   - **Reject**: Clear policy violation
   - **Needs Review**: Uncertain edge cases
5. For Approve/Reject: Generate reasoning with direct policy citations
6. For Needs Review: Escalate to pre-existing human approval workflow
7. User receives decision with transparent explanation

**Technical Architecture:** The system integrates with Ramp's existing workflow builder, allowing companies to layer deterministic rules (e.g., dollar thresholds, vendor blocklists) with agentic policy interpretation. Policies are stored in-platform with an editor for modifications, eliminating the PDF parsing problem.

## Key Insight

**Escape hatches build more trust than forced high-confidence decisions.** Allowing the agent to declare "not sure" and escalate uncertain cases to humans creates higher trust than forcing the LLM to always produce a decision with a confidence score.

**Why This Matters:**
- LLM confidence scores are unreliable—they typically output 70-80% regardless of actual uncertainty, creating false precision
- Categorical outcomes (Approve/Reject/Needs Review) force meaningful bucketing instead of arbitrary thresholds
- Transparency through cited reasoning enables users to verify decisions and developers to debug behavior
- Graduated trust deployment (suggestions → subset actions → full autonomy) allows users to validate patterns before delegating authority
- Golden datasets with expert review solve "affinity bias" where user feedback may be overly lenient

**Problem Selection Criteria:** Ramp deliberately chose expense approval because it has (1) ambiguity unsuitable for simple heuristics, (2) high volume justifying automation investment, and (3) asymmetric upside where value gained far exceeds error costs.

**Evaluation Strategy:** Created carefully-reviewed golden datasets independent of user feedback, addressing the issue where finance teams might approve reasonable-but-out-of-policy expenses, which would corrupt training data.

## Links

- [Original Article](https://engineering.ramp.com/post/how-to-build-agents-users-can-trust) - How to Build Agents Users Can Trust
