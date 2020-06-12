grammer = list()
i = 0
print("enter your grammer rules, enter \'exec\' when completed\n")
while(True):
    rule = input("enter " + str(i)+"th rule\n")
    if(rule != "exec"):
        grammer.append(rule)
        i = i + 1
    else:
        break
#p is a list used to store all grammar rules entered one rule at a time. Use "null" to represent null instead of using lambda or epsilon. 
print()
new_grammer = list()
for j in grammer:
    left = j[0]
    ext = list()
    t = j[3:].split('|')
    for k in t:
        ext.append(k)
    LR = False
    for q in ext:
        if(q[0] == left):
            LR = True  # left recursion is there
    if(LR == False):
        new_grammer.append(left+"->")
        for q in ext:
            new_grammer.append(q+"|")
        new_grammer[-1] = new_grammer[-1][:-1]
    else:
        new_grammer.append(left+"->")
        for q in ext:
            if(q[0] != left):
                new_grammer.append(q+left+"\'|")
        new_grammer[-1] = new_grammer[-1][:-1]
        new_grammer.append("_"+left+"\'->")
        for q in ext:
            if(q[0] == left):
                new_grammer.append(q[1:]+left+"\'|")
        new_grammer[-1] = new_grammer[-1][:-1]
        new_grammer.append("|null_")

new_grammer = [''.join(new_grammer)]
final_grammer = new_grammer[0].split('_')
print("final grammer after left recursion removal\n")
for p in final_grammer:
    print(p)
