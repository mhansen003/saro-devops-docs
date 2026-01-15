import os

def split_file(input_path, output_prefix, lines_per_chunk=500):
    """Split a large file into smaller chunks"""
    with open(input_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    total_lines = len(lines)
    print(f"Total lines in {os.path.basename(input_path)}: {total_lines}")

    chunk_num = 1
    for i in range(0, total_lines, lines_per_chunk):
        chunk_lines = lines[i:i + lines_per_chunk]
        output_path = f"{output_prefix}_chunk{chunk_num}.txt"
        with open(output_path, 'w', encoding='utf-8') as f:
            f.writelines(chunk_lines)
        print(f"Created {os.path.basename(output_path)} with {len(chunk_lines)} lines")
        chunk_num += 1

# Split both files
split_file(
    r'C:\Users\Mark Hansen\Desktop\saro\transcripts\part1_extracted.txt',
    r'C:\Users\Mark Hansen\Desktop\saro\transcripts\part1'
)

split_file(
    r'C:\Users\Mark Hansen\Desktop\saro\transcripts\part2_extracted.txt',
    r'C:\Users\Mark Hansen\Desktop\saro\transcripts\part2'
)

print("\nSplitting complete")
