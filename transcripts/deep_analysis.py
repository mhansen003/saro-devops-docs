import re

def extract_detailed_content(file_path):
    """Extract all meaningful dialogue from transcript"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by speaker timestamps
    pattern = r'([A-Za-z\s]+)\s+(\d{1,2}:\d{2}:\d{2})'
    parts = re.split(pattern, content)

    conversations = []
    for i in range(1, len(parts), 3):
        if i+2 < len(parts):
            speaker = parts[i].strip()
            timestamp = parts[i+1].strip()
            text = parts[i+2].strip()

            # Clean up the text
            if len(text) > 50:  # Only include substantive comments
                conversations.append({
                    'speaker': speaker,
                    'time': timestamp,
                    'text': text
                })

    return conversations

def categorize_content(conversations):
    """Categorize conversations by topic"""

    categories = {
        'features': [],
        'api_technical': [],
        'roles_permissions': [],
        'data_model': [],
        'email_functionality': [],
        'document_workflow': [],
        'byte_integration': [],
        'candor_integration': [],
        'open_questions': [],
        'decisions': [],
        'ui_design': [],
        'rollout_strategy': [],
        'audit_logging': []
    }

    for conv in conversations:
        text_lower = conv['text'].lower()

        # Features
        if any(kw in text_lower for kw in ['feature', 'functionality', 'capability', 'need to be able', 'should support']):
            categories['features'].append(conv)

        # API/Technical
        if any(kw in text_lower for kw in ['api', 'endpoint', 'payload', 'schema', 'get condition', 'post', 'byte api']):
            categories['api_technical'].append(conv)

        # Roles/Permissions
        if any(kw in text_lower for kw in ['role', 'permission', 'access', 'processor', 'underwriter', 'loan officer', 'closer', 'funder']):
            categories['roles_permissions'].append(conv)

        # Data Model
        if any(kw in text_lower for kw in ['data model', 'schema', 'field', 'attribute', 'condition list', 'many to many']):
            categories['data_model'].append(conv)

        # Email functionality
        if any(kw in text_lower for kw in ['email', 'template', 'borrower request', 'send', 'tone', 'ai generate', 'signature']):
            categories['email_functionality'].append(conv)

        # Document workflow
        if any(kw in text_lower for kw in ['document', 'upload', 'split', 'merge', 'rotate', 'link', 'clear docs']):
            categories['document_workflow'].append(conv)

        # Byte integration
        if any(kw in text_lower for kw in ['byte', 'los', 'integration', 'sync', 'bidirectional']):
            categories['byte_integration'].append(conv)

        # Candor integration
        if any(kw in text_lower for kw in ['candor', 'ocr', 'aus', 'jina']):
            categories['candor_integration'].append(conv)

        # Open questions/issues
        if any(kw in text_lower for kw in ['question', 'not sure', 'unclear', 'tbd', 'need to figure out', 'don\'t know', 'clarify']):
            categories['open_questions'].append(conv)

        # Decisions
        if any(kw in text_lower for kw in ['decision', 'decided', 'agreed', 'let\'s go with', 'we\'ll do']):
            categories['decisions'].append(conv)

        # UI/Design
        if any(kw in text_lower for kw in ['ui', 'design', 'button', 'screen', 'tab', 'wizard', 'flag', 'filter', 'search']):
            categories['ui_design'].append(conv)

        # Rollout/Beta
        if any(kw in text_lower for kw in ['rollout', 'beta', 'pilot', 'phased', 'production', 'deployment']):
            categories['rollout_strategy'].append(conv)

        # Audit/Logging
        if any(kw in text_lower for kw in ['audit', 'log', 'history', 'track', 'domo', 'report']):
            categories['audit_logging'].append(conv)

    return categories

def write_detailed_report(categories, output_path, part_name):
    """Write a detailed report"""
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("=" * 100 + "\n")
        f.write(f"DETAILED ANALYSIS: {part_name}\n")
        f.write("=" * 100 + "\n\n")

        for category, items in categories.items():
            if items:
                f.write(f"\n{'='*100}\n")
                f.write(f"{category.upper().replace('_', ' ')} ({len(items)} items)\n")
                f.write(f"{'='*100}\n\n")

                for item in items[:100]:  # Limit to prevent huge files
                    f.write(f"[{item['time']}] {item['speaker']}:\n")
                    # Wrap text at reasonable length
                    text = item['text']
                    if len(text) > 800:
                        text = text[:800] + "..."
                    f.write(f"{text}\n\n")
                    f.write("-" * 100 + "\n\n")

# Process Part 1
print("Processing Part 1...")
conv1 = extract_detailed_content(r'C:\Users\Mark Hansen\Desktop\saro\transcripts\part1_extracted.txt')
cat1 = categorize_content(conv1)
write_detailed_report(cat1, r'C:\Users\Mark Hansen\Desktop\saro\transcripts\detailed_part1.txt', "DAY 1 PART 1")
print(f"Part 1: Found {len(conv1)} conversation segments")

# Process Part 2
print("Processing Part 2...")
conv2 = extract_detailed_content(r'C:\Users\Mark Hansen\Desktop\saro\transcripts\part2_extracted.txt')
cat2 = categorize_content(conv2)
write_detailed_report(cat2, r'C:\Users\Mark Hansen\Desktop\saro\transcripts\detailed_part2.txt', "DAY 1 PART 2")
print(f"Part 2: Found {len(conv2)} conversation segments")

print("\nDetailed analysis complete!")
print("\nCategory counts for Part 1:")
for cat, items in cat1.items():
    if items:
        print(f"  {cat}: {len(items)}")

print("\nCategory counts for Part 2:")
for cat, items in cat2.items():
    if items:
        print(f"  {cat}: {len(items)}")
