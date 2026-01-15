import re
import json

def parse_transcript_line(line):
    """Parse a single line of transcript and extract key information"""
    # Keywords to look for
    feature_keywords = ['feature', 'functionality', 'capability', 'should be able to', 'need to', 'want to', 'requirement']
    decision_keywords = ['decision', 'decided', 'we\'ll go with', 'let\'s do', 'agreed']
    question_keywords = ['question', 'not sure', 'unclear', 'TBD', 'to be decided', 'need to figure out', 'don\'t know']
    api_keywords = ['API', 'endpoint', 'service', 'integration', 'Byte API', 'REST']
    workflow_keywords = ['workflow', 'process', 'step', 'then', 'after that', 'when']

    # Split by speaker
    speaker_pattern = r'([A-Za-z\s]+)\s+(\d{1,2}:\d{2}:\d{2}|\d{1,2}:\d{2})(.*?)(?=[A-Za-z\s]+\s+\d{1,2}:\d{2}|\Z)'

    results = {
        'features': [],
        'decisions': [],
        'questions': [],
        'api_mentions': [],
        'workflows': []
    }

    # Find all speaker segments
    segments = re.finditer(speaker_pattern, line, re.DOTALL)

    for match in segments:
        speaker = match.group(1).strip()
        timestamp = match.group(2).strip()
        text = match.group(3).strip() if len(match.groups()) > 2 else ''

        text_lower = text.lower()

        # Check for features
        for keyword in feature_keywords:
            if keyword in text_lower and len(text) > 20:
                results['features'].append({
                    'speaker': speaker,
                    'time': timestamp,
                    'text': text[:500]  # Limit length
                })
                break

        # Check for decisions
        for keyword in decision_keywords:
            if keyword in text_lower and len(text) > 20:
                results['decisions'].append({
                    'speaker': speaker,
                    'time': timestamp,
                    'text': text[:500]
                })
                break

        # Check for questions/issues
        for keyword in question_keywords:
            if keyword in text_lower and len(text) > 20:
                results['questions'].append({
                    'speaker': speaker,
                    'time': timestamp,
                    'text': text[:500]
                })
                break

        # Check for API mentions
        for keyword in api_keywords:
            if keyword in text_lower and len(text) > 20:
                results['api_mentions'].append({
                    'speaker': speaker,
                    'time': timestamp,
                    'text': text[:500]
                })
                break

        # Check for workflow descriptions
        for keyword in workflow_keywords:
            if keyword in text_lower and len(text) > 30:
                results['workflows'].append({
                    'speaker': speaker,
                    'time': timestamp,
                    'text': text[:500]
                })
                break

    return results

def analyze_file(input_path, output_path):
    """Analyze a transcript file and extract key information"""
    print(f"Analyzing {input_path}...")

    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()

    results = parse_transcript_line(content)

    # Write results
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("=" * 80 + "\n")
        f.write(f"ANALYSIS OF {input_path}\n")
        f.write("=" * 80 + "\n\n")

        f.write(f"\nFEATURES MENTIONED ({len(results['features'])} items):\n")
        f.write("-" * 80 + "\n")
        for item in results['features'][:50]:  # Limit to first 50
            f.write(f"[{item['time']}] {item['speaker']}: {item['text']}\n\n")

        f.write(f"\nDECISIONS MADE ({len(results['decisions'])} items):\n")
        f.write("-" * 80 + "\n")
        for item in results['decisions'][:50]:
            f.write(f"[{item['time']}] {item['speaker']}: {item['text']}\n\n")

        f.write(f"\nOPEN QUESTIONS/ISSUES ({len(results['questions'])} items):\n")
        f.write("-" * 80 + "\n")
        for item in results['questions'][:50]:
            f.write(f"[{item['time']}] {item['speaker']}: {item['text']}\n\n")

        f.write(f"\nAPI/INTEGRATION MENTIONS ({len(results['api_mentions'])} items):\n")
        f.write("-" * 80 + "\n")
        for item in results['api_mentions'][:50]:
            f.write(f"[{item['time']}] {item['speaker']}: {item['text']}\n\n")

        f.write(f"\nWORKFLOW DESCRIPTIONS ({len(results['workflows'])} items):\n")
        f.write("-" * 80 + "\n")
        for item in results['workflows'][:30]:
            f.write(f"[{item['time']}] {item['speaker']}: {item['text']}\n\n")

    print(f"Analysis written to {output_path}")
    return results

# Analyze both files
results1 = analyze_file(
    r'C:\Users\Mark Hansen\Desktop\saro\transcripts\part1_extracted.txt',
    r'C:\Users\Mark Hansen\Desktop\saro\transcripts\part1_analysis.txt'
)

results2 = analyze_file(
    r'C:\Users\Mark Hansen\Desktop\saro\transcripts\part2_extracted.txt',
    r'C:\Users\Mark Hansen\Desktop\saro\transcripts\part2_analysis.txt'
)

print("\nAnalysis complete!")
print(f"Part 1: {len(results1['features'])} features, {len(results1['decisions'])} decisions, {len(results1['questions'])} questions")
print(f"Part 2: {len(results2['features'])} features, {len(results2['decisions'])} decisions, {len(results2['questions'])} questions")
