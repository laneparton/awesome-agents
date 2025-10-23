---
title: "Harvard ChatLTV AI Teaching Assistant"
company: "Harvard Business School"
author: "Professor Jeffrey Bussgang"
source: "https://www.linkedin.com/pulse/ai-professor-harvard-chatltv-jeffrey-bussgang-oiaie/"
date: "2023-12"
category: "productivity"
tags: ["rag", "knowledge-retrieval", "customer-support", "production", "enterprise"]
description: "3,000+ queries from 170 students across full semester with RAG-powered Slack chatbot trained on proprietary course corpus, enabling at-scale faculty support and automated project feedback"
---

# Harvard ChatLTV AI Teaching Assistant

## The Problem

Harvard Business School faculty couldn't efficiently answer questions from 250+ students about course material before class. Students had limited access to clarification on case studies, frameworks, and administrative details, while instructors lacked visibility into student understanding and preparation levels.

**The Manual Process:**
- Faculty manually answered questions from 250+ students individually
- Students waited for responses or didn't ask questions at all
- Instructors had no way to gauge overall class preparation
- Final project feedback was impossible to provide at scale due to time constraints
- Traditional office hours and email couldn't scale to meet demand

**Key Pain Points:**
- **Limited faculty availability** - Impossible to answer hundreds of questions before each class
- **Student hesitation** - Many students reluctant to ask "basic" questions publicly
- **No scale for feedback** - Cannot provide personalized critique to 125+ final projects manually
- **Preparation invisibility** - Faculty couldn't see which topics confused students before class

## The Solution

ChatLTV is a Slack-integrated RAG-powered chatbot trained on a proprietary 200-document corpus (15 million words) that provides students instant answers to course questions while giving instructors visibility into class preparation. The system was deployed across a full semester for 250 students.

**Impact**:
- **3,000+ queries** made by ~170 students (57% of cohort actively using)
- **~130 queries per case** across 24 case sessions showing consistent engagement
- **40% of users** rated answer quality as "4" or "5" on 5-point scale
- **99% private usage** - students preferred confidential preparation over public collaboration
- **Custom GPT feedback tool** provided written critique to 125+ final projects with 2-hour setup

## How It Works

**Key Capabilities:**
- **RAG-Based Q&A** - Retrieves relevant context from vector database, generates answers with source citations
- **Slack Integration** - Students ask questions directly in familiar interface without context switching
- **Dual Knowledge Bases** - Separate corpuses for course content and administrative logistics
- **Source Citations** - Every answer includes specific document references for verification
- **Custom GPT Feedback** - Zero-code tool for automated project critiques at scale

**Process Flow:**
1. **Student Query** - Student asks question in Slack channel
2. **Vector Retrieval** - System searches Pinecone vector database for relevant context from 200-document corpus
3. **GPT-4 Generation** - Query + context sent to Azure OpenAI Service (GPT-4) for answer generation
4. **Cited Response** - Answer returned with specific source citations in required format
5. **Faculty Monitoring** - Instructors review question patterns to understand class preparation levels
6. **Feedback Loop** - Manual and automated testing ensures answer quality and reliability

**Technical Architecture:** LangChain middleware connects Slack frontend to Pinecone vector database (15M words) and Azure OpenAI Service (GPT-4). System uses explicit prompting: "You are a world-class algorithm to answer questions in a specific format. You use the context provided to answer the question and list your sources in the format specified. Do not make up answers." Azure deployment protects proprietary HBS content from public model retraining.

**Development Time:** ~2-3 person-months (8,000 backend lines + 9,000-line CMS); professor notes this could be 50% smaller with current tools. Custom GPT for project feedback required zero code—"English is the cool new programming language."

## Key Insight

**RAG systems need manual + automated testing infrastructure for reliability in education.** Harvard built 500 Q&A test sets to validate system accuracy before student deployment, recognizing that unreliable answers would undermine trust more than no answers at all.

**Why This Matters:**
- **Quality over speed** - Testing infrastructure prevented hallucinations that would damage credibility
- **Separate corpuses improve precision** - Splitting course content from administrative content reduced retrieval noise
- **Private access drives adoption** - 99% private usage shows students value confidential preparation space
- **Azure protects IP** - Using Azure OpenAI instead of public APIs prevents proprietary content from entering model training

**Scale Achievement:** System handled 3,000+ queries across 24 case sessions from 170 active users (57% of cohort) throughout full semester. Custom GPT extension provided feedback to 125+ final projects in minutes after 2-hour setup, demonstrating how same RAG infrastructure enables multiple use cases beyond Q&A.

**Long-term Strategy:** Harvard is porting the system to an in-house LLM for sustainability and tighter integration with university systems, showing path from prototype to institutional infrastructure.

## Links

- [Original Source](https://www.linkedin.com/pulse/ai-professor-harvard-chatltv-jeffrey-bussgang-oiaie/) - LinkedIn article by Professor Jeffrey Bussgang describing full implementation and results
