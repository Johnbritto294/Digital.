# 1. Update assets/css/style.css
with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace .cp-wrap.dash-mode.active rule
css = css.replace('.cp-wrap.dash-mode.active{display:grid!important;grid-template-columns:250px 1fr}', '.cp-wrap.dash-mode.active{display:grid;grid-template-columns:250px 1fr}')

# Replace line 201
old_rule = ".cp-wrap{display:grid!important;grid-template-columns:250px 1fr;min-height:100vh;background:#f7f7fb!important;font-family:'Manrope',system-ui,sans-serif;padding-top:68px;color:#0F0D2E}"
new_rule = """.cp-wrap{display:grid;grid-template-columns:250px 1fr;min-height:100vh;background:#f7f7fb;font-family:'Manrope',system-ui,sans-serif;padding-top:68px;color:#0F0D2E}
.cp-wrap.d-none,.adm-suite.d-none{display:none!important}"""

css = css.replace(old_rule, new_rule)

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated style.css successfully!")

# 2. Update assets/js/main.js
with open('assets/js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

old_toggle = """    if (role === 'admin') {
      if (clientDash) clientDash.classList.add('d-none');
      if (adminDash) adminDash.classList.remove('d-none');
      if (roleBtnClient) roleBtnClient.classList.remove('on');
      if (roleBtnAdmin) roleBtnAdmin.classList.add('on');
      document.body.classList.remove('cp-theme');
      showAdmTab('adm-overview');
    } else {
      if (adminDash) adminDash.classList.add('d-none');
      if (clientDash) clientDash.classList.remove('d-none');
      if (roleBtnAdmin) roleBtnAdmin.classList.remove('on');
      if (roleBtnClient) roleBtnClient.classList.add('on');
      document.body.classList.add('cp-theme');
      showCpTab('cp-overview');
    }"""

new_toggle = """    if (role === 'admin') {
      if (clientDash) {
        clientDash.classList.add('d-none');
        clientDash.style.setProperty('display', 'none', 'important');
      }
      if (adminDash) {
        adminDash.classList.remove('d-none');
        adminDash.style.removeProperty('display');
      }
      if (roleBtnClient) roleBtnClient.classList.remove('on');
      if (roleBtnAdmin) roleBtnAdmin.classList.add('on');
      document.body.classList.remove('cp-theme');
      showAdmTab('adm-overview');
    } else {
      if (adminDash) {
        adminDash.classList.add('d-none');
        adminDash.style.setProperty('display', 'none', 'important');
      }
      if (clientDash) {
        clientDash.classList.remove('d-none');
        clientDash.style.removeProperty('display');
      }
      if (roleBtnAdmin) roleBtnAdmin.classList.remove('on');
      if (roleBtnClient) roleBtnClient.classList.add('on');
      document.body.classList.add('cp-theme');
      showCpTab('cp-overview');
    }"""

js_norm = js.replace('\r\n', '\n')
old_toggle_norm = old_toggle.replace('\r\n', '\n')
new_toggle_norm = new_toggle.replace('\r\n', '\n')

if old_toggle_norm in js_norm:
    js = js_norm.replace(old_toggle_norm, new_toggle_norm)
    with open('assets/js/main.js', 'w', encoding='utf-8') as f:
        f.write(js)
    print("Updated main.js setDashboardRole successfully!")
else:
    print("Error: old_toggle not found in main.js!")
