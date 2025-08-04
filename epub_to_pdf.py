from ebooklib import epub, ITEM_DOCUMENT
from bs4 import BeautifulSoup
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import tempfile
import os

def epub_to_pdf_simple(epub_path, pdf_path):
    book = epub.read_epub(epub_path)
    c = canvas.Canvas(pdf_path, pagesize=A4)
    width, height = A4
    y = height - 50
    line_height = 14

    for item in book.items:
        if item.get_type() == ITEM_DOCUMENT:
            soup = BeautifulSoup(item.get_content(), 'html.parser')
            text = soup.get_text()

            for line in text.split('\n'):
                line = line.strip()
                if not line:
                    continue
                if y <= 50:
                    c.showPage()
                    y = height - 50
                c.drawString(50, y, line[:1000])
                y -= line_height

    c.save()
    print(f"✅ PDF saved to: {pdf_path}")

# Example usage
epub_to_pdf_simple(
    r"epub_path",
    r"epub_converted.pdf"
)
