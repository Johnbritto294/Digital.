with open('assets/js/main.js', 'r', encoding='utf-8') as f:
    text = f.read()

target = """    calcBrands.addEventListener('input', updateSim);
    calcSpend.addEventListener('input', updateSim);
  }"""

replacement = """    calcBrands.addEventListener('input', updateSim);
    calcSpend.addEventListener('input', updateSim);
    updateSim();
  }"""

if target in text:
    text = text.replace(target, replacement)
    print("Added updateSim() call successfully!")
else:
    # try normalized line endings
    text_norm = text.replace('\r\n', '\n')
    target_norm = target.replace('\r\n', '\n')
    if target_norm in text_norm:
        text = text_norm.replace(target_norm, replacement)
        print("Added updateSim() with normalized line endings!")

with open('assets/js/main.js', 'w', encoding='utf-8') as f:
    f.write(text)
