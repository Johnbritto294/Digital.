with open('assets/js/main.js', 'r', encoding='utf-8') as f:
    text = f.read()

import re
print("Has fillClientDemo in main.js?", "fillClientDemo" in text)
print("Has setDashboardRole in main.js?", "setDashboardRole" in text)
