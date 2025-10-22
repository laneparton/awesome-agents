# Grab RAG-Powered LLM for Analytics

**Company**: Grab
**Domain**: Data Analysis
**Published**: October 2024

## Problem

Data Analysts (DAs) at Grab struggle with the growing number of data queries from stakeholders across the organization. The conventional approach creates significant inefficiencies:

### Repetitive Manual Work
- Manually writing and running similar queries repeatedly
- Time-consuming process for routine tasks
- Same SQL queries executed with minor parameter changes (dates, filters, conditions)
- Limited ability to focus on higher-value analytical work

### Investigation Bottlenecks
- Fraud investigations require querying multiple data points
- Each investigation involves contextualizing several different pieces of information
- Traditional manual approach is slow and resource-intensive
- Delays in detecting and responding to fraud patterns

## Solution

Grab's Integrity Analytics team built a **RAG-powered LLM system** integrated with "Data-Arks" (custom Python API platform) to automate tedious analytical tasks including regular metric reports and fraud investigations.

### How It Works

**Data-Arks - The Data Middleware:**

Data-Arks is an in-house Python-based API platform that:
- Houses frequently used SQL queries packaged as individual APIs
- Integrates with Slack, Wiki, and JIRA APIs for information retrieval
- Allows self-service: employees can upload any SQL query to the platform
- Serves as the bridge between data sources and LLM agents

**Integration Architecture:**

1. **Spellvault**: Internal LLM platform with low/no-code RAG capabilities
2. **Data-Arks**: Executes exact SQL queries and channels output to LLM
3. **Scheduler**: Runs LLM applications at regular intervals for automation
4. **Slack**: User interface for interaction and report delivery

**Report Summarizer Workflow:**
1. Scheduler triggers report generation
2. Data-Arks API called to generate data in tabular format
3. LLM summarizes data and generates key insights
4. Automated report delivered through Slack

**A* Bot - Fraud Investigation Helper:**
1. User submits fraud investigation query via Slack
2. Spellvault selects most relevant queries using RAG
3. Data-Arks executes selected queries
4. LLM contextualizes multiple data points
5. Summary of results provided through Slack

### Impact

- **3-4 hours saved per report** through automated generation and summarization
- **Fraud investigations reduced to minutes** from time-consuming manual process
- **Simultaneous multi-query execution**: A* bot provides all necessary fraud investigation information at once
- **Production deployment** across Integrity Analytics team with multiple use cases

## Key Insights

### 1. RAG Over Fine-Tuning for Analytics

The team chose RAG instead of fine-tuning based on three critical factors:

**Effort and Cost**:
- Fine-tuning requires significant computational cost for domain-specific training
- RAG computationally less expensive - retrieves only relevant data
- Same base model reusable for different use cases with RAG

**Latest Information**:
- Fine-tuning requires model re-training with each update
- RAG retrieves current information from production database
- Eliminates need for constant model re-training

**Speed and Scalability**:
- No burden of model re-training enables rapid scaling
- Team can quickly build new LLM applications
- Well-managed knowledge base supports multiple use cases

### 2. Multi-Tool Integration is Essential

LLMs alone are insufficient - comprehensive solution requires:
- **LLM Platform** (Spellvault): Low/no-code RAG capabilities
- **Data Middleware** (Data-Arks): Executes queries, serves formatted data
- **Scheduler**: Automates routine tasks
- **Messaging Tool** (Slack): User interaction interface

Integration creates seamless end-to-end automation from data retrieval to insight delivery.

### 3. Self-Service Democratizes AI

Data-Arks' self-service model:
- Any employee can upload SQL queries to platform
- Queries surfaced as APIs callable by LLM agents
- Extends analytics automation across teams and functions
- Lowers barrier to entry for creating LLM applications

### 4. Context Retrieval Beats Memorization

For analytical tasks where required data and format are known:
- RAG retrieves exact information from knowledge base
- More reliable than expecting LLM to "remember" specifics
- Reduces hallucinations by grounding in actual data
- Ensures consistency across reports and investigations

## Technical Architecture

```
Data Sources (Production DB, Slack, Wiki, JIRA)
         ↓
   [Data-Arks APIs]
- Frequently used SQL queries
- Python functions
- Integration APIs
         ↓
   [Spellvault - LLM Platform]
- RAG-powered query selection
- Context retrieval
- Response generation
         ↓
   [Use Cases]
         ├─→ Report Summarizer
         │   - Scheduled execution
         │   - Tabular data → LLM summarization
         │   - Key insights extraction
         │   - Slack delivery
         │
         └─→ A* Bot (Fraud Investigation)
             - User prompt → Relevant query selection
             - Multi-query execution
             - Data contextualization
             - Summary delivery

[Future]: GPT-4o vision capabilities for image analysis
```

## References

- **Primary Source**: [Leveraging RAG-powered LLMs for analytical tasks](https://engineering.grab.com/transforming-the-analytics-landscape-with-RAG-powered-LLM)
- **Authors**: Edmund Hong, Yi Ni Ong (Grab Integrity Analytics Team)
- **Contributors**: Meichen Lu, Jia Long Loh, Pu Li
- **Date**: October 2024

## Tags

`rag` `analytics` `report-generation` `fraud-detection` `production` `llm` `api-middleware` `slack-integration`
