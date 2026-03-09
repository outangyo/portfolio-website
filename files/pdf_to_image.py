import fitz  # PyMuPDF
import os

# 1. หาตำแหน่งปัจจุบันของไฟล์สคริปต์นี้
current_dir = os.path.dirname(os.path.abspath(__file__))

# 2. ชี้ไปที่ไฟล์ PDF (ใช้ชื่อให้ตรงกับไฟล์ในโฟลเดอร์)
pdf_name = "Resume EN Developer.pdf" 
pdf_path = os.path.join(current_dir, pdf_name)

# ดึงชื่อไฟล์ออกมาโดยไม่มีนามสกุล (จะได้คำว่า "Resume EN Developer")
base_name = os.path.splitext(pdf_name)[0]

doc = fitz.open(pdf_path)

for i, page in enumerate(doc):
    # ปรับความคมชัด (zoom = 2 คือ 200%)
    zoom = 2
    mat = fitz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat)
    
    # ตั้งชื่อไฟล์ใหม่ตามชื่อ PDF เดิม 
    # ถ้ามีหลายหน้า มันจะต่อท้ายด้วย _1, _2 ให้เองครับ
    if len(doc) > 1:
        output_filename = f"{base_name}_{i+1}.png"
    else:
        output_filename = f"{base_name}.png"


    output_path = os.path.join(current_dir, "..", "images", output_filename)
    
    pix.save(output_path)
    print(f"Success! Saved: {output_path}")