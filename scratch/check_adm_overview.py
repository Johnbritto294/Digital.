with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
adm_overview = re.search(r'<section id="adm-overview"[^>]*>(.*?)</section>', text, re.DOTALL)
if adm_overview:
    print("Found adm-overview, length:", len(adm_overview.group(1)))
