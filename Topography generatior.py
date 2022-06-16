import pygame,math,random,time
t = time.time()

#Defining Parameters
mapx = 1000
mapz = 1000
mapy = 250
smoothness = 60
lakemin = 1
lakemax = 100
riverwet = 100
plainwet = 60
mountainheight = 30
snowymountainheight = 70
polar = .15
tropic = .95



topomap = []
petromap = []
biomap = []
hydromap = []
thermomap = []
mapa = []
rngx = range(mapx)
rngz = range(mapz)
for e in rngz:
    mapa.append(0.0)
for e in rngx:
    topomap.append(mapa[:])
for e in rngx:
    biomap.append(mapa[:])
for e in rngx:
    hydromap.append(mapa[:])
for e in rngx:
    thermomap.append(mapa[:])
#ntopomap = []
#for e in range(500):
 #   ntopomap.append(mapa[:])
def topofunction(width):
    chart = []
    for e in range(width):
        chart.append(0.0)
    px = 0
    py = 0
    vx = 0
    vy = 0
    angle = 0
    while px < width - 1:
        angle = random.uniform(0.0,2 * math.pi)
        vx += math.cos(angle)
        if vx < 0.1:
            vx = 0.1
        vy += math.sin(angle) - (py / mapy)
        px += 1
        py += (vy / vx) / 10
        #if vy > 0:
         #   py += (vy / vx) * (62500.0 - py*abs(py)) / 62500 / 10
        #elif vy < 0:
         #   py += (vy / vx) * (62500.0 + py*abs(py)) / 62500 / 10
        if py < -mapy:
            py = -mapy
        elif py > mapy:
            py = mapy
        chart[px] = py
    return chart
def smooth(chart):
    for d in range(len(chart) - 2):
        chart[d + 1] = (chart[d] + chart[d + 2]) / 2
    return chart
def hydrate(point,hydration):
    
    if point[0] == mapx - 1 or point[1] == mapz - 1 or point[0] == 0 or point[1] == 0:
        return
    for di in [[1,0],[-1,0],[0,1],[0,-1]]:
        loss = 1
        
        """if topomap[point[0] + di[0]][point[1] + di[1]] + 1 < topomap[point[0]][point[1]]:
            loss = -1 / (topomap[point[0] + di[0]][point[1] + di[1]] - topomap[point[0]][point[1]])
        elif topomap[point[0] + di[0]][point[1] + di[1]] - 1 > topomap[point[0]][point[1]]:
            loss = (topomap[point[0] + di[0]][point[1] + di[1]] - topomap[point[0]][point[1]])"""
        
        if hydromap[point[0] + di[0]][point[1] + di[1]] < hydration - loss:# and biomap[point[0] + di[0]][point[1] + di[1]] != "mountain"and biomap[point[0] + di[0]][point[1] + di[1]] != "snowymountain":
            hydromap[point[0] + di[0]][point[1] + di[1]] = hydration - loss
            hydrate([point[0] + di[0],point[1] + di[1]],hydration - loss)
            
    for di in [[1,1],[-1,1],[1,-1],[-1,-1]]:
        if hydromap[point[0] + di[0]][point[1] + di[1]] < hydration - 2 ** .5 and biomap[point[0] + di[0]][point[1] + di[1]] != "mountain" and biomap[point[0] + di[0]][point[1] + di[1]] != "snowymountain":
            hydromap[point[0] + di[0]][point[1] + di[1]] = hydration - 2 ** .5
            hydrate([point[0] + di[0],point[1] + di[1]],hydration - 2 ** .5)

def hydrateb(point):
    tohydrate = []
    if point[0] == mapx - 1 or point[1] == mapz - 1 or point[0] == 0 or point[1] == 0:
        return []
    for di in [[1,0],[-1,0],[0,1],[0,-1]]:
        loss = 1.5 - thermomap[point[0] + di[0]][point[1] + di[1]] / mapy / 3
        if topomap[point[0] + di[0]][point[1] + di[1]] + 1 < topomap[point[0]][point[1]]:
            loss = -loss / (topomap[point[0] + di[0]][point[1] + di[1]] - topomap[point[0]][point[1]])
        elif topomap[point[0] + di[0]][point[1] + di[1]] - 1 > topomap[point[0]][point[1]]:
            loss = loss * (topomap[point[0] + di[0]][point[1] + di[1]] - topomap[point[0]][point[1]])
        if hydromap[point[0] + di[0]][point[1] + di[1]] < hydromap[point[0]][point[1]] - loss:# and biomap[point[0] + di[0]][point[1] + di[1]] != "mountain" and biomap[point[0] + di[0]][point[1] + di[1]] != "snowymountain":
            tohydrate.append([point[0] + di[0],point[1] + di[1]])
            hydromap[point[0] + di[0]][point[1] + di[1]] = hydromap[point[0]][point[1]] - loss
    for di in [[1,1],[-1,1],[1,-1],[-1,-1]]:
        loss = (1.5 - thermomap[point[0] + di[0]][point[1] + di[1]] / mapy / 3)*2 ** .5
        if topomap[point[0] + di[0]][point[1] + di[1]] + 1 < topomap[point[0]][point[1]]:
            loss = -loss / (topomap[point[0] + di[0]][point[1] + di[1]] - topomap[point[0]][point[1]])
        elif topomap[point[0] + di[0]][point[1] + di[1]] - 1 > topomap[point[0]][point[1]]:
            loss = loss * (topomap[point[0] + di[0]][point[1] + di[1]] - topomap[point[0]][point[1]])
        if hydromap[point[0] + di[0]][point[1] + di[1]] < hydromap[point[0]][point[1]] - loss:# and biomap[point[0] + di[0]][point[1] + di[1]] != "mountain" and biomap[point[0] + di[0]][point[1] + di[1]] != "snowymountain":
            tohydrate.append([point[0] + di[0],point[1] + di[1]])
            hydromap[point[0] + di[0]][point[1] + di[1]] = hydromap[point[0]][point[1]] - loss
    return tohydrate
    
def buildlake(point,cap):
    lakes = [point]
    shore = [[point[0] + 1,point[1]],[point[0] - 1,point[1]],[point[0],point[1] + 1],[point[0],point[1] - 1]]
    for s in shore:
        if s[0] == mapx or s[1] == mapz or s[0] == 0 or s[1] == 0:
            shore.remove(s)
    d = point
    while len(lakes) < cap:
        dim = topomap[shore[0][0]][shore[0][1]]
        dicord = shore[0]
        for di in shore[1:]:
            if topomap[di[0]][di[1]] < dim:
                dim = topomap[di[0]][di[1]]
                dicord = di
        lakes.append(dicord)
        shore.remove(dicord)
        biomap[dicord[0]][dicord[1]] = "lake"
        for d in [[1,0],[-1,0],[0,1],[0,-1]]:
            if not [dicord[0] + d[0],dicord[1] + d[1]] in shore and not [dicord[0] + d[0],dicord[1] + d[1]] in lakes:
                shore.append([dicord[0] + d[0],dicord[1] + d[1]])
        for s in shore:
            if s[0] == mapx or s[1] == mapz or s[0] == 0 or s[1] == 0:
                shore.remove(s)
        for d in lakes:
            topomap[d[0]][d[1]] = dim
        found = False
        stand = dim
        for d in shore:
            if topomap[d[0]][d[1]] < stand:
                found = True
                foundcord = d
                stand = topomap[d[0]][d[1]]
        if found:
            return True,d,lakes,shore
    return False,d,lakes,shore
                
flip = False
for slant in range(0,smoothness):
    angle = slant / float(smoothness) * math.pi * 2.0
    slope = math.tan(angle)
    if angle == math.pi:
        slope = 0
    if not flip and angle >= math.pi:
        flip = True
    if slope >= 1:
        for px in range(mapx + int(-mapx/slope), mapx + mapx):
            chart = topofunction(mapz)
            if flip:
                chart.reverse()
            for pz in rngz:
                valx = int(px + pz/slope)
                if valx - mapx < mapx and valx - mapx >= 0 and pz < mapz and pz >= 0:
                    topomap[valx - mapx][pz] += chart[pz]
    elif slope <= -1:
        for px in range(mapx + 0,mapx + int(mapx - mapx/slope) + 1):
            chart = topofunction(mapz)
            if flip:
                chart.reverse()
            for pz in rngz:
                valx = int(px + pz/slope)
                if valx - mapx < mapx and valx - mapx >= 0 and pz < mapz and pz >= 0:
                    topomap[valx - mapx][pz] += chart[pz]
    elif slope < 1 and slope >= 0:
        for pz in range(mapz + int(-mapz*slope),mapz + mapz):
            chart = topofunction(mapx)
            if flip:
                chart.reverse()
            for px in rngx:
                valz = int(pz + px*slope)
                if px < mapx and px >= 0 and valz - mapz < mapz and valz - mapz >= 0:
                    topomap[px][valz - mapz] += chart[px]
    elif slope > -1 and slope < 0:
        for pz in range(mapz + 0,mapz + int(mapz - mapz*slope) + 1):
            chart = topofunction(mapx)
            if flip:
                chart.reverse()
            for px in rngx:
                valz = int(pz + px*slope)
                if px < mapx and px >= 0 and valz - mapz < mapz and valz - mapz >= 0:
                    topomap[px][valz - mapz] += chart[px]
    print slant

high = topomap[0][0]
for gx in topomap:
    for gz in gx:
        if abs(gz) > high:
            high = gz
mult = mapy / high
#mult = math.log(mapy,high)
for gx in rngx:
    for gz in rngz:
        topomap[gx][gz] = topomap[gx][gz] * mult
        if topomap[gx][gz] > mapy:
            topomap[gx][gz] = mapy
        elif topomap[gx][gz] < -mapy:
            topomap[gx][gz] = -mapy
for smx in rngx:
    topomap[smx] = smooth(topomap[smx])

for smz in rngz:
    cutz = []
    for cutx in rngx:
        cutz.append(topomap[cutx][smz])
    cutz = smooth(cutz)
    for cutx in rngx:
        topomap[cutx][smz] = cutz[cutx]
for r in topomap:
    petromap.append(r[:])
print time.time() - t

for rx in rngx:
    for rz in rngz:
        thermomap[rx][rz] =   mapy * 2 * (mapz/2 - abs(rz - mapz/2))/mapz - (topomap[rx][rz] * 2)


#generate rivers
rivers = []
for rx in rngx:
    for rz in rngz:
        if topomap[rx][rz] >= mountainheight:
            biomap[rx][rz] = "mountain"
        if topomap[rx][rz] >= mountainheight and thermomap[rx][rz] < polar * mapy:
            biomap[rx][rz] = "snowymountain"
            growingriver = True
            rivx = rx
            rivz = rz
            rivd = [0,1]
            lakecount = 0
            while growingriver:
                if biomap[rivx][rivz] == "river" or biomap[rivx][rivz] == "snowymountainriver":
                    growingriver = False
                    break
                if rivx == mapx - 1 or rivx == 0 or rivz == mapz - 1 or rivz == 0:
                    growingriver = False
                    break
                if biomap[rivx][rivz] != "snowymountain":
                    biomap[rivx][rivz] = "river"
                    rivers.append([rivx,rivz])
                else:
                    biomap[rivx][rivz] = "snowymountainriver"
                if topomap[rivx + 1][rivz] < topomap[rivx][rivz] and topomap[rivx + 1][rivz] < topomap[rivx - 1][rivz] and topomap[rivx + 1][rivz] < topomap[rivx][rivz + 1] and topomap[rivx + 1][rivz] < topomap[rivx][rivz - 1]:
                    rivx += 1
                    rivz += 0
                    rivd = [1,0]
                elif topomap[rivx - 1][rivz] < topomap[rivx][rivz] and topomap[rivx - 1][rivz] < topomap[rivx + 1][rivz] and topomap[rivx - 1][rivz] < topomap[rivx][rivz + 1] and topomap[rivx - 1][rivz] < topomap[rivx][rivz - 1]:
                    rivx += -1
                    rivz += 0
                    rivd = [-1,0]
                elif topomap[rivx][rivz + 1] < topomap[rivx][rivz] and topomap[rivx][rivz + 1] < topomap[rivx][rivz - 1] and topomap[rivx][rivz + 1] < topomap[rivx + 1][rivz] and topomap[rivx][rivz + 1] < topomap[rivx - 1][rivz]:
                    rivx += 0
                    rivz += 1
                    rivd = [0,1]
                elif topomap[rivx][rivz - 1] < topomap[rivx][rivz] and topomap[rivx][rivz - 1] < topomap[rivx][rivz + 1] and topomap[rivx][rivz - 1] < topomap[rivx + 1][rivz] and topomap[rivx][rivz - 1] < topomap[rivx - 1][rivz]:
                    rivx += 0
                    rivz += -1
                    rivd = [0,-1]
                elif topomap[rivx][rivz] < topomap[rivx][rivz - 1] and topomap[rivx][rivz] < topomap[rivx][rivz + 1] and topomap[rivx][rivz] < topomap[rivx + 1][rivz] and topomap[rivx][rivz] < topomap[rivx - 1][rivz]:
                    biomap[rivx][rivz] = "lake"
                    found,d,lakes,shores = buildlake([rivx,rivz],random.randint(lakemin,lakemax))
                    rivers.extend(lakes)
                    #for s in shores:
                        #biomap[s[0]][s[1]] = "shore"
                    if found:
                        rivx = d[0]
                        rivz = d[1]
                    else:
                        growingriver = False
                        break
                else:
                    if topomap[rivx + rivd[0]][rivz + rivd[1]] <= topomap[rivx][rivz] and topomap[rivx + rivd[0]][rivz + rivd[1]] <= topomap[rivx + rivd[1]][rivz + rivd[0]] and topomap[rivx + rivd[0]][rivz + rivd[1]] <= topomap[rivx - rivd[1]][rivz - rivd[0]]:
                        rivx += rivd[0]
                        rivz += rivd[-1]
                    elif topomap[rivx + rivd[1]][rivz + rivd[0]] <= topomap[rivx - rivd[1]][rivz - rivd[0]]:
                        rivx += rivd[1]
                        rivz += rivd[0]
                        rivd = [rivd[1],rivd[0]]
                    else:
                        rivx += -rivd[1]
                        rivz += -rivd[0]
                        rivd = [-rivd[1],-rivd[0]]
print time.time() - t
for point in rivers:
    hydromap[point[0]][point[1]] = riverwet
while len(rivers) > 0:
    hriv = rivers[:]
    rivers = []
    for point in hriv:
        rivers.extend(hydrateb(point))
print time.time() - t

for rx in rngx:
    for rz in rngz:
        temperature = thermomap[rx][rz]
        if biomap[rx][rz] == 0:
            if temperature < polar * mapy:#rz > 9.0/10*mapz or rz < 1.0/10*mapz:
                if hydromap[rx][rz] <= 0:
                    biomap[rx][rz] = "frozendesert"
                elif hydromap[rx][rz] < plainwet:
                    biomap[rx][rz] = "iceplain"
                else:
                    biomap[rx][rz] = "taiga"
            elif temperature > tropic * mapy:#rz > 4.0/10*mapz and rz < 6.0/10*mapz:
                if hydromap[rx][rz] <= 0:
                    biomap[rx][rz] = "desert"
                elif hydromap[rx][rz] < plainwet:
                    biomap[rx][rz] = "savana"
                else:
                    biomap[rx][rz] = "jungle"
            else:
                if hydromap[rx][rz] <= 0:
                    biomap[rx][rz] = "desert"
                elif hydromap[rx][rz] < plainwet:
                    biomap[rx][rz] = "plain"
                else:
                    biomap[rx][rz] = "forest"
        elif biomap[rx][rz] == "river":
            if temperature < polar * mapy:#rz > 9.0/10*mapz or rz < 1.0/10*mapz:
                biomap[rx][rz] = "frozenriver"
            elif temperature > tropic * mapy:#rz > 4.0/10*mapz and rz < 6.0/10*mapz:
                biomap[rx][rz] = "jungleriver"
        elif biomap[rx][rz] == "lake":
            if temperature < polar * mapy:#rz > 9.0/10*mapz or rz < 1.0/10*mapz:
                biomap[rx][rz] = "frozenlake"
            elif temperature > tropic * mapy:#rz > 4.0/10*mapz and rz < 6.0/10*mapz:
                biomap[rx][rz] = "junglelake"
for rx in rngx:
    for rz in rngz:
        if topomap[rx][rz] - petromap[rx][rz] > 0 and topomap[rx][rz] - petromap[rx][rz] < 10 and( biomap[rx][rz] == "lake" or biomap[rx][rz] == "junglelake"):
            biomap[rx][rz] = "swamp"
for rx in rngx:
    for rz in rngz:
        if biomap[rx][rz] == "forest":
            if topomap[rx][rz] * ((hydromap[rx][rz] - plainwet) ** 2) < -7000 * 4:
                biomap[rx][rz] = "darkforest"
            elif topomap[rx][rz] * ((hydromap[rx][rz] - plainwet) ** 2) < -100 * 4:
                biomap[rx][rz] = "denseforest"
biolist = {}
for rx in rngx:
    for rz in rngz:
        if not biomap[rx][rz] in biolist:
            biolist[biomap[rx][rz]] = 1
        else:
            biolist[biomap[rx][rz]] += 1
print biolist

screen = pygame.display.set_mode((mapx,mapz))
for gx in rngx:
    for gz in rngz:
        if biomap[gx][gz] == "river":
            screen.set_at([gx,gz],[0,100,255])
        elif biomap[gx][gz] == "lake":
            screen.set_at([gx,gz],[0,0,255])
        elif biomap[gx][gz] == "snowymountain":
            screen.set_at([gx,gz],[255,255,255])
        elif biomap[gx][gz] == "snowymountainriver":
            screen.set_at([gx,gz],[255,255,255])
        elif biomap[gx][gz] == "mountain":
            screen.set_at([gx,gz],[100,100,100])
        elif biomap[gx][gz] == "desert":
            screen.set_at([gx,gz],[255,255,0])
        elif biomap[gx][gz] == "forest":
            screen.set_at([gx,gz],[0,200,0])
        elif biomap[gx][gz] == "plain":
            screen.set_at([gx,gz],[0,255,0])
        elif biomap[gx][gz] == "shore":
            screen.set_at([gx,gz],[255,255,100])
        elif biomap[gx][gz] == "swamp":
            screen.set_at([gx,gz],[25 ,50,0])
        elif biomap[gx][gz] == "denseforest":
            screen.set_at([gx,gz],[0,100,0])
        elif biomap[gx][gz] == "darkforest":
            screen.set_at([gx,gz],[0,50,0])
        elif biomap[gx][gz] == "savana":
            screen.set_at([gx,gz],[100,200,0])
        elif biomap[gx][gz] == "jungle":
            screen.set_at([gx,gz],[50,255,100])
        elif biomap[gx][gz] == "iceplain":
            screen.set_at([gx,gz],[230,230,230])
        elif biomap[gx][gz] == "taiga":
            screen.set_at([gx,gz],[150,255,150])
        elif biomap[gx][gz] == "frozenriver":
            screen.set_at([gx,gz],[220,220,255])
        elif biomap[gx][gz] == "frozenlake":
            screen.set_at([gx,gz],[200,200,255])
        elif biomap[gx][gz] == "frozendesert":
            screen.set_at([gx,gz],[200,200,200])
        elif biomap[gx][gz] == "jungleriver":
            screen.set_at([gx,gz],[50,170,255])
        elif biomap[gx][gz] == "junglelake":
            screen.set_at([gx,gz],[75,170,230])
        #screen.set_at([gx,gz],[int(127 + 127 * topomap[gx][gz] / 250),int(127 + 127 * topomap[gx][gz] / 250),int(127 + 127 * topomap[gx][gz] / 250)])
"""for gx in range(500):
    gy = 250 - chart[gx]
    for gry in range(int(gy),500):
        screen.set_at([int(gx / 1),gry],[0,255,0])"""
print time.time() - t
pygame.display.flip()
on = True
while on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            on = False
            break
pygame.quit()


