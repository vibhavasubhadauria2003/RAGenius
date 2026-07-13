import fitz  # PyMuPDF

class PDFLoader:
    @staticmethod
    def extract_text(pdf_path):
        text = ""
        print(f"Extracting text from PDF: {pdf_path}")
        try:
            pdf_document = fitz.open(pdf_path)
        
        # Iterate through each page and extract text
            for page_num in range(pdf_document.page_count):
                page = pdf_document.load_page(page_num)
                text += page.get_text()
        
            pdf_document.close()
        except Exception as e:
            print(f"Error occurred while extracting text from PDF: {e}")

        return text
