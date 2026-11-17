with open('login.html', 'r', encoding='utf-8') as f:
    login_html = f.read()

with open('dashboard.html', 'r', encoding='utf-8') as f:
    dash_html = f.read()

with open('assets/js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

print("--- Testing login.html ---")
assert 'data-role="client"' in login_html, "Missing client role button"
assert 'data-role="admin"' in login_html, "Missing admin role button"
assert 'id="fillClientDemo"' in login_html, "Missing fillClientDemo"
assert 'id="fillAdminDemo"' in login_html, "Missing fillAdminDemo"
assert 'name="role"' in login_html, "Missing hidden role input"
print("login.html: ALL CHECKS PASSED!")

print("--- Testing dashboard.html ---")
assert 'id="clientDash"' in dash_html, "Missing clientDash"
assert 'id="adminDash"' in dash_html, "Missing adminDash"
assert 'id="roleBtnClient"' in dash_html, "Missing roleBtnClient"
assert 'id="roleBtnAdmin"' in dash_html, "Missing roleBtnAdmin"
assert 'id="adm-overview"' in dash_html, "Missing adm-overview"
assert 'id="adm-clients"' in dash_html, "Missing adm-clients"
assert 'id="adm-pods"' in dash_html, "Missing adm-pods"
assert 'id="adm-channels"' in dash_html, "Missing adm-channels"
assert 'id="adm-lab"' in dash_html, "Missing adm-lab"
assert 'adm-bento-hero' in dash_html, "Missing adm-bento-hero"
assert 'calcBrands' in dash_html, "Missing calcBrands"
assert 'calcSpend' in dash_html, "Missing calcSpend"
print("dashboard.html: ALL CHECKS PASSED!")

print("--- Testing main.js ---")
assert 'setDashboardRole' in js, "Missing setDashboardRole"
assert 'fillClientDemo' in js, "Missing fillClientDemo handler"
assert 'fillAdminDemo' in js, "Missing fillAdminDemo handler"
assert "dashboard.html?role=" in js, "Missing role redirect"
assert 'showAdmTab' in js, "Missing showAdmTab"
assert 'showCpTab' in js, "Missing showCpTab"
print("main.js: ALL CHECKS PASSED!")
