# Meta AI for Efficient Incident Response

**Source**: [Meta Engineering Blog - Leveraging AI for efficient incident response](https://engineering.fb.com/2024/06/24/data-infrastructure/leveraging-ai-for-efficient-incident-response/)
**Authors**: Diana Hsu, Michael Neu, Mohamed Farrag, Rahul Kindi
**Date**: June 24, 2024
**Category**: Development & Engineering

## Problem

Investigation is a critical part of ensuring system reliability at Meta and a prerequisite to mitigating issues quickly. However, investigating anomalies presents significant challenges:

**Investigation Challenges:**
- **Every investigation is unique**: Identifying the root cause is necessary to mitigate properly
- **Monolithic repository scalability**: Accumulating number of changes across many teams makes investigations complex
- **Context building overhead**: Responders need to build context on what is broken, which systems are involved, and who might be impacted
- **Large search space**: Thousands of potential code changes to review
- **Time-consuming process**: Complex and lengthy investigations delay mitigation

The challenge was particularly acute for systems dependent on monolithic repositories where the volume of changes and cross-team dependencies create a massive search space for root cause identification.

## Solution

Meta developed an **AI-assisted root cause analysis system** that streamlines investigations through a combination of heuristic-based retrieval and large language model (LLM)-based ranking to speed up root cause identification.

### Two-Stage Approach

#### Stage 1: Heuristics-Based Retriever

Reduces the search space from **thousands of changes to a few hundred** without significant reduction in accuracy using:
- Code and directory ownership analysis
- Runtime code graph exploration of impacted systems
- Other novel heuristics specific to Meta's infrastructure

**Purpose**: Intelligent filtering to maintain high recall while dramatically reducing the search space.

#### Stage 2: LLM-Based Ranker

Once the search space is reduced to a few hundred changes, the system uses a **fine-tuned Llama 2 (7B) model** to further reduce to the **top 5 most likely root causes**.

**Ranking Through Election:**
- Structures prompts to contain maximum of 20 changes at a time
- Asks LLM to identify top 5 changes from each batch
- Aggregates outputs across LLM requests
- Repeats process until only 5 candidates remain

**Key Innovation**: This election-based approach accommodates context window limitations while enabling the model to reason across different changes effectively.

### Training Process

The biggest lever to achieving high accuracy was **fine-tuning a Llama 2 (7B) model** using historical investigations with known root causes.

#### Continued Pre-Training (CPT)
- Used limited and approved internal wikis, Q&As, and code
- Exposed model to Meta-specific artifacts and terminology
- Built foundation for understanding Meta's infrastructure

#### Supervised Fine-Tuning (SFT)
- Mixed Llama 2's original SFT data with internal context
- Created dedicated investigation root cause analysis (RCA) SFT dataset
- Taught model to follow RCA instructions

**RCA SFT Dataset:**
- ~5,000 instruction-tuning examples
- Details of 2-20 changes from retriever
- Known root cause included
- Information available at investigation start (title, observed impact)
- Intentionally limited information density to match real-world scenarios

**Advanced Fine-Tuning for Ranked Lists:**
- Gathered model's log probabilities (logprobs) for each possible culprit
- Ranked search space based on relevancy to given investigation
- Created fine-tuning examples where model yields ranked list of potential code changes
- Expected root cause appears first in ranked output
- Re-ran SFT with this augmented dataset to enable proper ranking behavior

## Impact

### Accuracy Metrics
- **42% accuracy** in identifying root causes for investigations at their creation time (related to web monorepo)
- Root cause appears in **top 5 suggested code changes** for 42% of backtested investigations
- Based on exhaustive backtesting with historical investigations and information available at their start

### Time Savings
- Significantly reduced effort and time needed to root cause an investigation
- Streamlined onboarding of engineers to investigations
- Accelerated root cause isolation process

### Operational Impact
- Production deployment at Meta scale
- Integrated into internal investigation tools
- Used alongside existing tools like Hawkeye (end-to-end ML workflow debugging)

## Key Insights

1. **Two-Stage Retrieval Works**: Combining heuristic-based filtering (thousands → hundreds) with LLM-based ranking (hundreds → top 5) provides optimal balance of recall and precision.

2. **Election-Based Ranking Handles Context Limits**: Processing 20 changes at a time and aggregating results enables reasoning across large candidate sets despite context window limitations.

3. **Fine-Tuning is Critical**: The biggest performance lever was fine-tuning on ~5,000 historical investigations with known root causes, not just using pre-trained models.

4. **Limited Information Training Matches Reality**: Training on intentionally sparse information (what's known at investigation start) makes the model perform better in real-world scenarios.

5. **Log Probabilities Enable Ranking**: Using logprobs to rank relevancy and training the model to produce ranked lists significantly improved output quality.

6. **Closed Feedback Loops for Trust**: Ensuring responders can independently reproduce results validates AI suggestions and prevents misleading recommendations.

7. **Precision Over Reach**: Using confidence measurement methodologies to detect low confidence answers—sacrificing reach in favor of precision—maintains trust.

8. **Domain-Specific Training Matters**: Continued pre-training on internal wikis, Q&As, and code exposed the model to Meta-specific context, improving performance on Meta infrastructure.

## Risk Mitigation

The team identified key risks and implemented mitigations:

**Risk: Wrong Root Cause Suggestions**
- **Mitigation**: Prioritize closed feedback loops and explainability
- Ensure responders can independently reproduce results
- Validate AI-generated results before acting

**Risk: Low Confidence Answers**
- **Mitigation**: Confidence measurement methodologies
- Avoid recommending low-confidence results
- Sacrifice reach in favor of precision

**Risk: Over-Reliance on AI**
- **Mitigation**: AI assists but doesn't replace human judgment
- Responders maintain control of investigation process
- AI suggestions are starting points, not final answers

## What's Next

### Autonomous Workflows
- Expanding AI capabilities to autonomously execute full workflows
- AI systems validate their own results
- Reduced need for human intervention in routine investigations

### Proactive Incident Detection
- Detect potential incidents prior to code push
- Proactively mitigate risks before they arise
- Shift from reactive investigation to preventive detection

### Broader Integration
- Expand beyond web monorepo to other systems
- Integrate deeper into existing investigation tooling
- Scale AI-assisted investigation across Meta's infrastructure

## Technical Stack

- **LLM**: Fine-tuned Llama 2 (7B) model
- **Training Data**: ~5,000 instruction-tuning examples from historical investigations
- **Training Process**: Continued pre-training (CPT) + supervised fine-tuning (SFT)
- **Ranking Algorithm**: Election-based ranking with max 20 changes per prompt
- **Retrieval**: Novel heuristics-based retrieval (code ownership, runtime code graph analysis)
- **Integration**: Internal investigation tooling, Hawkeye debugging system

## Training Dataset Composition

**RCA SFT Dataset Structure:**
- Investigation title and observed impact
- 2-20 code changes from retriever
- Known root cause (for training)
- Change metadata (author, timestamp, affected files, etc.)
- Ranked list format with logprobs

**Fine-Tuning Data Sources:**
- Llama 2's original SFT data (base instruction-following)
- Internal context (wikis, Q&As, code)
- Historical RCA investigations (~5,000 examples)
- Ranked list examples (augmented dataset)

---

**Tags**: AI-Assisted Investigation, Root Cause Analysis, LLM, Llama, Fine-Tuning, Incident Response, System Reliability, Heuristic Retrieval, Production System, Meta Infrastructure

**Related Examples**:
- Other AI-assisted development and debugging tools
- LLM-based code analysis systems
- Incident response automation platforms
