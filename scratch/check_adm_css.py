with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'(\.adm-[^{]+{[^}]+})', text)
print(f"Total .adm- rules: {len(matches)}")
for m in matches[:15]:
    print(m[:90])
