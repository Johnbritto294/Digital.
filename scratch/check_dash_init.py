with open('assets/js/main.js', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find("if(page=='dashboard')")
print(text[start:start+1200])
