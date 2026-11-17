import glob, re

for html in glob.glob('*.html'):
    with open(html, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = re.sub(r'style\.css\?v=\d+', 'style.css?v=37', content)
    new_content = re.sub(r'main\.js\?v=\d+', 'main.js?v=42', new_content)

    if new_content != content:
        with open(html, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print('Bumped versions in:', html)
