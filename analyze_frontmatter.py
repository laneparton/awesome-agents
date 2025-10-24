#!/usr/bin/env python3
"""
Analyze frontmatter completeness across all example files.
"""
import os
import re
from pathlib import Path
from collections import defaultdict
import json

# Expected schema fields based on the best examples
EXPECTED_FIELDS = {
    'metadata': ['title', 'company', 'author', 'source', 'date', 'category', 'tags', 'description'],
    'problem': ['problemPattern', 'problemComplexity'],
    'architecture': ['architecture.type', 'architecture.pattern', 'architecture.rationale', 'architecture.components'],
    'breakthrough': ['breakthroughInsight', 'criticalConstraints', 'antiPatterns'],
    'tech': ['techStack.framework', 'techStack.llmProvider', 'techStack.knowledgeRetrieval', 'techStack.otherTools'],
    'scale': ['scale.volume', 'scale.latency']
}

def extract_frontmatter(file_path):
    """Extract YAML frontmatter from markdown file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find frontmatter between --- markers
    match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return None

    return match.group(1)

def parse_yaml_simple(yaml_content):
    """Simple YAML parser for frontmatter."""
    result = {}
    lines = yaml_content.split('\n')
    current_key = None
    current_indent = 0
    nested_path = []

    for line in lines:
        if not line.strip() or line.strip().startswith('#'):
            continue

        # Get indent level
        indent = len(line) - len(line.lstrip())

        # Check if it's a key-value pair
        if ':' in line:
            parts = line.split(':', 1)
            key = parts[0].strip()
            value = parts[1].strip() if len(parts) > 1 else ''

            # Update nested path based on indent
            if indent == 0:
                nested_path = [key]
            elif indent > current_indent:
                nested_path.append(key)
            elif indent == current_indent:
                nested_path[-1] = key
            else:
                # Going back up the tree
                while len(nested_path) > 1 and indent <= current_indent:
                    nested_path.pop()
                    current_indent -= 2
                nested_path[-1] = key

            # Store the value
            if value and value != '':
                full_key = '.'.join(nested_path)
                result[full_key] = value.strip('"\'')

            current_indent = indent
            current_key = key
        elif line.strip().startswith('-'):
            # It's a list item
            if current_key:
                full_key = '.'.join(nested_path)
                if full_key not in result:
                    result[full_key] = []
                result[full_key].append(line.strip()[1:].strip().strip('"\''))

    return result

def check_field_completeness(frontmatter):
    """Check which expected fields are present and which are missing."""
    missing = defaultdict(list)
    present = defaultdict(list)

    for category, fields in EXPECTED_FIELDS.items():
        for field in fields:
            if field in frontmatter and frontmatter[field]:
                present[category].append(field)
            else:
                missing[category].append(field)

    return present, missing

def analyze_files(examples_dir):
    """Analyze all example files for frontmatter completeness."""
    results = []

    # Find all markdown files except READMEs
    for root, dirs, files in os.walk(examples_dir):
        for file in files:
            if file.endswith('.md') and file != 'README.md':
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, examples_dir)

                # Extract frontmatter
                frontmatter_text = extract_frontmatter(file_path)
                if not frontmatter_text:
                    results.append({
                        'file': rel_path,
                        'status': 'NO_FRONTMATTER',
                        'missing': EXPECTED_FIELDS
                    })
                    continue

                # Parse frontmatter
                frontmatter = parse_yaml_simple(frontmatter_text)

                # Check completeness
                present, missing = check_field_completeness(frontmatter)

                # Calculate completeness score
                total_fields = sum(len(fields) for fields in EXPECTED_FIELDS.values())
                present_count = sum(len(fields) for fields in present.values())
                completeness = (present_count / total_fields) * 100

                results.append({
                    'file': rel_path,
                    'status': 'OK' if completeness == 100 else 'INCOMPLETE',
                    'completeness': round(completeness, 1),
                    'present': dict(present),
                    'missing': dict(missing)
                })

    return results

def generate_report(results):
    """Generate a human-readable report."""
    print("=" * 80)
    print("FRONTMATTER COMPLETENESS ANALYSIS")
    print("=" * 80)
    print()

    # Summary statistics
    total = len(results)
    complete = sum(1 for r in results if r['status'] == 'OK')
    incomplete = sum(1 for r in results if r['status'] == 'INCOMPLETE')
    no_frontmatter = sum(1 for r in results if r['status'] == 'NO_FRONTMATTER')

    avg_completeness = sum(r.get('completeness', 0) for r in results) / total if total > 0 else 0

    print(f"Total Files: {total}")
    print(f"Complete (100%): {complete}")
    print(f"Incomplete: {incomplete}")
    print(f"No Frontmatter: {no_frontmatter}")
    print(f"Average Completeness: {avg_completeness:.1f}%")
    print()

    # Sort by completeness (ascending) to show worst offenders first
    sorted_results = sorted(results, key=lambda x: x.get('completeness', 0))

    print("=" * 80)
    print("FILES NEEDING ATTENTION (sorted by completeness)")
    print("=" * 80)
    print()

    for result in sorted_results:
        if result['status'] != 'OK':
            print(f"📄 {result['file']}")
            print(f"   Status: {result['status']}")
            if 'completeness' in result:
                print(f"   Completeness: {result['completeness']}%")

            if result['status'] == 'INCOMPLETE' and 'missing' in result:
                print(f"   Missing fields:")
                for category, fields in result['missing'].items():
                    if fields:
                        print(f"      {category}: {', '.join(fields)}")

            print()

    # Generate summary of most common missing fields
    print("=" * 80)
    print("MOST COMMON MISSING FIELDS")
    print("=" * 80)
    print()

    field_missing_count = defaultdict(int)
    for result in results:
        if 'missing' in result:
            for category, fields in result['missing'].items():
                for field in fields:
                    field_missing_count[field] += 1

    sorted_missing = sorted(field_missing_count.items(), key=lambda x: x[1], reverse=True)
    for field, count in sorted_missing[:15]:
        pct = (count / total) * 100
        print(f"  {field}: {count} files ({pct:.1f}%)")

    print()

    # Save detailed JSON report
    output_file = '/Users/laneparton/Projects/Personal/awesome-agents/frontmatter_analysis.json'
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)

    print(f"Detailed JSON report saved to: {output_file}")

if __name__ == '__main__':
    examples_dir = '/Users/laneparton/Projects/Personal/awesome-agents/examples'
    results = analyze_files(examples_dir)
    generate_report(results)
