with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'Leads [oO]ver [tT]ime', text)]
print("Leads Over Time occurrences:", len(matches))
for pos in matches:
    print("At pos:", pos)
    print(text[max(0, pos-100):min(len(text), pos+200)])
    print("="*40)
