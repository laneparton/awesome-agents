---
title: "Duolingo DuoRadio - Scaling Content Generation with Generative AI"
category: "Content Creation"
company: "Duolingo"
author: "Luis Mas Castillo, Sophie Mackey, Cindy Berger"
source: "https://blog.duolingo.com/scaling-duoradio/"
date: "March 11, 2025"
---

# Duolingo DuoRadio - Scaling Content Generation with Generative AI

**Source**: [Duolingo Engineering Blog - Using generative AI to scale DuoRadio 10x faster](https://blog.duolingo.com/scaling-duoradio/)
**Authors**: Luis Mas Castillo, Sophie Mackey, Cindy Berger
**Date**: March 11, 2025
**Category**: Content Creation

## Problem

DuoRadio is an audio experience that improves listening comprehension through short, podcast-like radio shows featuring Duolingo's beloved World characters. While the feature had enormous learning potential, its reach was severely limited by a labor-intensive production process.

**The Scaling Challenge:**
- **Nearly a year to produce just 300 episodes** for a handful of courses
- Each episode demanded meticulous scripting, precise alignment with curriculum goals, voice actors, and specialized audio editing
- **Initial AI attempts failed**: Generating original scripts produced subpar results requiring extensive manual editing; automated translations frequently missed the mark on accuracy and proficiency level
- As a result, **only a small percentage of learners had access** to this listening content
- The manual process made it impossible to scale to the broader Duolingo community

## Solution

During a Duolingo Hackathon, a team of Product Managers and Learning Designers discovered a breakthrough approach: **instead of asking generative AI to create original content with complex instructions, feed it existing curriculum content to give it specific patterns to follow**.

### The Hackathon Breakthrough

**Key Discovery**: Feeding existing content from Duolingo's learning curriculum (well-crafted sentences and exercises created by Learning Designers) to generative AI produced far better results than adding more constraints to prompts.

**Quality Control**: The team created comprehensive evaluator prompts that assessed AI-generated outputs for naturalness, grammaticality, coherence, logic, and other key learning criteria. Only scripts that passed through these filters met quality standards.

**Validation**: After the Hackathon, they used Workflow Builder (Duolingo's internal content generation prototyping tool) to automatically generate DuoRadio content at scale and demoed it to leadership, proving automation could maintain quality while significantly increasing coverage.

### DuoRadio's Scaling Formula

The production system consists of five key components:

#### 1. Curriculum-Driven AI Script Generation
- Leveraged language-specific content from each course curriculum
- English-only generative AI prompt instructions were less effective
- Using curriculum content dramatically improved accuracy and relevance

#### 2. Exercise Standardization
- Initially, AI prompts had freedom to sequence and place exercises, but quality was hit or miss
- Leveraged learner session data to place exercises optimally within episodes
- Standardizing exercise order and placement kept session structure consistent and made automation more reliable

#### 3. Comprehensive Evaluators
- Generated many potential episodes, then filtered using AI-powered evaluation
- Evaluators assessed scripts on naturalness, grammaticality, coherence, logic, etc.
- Learning Designers refined evaluator prompts over time to continuously improve content quality
- Only the best scripts made it to learners

#### 4. Automated Audio Production
- **Advanced Text-to-Speech (TTS)**: Automatically created lifelike voiceovers in multiple languages
- **Audio hashing**: Technique for quickly storing and retrieving pre-generated audio, ensuring consistent intros and outros
- Dramatically reduced manual editing time

#### 5. End-to-End Generation Pipelines
- Built pipelines to automate entire lifecycle from script creation to final deployment
- **Zero human intervention post-initiation**
- Enabled DuoRadio to scale at a pace once thought impossible

## Impact

### Reaching More Learners Faster
- **DuoRadio daily sessions grew from 500K to 5M in fewer than 6 months**
- Brought immersive listening practice to millions more people learning with Duolingo

### Course Content Expansion
- Increased from **2 to 25+ courses**
- Episodes expanded from **300 to 15,000+**
- **99% cost savings** compared to manual production
- What would have taken **5+ years took fewer than two quarters**

### More Episodes Per Unit
- Automation allowed for more episodes per unit
- Team could focus on developing wider range of DuoRadio show concepts
- Learners exposed to more DuoRadio nodes
- Each episode remained engaging and reflective of Duolingo's curriculum

## Key Insights

1. **Patterns over Prompts**: Adding more constraints on generative AI prompts didn't work well. Feeding existing curriculum content gave AI specific patterns to follow, which was more effective than complex instructions.

2. **Generate Many, Filter to Best**: The solution wasn't to make AI generate perfect content on first try, but to generate many potential episodes and use AI-powered filtering to keep only the highest quality.

3. **Iterative Refinement**: Learning Designers continuously refined evaluator prompts over time, raising the quality bar with each iteration.

4. **Expert Oversight**: Success came from balancing automation with expert oversight - generative AI for scale, Learning Designers for quality control.

5. **Structured Evaluation**: Creating systematic evaluation criteria (naturalness, grammaticality, coherence, logic) enabled consistent quality assessment at scale.

6. **Curriculum as Foundation**: Using well-crafted curriculum content as the foundation ensured scripts were level-appropriate, grammatically sound, and used correct vocabulary.

## What's Next

**Improving DuoRadio**: Refining session length and exercise variety to ensure each episode stays fresh, engaging, and effective.

**Expanding Longform Content**: Integrating more longform content into more courses, giving learners various ways to build language skills through immersive and context-rich experiences.

## Technical Stack

- **Workflow Builder**: Duolingo's internal content generation prototyping tool
- **Generative AI**: For script generation and quality evaluation
- **Text-to-Speech (TTS)**: Advanced TTS for multi-language voiceover generation
- **Audio Hashing**: Efficient audio storage and retrieval system
- **End-to-End Pipelines**: Automated deployment infrastructure

---

**Tags**: Content Generation, Generative AI, Text-to-Speech, Quality Filtering, Curriculum Design, Audio Production, Hackathon, Production System

**Related Examples**:
- Other content generation examples using generative AI
- Educational content automation systems
