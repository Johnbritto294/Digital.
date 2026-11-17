with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("Length of dashboard.html:", len(text))
print("Has clientDash?", "clientDash" in text)
print("Has adminDash?", "adminDash" in text)
print("Has role-badge-switch?", "role-badge-switch" in text)
