with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

with open('assets/js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

assert ".cp-wrap.d-none,.adm-suite.d-none{display:none!important}" in css
assert "clientDash.style.setProperty('display', 'none', 'important');" in js
assert "adminDash.style.setProperty('display', 'none', 'important');" in js
print("All checks passed successfully!")
