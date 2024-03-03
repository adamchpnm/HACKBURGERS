import operator
operations = [operator.add, operator.sub]
# add two numbers
s = operations[0](1, 2)
# print(s)


scriptBodyOper = [operator.add, operator.sub]
scriptBodyArgs = [[1,2],[75,47]]

for i in range(0,len(scriptBodyArgs)):
    print(i)
    oper = scriptBodyOper[i]
    print(scriptBodyArgs[i])
    print(oper(scriptBodyArgs[i]))