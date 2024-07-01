import random
while True:
    raw_input()
    e = []
    for d in range(4):
        e.append(random.choice(["babydragon","pyroclast","lavamonster","lavamonster"]))
        while None in e:
            e.remove(None)
    s = "["
    c = False
    for i in e:
        if c:
            s += ","
        else:
            c = True
        s += '"%s"' % i
    s += "]"
    print s,
        
