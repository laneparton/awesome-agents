import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const examples = defineCollection({
  loader: glob({
    pattern: ['**/*.md', '!**/README.md'],
    base: '../examples',
  }),
  schema: z.object({
    title: z.string(),
    company: z.string().optional(),
    author: z.string().optional(),
    source: z.string().url().optional(),
    date: z.string().optional(),
    category: z.string(),
    tags: z.array(z.string()).optional(),
    description: z.string().optional(),
  }),
});

export const collections = { examples };
