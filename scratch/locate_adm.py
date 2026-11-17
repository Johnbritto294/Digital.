# Read dashboard.html
with open('dashboard.html', 'r', encoding='utf-8') as f:
    dash = f.read()

# Let's locate #adminDash
adm_start = dash.find('<!-- ======================= 2. ADMIN ROLE DASHBOARD ======================== -->')
if adm_start == -1:
    adm_start = dash.find('<div id="adminDash"')

adm_end = dash.find('<!-- Toast Notification -->')

print(f"adm_start: {adm_start}, adm_end: {adm_end}")
