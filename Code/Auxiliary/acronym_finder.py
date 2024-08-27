import fitz  # PyMuPDF
import re

def extract_text_from_pdf(pdf_path):
    # Open the PDF file
    document = fitz.open(pdf_path)
    text = ""
    # Iterate through each page and extract text
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text += page.get_text()
    return text

def find_acronyms(text):
    # Regular expression to find acronyms (e.g., "NASA", "HTML")
    # This pattern assumes acronyms are 2 or more uppercase letters
    pattern = re.compile(r'\b[A-Z]{2,}\b')
    acronyms = set(pattern.findall(text))
    return acronyms

def main(pdf_path):
    # Extract text from the PDF
    text = extract_text_from_pdf(pdf_path)
    # Find acronyms in the text
    acronyms = find_acronyms(text)
    # Print the list of acronyms
    for acronym in sorted(acronyms):
        print(acronym)

if __name__ == "__main__":
    # Replace 'your_thesis.pdf' with the path to your PDF file
    pdf_path = "C:/Users/migue/OneDrive/Ambiente de Trabalho/FEUP_Dissertation_MR_vf.pdf"
    main(pdf_path)