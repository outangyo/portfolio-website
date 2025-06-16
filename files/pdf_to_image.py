import fitz  # PyMuPDF

doc = fitz.open("ResumeEN.pdf")

for i, page in enumerate(doc):
    zoom = 2
    mat = fitz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat)

    filename = f"resume_page_{i+1}.png"
    pix.save(filename)
    print(f"Saved page {i+1} as {filename}")