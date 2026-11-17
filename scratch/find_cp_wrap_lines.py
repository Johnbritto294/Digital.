with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    if 'cp-wrap' in line:
        print(f"Line {idx+1}: {line.strip()}")
