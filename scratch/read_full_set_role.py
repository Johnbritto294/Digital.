with open('assets/js/main.js', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find("const setDashboardRole")
end = text.find("window.setDashboardRole")
print(text[start:end])
