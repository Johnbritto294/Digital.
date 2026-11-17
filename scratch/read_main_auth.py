with open('assets/js/main.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines[40:150]):
    print(f"{i+41}: {l.rstrip()}")
