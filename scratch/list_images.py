import os

for f in sorted(os.listdir('images')):
    if f.endswith('.webp'):
        size = os.path.getsize(os.path.join('images', f))
        print(f'{f:45} {size:>8}')
