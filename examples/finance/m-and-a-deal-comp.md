# M&A Deal Comp Generator

**Author**: Jerry Liu

**Source**: [Twitter/X Post](https://x.com/jerryjliu0/status/1980021068158099634)

**Date**: January 2025

**Tags**: `finance` `m&a` `pdf-parsing` `excel-automation` `claude` `llamacloud` `semtools`

## The Problem

Investment analysts and bankers need to create comparable deal analyses for M&A transactions by manually processing SEC DEF 14A filings. Each filing contains critical transaction details buried in complex PDF documents with nested tables, inconsistent formatting, and varied structures.

**The Manual Process:**
- Processing 20-50 M&A filings per project
- 30-45 minutes per filing to extract key metrics (deal value, multiples, terms)
- Manual data entry into Excel spreadsheets
- High risk of human error due to document complexity
- Total time investment: 20-50 hours per deal comp analysis

**Key Pain Points:**
- Complex PDF tables with nested structures
- Inconsistent formatting across different filings
- Easy to miss critical details in lengthy documents
- Tedious, repetitive work that takes analysts away from actual analysis

## The Solution

An AI agent that batch processes SEC DEF 14A filings and automatically generates Excel comparable deal spreadsheets with extracted transaction metrics.

**Impact**: Reduced processing time from 20-50 hours to approximately 5 minutes, with 95% extraction accuracy for key deal metrics.

## How It Works

**Key Technologies:**
- **Claude Code Skills** - Orchestrates the workflow and provides native Excel writing capabilities
- **LlamaIndex Semtools** - Integration layer connecting Claude with LlamaCloud
- **LlamaCloud** - Advanced PDF parsing engine that handles deeply complex financial tables, charts, and documents

**Process Flow:**
1. Input: Directory of public M&A filings (SEC DEF 14A PDFs)
2. LlamaCloud (via Semtools) parses each PDF, handling:
   - Deeply complex financial tables
   - Nested table structures
   - Charts and mixed content
   - Inconsistent formatting across documents
3. Claude analyzes each filing to extract key deal metrics:
   - Deal terms and structure
   - Transaction multiples and valuations
   - Payment terms
   - Key dates and conditions
4. Claude's native Excel skills generate formatted spreadsheet with deal comparables
5. Output: Excel sheet ready for comparative analysis

**Setup Time:** Less than 5 minutes to configure LlamaCloud + Semtools access

## Key Insight

**Native PDF parsing (pypdf) wasn't sufficient for complex financial documents.** The solution was swapping it out with LlamaIndex Semtools, which uses LlamaCloud's advanced parsing capabilities.

**Why This Matters:**
- pypdf (the default parser) struggles with deeply complex financial tables, nested structures, and mixed content
- LlamaCloud's parsing engine is specifically designed to handle complex document layouts
- This parsing quality difference is critical for financial documents where accuracy is non-negotiable
- Combined with Claude's native Excel writing skills, the entire pipeline becomes seamless

**Quick Setup:** The entire LlamaCloud + Semtools integration took less than 5 minutes to configure, demonstrating how modern AI tools can be rapidly composed to solve domain-specific problems.

**Known Issues:** Some values in the generated Excel may appear 100x larger due to percentage formatting (percentages formatted as raw values rather than proper Excel percentages).

## Links

- [Original Tweet](https://x.com/jerryjliu0/status/1980021068158099634) - Jerry Liu's announcement with video demo
- [Semtools GitHub](https://github.com/run-llama/semtools) - LlamaIndex Semtools integration
- [LlamaCloud](https://cloud.llamaindex.ai/) - Advanced PDF parsing service
- [Claude Code Skills](https://docs.anthropic.com/claude/docs/claude-code) - Documentation for Claude Code
