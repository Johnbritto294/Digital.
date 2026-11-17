with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
print("Johnbrittoj in dashboard.html?", "Johnbrittoj" in text)
print("Johnbrittoj in all files:")
import os
for root, dirs, files in os.walk('.'):
    for fn in files:
        if fn.endswith(('.html', '.js', '.css')):
            fp = os.path.join(root, fn)
            try:
                with open(fp, 'r', encoding='utf-8') as f2:
                    c = f2.read()
                    if 'Johnbrittoj' in c:
                        print("Found in", fp)
            except Exception:
                pass
