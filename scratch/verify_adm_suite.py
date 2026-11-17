with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'(\.adm-suite[^{]*{[^}]+})', text)
for m in matches:
    print(m)
