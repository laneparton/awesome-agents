---
title: "Cisco Outshift JARVIS - Agentic AI Platform Engineer"
company: "Cisco Outshift"
author: "Outshift by Cisco"
source: "https://blog.langchain.com/cisco-outshift/"
date: "2025-05"
category: "development"
tags: ["multi-agent", "platform-engineering", "workflow-automation", "production"]
description: "10x productivity boost - CI/CD setup from 1 week to <1 hour, resource provisioning from half-day to seconds"
---

# Cisco Outshift JARVIS - Agentic AI Platform Engineer

## The Problem

Outshift is the incubation engine at Cisco driving innovation in emerging technologies. Their small Platform Engineering team managed complex, distributed cloud-native SaaS environments while supporting multiple incubation projects. Platform engineers had to constantly context-switch to service frequent developer requests ranging from access management to infrastructure provisioning while also developing new platform features.

**The Manual Process:**
- Developers would request routine tasks like CI/CD pipeline setup (taking up to a week)
- Resource provisioning requests (S3 buckets, EC2 instances, LLM keys) took half a day
- Access management and permissions required manual back-and-forth communication
- Platform engineers had to monitor and diagnose issues across multiple heterogeneous systems
- Information was scattered across runtime environments, telemetry systems, and documentation sites
- Constant context switching between tools and workflows for routine requests

**Key Pain Points:**
- **Long wait times** - Simple, frequent requests often took days to complete due to queue backlog
- **Increased cognitive load** - Constant context switching between different tools and workflows reduced efficiency
- **Operational inefficiencies** - High-value engineering tasks (new features, platform advancement) were deprioritized in favor of routine platform maintenance
- **Bottleneck effect** - Small team size meant developer velocity was limited by platform team availability

## The Solution

Outshift developed JARVIS, an AI Platform Engineer designed as a distributed Multi-Agent System (MAS) that automates routine platform engineering tasks. JARVIS is orchestrated using LangGraph and connected through the AGNTCY Agent Connect Protocol (ACP) for seamless agent-to-agent collaboration across systems.

**Impact**: Achieved 10x productivity boost - tasks that previously took a week (CI/CD setup) now complete in under an hour, and resource provisioning reduced from half-day tasks to seconds. Organization now handles significantly higher volume of requests with same team size while reducing burnout.

## How It Works

**Key Capabilities:**
- **Knowledge Management** - Integrates with platform knowledge bases (documentation, policies, Jira, code repositories) using RAG for unstructured data and GraphRAG for structured data
- **Self-Service Automation** - Automates CI/CD onboarding, cloud resource provisioning, and developer sandbox environment setup
- **Code Generation** - Translates natural language inputs into Kubernetes manifests and infrastructure templates using hybrid ML approach
- **Multi-Interface Access** - Embedded in Jira, Backstage, Webex, and CLI so developers interact without changing existing workflows
- **Autonomous Task Execution** - Executes assigned tasks autonomously and reaches out for additional input only when needed

**Process Flow:**
1. Developer submits request through preferred interface (Jira ticket, Backstage chat, Webex message, or CLI command)
2. JARVIS receives request and analyzes required workflow using specialized agents
3. System retrieves relevant context from knowledge bases using RAG/GraphRAG
4. Distributed agents collaborate via AGNTCY Agent Connect Protocol to execute across heterogeneous systems
5. For code generation needs, JARVIS translates natural language to K8s manifests or infrastructure templates
6. JARVIS autonomously executes the workflow (provisioning, configuration, deployment)
7. System provides real-time notifications and updates through developer's chosen interface
8. If additional input needed, JARVIS reaches out to developer; otherwise completes fully autonomous

**Technical Architecture:** Built as distributed Multi-Agent System with LangGraph providing scalable, deterministic workflow orchestration. Uses AGNTCY Agent Connect Protocol (ACP) as open standard for agent-to-agent communication across heterogeneous systems. Implements both RAG (unstructured data) and GraphRAG (structured data) for knowledge retrieval. Continuous monitoring via LangSmith tracing and evaluation with agentevals framework.

**Development Approach:** Followed AGNTCY's Four-Phase methodology:
1. **Discover** - Mapped critical platform workflows with specialized first- and third-party agents
2. **Compose** - Designed flexible, modular workflows with LangGraph and ACP for seamless collaboration
3. **Deploy** - Operationalized across cloud-native ecosystem using AGNTCY Workflow Server
4. **Evaluate** - Continuous tracing, benchmarking, and feedback loops for refinement

## Key Insight

**Meeting developers where they already work is critical for adoption** - Rather than forcing developers to learn a new interface, JARVIS embedded agentic capabilities directly into existing tools (Jira, Backstage, Webex, CLI). This eliminated friction and drove immediate adoption across the organization.

**Why This Matters:**
- Open standards like AGNTCY Agent Connect Protocol enable reliable agent-to-agent communication across heterogeneous systems, essential for enterprise multi-agent systems
- Distributed multi-agent architecture allows seamless integration of first-party and third-party agents to automate complex platform workflows
- Continuous evaluation and benchmarking ensure reliability - LangSmith tracing and agentevals allow teams to analyze reasoning patterns, detect inconsistencies, and refine performance at scale
- Internet of Agents (IoA) approach unlocks true potential by enabling discoverability, collaboration, reuse, and simplified creation of complex deterministic multi-agent systems
- Embedding GenAI-driven agent outputs within traditional interfaces ensures intuitive interaction with complex workflows without disrupting daily routines

**Scale Achievement:** The system successfully handles significantly higher request volumes with the same team size. Routine communication overhead for simple tasks has been completely eliminated, allowing platform engineers to focus on high-value feature development while maintaining (and improving) developer experience.

## Links

- [Case Study: Cisco Outshift JARVIS AI Platform Engineer](https://blog.langchain.com/cisco-outshift/) - Original LangChain blog post
- [AGNTCY - Internet of Agents](https://agntcy.org) - Open collaboration layer for AI agent ecosystem
- [Outshift Incubations](https://outshift.cisco.com/) - Cisco's innovation incubation engine
