import glob, re

def add_src_to_imgs(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    def repl(m):
        full_tag = m.group(0)
        if 'src=' in full_tag:
            return full_tag
        data_img_match = re.search(r'data-img=["\']([^"\']+)["\']', full_tag)
        if data_img_match:
            img_id = data_img_match.group(1).replace('photo-', '')
            src = f'images/photo-{img_id}.webp'
            # Insert src right after <img
            return full_tag.replace('<img', f'<img src="{src}"', 1)
        return full_tag

    new_content = re.sub(r'<img\b[^>]*>', repl, content)
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print('Updated:', filepath)

for html in glob.glob('*.html'):
    add_src_to_imgs(html)
