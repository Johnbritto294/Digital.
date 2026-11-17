with open('assets/js/main.js', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('const setDashboardRole = role => {')
end = text.find('window.setDashboardRole = setDashboardRole;')
print(text[start:end])
