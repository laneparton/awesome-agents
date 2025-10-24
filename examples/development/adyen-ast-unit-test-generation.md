---
title: "Adyen AST-Based Unit Test Generation with LLMs"
category: "Development & Engineering"
company: "Adyen"
date: "March 2024"
---

# Adyen AST-Based Unit Test Generation with LLMs

**Company**: Adyen
**Domain**: Development & Engineering
**Published**: March 2024

## Problem

Writing unit tests is often a downplayed aspect of software development, yet it's crucial for maintaining code quality. The challenge intensifies in large, complex codebases where understanding context is essential:

- **Simple cases work**: Tools like GitHub Copilot excel at generating boilerplate code for straightforward functions without external dependencies
- **Complex integration fails**: Creating unit tests for code deeply integrated into large frameworks requires understanding how segments interact with the overall architecture
- **Context is everything**: A method doesn't exist in isolation - it has dependencies, interacts with other system parts, and relies on implicit logic not visible in the method itself

Traditional approaches using vector embeddings and conventional RAG struggle with code because:
- They miss context-specific subtleties crucial for identifying precise code snippets
- The same code snippet can have different meanings depending on placement and context
- They can't map state changes and dependency structures integral to programming
- Surface-level semantic similarities don't capture the logical and structural essence of code

## Solution

Adyen developed an **AST (Abstract Syntax Tree) and Knowledge Graph-based approach** for augmented unit test generation that moves beyond text-based code representations to understand programming logic and structure.

### How It Works

**Abstract Syntax Tree (AST) Parsing:**

Rather than treating code as linear text, ASTs provide a hierarchical structural representation where each node corresponds to specific code constructs:
- Clear overview of variable scope
- Sequence of function calls
- Nesting of conditional statements
- Patterns and structures not apparent in raw source code

**Knowledge Graph Construction:**

Building on ASTs, Knowledge Graphs represent the codebase as entities (variables, functions, classes) and their interrelations as nodes and edges:
- Dependencies and inheritance hierarchies are explicit
- Data-flow and control-flow interactions between variables are labeled
- Transform traditional AST into a directed multigraph
- Semantic layer complements syntactic AST representation

**Graph Database Storage:**

Processed code is stored in a graph database, enabling:
- Sophisticated queries considering both structural and semantic relationships
- Insights into functionality and dependencies crucial for code generation
- Moving beyond semantic similarity search to actual relational understanding

### Impact

- **Tested and proven** on Adyen's open-source products
- **Solves the context problem**: Enables LLMs to understand "invisible" logic in code through proper snippet selection
- **Higher accuracy**: Graph-based approach captures interconnected nature of code elements that embeddings miss
- **Planned internal deployment**: Building on open-source success to create internal tool for main source code
- **Developer productivity**: Frees teams to engage in complex, rewarding work by automating routine test generation

## Key Insights

### 1. Vector Embeddings Fail for Code Context

While vector embeddings excel at text generation, they encounter critical challenges in code:
- **Context-dependent semantics**: The same line of code assumes different functionalities based on placement, paradigm, or interactions
- **State and dependencies**: Fixed vector representations can't capture dynamic state changes and dependency structures
- **Surface-level only**: Embeddings capture textual similarities but miss architectural essence of code

The complexities of imports, hierarchies, sequences, and interdependencies require going beyond lexical analysis to comprehend programming logic and structure.

### 2. AST + Knowledge Graphs = Holistic Understanding

The combination provides complementary views:
- **AST handles syntax**: Structural representation of code constructs
- **KG adds semantics**: Relationships, dependencies, and inheritance hierarchies
- **Together**: Syntactic correctness + functional intent + contextual understanding

In object-oriented programming, this technique maps out class and object relationships for in-depth contextual understanding that LLMs can leverage.

### 3. Graph Queries Beat Similarity Search

Storing code in a graph database rather than relying on vector similarity search:
- Captures interconnected nature of code elements
- Enables queries that consider structural AND semantic relationships
- Provides insights into functionality dependencies crucial for accurate generation
- Moves from "similar text" to "actual logical connections"

### 4. Augment, Don't Just Automate

The goal isn't merely to automate test generation but to augment it - maintaining high-quality standards with consistency across all tests while minimizing variability of manual processes. The system functions as a partner in assuring quality, not just a productivity tool.

### 5. Separate Concerns from Text Generation

Code generation requires precision, context-sensitivity, and logic-driven understanding - distinct from text generation which relies on broader contexts and language patterns. This necessitates specialized approaches beyond general-purpose RAG architectures.

## Technical Architecture

```
Source Code
     ↓
[AST Parsing]
- Hierarchical structural representation
- Nodes = code constructs
- Scope, calls, nesting captured
     ↓
[Knowledge Graph Construction]
- Entities (vars, functions, classes) = nodes
- Relations (dependencies, inheritance) = edges
- Data-flow and control-flow labels
- Directed multigraph representation
     ↓
[Graph Database Storage]
- Structural + semantic relationships
- Sophisticated relational queries
- Context-aware code retrieval
     ↓
[LLM Integration]
- Receives relevant code snippets with full context
- Understands "invisible" logic
- Generates context-aware unit tests
     ↓
Augmented Unit Test Generation
```

## Future Vision

Adyen plans to:
1. **Internal tool deployment**: Leverage open-source success to build internal tool for main source code
2. **Self-hosted LLM**: Combine AST/KG approach with fine-tuned self-hosted LLM tailored to Adyen's environment
3. **Productivity boost**: Enable developers to focus on creative and innovative tasks
4. **Quality elevation**: Enhance reliability of platform through better automated testing

## References

- **Primary Source**: [Elevating Code Quality Through LLM Integration](https://www.adyen.com/knowledge-hub/elevating-code-quality-through-llm-integration)
- **Author**: Rok Popov Ledinski (Software Engineer, Adyen)
- **Date**: March 2024
- **Related Research**: [Open Vocabulary Learning on Source Code with a Graph-Structured Cache](https://proceedings.mlr.press/v139/hellendoorn21a.html)

## Tags

`code-generation` `knowledge-graphs` `ast-parsing` `testing` `graph-database` `llm` `code-analysis` `developer-tools`
