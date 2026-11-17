with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

hero_start = text.find('class="adm-hero"')
hero_end = text.find('class="adm-nav-bar"')
print("HERO MARKUP:")
print(text[hero_start:hero_end])
