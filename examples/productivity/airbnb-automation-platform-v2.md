# Airbnb Automation Platform v2 - LLM-Powered Conversational AI

**Source**: [Airbnb Engineering Blog - Automation Platform v2: Improving Conversational AI at Airbnb](https://medium.com/airbnb-engineering/automation-platform-v2-improving-conversational-ai-at-airbnb-d86c9386e0cb)
**Authors**: Chutian Wang, Zhiheng Xu, Paul Lou, Ziyi Wang, Jiayu Lou, Liuming Zhang, Jingwen Qiang, Clint Kelly, Lei Shi, Dan Zhao, Xu Hu, Jianqi Liao, Zecheng Xu, Tong Chen
**Date**: October 28, 2024
**Category**: Productivity & Automation

## Problem

Airbnb's Automation Platform v1 supported conversational AI products through predefined step-by-step workflows designed by product engineering and business teams. While functional, this approach faced significant limitations.

**Challenges of Traditional Conversational AI Systems (v1):**
- **Not flexible enough**: AI products followed predefined (usually rigid) processes that couldn't adapt to nuanced user needs
- **Hard to scale**: Product creators needed to manually create workflows and tasks for every scenario, repeating the entire process for any new use case
- **Time-consuming and error-prone**: Manual workflow creation was labor-intensive and prone to mistakes
- **Limited natural dialogue**: Predefined workflows couldn't handle open-ended questions or capture nuanced information from ongoing conversations

**The LLM Opportunity:**
Early experiments showed that LLM-powered conversation could provide a more natural and intelligent conversational experience than human-designed workflows. Customers could engage in natural dialogue, ask open-ended questions, and explain issues in detail, with LLMs accurately interpreting queries and capturing nuanced information.

**The Challenge:**
LLM-powered applications were still relatively new, with the community working to improve aspects like latency and hallucination. Too early to fully rely on them for large-scale diverse experiences serving millions of customers. For instance, sensitive data and strict validations (like claim processing) were better suited for traditional workflows.

## Solution

Airbnb developed **Automation Platform v2**, a conversational AI platform designed specifically for emerging LLM applications that combines the benefits of both LLM-powered conversation and traditional workflows.

### Hybrid Approach: Best of Both Worlds

The team's strategy: **combine LLM-powered conversation with traditional workflows** to leverage the benefits of both approaches:
- **Traditional workflows**: Better for sensitive data, strict validations, and deterministic processes
- **LLM-powered workflows**: Better for natural dialogue, nuanced understanding, and adaptive reasoning

### Architecture Overview

When a user inquiry arrives (e.g., "where is my next reservation?"):
1. Platform collects relevant contextual information (previous chat history, user id, user role, etc.)
2. Platform loads and assembles prompt using inquiry and context, sends to LLM
3. LLM response requests tool execution (e.g., service call to fetch most recent reservation)
4. Platform follows order, executes actual service call, saves responses into current context
5. Platform sends updated context to LLM
6. LLM generates complete response (e.g., describing location of next reservation)
7. Platform returns LLM response and records conversation for future reference

### Key Components

#### 1. Chain of Thought Workflow

Implementation of the **Chain of Thought** AI agent framework that enables LLMs to reason about issues.

**Core Idea**: Use LLM as reasoning engine to determine which tools to use and in which order. Tools are the way an LLM interacts with the world to solve real problems (e.g., checking reservation status, checking listing availability).

**Main Steps**:
1. **Prepare context**: Prompt, contextual data, and historical conversations
2. **Trigger reasoning loop**:
   - Ask LLM for reasoning
   - Execute LLM-requested tool
   - Process tool's outcome
3. **Loop until result**: Chain of Thought stays in reasoning loop until a result is generated

**Components**:
- **CoT IO Handler**: Assemble prompt, prepare contextual data, collect user input, general data processing before sending to LLM
- **Tool Manager**: Prepare tool payload with LLM input & output, manage tool execution, offer quality of life features like retry or rate limiting
- **LLM Adapter**: Allow developers to add customized logic facilitating integration with different types of LLMs

**Key Innovation**: Tools are essentially actions and workflows from v1, which work well as tools in Chain of Thought because of their unified interface and managed execution environment.

#### 2. Context Management

To ensure the LLM makes the best decision, the system provides all necessary and relevant information:
- Historical interactions with the LLM
- Intent of the customer support inquiry
- Current trip information
- For offline evaluation: point-in-time data retrieval

**Developer Flexibility**:
- Statically declare needed context (e.g., customer name)
- Name a dynamic context retriever (e.g., relevant help articles for customer's questions)

**Components**:
- **Context Loader**: Connect to different sources and fetch relevant context based on developers' customizable fetching logic
- **Runtime Context Manager**: Maintain runtime context, process context for each LLM call, interact with context storage

#### 3. Guardrails Framework

A safe-guarding mechanism that monitors communications with the LLM, ensuring responses are helpful, relevant, and ethical.

**Addresses LLM Issues**:
- **Hallucinations**: LLM generating false or nonsensical information
- **Jailbreaks**: Attempts to bypass LLM safety restrictions

**Architecture**:
- Engineers from different teams create reusable guardrails
- During runtime, guardrails executed in parallel
- Leverage different downstream tech stacks

**Examples**:
- **Content Moderation Guardrail**: Calls various LLMs to detect violations in communication content
- **Tool Guardrails**: Use rules to prevent bad execution (e.g., updating listings with invalid setup)

#### 4. Additional Developer Support Components

While not detailed in the post, the platform also includes:
- **Playground feature**: Bridges gap between development and production tech stacks, allowing prompt writers to freely iterate on prompts
- **LLM-oriented observability**: Detailed insights into each LLM interaction (latency, token usage)
- **Enhanced Tool management**: Responsible for tool registration, publishing process, execution, and observability

## Impact

While specific metrics weren't provided, the platform enables:
- **More efficient customer support**: Agents work more efficiently with LLM assistance
- **Better resolutions**: More accurate understanding of customer needs
- **Quicker responses**: Automated reasoning and tool execution
- **Production deployment**: Real system serving millions of Airbnb customers
- **Developer productivity**: Seamless integration between system and developer tools

## Key Insights

1. **Hybrid Approach Works Best**: At this stage, combining LLM-powered conversation with traditional workflows leverages the benefits of both approaches. Don't fully replace traditional systems yet.

2. **Use Traditional Workflows for Sensitive Data**: Processes requiring strict validations, sensitive data handling, or deterministic outcomes are better suited for traditional workflows.

3. **Tools as Bridge Between Old and New**: Reusing actions and workflows from v1 as tools in Chain of Thought provides unified interface and managed execution environment.

4. **Context is Critical**: Providing all necessary contextual information (history, intent, trip info, etc.) is essential for LLM decision-making quality.

5. **Guardrails are Non-Negotiable**: Production LLM applications must have robust guardrails to address hallucinations, jailbreaks, and ensure helpful, relevant, ethical responses.

6. **Developer Experience Matters**: Providing playground, observability, and tool management significantly improves developer productivity when building LLM applications.

7. **Modular Architecture Enables Flexibility**: Separating concerns (IO handling, tool management, LLM adapter, context management, guardrails) allows customization and scalability.

## What's Next

The team plans to continue evolving with transformative technologies:
- **Explore other AI agent frameworks**: Beyond Chain of Thought
- **Expand Chain of Thought tool capabilities**: Add more tools and improve existing ones
- **Investigate LLM application simulation**: Testing and validation approaches
- **Anticipate further gains**: Efficiency and productivity improvements for all AI practitioners at Airbnb

## Technical Stack

- **LLMs**: Large language models (specific models not disclosed)
- **Chain of Thought**: AI agent framework for reasoning
- **Automation Platform v1**: Actions and workflows repurposed as tools
- **Context Management System**: Custom-built for context loading and runtime management
- **Guardrails Framework**: Multi-LLM content moderation and rule-based validation
- **Developer Tools**: Playground, observability, tool management

## Architecture Comparison

### Traditional Workflows (v1)
- Predefined step-by-step processes
- Static, rigid structure
- Manual creation for each scenario
- Time-consuming to scale
- Good for: Sensitive data, strict validations, deterministic processes

### AI-Driven Workflows (v2)
- LLM reasoning to determine tool usage and order
- Dynamic, adaptive structure
- Automatic reasoning and tool selection
- Scales through additional tools
- Good for: Natural dialogue, nuanced understanding, open-ended questions

### Hybrid Approach (v2 Strategy)
- Combines both traditional and AI-driven workflows
- Leverages strengths of each approach
- Traditional workflows called as tools by LLM
- Production-ready balance of flexibility and reliability

---

**Tags**: Conversational AI, LLM, Chain of Thought, Customer Support, Guardrails, Context Management, Tool Management, Hybrid Architecture, Production System, Developer Platform

**Related Examples**:
- [Airtable Event-Driven Agentic Framework](airtable-agentic-framework.md)
- [Uber Enhanced Agentic-RAG - Genie On-Call Copilot](uber-enhanced-agentic-rag.md)
- [Minimal Multi-Agent Customer Support System](minimal-multi-agent-customer-support.md)
