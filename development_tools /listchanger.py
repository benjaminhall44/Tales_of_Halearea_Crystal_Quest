p = []
n = []
for d in p:
    if len(d) == 2:
        n.append([d[0] - 30,d[1] + 7,"plain"])
    else:
        n.append([d[0] - 10,d[1] + 42,"plain"])
print n
        
