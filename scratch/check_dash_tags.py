with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's check initial classes on #clientDash and #adminDash
import re
client_dash_tag = re.search(r'<div id="clientDash"[^>]*>', text)
admin_dash_tag = re.search(r'<div id="adminDash"[^>]*>', text)

print("clientDash tag:", client_dash_tag.group(0) if client_dash_tag else "NOT FOUND")
print("adminDash tag:", admin_dash_tag.group(0) if admin_dash_tag else "NOT FOUND")
