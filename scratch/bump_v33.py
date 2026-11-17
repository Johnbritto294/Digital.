import os, re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for fn in html_files:
    with open(fn, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = re.sub(r'\?v=\d+', '?v=33', content)
    
    if new_content != content:
        with open(fn, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Bumped cache version to v=33 in {fn}")
