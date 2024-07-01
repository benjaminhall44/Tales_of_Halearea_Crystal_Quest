import random
for y in range(-8,1):
    for x in range(-4,3):
        e = []
        for d in range(4):
            e.append(random.choice(["ghost","ghost","angryghost"]))
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
        print '(%s,%s):room((%s,%s),"battle",[[1,0],[-1,0],[0,1],[0,-1]],%s),' % (x,y,x,y,s)
    print ""
        
