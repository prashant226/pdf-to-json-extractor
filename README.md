# PDF to JSON Extractor

A Python tool to extract text and tables from PDF files and save them in structured JSON format. Perfect for automating PDF data extraction for analysis, reporting, or data pipelines.

## Features

- 📄 **Text Extraction**: Extract text content with layout-based paragraph detection using pdfplumber
- 📊 **Table Extraction**: Extract tables using Camelot with lattice mode and improved settings
- 🔗 **Unified Structure**: Merge text and tables into a unified JSON structure
- 💾 **Simple Workflow**: Script-based workflow—run and get JSON output in seconds

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/prashant226/pdf-to-json--extractor.git
cd pdf-to-json--extractor
```

### 2. Install Python dependencies

```bash
pip install pdfplumber camelot-py[cv] pandas
```

### 3. Additional Requirements

⚠️ **Note**: `camelot` requires Ghostscript and Tkinter.

- **Ghostscript**: Download from [here](https://www.ghostscript.com/download/gsdnld.html)
- **Tkinter**: Usually included with Python on most systems

## Usage

### Quick Start

1. Place your PDF file in the project folder
2. Update the script variables if necessary:
   ```python
   input_pdf = "sample.pdf"    # Your PDF file
   output_json = "output.json" # Output JSON file
   ```
3. Run the script:
   ```bash
   python extract_pdf_to_json.py
   ```
4. The JSON output will be saved in the same folder as `output.json`

## Example Output

```json
{
    "pages": [
        {
            "page_number": 1,
            "content": [
                {
                    "type": "paragraph",
                    "section": null,
                    "sub_section": null,
                    "text": "This is an example paragraph extracted from the PDF."
                },
                {
                    "type": "table",
                    "section": null,
                    "description": null,
                    "table_data": [
                        ["Header1", "Header2"],
                        ["Row1Col1", "Row1Col2"]
                    ]
                }
            ]
        }
    ]
}
```

## How It Works

The extraction process follows these steps:

1. **Text Extraction**: Uses `pdfplumber` to read each page, detect paragraphs, and structure the text
2. **Table Extraction**: Uses `Camelot` in lattice mode to detect tables on each page
3. **Merge**: Combines extracted text and tables into one structured JSON
4. **Save**: Outputs the JSON file for further processing

## Project Structure

```
pdf-to-json--extractor/
│
├─ extract_pdf_to_json.py   # Main extraction script
├─ sample.pdf               # Example PDF (replace with your own)
├─ output.json              # JSON output generated after running
└─ README.md                # This documentation file
```

## Technical Details

### Dependencies

- **pdfplumber**: For text extraction and layout analysis
- **camelot-py[cv]**: For table detection and extraction
- **pandas**: For data manipulation and processing

### Output Format

The tool generates a structured JSON with the following schema:

- **pages**: Array of page objects
  - **page_number**: Integer representing the page number
  - **content**: Array of content objects (paragraphs and tables)
    - **type**: Either "paragraph" or "table"
    - **section**: Section identifier (if applicable)
    - **sub_section**: Sub-section identifier (if applicable)
    - **text**: Text content (for paragraphs)
    - **table_data**: 2D array of table data (for tables)
    - **description**: Table description (if applicable)

## Contributing

Contributions, bug reports, and feature requests are welcome!

### How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -m "Add feature"`)
4. Push to the branch (`git push origin feature-name`)
5. Open a pull request

## Troubleshooting

### Common Issues

1. **Ghostscript not found**: Ensure Ghostscript is properly installed and added to your system PATH
2. **Camelot installation issues**: Try installing with `pip install camelot-py[base]` first, then add CV dependencies
3. **Table extraction problems**: Camelot works best with PDFs that have clear table structures with borders

### System Requirements

- Python 3.6+
- Ghostscript
- Tkinter (usually included with Python)

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

- Built with [pdfplumber](https://github.com/jsvine/pdfplumber) for text extraction
- Built with [Camelot](https://github.com/atlanhq/camelot) for table extraction
- Inspired by the need for automated PDF data processing

---

**Repository**: https://github.com/prashant226/pdf-to-json--extractor

*For questions, issues, or feature requests, please open an issue on GitHub.*
