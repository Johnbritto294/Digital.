with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

adm_start = text.find('id="adminDash"')
adm_content = text[adm_start:]

import re
print("Top elements in adminDash:")
for tag in re.findall(r'<div class="([^"]+)"', adm_content[:2000]):
    print(" -", tag)
