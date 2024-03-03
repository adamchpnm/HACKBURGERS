with open('testFile') as f:
    lines = f.readlines()
print(lines)
toPrint = ""
for i in lines:
    formatted = f"{{" + i + f"}}"
    print(formatted)
