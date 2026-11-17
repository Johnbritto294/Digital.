import os
from PIL import Image

dirs = ['images', 'assets/images']
for d in dirs:
    if not os.path.exists(d):
        continue
    for f in os.listdir(d):
        if 'logo' in f:
            continue
        if f.endswith('.webp'):
            p = os.path.join(d, f)
            try:
                im = Image.open(p)
                if 'A' in im.mode:
                    im.save(p, 'WEBP', quality=85, method=6)
                else:
                    im.convert('RGB').save(p, 'WEBP', quality=85, method=6)
                print('Re-saved:', p)
            except Exception as e:
                print('Error:', p, e)
