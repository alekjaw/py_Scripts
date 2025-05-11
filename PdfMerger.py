from pypdf import PdfReader, PdfWriter

pdfs = [
    r'C:\Users\x\x\x\x\x\x\.pdf', #kopiuj wklej scieżke do pliku1
    r'C:\Users\x\x\x\x\x\x\.pdf'  #kopiuj wklej scieżke do pliku2
]

writer = PdfWriter()

for pdf_path in pdfs:
    reader = PdfReader(pdf_path)  # przekazujesz ścieżkę do pliku jako string
    for page in reader.pages:
        writer.add_page(page)

output_path = r'C:\Users\Alek\Desktop\merged.pdf'  # lub inna wybrana lokalizacja

with open(output_path, "wb") as output_pdf:
    writer.write(output_pdf)