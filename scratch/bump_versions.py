import os, re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for fn in html_files:
    with open(fn, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # replace any ?v=XX with ?v=32
    new_content = re.sub(r'\?v=\d+', '?v=32', content)
    
    if new_content != content:
        with open(fn, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Bumped cache version to v=32 in {fn}")
    else:
        print(f"No version query found in {fn}")
