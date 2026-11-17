with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

print('class="dash"' in text)
print('class="side"' in text)
print('EXECUTIVE CENTER' in text)
print('Client Portfolios' in text)
print('Pods & Staff' in text)
