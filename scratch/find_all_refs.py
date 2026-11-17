import glob, re

for html in glob.glob('*.html'):
    content = open(html, encoding='utf-8').read()
    refs = re.findall(r'(?:data-img=["\']([^"\']+)["\']|src=["\']images/([^"\']+)["\'])', content)
    for r in refs:
        ref = r[0] or r[1]
        print(f'{html:15}: {ref}')
