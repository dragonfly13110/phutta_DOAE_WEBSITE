import sys
from pypdf import PdfReader

try:
    reader = PdfReader(r"t:\web\เว็บ สำนักงานพุทธมณฑล\แผนพัฒนาการเกษตร อำเภอพุทธมณฑล ปี 2568 รวมเล่.pdf")
    number_of_pages = len(reader.pages)
    print(f"Total Pages: {number_of_pages}")
    
    # Read first 5 pages to get an overview
    text = ""
    for i in range(min(5, number_of_pages)):
        page = reader.pages[i]
        text += page.extract_text() + "\n"
        
    print(text)
except Exception as e:
    print(f"Error: {e}")
