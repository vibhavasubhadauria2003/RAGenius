import fitz  # PyMuPDF
def extract_text(pdf_path):
    text = ""
    print(f"Extracting text from PDF: {pdf_path}")
    try:
        # Open the PDF file
        pdf_document = fitz.open(pdf_path)
        
        # Iterate through each page and extract text
        for page_num in range(len(pdf_document)):
            page = pdf_document.load_page(page_num)
            text += page.get_text()
        
        pdf_document.close()
    except Exception as e:
        print(f"Error occurred while extracting text from PDF: {e}")

    return text

#pdf_text = extract_text("../../data/raw/sample.pdf")

#print(pdf_text)