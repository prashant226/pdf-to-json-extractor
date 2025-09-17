import pdfplumber # type: ignore
import camelot # type: ignore
import json

def extract_with_pdfplumber(file_path):
    """ Extract text content using layout analysis from pdfplumber """
    content = []
    with pdfplumber.open(file_path) as pdf:
        for page_num, page in enumerate(pdf.pages, start=1):
            page_dict = {"page_number": page_num, "content": []}
            
            # Extract words with positions
            words = page.extract_words()
            paragraphs = []
            current_paragraph = []
            last_bottom = None

            for word in words:
                top = word['top']
                if last_bottom and abs(top - last_bottom) > 10:  # paragraph break
                    paragraphs.append(current_paragraph)
                    current_paragraph = []
                current_paragraph.append(word['text'])
                last_bottom = word['bottom']
            
            if current_paragraph:
                paragraphs.append(current_paragraph)

            # Combine words into paragraph text
            for para_words in paragraphs:
                para_text = " ".join(para_words).strip()
                if para_text:  # only add non-empty paragraphs
                    page_dict["content"].append({
                        "type": "paragraph",
                        "section": None,
                        "sub_section": None,
                        "text": para_text
                    })
            
            content.append(page_dict)
    return content

def extract_tables_with_camelot(file_path):
    """ Extract tables using camelot with improved settings """
    tables_by_page = {}
    try:
        tables = camelot.read_pdf(file_path, pages='all', flavor='lattice', strip_text='\n', process_background=True)
        for table in tables:
            page_num = int(table.page)
            if page_num not in tables_by_page:
                tables_by_page[page_num] = []
            
            tables_by_page[page_num].append({
                "type": "table",
                "section": None,
                "description": None,
                "table_data": table.df.values.tolist()
            })
    except Exception as e:
        print(f"⚠ Table extraction error: {e}")
    return tables_by_page

def merge_content(text_content, tables_content):
    """ Merge text and tables into one unified structure """
    for page in text_content:
        page_num = page["page_number"]
        if page_num in tables_content:
            page["content"].extend(tables_content[page_num])
    return text_content

def save_json(data, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump({"pages": data}, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    input_pdf = "sample.pdf"    # Your PDF file name
    output_json = "output.json" # Output JSON file name
    
    print("📄 Extracting text content...")
    text_content = extract_with_pdfplumber(input_pdf)
    
    print("📊 Extracting tables...")
    tables_content = extract_tables_with_camelot(input_pdf)
    
    print("🔗 Merging content...")
    final_content = merge_content(text_content, tables_content)
    
    print("💾 Saving JSON file...")
    save_json(final_content, output_json)
    
    print(f"✅ JSON file created successfully: {output_json}")
