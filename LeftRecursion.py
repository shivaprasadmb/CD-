p = list()
while(1):
    n = input("Enter grammar production rule(Enter \'done\' when completed) ")
    if (n!="done"):
        p.append(n)
    else:
        break
#p is a list used to store all grammar rules entered one rule at a time. Use "null" to represent null instead of using lambda or epsilon.    
q = list()
for i in p:
    if (i[1:3]=="->") and (i[0]==i[3]):
        if not (i[0] in q):
            q.append(i[0])
#q is a list used to store all the non terminals that have a rule with left recursion. This program can only work for CFG.
r = list()
for i in p:
    if i[0] in q:
        if i[3:] == "null":
            y = str(i[0:3])+str(i[0])+"\'"
            r.append(y)
        elif i[0]!=i[3]:
            y = (i+i[0]+'\'')
            r.append(y)
            y = str(i[0])+"\'"+"->null"
            if not (y in r):
                r.append(y)
        elif i[0] == i[3]:
            y = str(i[0])+"\'->"+i[4:]+str(i[0])+"\'"
            r.append(y)
    else:
        r.append(i)
#r is a list used to store all the grammar rules after left recursion is removed.
print("\nLeft recursion removed grammar is \n")
for i in r:
    print(i)
