# Let's inspect the exact sections in adminDash
with open('dashboard.html', 'r', encoding='utf-8') as f:
    dash = f.read()

clients_start = dash.find('<!-- ================= 2. CLIENT ROSTER SECTION ================= -->')
print("Clients section starts at:", clients_start)

# Let's see how clients section looks
print(dash[clients_start:clients_start+400])
