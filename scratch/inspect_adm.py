with open('dashboard.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    if 'id="adm-' in line or 'class="adm-sec' in line:
        print(f"Line {idx+1}: {line.strip()}")
