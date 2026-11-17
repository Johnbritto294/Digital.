bento_css = """
/* Executive Bento & Typography Enhancement */
.adm-bento-hero{background:#ffffff;border:1.5px solid #dcd8fc;box-shadow:0 8px 30px rgba(59,43,240,.06)}
.adm-bento-hero-val{font-family:'Syne',sans-serif;font-size:2.6rem;font-weight:800;color:#0F0D2E;line-height:1.1;letter-spacing:-.03em}
.adm-bento-unit{font-size:1rem;color:#615f85;font-weight:600;margin-left:.3rem;letter-spacing:normal}
.adm-bento-stat{font-family:'Syne',sans-serif;font-size:2.2rem;font-weight:800;line-height:1;letter-spacing:-.02em}
.tag-cobalt{display:inline-flex;align-items:center;background:rgba(59,43,240,.1);color:var(--cobalt);font-size:.76rem;font-weight:800;border-radius:999px;padding:.25rem .75rem;letter-spacing:.02em}
"""

with open('assets/css/style.css', 'a', encoding='utf-8') as f:
    f.write(bento_css)

print("Appended bento CSS successfully!")
