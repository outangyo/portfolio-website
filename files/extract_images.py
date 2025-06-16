import fitz  # PyMuPDF

doc = fitz.open("professional Diploma of Associate Engineer from COE.pdf")  # ใช้ชื่อไฟล์ PDF ที่คุณวางไว้

for i, page in enumerate(doc):
    images = page.get_images(full=True)
    for img_index, img in enumerate(images):
        xref = img[0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]
        image_ext = base_image["ext"]
        with open(f"image_page{i+1}_{img_index}.{image_ext}", "wb") as f:
            f.write(image_bytes)