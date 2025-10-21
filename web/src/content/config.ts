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
      'document-processing-at-scale',
      'multi-source-research',
      'workflow-automation',
      'framework-platform-building',
      'structured-data-extraction',
      'content-discovery',
    ]).optional(),
    problemComplexity: z.enum(['simple', 'moderate', 'complex']).optional(),

    // Architecture insights
    architecture: z.object({
      type: z.enum(['single-agent', 'multi-agent', 'event-driven', 'hybrid']),
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
