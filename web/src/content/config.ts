import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const examples = defineCollection({
  loader: glob({
    pattern: ['**/*.md', '!**/README.md'],
    base: '../examples',
  }),
  schema: z.object({
    // Required
    title: z.string(),
    category: z.string(),
    description: z.string().optional(),

    // Source metadata
    company: z.string().optional(),
    author: z.string().optional(),
    source: z.string().url().optional(),
    date: z.string().optional(),
    tags: z.array(z.string()).optional(),

    // Problem classification
    problemPattern: z.enum([
      'code-generation',
      'content-discovery',
      'content-generation',
      'customer-support',
      'data-annotation',
      'data-classification',
      'developer-productivity',
      'document-processing-at-scale',
      'framework-platform-building',
      'fraud-detection',
      'knowledge-retrieval',
      'multi-source-research',
      'quality-evaluation',
      'recommendation-system',
      'root-cause-analysis',
      'structured-data-extraction',
      'text-to-query',
      'text-to-sql',
      'workflow-automation',
    ]).optional(),
    problemComplexity: z.enum(['simple', 'moderate', 'complex']).optional(),

    // Architecture insights
    architecture: z.object({
      type: z.enum(['single-agent', 'multi-agent', 'multi-stage-system', 'event-driven', 'hybrid', 'ensemble', 'pipeline']),
      pattern: z.string().optional(),
      rationale: z.string().optional(),
      components: z.array(z.string()).optional(),
    }).optional(),

    // What made it work
    breakthroughInsight: z.string().optional(),
    criticalConstraints: z.array(z.string()).optional(),
    antiPatterns: z.array(z.string()).optional(),

    // Tech stack
    techStack: z.object({
      framework: z.union([z.string(), z.array(z.string())]).optional(),
      llmProvider: z.union([z.string(), z.array(z.string())]).optional(),
      knowledgeRetrieval: z.string().optional(),
      otherTools: z.array(z.string()).optional(),
    }).optional(),

    // Scale
    scale: z.object({
      users: z.number().optional(),
      volume: z.string().optional(),
      latency: z.string().optional(),
    }).optional(),
  }),
});

export const collections = { examples };
