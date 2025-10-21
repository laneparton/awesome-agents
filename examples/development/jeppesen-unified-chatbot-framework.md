---
title: "Unified Chatbot Framework at Jeppesen (Boeing)"
company: "Jeppesen (Boeing)"
author: "Jeppesen AI Engineering Team (Divya Basu, Yamini Guhe, Karan Dodiya)"
source: "https://www.llamaindex.ai/blog/jeppesen-a-boeing-company-saves-2-000-engineering-hours-with-unified-chat-framework-built-on"
date: "2025-01"
category: "development"
tags: ["development", "enterprise", "agent-framework", "llamaindex", "boeing", "chatbots", "automation"]
description: "87% reduction in agent development time (512 to 64 hours), saving ~2,000 engineering hours"
---

# Unified Chatbot Framework at Jeppesen (Boeing)

## The Problem

Jeppesen's enterprise AI engineering team faced a growing challenge: internal teams across the organization were independently piloting and experimenting with AI-powered chatbots. This fragmented approach led to duplicated work, compliance hurdles, and isolated deployments with no shared learning or reusable components.

**The Manual Process:**
- Each team building chatbots from scratch independently
- 512 hours to build a single chatbot or agent from scratch
- Every team navigating AI governance and IT policy approvals separately
- No shared templates, components, or knowledge base
- Custom interfaces, deployment models, and tool integrations per team

**Key Pain Points:**
- Redundant effort across multiple teams building similar components
- Compliance burdens requiring each team to individually handle governance
- Long development cycles preventing rapid experimentation
- Lack of standardization creating maintenance nightmares
- No way to share learnings or improvements across teams

## The Solution

A lean 5-7 person frameworks team built the Unified Chatbot Framework (UCF)—a templatized platform that dramatically simplifies agent creation using LlamaIndex's open-source components. The framework provides shared infrastructure with built-in security, compliance, and privileged access to internal systems.

**Impact**: Reduced development time from 512 hours to 64 hours per agent (87% reduction). Already saved 1,792 collective hours across teams, with projections of ~4,900 hours saved annually after global rollout. Now powering 10-11 production products across Boeing.

## How It Works

**Key Technologies:**
- **LlamaIndex Event-Driven Workflows** - Flexible agent orchestration with session and state management
- **Tool Connectors** - GraphQL, SQL, REST APIs, Neo4j, Databricks Data Mesh
- **Multi-LLM Support** - Azure, AWS, HuggingFace, open models
- **Vector Database Options** - Azure AI Search, Qdrant
- **Conversation Memory** - Azure CosmosDB, Azure Table, Azure Cache for Redis

**Process Flow:**
1. Teams start with pre-built workflow templates for single or multi-agent systems
2. Import a template and configure with a simple JSON config file
3. Bring your own LLM, vector database, and data sources
4. Connect to internal systems using pre-built tool connectors
5. Build custom tools based on your data without worrying about base LLM app components
6. Deploy with built-in enterprise compliance and security standards
7. Framework handles governance, privileged access, and standardization automatically

**Developer Experience:** Agents can be built with ~50 lines of code and a JSON config file, with all enterprise requirements handled automatically.

## Key Insight

**Jeppesen evaluated several agent frameworks, including chain and graph-based options, but chose LlamaIndex for its flexibility and production-grade control.** Rigid graph-based frameworks couldn't meet enterprise constraints.

**Why This Matters:**
- Event-driven workflows with full control over state transitions vs. rigid predefined flows
- Transparent, open-source tooling with strong developer community support
- Fine-grained control over agent logic, inputs, and execution flow
- Modular design allows bringing your own components (LLM, vector DB, data sources)
- Low-code configuration (JSON file) while maintaining full customization capability
- Built-in support for custom tool creation and template injection

**Platform Evolution:** UCF started as a chatbot framework but is naturally evolving into a full agent orchestration system. Because LlamaIndex treats everything as a workflow, it supports both conversational and automated event-triggered tasks.

**Success Measurement:** "We measure success not just in hours saved, but in how quickly teams can explore, contribute back, and scale securely." —Karan Dodiya, Technical Product Owner

## Links

- [Original Blog Post](https://www.llamaindex.ai/blog/jeppesen-a-boeing-company-saves-2-000-engineering-hours-with-unified-chat-framework-built-on) - Full case study
- [LlamaIndex](https://www.llamaindex.ai/) - Agent framework used
- [LlamaIndex Workflows](https://docs.llamaindex.ai/en/stable/understanding/workflows/) - Documentation on event-driven workflows
