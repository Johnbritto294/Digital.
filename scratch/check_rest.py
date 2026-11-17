with open('dashboard.html', 'r', encoding='utf-8') as f:
    dash = f.read()

clients_start = dash.find('<!-- ================= 2. CLIENT ROSTER SECTION ================= -->')
rest = dash[clients_start:69353]
print("Remaining length:", len(rest))
print("Contains adm-clients?", "id=\"adm-clients\"" in rest)
print("Contains adm-pods?", "id=\"adm-pods\"" in rest)
print("Contains adm-channels?", "id=\"adm-channels\"" in rest)
print("Contains adm-lab?", "id=\"adm-lab\"" in rest)
