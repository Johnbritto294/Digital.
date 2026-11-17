with open('assets/js/main.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("Lines 45-65:")
for idx, l in enumerate(lines[44:65]):
    print(f"{idx+45}: {l.rstrip()}")

print("\nLines 110-135:")
for idx, l in enumerate(lines[109:135]):
    print(f"{idx+110}: {l.rstrip()}")
