p = list()
while(1):
    n = input("Enter grammar production rule(Enter \'done\' when completed) ")
    if (n!="done"):
        p.append(n)
    else:
        break
    
q = list()
for i in p:
    if (i[1:3]=="->") and (i[0]==i[3]):
        if not (i[0] in q):
            q.append(i[0])
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
print("\nLeft recursion removed grammar is \n")
for i in r:
    print(i)