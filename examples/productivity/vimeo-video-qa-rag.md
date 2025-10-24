---
title: "Vimeo Video Q&A with RAG"
company: "Vimeo"
author: "Alon Faktor, Yedidya Hyams, Naama Ben-Dor"
source: "https://medium.com/vimeo-engineering-blog/unlocking-knowledge-sharing-for-videos-with-rag-810ab496ae59"
date: "2024-07"
category: "productivity"
tags: ["rag", "video-processing", "semantic-search", "transcript-analysis", "production", "embeddings", "multi-level-retrieval"]
description: "Multi-level RAG system for video Q&A with bottom-up processing (100-500 word chunks), speaker detection via conversation transitions, and timestamp-precise moment navigation without facial recognition"

# Problem Classification
problemPattern: "knowledge-retrieval"
problemComplexity: "medium"

# Architecture
architecture:
  type: "single-agent"
  pattern: "multi-level-rag"
  rationale: "Bottom-up processing with multiple granularities (100, 200, 500 words, full video summary) stored in single vector database enables answering all question types - general overviews, speaker-specific queries, and specific detail requests - from one unified system"
  components: ["transcript-processor", "multi-level-chunker", "vector-database", "speaker-detector", "two-prompt-answer-system", "question-generator"]

# What Made It Work
breakthroughInsight: "Multi-level bottom-up processing creates different granularity chunks enabling single RAG system to answer all question types; speaker names detected from conversation transitions (where names naturally appear during handovers) without facial recognition; separating answer generation from quote extraction into two prompts improves both accuracy and source attribution"

criticalConstraints:
  - "long-video-content"
  - "multi-speaker-conversations"
  - "precise-timestamp-navigation"
  - "no-facial-recognition"
  - "question-variety-general-to-specific"
  - "speaker-attribution-accuracy"

antiPatterns:
  - "single-prompt-answer-and-reference: Combining question answering with quote extraction in one prompt degraded performance with ChatGPT 3.5 - separating into two prompts improved both tasks"
  - "facial-recognition-dependency: Privacy concerns and technical complexity avoided through textual transition analysis where speaker names naturally appear during conversation handovers"
  - "single-granularity-chunking: Fixed chunk size can't handle both general overview questions and specific detail questions effectively - multi-level approach (100, 200, 500 words) essential"
  - "open-world-question-generation: Generating related questions without RAG context leads to unanswerable questions - grounding in retrieved video content ensures questions are actually answerable"

# Tech Stack
techStack:
  framework: "custom-rag"
  llmProvider: "LLM-based"
  knowledgeRetrieval: "multi-level-rag"
  otherTools: ["vector-database", "automatic-transcription", "audio-clustering", "embeddings", "masking-prompts", "voting-mechanism"]

# Scale
scale:
  volume: "Production deployment on Vimeo platform for video Q&A and previews"
  latency: "Instant summaries and timestamp-precise moment navigation"
---

# Vimeo Video Q&A with RAG

**Company**: Vimeo
**Domain**: Productivity & Automation
**Published**: July 2024

## Problem

Viewers often need specific information from videos but don't have time to watch lengthy content in its entirety. Consider a 15-minute video like Steve Jobs' Stanford Commencement Address - a viewer might need a summary or want to find a specific topic discussed without watching the full video.

For knowledge-sharing videos (meetings, lectures, presentations, tutorials), this problem becomes even more acute. Viewers need to:
- Quickly understand what a video covers without watching
- Find specific details or moments within long recordings
- Navigate directly to relevant sections based on questions
- Understand who said what in multi-speaker discussions

The traditional approach requires manual scrubbing through timelines and watching segments to find information, wasting significant time.

## Solution

Vimeo developed a **video Q&A system** that enables viewers to converse with video content in natural language using Retrieval Augmented Generation (RAG). The system allows viewers to ask questions about a video and receive textual answers along with relevant playable moments cued to exact timestamps.

### How It Works

**Bottom-Up Transcript Processing:**

The system processes video transcripts (from Vimeo's automatic closed captions) using a multi-level approach:

1. **Bottom Level (100-200 words)**: Standard chunking of transcript into 1-2 minute segments
2. **Middle Level (500 words)**: LLM summarizes larger chunks to 100 words, focusing on specific details, numbers, dates, and speaker names
3. **Top Level (Video Description)**: Combines all summaries to generate a high-level video description focusing on main topics

All levels are embedded and stored in a vector database with original transcript timings for precise moment navigation.

**Speaker Detection Without Facial Recognition:**

To handle speaker-specific questions ("What did Rachel say about...?"), Vimeo developed a novel approach that:
- Segments conversation by audio clustering (Speaker 1, Speaker 2, etc.)
- Focuses on conversation transitions where names are most commonly mentioned
- Uses LLM with masking prompts to identify names from context
- Employs voting mechanism across multiple prompts for high-confidence identification
- Avoids assigning names when confidence is low (better than wrong attribution)

**Two-Prompt Answer System:**

Separating answer generation from reference finding proved essential:
1. **First Prompt**: Answers the question using retrieved context
2. **Second Prompt**: Finds relevant quotes and timestamps in original transcript

The system computes similarity between the answer and retrieved matches to ensure extracted quotes align with the response.

**Guided Question Generation:**

To engage viewers who don't know what to ask:
- **Pre-generated questions**: Created during transcript registration using all summary chunks
- **Related questions**: After each answer, system uses RAG to generate follow-up questions that can be answered from the video content

### Impact

- **Production deployment** on Vimeo platform for video previews
- **Instant summaries** of lengthy videos without watching
- **Precise moment navigation** with playable timestamps
- **Multi-level context** handling from specific details to high-level overviews
- **Speaker attribution** in conversations without facial recognition
- **Engagement features** with pre-generated and related questions

## Key Insights

### 1. Bottom-Up Processing for Different Question Types

Users ask three main question types:
- **General**: "What is this video about?" (requires full video context)
- **Speakers**: "What did Speaker X say?" (requires large portions)
- **Specific details**: "What was that metric mentioned?" (requires small chunks)

The bottom-up approach with multiple granularities (100, 200, 500 words, and full summary) enables answering all question types effectively from a single vector database.

### 2. Conversation Transitions Reveal Speaker Names

Rather than using facial recognition, the key insight is that speaker names most commonly appear during conversation transitions - handovers between participants where self-introductions, presentations, and thanks occur. This enables accurate name detection through textual analysis alone.

### 3. Masking and Voting for Robustness

Using four different prompt types with masking (hiding one speaker while analyzing the other) and requiring multiple agreeing votes dramatically reduces misidentification. The system prefers leaving speakers unnamed rather than risking incorrect attribution.

### 4. Separate Tasks for Answer and Reference

Trying to answer questions AND find supporting quotes in a single prompt degraded performance (observed with ChatGPT 3.5). Separating these tasks and using answer-to-context similarity filtering ensures references genuinely support the response.

### 5. RAG for Safe Question Generation

When generating related questions, using RAG to retrieve context based on the answer ensures suggested questions can actually be answered from the video. This avoids the "open-world" problem of generating unanswerable questions.

## Technical Architecture

```
Video Upload → Automatic Transcription
                      ↓
         [Bottom-Up Processing]

Level 1: 100-200 word chunks (specific details)
Level 2: 500→100 word LLM summaries (sections/topics)
Level 3: Full video description (main topics)
                      ↓
         [Vector Database Storage]
     (chunks + embeddings + timings)
                      ↓
    [Parallel: Speaker Detection]
    - Audio clustering → Speaker IDs
    - Transition analysis with masking
    - Multi-prompt voting for names
                      ↓
         [User Question] → Embed
                ↓
    Query Vector Database
                ↓
         Retrieved Context
                ↓
    [Two-Step Answer Process]
    1. Generate answer from context
    2. Find relevant quotes & timestamps
                ↓
    Answer + Playable Moments + Related Questions
```

## References

- **Primary Source**: [Unlocking knowledge sharing for videos with RAG](https://medium.com/vimeo-engineering-blog/unlocking-knowledge-sharing-for-videos-with-rag-810ab496ae59)
- **Author**: Alon Faktor (Director of AI Research, Vimeo)
- **Team**: Yedidya Hyams, Naama Ben-Dor
- **Date**: July 2024

## Tags

`rag` `video-processing` `semantic-search` `transcript-analysis` `production` `embeddings` `llm` `multi-level-retrieval`
