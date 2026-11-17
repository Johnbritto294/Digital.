with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

adm_start = text.find('id="adminDash"')
adm_end = text.find('</div><!-- #adminDash -->')
print(f"adminDash starts at {adm_start}, ends at {adm_end}, length {adm_end - adm_start}")
