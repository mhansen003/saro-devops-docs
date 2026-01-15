import zipfile
import xml.etree.ElementTree as ET
import os

def extract_text_from_docx(docx_path, output_path):
    """Extract text from a .docx file"""
    namespace = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}

    with zipfile.ZipFile(docx_path) as docx:
        xml_content = docx.read('word/document.xml')
        root = ET.fromstring(xml_content)

        paragraphs = []
        for paragraph in root.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
            texts = []
            for text in paragraph.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t'):
                if text.text:
                    texts.append(text.text)
            if texts:
                paragraphs.append(''.join(texts))

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(paragraphs))

# Extract both files
extract_text_from_docx(
    r'C:\Users\Mark Hansen\Desktop\saro\transcripts\Conditions Portal offsite_DAY1.docx',
    r'C:\Users\Mark Hansen\Desktop\saro\transcripts\part1_extracted.txt'
)

extract_text_from_docx(
    r'C:\Users\Mark Hansen\Desktop\saro\transcripts\Conditions Portal offsite_Day1_Part2.docx',
    r'C:\Users\Mark Hansen\Desktop\saro\transcripts\part2_extracted.txt'
)

print("Extraction complete")
