p = list()
while(1):
    n = input("Enter grammar production rule<make sure letters T-Z aren't used>(Enter \'done\' when completed) ")
    if (n!="done"):
        p.append(n)
    else:
        break
print(p)
q = list()
r = list()
ch = 'T'
c=(p[0])[0]
for i in p:
    if i[0]!=c:
        ch = ch +1
        c = i[0]
    for j in range(1,len(i))[::-1]:
        if j>2:
            y = i[:j+1]
            print(y)
            if not (y in q):
                q.append(y)
            else:
                z = y+ch
                if not (z in r):
                    r.append(z)
    
print(q)
print(r)




# for i in p:
#     if i[0] in q:
#         if i[3:] == "null":
#             y = str(i[0:3])+str(i[0])+"\'"
#             r.append(y)
#         elif i[0]!=i[3]:
#             y = (i+i[0]+'\'')
#             r.append(y)
#             y = str(i[0])+"\'"+"->null"
#             if not (y in r):
#                 r.append(y)
#         elif i[0] == i[3]:
#             y = str(i[0])+"\'->"+i[4:]+str(i[0])+"\'"
#             r.append(y)
#     else:
#         r.append(i)
# print("\nLeft recursion removed grammar is \n")
# for i in r:
#     print(i)