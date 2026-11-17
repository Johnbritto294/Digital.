with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

adm_start = text.find('id="adm-overview"')
adm_end = text.find('id="adm-clients"')
print(text[adm_start:adm_end])
