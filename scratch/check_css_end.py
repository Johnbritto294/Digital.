with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

print("CSS length:", len(css))
print("Last 200 chars:")
print(css[-200:])
