with open('testFile') as f:
    lines = f.readlines()

nicer = []
for i in range(len(lines)):
    nicer.append(lines[i].strip('\n'))

toPrint = "("
for i in nicer:
    formatted = f"{{" + i + f"}}"
    # print(formatted)
    toPrint += f"\"" + i + f"\"" + " : " + i + ","

list1 = list(toPrint)
list1[-1] = ")"
print("".join(list1))

