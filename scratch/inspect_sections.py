with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
sections = re.findall(r'<section id="(adm-[^"]+)"[^>]*>(.*?)</section>', text, re.DOTALL)
for sid, scontent in sections:
    print(f"Section {sid}: {len(scontent)} chars, {len(scontent.splitlines())} lines")
