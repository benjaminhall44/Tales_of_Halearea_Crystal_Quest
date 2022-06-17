class room:
    def __init__(self,position,contents,exits,extra):
        self.position = position
        self.contents = contents
        self.backup = contents
        self.exits = exits
        self.extra = extra
class dungeon:
    def __init__(self,name,decor,value,size,position,entrance,inside):
        self.name = name
        self.decor = decor
        self.value = value
        self.size = size
        self.position = position
        self.inside = inside.copy()
        self.entrance = entrance
    def play(self):
        global team,inventory,money,mouseposition,mousedown
        for d in self.inside:
            self.inside[d].contents = self.inside[d].backup
        dungeonposition = (0,0)
        explored = [(0,0)]
        inven = []
        for r in self.inside[(0,0)].exits:
            explored.append((r[0],r[1]))
        entered = []
        dungeon = True
        self.animate(explored,dungeonposition,inven)
        pygame.display.flip()
        while dungeon:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    playing = False
                    dungeon = False
                    break
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    go = False
                    for d in explored:
                        if mouseposition[0] > self.entrance[0] + 40 * d[0] and mouseposition[0] < self.entrance[0] + 40 * d[0] + 40 and mouseposition[1] > self.entrance[1] + 40 * d[1] and mouseposition[1] < self.entrance[1] + 40 * d[1] + 40 and ( not (self.inside[d].contents == "bronzelock" or self.inside[d].contents == "silverlock" or self.inside[d].contents == "goldlock" or self.inside[d].contents == "magiclock") or ((self.inside[d].contents == "bronzelock" and "bronzekey" in inven) or (self.inside[d].contents == "silverlock" and "silverkey" in inven) or (self.inside[d].contents == "goldlock" and "goldkey" in inven) or (self.inside[d].contents == "magiclock" and "magickey" in inven))):
                            go = True
                            break
                    if go:
                        if not d in entered:
                            if self.inside[d].contents == "bronzelock" and "bronzekey" in inven:
                                inven.remove("bronzekey")
                                self.inside[d].contents = "empty"
                            elif self.inside[d].contents == "silverlock" and "silverkey" in inven:
                                inven.remove("silverkey")
                                self.inside[d].contents = "empty"
                            elif self.inside[d].contents == "goldlock" and "goldkey" in inven:
                                inven.remove("goldkey")
                                self.inside[d].contents = "empty"
                            elif self.inside[d].contents == "magiclock" and "magickey" in inven:
                                inven.remove("magickey")
                                self.inside[d].contents = "empty"
                        posi = dungeonposition
                        for t in range(8):
                            dungeonposition = [dungeonposition[0] + ((d[0] - posi[0]) * .125),dungeonposition[1] + ((d[1] - posi[1]) * .125)]
                            self.animate(explored,dungeonposition,inven)
                            pygame.time.delay(62)
                            pygame.display.flip()
                        dungeonposition = d
                        self.animate(explored,dungeonposition,inven)
                        pygame.display.flip()
                        if not d in entered:
                            entered.append(d)
                            if self.inside[d].contents == "battle":
                                enemies = []
                                for en in self.inside[d].extra:
                                    enemies.append(enemy(enemylist[en]))
                                if battle(enemies,self.decor):
                                    self.inside[d].contents = "empty"
                                else:
                                    for dd in team:
                                        dd.effect = [None,0,0]
                                        dd.health = dd.maxhealth
                                        dd.delay = int(6000 / (dd.speed + dd.effect[1] * (dd.effect[0] == "swiftness")))
                                        dd.charge = 0
                                        dd.spellcharge = 0
                                    return False
                                for dd in team:
                                    dd.delay = int(6000 / (dd.speed + dd.effect[1] * (dd.effect[0] == "swiftness")))
                                    dd.charge = 0
                                
                            elif self.inside[d].contents == "boss":
                                enemies = []
                                for en in self.inside[d].extra:
                                    enemies.append(enemy(enemylist[en]))
                                if battle(enemies,self.decor):
                                    if self.name == "darkcastle4":
                                        playclip("mazorovdefeat")
                                    for dd in team:
                                        dd.delay = int(6000 / (dd.speed + dd.effect[1] * (dd.effect[0] == "swiftness")))
                                        dd.charge = 0
                                    return True
                                else:
                                    for dd in team:
                                        dd.effect = [None,0,0]
                                        dd.health = dd.maxhealth
                                        dd.delay = int(6000 / (dd.speed + dd.effect[1] * (dd.effect[0] == "swiftness")))
                                        dd.charge = 0
                                        dd.spellcharge = 0
                                    return False
                                
                            elif self.inside[d].contents == "door":
                                for dd in team:
                                    dd.effect = [None,0,0]
                                    dd.health = dd.maxhealth
                                    dd.delay = int(6000 / (dd.speed + dd.effect[1] * (dd.effect[0] == "swiftness")))
                                    dd.charge = 0
                                    dd.spellcharge = 0
                                return False
                            elif self.inside[d].contents == "heal":
                                for dd in team:
                                    dd.health = dd.maxhealth
                                self.inside[d].contents = "empty"
                            elif self.inside[d].contents == "game":
                                need = 0
                                for dd in team:
                                    need += dd.maxhealth - dd.health
                                if need > 0:
                                    game(need)
                                self.inside[d].contents = "empty"
                            elif self.inside[d].contents == "bronzekey":
                                inven.append("bronzekey")
                                self.inside[d].contents = "empty"
                            elif self.inside[d].contents == "silverkey":
                                inven.append("silverkey")
                                self.inside[d].contents = "empty"
                            elif self.inside[d].contents == "goldkey":
                                inven.append("goldkey")
                                self.inside[d].contents = "empty"
                            elif self.inside[d].contents == "magickey":
                                inven.append("magickey")
                                self.inside[d].contents = "empty"
                            elif self.inside[d].contents == "chest":
                                if quests[self.inside[d].extra[0]] == False:
                                    if self.inside[d].extra[1][0] == "money":
                                        money += self.inside[d].extra[1][1]
                                        quests[self.inside[d].extra[0]] = True
                                        self.inside[d].contents = "empty"
                                        screen.blit(pygame.image.load("assets/graphics/extra/coingold.png"),[self.entrance[0] + 40 * d[0] + 12,self.entrance[1] + 40 * d[1] + 8])
                                        pygame.display.flip()
                                        pygame.time.delay(500)
                                    else:
                                        if None in inventory[:15 * len(team)]:
                                            inventory[inventory.index(None)] = self.inside[d].extra[1][1]
                                            quests[self.inside[d].extra[0]] = True
                                            self.inside[d].contents = "empty"
                                            screen.blit(pygame.image.load("assets/graphics/items/%s.png" % items[self.inside[d].extra[1][1]].name),[self.entrance[0] + 40 * d[0],self.entrance[1] + 40 * d[1]])
                                            pygame.display.flip()
                                            pygame.time.delay(500)
                                else:
                                    if self.inside[d].extra[2][0] == "money":
                                        money += self.inside[d].extra[2][1]
                                        self.inside[d].contents = "empty"
                                        screen.blit(pygame.image.load("assets/graphics/extra/coingold.png"),[self.entrance[0] + 40 * d[0] + 12,self.entrance[1] + 40 * d[1] + 8])
                                        pygame.display.flip()
                                        pygame.time.delay(500)
                                    else:
                                        if None in inventory[:15 * len(team)]:
                                            inventory[inventory.index(None)] = self.inside[d].extra[2][1]
                                            self.inside[d].contents = "empty"
                                            screen.blit(pygame.image.load("assets/graphics/items/%s.png" % items[self.inside[d].extra[2][1]].name),[self.entrance[0] + 40 * d[0],self.entrance[1] + 40 * d[1]])
                                            pygame.display.flip()
                                            pygame.time.delay(500)
                        for r in self.inside[d].exits:
                            if not r in explored:
                                explored.append((d[0] + r[0],d[1] + r[1]))
                        self.animate(explored,dungeonposition,inven)
                        pygame.display.flip()
                if event.type == pygame.MOUSEMOTION:
                    mouseposition = event.pos[:]
                    self.animate(explored,dungeonposition,inven)
                    pygame.display.flip()
    def animate(self,explored,dungeonposition,inven):
        global mouseposition,mousedown
        screen.fill([0,0,0])
        for d in explored:
            screen.blit(pygame.image.load("assets/graphics/rooms/%s%s%s%s.png" % ("north" * ([0,-1] in self.inside[d].exits),"south" * ([0,1] in self.inside[d].exits),"east" * ([1,0] in self.inside[d].exits),"west" * ([-1,0] in self.inside[d].exits))),[self.entrance[0] + 40 * d[0],self.entrance[1] + 40 * d[1]])
        for d in explored:
            if self.inside[d].contents != "empty":
                screen.blit(pygame.image.load("assets/graphics/rooms/%s.png" % self.inside[d].contents),[self.entrance[0] + 40 * d[0],self.entrance[1] + 40 * d[1]])
        screen.blit(pygame.image.load("assets/graphics/rooms/%s.png" % team[0].name),[self.entrance[0] + 40 * dungeonposition[0],self.entrance[1] + 40 * dungeonposition[1]])        
        for d in explored:
            if mouseposition[0] > self.entrance[0] + 40 * d[0] and mouseposition[0] < self.entrance[0] + 40 * d[0] + 40 and mouseposition[1] > self.entrance[1] + 40 * d[1] and mouseposition[1] < self.entrance[1] + 40 * d[1] + 40:
                if d[0] == dungeonposition[0] + 1 and d[1] == dungeonposition[1]:
                    screen.blit(pygame.image.load("assets/graphics/rooms/easthighlight.png"),[self.entrance[0] + 40 * d[0],self.entrance[1] + 40 * d[1]])
                elif d[0] == dungeonposition[0] - 1 and d[1] == dungeonposition[1]:
                    screen.blit(pygame.image.load("assets/graphics/rooms/westhighlight.png"),[self.entrance[0] + 40 * d[0],self.entrance[1] + 40 * d[1]])
                elif d[0] == dungeonposition[0] and d[1] == dungeonposition[1] + 1:
                    screen.blit(pygame.image.load("assets/graphics/rooms/southhighlight.png"),[self.entrance[0] + 40 * d[0],self.entrance[1] + 40 * d[1]]) 
                elif d[0] == dungeonposition[0] and d[1] == dungeonposition[1] - 1:
                    screen.blit(pygame.image.load("assets/graphics/rooms/northhighlight.png"),[self.entrance[0] + 40 * d[0],self.entrance[1] + 40 * d[1]]) 
                #else:
                 #   screen.blit(pygame.image.load("assets/graphics/rooms/highlight.png"),[self.entrance[0] + 40 * d[0] - 10,self.entrance[1] + 40 * d[1] - 10]) 
        k = 40
        for i in inven:
            screen.blit(pygame.image.load("assets/graphics/rooms/%s.png" % i),[k,40])
            k += 40
enemylist = { "greengrobble":["greengrobble",20,5,0,2 * 3,10,"melee",1,[1,6],False],
              "greengrobbleking":["greengrobbleking",50,5,0,2 * 3,10,"melee",1,[7,12],True],
              "redgrobble":["redgrobble",30,6,0,2 * 3,10,"melee",1,[3,8],False],
              "redgrobbleking":["redgrobbleking",60,6,0,2 * 3,10,"melee",1,[9,14],True],
              "yellowgrobble":["yellowgrobble",40,7,0,2 * 3,10,"melee",1,[5,10],False],
              "yellowgrobbleking":["yellowgrobbleking",80,7,0,2 * 3,10,"melee",1,[13,18],True],
              "blackgrobble":["blackgrobble",50,8,0,2 * 3,10,"melee",1,[7,12],False],
              "blackgrobbleking":["blackgrobbleking",100,8,0,2 * 3,10,"melee",1,[17,22],True],
              
              "deadtree":["deadtree",40,6,4,7,10,"melee",2,[5,10],False],
              "deadtreeking":["deadtreeking",100,7,4,7,10,"melee",2,[16,21],True],
              "mushroom":["mushroom",50,6,1,8,10,"range",2,[5,10],False],
              "mushroomking":["mushroomking",120,10,1,8,10,"range",2,[16,21],True],
              "tree":["tree",40,8,10,7,10,"melee",2,[8,13],False],
              "treeking":["treeking",100,10,10,7,10,"melee",2,[25,30],True],
              "treeworm":["treeworm",70,8,2,17,10,"melee",2,[8,13],False],
              "soldiertreeworm":["soldiertreeworm",50,14,2,8,10,"melee",2,[5,10],False],
              "treewormqueen":["treewormqueen",300,16,2,20,10,"range",2,[44,49],True],
              
              "swampdeadtree":["deadtree",60,10,4,7,10,"melee",3,[8,13],False],
              "swampdeadtreeking":["deadtreeking",300,13,4,20,10,"melee",3,[50,55],True],
              "swampmushroom":["mushroom",75,9,1,8,10,"range",3,[8,13],False],
              "swampmushroomking":["mushroomking",360,14,1,20,10,"range",3,[50,55],True],
              "poisonmushroom":["poisonmushroom",70,7,1,8,10,"range",3,[8,13],False],
              "poisonmushroomking":["poisonmushroomking",140,12,1,3,10,"range",3,[19,24],True],
              "snail":["snail",50,20,10,5,10,"melee",3,[11,16],False],
              "snailking":["snailking",100,20,10,5,10,"melee",3,[25,30],True],
              "mudmonster":["mudmonster",100,16,0,7,10,"melee",3,[11,16],False],
              "mudking":["mudking",200,16,0,6,10,"melee",3,[25,30],True],
              "mudmound":["mudmound",1500,16,0,12,10,"range",3,[207,212],True,[240,100]],
              "mudhill":["mudmound",2000,16,0,16,10,"range",3,[277,282],True,[240,100]],
              
              "bat":["bat",50,10,1,19,10,"melee",4,[5,10],False],
              "batking":["batking",400,15,1,19,10,"melee",4,[58,63],True],
              "rockmonster":["rockmonster",40,18,10,9,10,"melee",4,[8,13],False],
              "rockking":["rockking",200,24,10,14,10,"melee",4,[53,58],True],
              "bouldermonster":["bouldermonster",50,20,10,9,10,"melee",4,[11,16],False],
              "boulderking":["boulderking",240,24,10,14,10,"melee",4,[64,69],True],
              "driller":["driller",100,15,3,15,10,"melee",4,[13,18],False],
              "drillerking":["drillerking",500,15,4,15,10,"melee",4,[86,91],True],
              "skeletonminer":["skeletonminer",100,15,4,14,10,"melee",4,[16,21],False],
              "rockskeleton":["rockskeleton",700,18,5,15,10,"melee",4,[128,133],True],
              "mole":["mole",120,12,2,14,10,"melee",4,[16,21],False],
              "moleknight":["moleknight",800,15,6,20,10,"melee",4,[159,164],True],
              "moleguard":["moleguard",120,10,2,18,10,"melee",4,[16,21],False],
              "moleking":["moleking",1000,16,6,20,10,"melee",4,[198,203],True],
              
              "cactus":["cactus",70,11,5,10,10,"melee",5,[11,16],False],
              "cactusking":["cactusking",400,12,5,15,10,"melee",5,[72,77],True],
              "skeleton":["skeleton",60,10,3,14,10,"melee",5,[8,13],False],
              "skeletongiant":["skeletongiant",300,14,3,18,10,"melee",5,[47,52],True],
              "skeletonserpent":["skeletonserpent",2000,15,5,20,10,"range",5,[372,377],True,[240,150]],
              "scorpion":["scorpion",40,8,10,25,10,"melee",5,[8,13],False],
              "scorpionking":["scorpionking",1000,16,10,25,10,"melee",5,[277,282],True,[100,100]],
              "bandit":["bandit",50,18,15,15,10,"melee",5,[25,30],False],
              "banditking":["banditking",2000,25,15,22,10,"melee",5,[1117,1122],True],
              "statue":["statue",520,21,18,16,10,"melee",5,[21,26],False,[120,200]],
              "statueking":["statueking",1120,26,18,16,10,"melee",5,[36,41],True,[120,200]],
              "mummy":["mummy",85,18,9,14,10,"melee",5,[18,23],False],
              "pharoh":["pharoh",520,37,9,22,10,"melee",5,[27,32],True],
              "sphinx":["sphinx",1950,45,19,23,10,"range",5,[36,41],True,[90,150]],
              
              "hermitcrab":["hermitcrab",60,27,10,15,10,"melee",6,[13,18],False],
              "hermitcrabking":["hermitcrabking",400,36,10,15,10,"melee",6,[103,108],True],
              "crab":["crab",90,21,7,20,10,"melee",6,[18,23],False],
              "crabking":["crabking",600,27,7,20,10,"melee",6,[141,146],True],
              "seagull":["seagull",120,16,6,30,10,"melee",6,[23,28],False],
              "seagullking":["seagullking",800,20,6,30,10,"melee",6,[178,183],True],
              "sandmonster":["sandmonster",100,18,0,28,10,"melee",6,[18,23],False],
              "sandking":["sandking",800,42,0,28,10,"melee",6,[141,146],True,[120,120]],
              "sandguard":["sandguard",70,10,0,20,10,"melee",6,[13,18],False],
              "sandknight":["sandknight",2000,30,0,40,10,"melee",6,[354,359],True],
              "sandmazorov":["sandmazorov",4000,40,0,40,10,"range",6,[711,716],True,[150,120]],
              
              "fish":["fish",120,20,12,14,10,"melee",7,[13,18],False],
              "giantfish":["giantfish",900,40,12,14,10,"melee",7,[90,95],True],
              "octopus":["octopus",800,40,8,20,8,"melee",7,[83,88],True],
              "pirate":["pirate",200,50,20,20,10,"melee",7,[24,29],False],
              "captain":["captain",700,30,20,15,10,"melee",7,[90,95],True],
              "tropicalfish":["tropicalfish",200,37,0,19,10,"melee",7,[13,18],False],
              "coral":["coral",100,53,30,10,10,"melee",7,[16,21],False],
              "coralmonster":["coralmonster",500,60,30,15,10,"melee",7,[90,95],True],
              "oyster":["oyster",150,45,24,15,10,"melee",7,[20,25],False],
              "giantoyster":["giantoyster",600,50,24,20,10,"range",7,[90,95],True],
              "fishguard":["fishguard",200,35,10,20,10,"melee",7,[16,21],False],
              "fishknight":["fishknight",3000,65,15,18,10,"melee",7,[320,325],True],
              "fishking":["fishking",5000,75,15,18,10,"melee",7,[540,545],True],
              
              "evilplant":["evilplant",200,45,10,18,10,"melee",8,[47,52],False],
              "giantvine":["giantvine",700,56,10,18,10,"melee",8,[177,182],True],
              "muncher":["muncher",200,54,10,14,10,"melee",8,[47,52],False],
              "devourer":["devourer",800,80,10,14,10,"melee",8,[197,202],True],
              "spider":["spider",100,55,25,18,10,"melee",8,[37,42],False],
              "giantspider":["giantspider",2000,70,25,17,10,"melee",8,[797,802],True],
              "snake":["snake",240,30,4,22,10,"melee",8,[57,62],False],
              "snakeking":["snakeking",1000,75,4,12,10,"melee",8,[217,222],True],
              "tiger":["tiger",7000,60,10,30,10,"melee",8,[1747,1752],True,[100,100]],
              "templeguardian":["templeguardian",4000,120,0,24,10,"range",8,[797,802],True],
              "raptor":["raptor",400,80,18,22,10,"melee",8,[127,132],False],
              "tyrannosaurusrex":["tyrannosaurusrex",4000,160,10,17,10,"melee",8,[997,1002],True,[120,200]],
              "pterodactyl":["pterodactyl",5000,85,12,55,10,"melee",8,[1317,1322],True],
              
              "bird":["bird",200,50,6,24,10,"melee",9,[93,98],False],
              "albatross":["albatross",1000,60,6,50,10,"melee",9,[381,386],True],
              "cloud":["cloud",300,40,0,20,10,"melee",9,[117,122],False],
              "giantcloud":["giantcloud",2000,100,0,24,10,"melee",9,[693,698],True,[120,200]],
              "fogspector":["fogspector",100,44,60,50,10,"melee",9,[237,242],False],
              "fogmonster":["fogmonster",1000,64,30,40,10,"melee",9,[597,602],True],
              "thundercloud":["thundercloud",300,60,0,15,10,"range",9,[117,122],False],
              "cumulonimbus":["cumulonimbus",6000,80,0,60,10,"range",9,[2061,2066],True,[120,200]],
              "eyeofthestorm":["eyeofthestorm",7000,70,0,50,10,"range",9,[2397,2402],True],
              "skydragon":["skydragon",5000,50,20,70,10,"range",9,[2397,2402],True,[90,150]],
              "skyserpent":["skyserpent",7000,70,0,50,10,"range",9,[2397,2402],True,[90,150]],
              "skyguard":["skyguard",100,50,14,25,10,"melee",9,[45,50],False],
              "skyknight":["skyknight",10000,55,14,50,10,"melee",9,[4293,4298],True],
              
              "stonemonster":["stonemonster",200,40,24,20,10,"melee",10,[117,122],False],
              "stoneking":["stoneking",1000,60,24,50,10,"melee",10,[525,530],True],
              "goat":["goat",240,30,12,34,10,"melee",10,[117,122],False],
              "mountainwolf":["mountainwolf",300,40,14,30,10,"melee",10,[141,146],False],
              "alpha":["alpha",3000,70,14,50,10,"melee",10,[1293,1298],True,[100,100]],
              "mountainlion":["mountainlion",4000,60,10,50,10,"melee",10,[1605,1610],True,[100,100]],
              "griffin":["griffin",5000,50,16,60,10,"melee",10,[2229,2234],True],
              "stonethrower":["stonethrower",500,100,20,10,10,"range",10,[237,242],False],
              "yeti":["yeti",3000,150,20,10,10,"melee",10,[1437,1442],True,[90,150]],
              "icemonster":["icemonster",200,32,24,20,10,"melee",10,[117,122],False],
              "icedragon":["icedragon",6000,60,20,50,10,"range",10,[2877,2882],True,[100,100]],
              "goldcrab":["goldcrab",420,40,0,20,10,"melee",10,[141,146],False],
              "goldbat":["goldbat",300,28,0,40,10,"melee",10,[117,122],False],
              "goldsnake":["goldsnake",360,60,0,10,10,"melee",10,[141,146],False],
              "hoarderdragon":["hoarderdragon",20000,70,22,45,10,"range",10,[10005,10010],True,[100,140]],
              "mountainbird":["mountainbird",25000,65,10,55,10,"melee",10,[10005,10010],True,[100,140]],
              
              "pyroclast":["pyroclast",240,45,18,25,10,"melee",11,[177,182],False],
              "pyroclastking":["pyroclastking",1200,75,12,60,10,"melee",11,[837,842],True],
              "babydragon":["babydragon",300,40,12,30,10,"range",11,[237,242],False],
              "dragon":["dragon",5000,70,14,70,10,"range",11,[3537,3542],True,[110,100]],
              "lavamonster":["lavamonster",180,50,5,20,10,"melee",11,[117,122],False],
              "lavaking":["lavaking",4000,80,5,50,10,"melee",11,[2577,2582],True],
              "lavaspider":["lavaspider",4000,70,18,60,10,"range",11,[2937,2942],True,[100,100]],
              "lavaseamonster":["lavaseamonster",6000,80,14,40,10,"range",11,[4197,4202],True,[160,140]],
              "phoenix":["phoenix",7000,70,10,70,10,"range",11,[4677,4682],True,[60,100]],
              "firedragon":["firedragon",6000,80,25,60,10,"range",11,[4797,4802],True,[120,110]],
              "fireguard":["fireguard",150,50,16,25,10,"melee",11,[117,122],False],
              "fireknight":["fireknight",20000,80,16,50,10,"melee",11,[14337,14342],True],
              
              "ghosttree":["ghosttree",300,60,22,20,10,"melee",12,[237,242],False],
              "raven":["raven",200,50,15,30,10,"melee",12,[177,182],False],
              "spiritmist":["spiritmist",2000,90,10,50,10,"melee",12,[1377,1382],True],
              "bigghost":["bigghost",3000,100,13,60,10,"melee",12,[2097,2102],True],
              "ghost":["ghost",350,70,10,22,10,"melee",12,[237,242],False],
              "shadowghost":["shadowghost",3000,100,24,60,10,"melee",12,[2397,2402],True],
              "specter":["specter",400,80,24,16,10,"melee",12,[357,362],False],
              "shadowspecter":["shadowspecter",8000,100,24,50,10,"melee",12,[6357,6362],True],
              "angryghost":["angryghost",200,100,10,20,10,"melee",12,[177,182],False],
              "phantom":["phantom",5000,100,15,60,10,"melee",12,[3537,3542],True,[80,100]],
              "angryphantom":["angryphantom",9000,120,15,60,10,"melee",12,[6357,6362],True,[80,100]],
              "frightfulphantom":["frightfulphantom",15000,140,15,60,10,"melee",12,[10617,10622],True,[80,100]],
              "shadowphantom":["shadowphantom",20000,150,15,60,10,"melee",12,[14157,14162],True,[80,100]],
              
              "darkguard":["darkguard",200,60,20,30,10,"melee",13,[177,182],False],
              "darkknight":["darkknight",20000,100,20,60,10,"melee",13,[14997,15002],True],
              "mazorov":["mazorov",30000,100,20,70,10,"range",13,[100000,100005],True,[150,120]]
              }
from dungeons import enemylist
dungeons = [
    dungeon("plain1","dungeon",1,1,[274,9941],[260,180],{
        (0,0):room((0,0),"door",[[0,-1]],None),
        (0,-1):room((0,-1),"battle",[[0,-1],[0,1]],["greengrobble","greengrobble"]),
        (0,-2):room((0,-2),"boss",[[0,1]],["greengrobble","greengrobble","greengrobbleking"])}),
        
    dungeon("plain2","dungeon",2,1,[304,9870],[260,200],{
        (0,0):room((0,0),"door",[[0,-1]],None),
        (0,-1):room((0,-1),"battle",[[0,-1],[0,1]],["greengrobble","greengrobble"]),
        (0,-2):room((0,-2),"battle",[[0,-1],[0,1]],["greengrobble","greengrobble","redgrobble"]),
        (0,-3):room((0,-3),"boss",[[0,1]],["greengrobble","redgrobble","greengrobbleking"])}),

    dungeon("plain3","dungeon",3,1,[300,9778],[260,200],{
        (0,0):room((0,0),"door",[[0,-1]],None),
        (0,-1):room((0,-1),"battle",[[0,-1],[0,1]],["redgrobble","redgrobble","redgrobble"]),
        (0,-2):room((0,-2),"chest",[[0,-1],[0,1]],[7,["money",60],["money",10]]),
        (0,-3):room((0,-3),"boss",[[0,1]],["redgrobble","redgrobble","redgrobbleking"])}),

    dungeon("plain4","dungeon",4,1,[284,9700],[260,220],{
        (0,0):room((0,0),"door",[[0,-1]],None),
        (0,-1):room((0,-1),"battle",[[0,-1],[0,1]],["redgrobble","redgrobble"]),
        (0,-2):room((0,-2),"battle",[[0,-1],[0,1]],["yellowgrobble","yellowgrobble"]),
        (0,-3):room((0,-3),"heal",[[0,-1],[0,1]],None),
        (0,-4):room((0,-4),"boss",[[0,1]],["redgrobble","yellowgrobble","redgrobbleking"])}),

    dungeon("plain5","dungeon",5,1,[340,9636],[260,220],{
        (0,0):room((0,0),"door",[[0,-1]],None),
        (0,-1):room((0,-1),"battle",[[0,-1],[0,1]],["yellowgrobble","yellowgrobble"]),
        (0,-2):room((0,-2),"battle",[[0,-1],[0,1]],["yellowgrobble","yellowgrobble"]),
        (0,-3):room((0,-3),"game",[[0,-1],[0,1]],None),
        (0,-4):room((0,-4),"boss",[[0,1]],["yellowgrobble","yellowgrobble","yellowgrobbleking"])}),

    dungeon("plain6","dungeon",6,1,[410,9592],[260,220],{
        (0,0):room((0,0),"door",[[0,-1]],None),
        (0,-1):room((0,-1),"battle",[[0,-1],[0,1]],["yellowgrobble","yellowgrobble"]),
        (0,-2):room((0,-2),"battle",[[0,-1],[0,1],[1,0]],["yellowgrobble","blackgrobble"]),
        (1,-2):room((1,-2),"battle",[[1,0],[-1,0]],["yellowgrobble","blackgrobble"]),
        (2,-2):room((2,-2),"bronzekey",[[-1,0]],None),
        (0,-3):room((0,-3),"bronzelock",[[0,-1],[0,1]],None),
        (0,-4):room((0,-4),"boss",[[0,1]],["yellowgrobble","blackgrobble","yellowgrobbleking"])}),

    dungeon("plain7","dungeon",7,1,[422,9496],[260,300],{
        (0,0):room((0,0),"door",[[0,-1]],None),
        (0,-1):room((0,-1),"battle",[[0,-1],[0,1]],["yellowgrobble","blackgrobble"]),
        (0,-2):room((0,-2),"battle",[[0,-1],[0,1],[1,0],[-1,0]],["yellowgrobble","blackgrobble"]),
        (1,-2):room((1,-2),"battle",[[1,0],[-1,0]],["yellowgrobble","blackgrobble"]),
        (2,-2):room((2,-2),"bronzekey",[[-1,0]],None),
        (-1,-2):room((-1,-2),"bronzelock",[[1,0],[-1,0]],None),
        (-2,-2):room((-2,-2),"battle",[[1,0],[-1,0]],["yellowgrobble","blackgrobble"]),
        (-3,-2):room((-3,-2),"silverkey",[[1,0]],None),
        (0,-3):room((0,-3),"silverlock",[[0,-1],[0,1]],None),
        (0,-4):room((0,-4),"heal",[[0,-1],[0,1]],None),
        (0,-5):room((0,-5),"chest",[[0,-1],[0,1]],[8,["item",1],["money",15]]),
        (0,-6):room((0,-6),"boss",[[0,1]],["yellowgrobble","blackgrobble","yellowgrobbleking"])}),

    dungeon("plain8","dungeon",8,2,[403,9379],[260,220],{
        (0,0):room((0,0),"door",[[0,-1]],None),
        (0,-1):room((0,-1),"battle",[[0,-1],[0,1],[1,0],[-1,0]],["blackgrobble","blackgrobble"]),

        (1,-1):room((1,-1),"battle",[[0,-1],[-1,0]],["blackgrobble","blackgrobble"]),
        (1,-2):room((1,-2),"battle",[[0,1],[-1,0],[1,0]],["blackgrobble","blackgrobble"]),
        (2,-2):room((2,-2),"battle",[[0,-1],[-1,0]],["blackgrobble","blackgrobble"]),
        (2,-3):room((2,-3),"bronzekey",[[0,1]],None),
        
        (-1,-1):room((-1,-1),"bronzelock",[[0,-1],[1,0]],None),
        (-1,-2):room((-1,-2),"battle",[[0,1],[1,0],[-1,0]],["blackgrobble","blackgrobble"]),
        (-2,-2):room((-2,-2),"battle",[[0,-1],[1,0]],["blackgrobble","blackgrobble"]),
        (-2,-3):room((-2,-3),"silverkey",[[0,1]],None),
        
        (0,-2):room((0,-2),"silverlock",[[0,-1],[0,1],[1,0],[-1,0]],None),
        (0,-3):room((0,-3),"game",[[0,-1],[0,1]],None),
        (0,-4):room((0,-4),"boss",[[0,1]],["blackgrobble","blackgrobble","blackgrobbleking"])}),

    dungeon("forest1","forest",9,1,[431,9236],[260,200],{
        (0,0):room((0,0),"door",[[0,-1]],None),
        (0,-1):room((0,-1),"battle",[[0,-1],[0,1]],["deadtree","deadtree"]),
        (0,-2):room((0,-2),"battle",[[0,-1],[0,1]],["deadtree","deadtree"]),
        (0,-3):room((0,-3),"boss",[[0,1]],["deadtree","deadtree","deadtreeking"])}),

    dungeon("forest2","forest",10,1,[405,9116],[260,180],{
        (0,0):room((0,0),"door",[[0,-1]],None),
        (0,-1):room((0,-1),"battle",[[0,-1],[0,1]],["deadtree","deadtree"]),
        (0,-2):room((0,-2),"battle",[[0,1],[1,0]],["deadtree","mushroom"]),
        (1,-2):room((1,-2),"battle",[[0,1],[-1,0]],["deadtree","mushroom"]),
        (1,-1):room((1,-1),"boss",[[0,-1]],["deadtree","deadtree","deadtreeking"])}),

    dungeon("forest3","forest",11,1,[376,9023],[260,180],{
        (0,0):room((0,0),"door",[[0,-1]],None),
        (0,-1):room((0,-1),"battle",[[0,-1],[0,1]],["deadtree","mushroom"]),
        (0,-2):room((0,-2),"battle",[[0,1],[1,0],[-1,0]],["deadtree","mushroom"]),
        (1,-2):room((1,-2),"battle",[[0,1],[-1,0]],["mushroom","mushroom"]),
        (1,-1):room((1,-1),"bronzekey",[[0,-1]],None),
        (-1,-2):room((-1,-2),"bronzelock",[[0,1],[1,0]],None),
        (-1,-1):room((-1,-1),"boss",[[0,-1]],["deadtree","mushroom","deadtreeking"])}),

    dungeon("forest4","mushroom",12,1,[330,8956],[260,180],{
        (0,0):room((0,0),"door",[[0,-1]],None),
        (0,-1):room((0,-1),"battle",[[0,-1],[0,1]],["mushroom","mushroom"]),
        (0,-2):room((0,-2),"battle",[[0,1],[1,0],[-1,0]],["mushroom","mushroom"]),
        (1,-2):room((1,-2),"battle",[[0,1],[-1,0]],["mushroom","mushroom"]),
        (1,-1):room((1,-1),"battle",[[0,-1],[1,0]],["mushroom","mushroom"]),
        (2,-1):room((2,-1),"bronzekey",[[-1,0]],None),
        (-1,-2):room((-1,-2),"bronzelock",[[0,1],[1,0]],None),
        (-1,-1):room((-1,-2),"heal",[[0,-1],[-1,0]],None),
        (-2,-1):room((-2,-1),"boss",[[1,0]],["mushroom","mushroom","mushroomking"])}),

    dungeon("forest5","forest",14,1,[170,8624],[260,180],{
        (0,0):room((0,0),"door",[[0,-1]],None),
        (0,-1):room((0,-1),"battle",[[0,-1],[0,1]],["deadtree","deadtree","deadtree"]),
        (0,-2):room((0,-2),"battle",[[0,1],[1,0],[-1,0]],["deadtree","deadtree","mushroom"]),
        (1,-2):room((1,-2),"battle",[[1,0],[-1,0]],["deadtree","deadtree","mushroom"]),
        (2,-2):room((2,-2),"bronzekey",[[-1,0]],None),
        (-1,-2):room((-1,-2),"bronzelock",[[-1,0],[1,0]],None),
        (-2,-2):room((-2,-2),"boss",[[1,0]],["deadtree","deadtree","deadtree","deadtreeking"])}),

    dungeon("forest6","forest",15,1,[123,8504],[260,180],{
        (0,0):room((0,0),"door",[[0,-1]],None),
        (0,-1):room((0,-1),"battle",[[1,0],[-1,0],[0,1]],["deadtree","deadtree","deadtree"]),
        (1,-1):room((1,-1),"battle",[[1,0],[-1,0]],["deadtree","deadtree","deadtree"]),
        (2,-1):room((2,-1),"battle",[[-1,0],[0,-1]],["deadtree","deadtree","deadtree"]),
        (2,-2):room((2,-2),"battle",[[-1,0],[0,1]],["deadtree","deadtree","deadtree"]),
        (1,-2):room((1,-2),"bronzekey",[[1,0]],None),
        (-1,-1):room((-1,-1),"bronzelock",[[1,0],[-1,0]],None),
        (-2,-1):room((-2,-1),"battle",[[1,0],[0,-1]],["deadtree","deadtree","deadtree","deadtree"]),
        (-2,-2):room((-2,-2),"battle",[[1,0],[0,1]],["deadtree","deadtree","deadtree","deadtree"]),
        (-1,-2):room((-1,-2),"boss",[[-1,0]],["deadtree","deadtree","deadtree","deadtreeking"])}),
    
    dungeon("forest7","forest",16,1,[194,8410],[260,200],{
        (0,0):room((0,0),"door",[[0,-1]],None),
        (0,-1):room((0,-1),"battle",[[1,0],[-1,0],[0,1],[0,-1]],["tree","tree"]),
        (1,-1):room((1,-1),"battle",[[1,0],[-1,0]],["tree","tree"]),
        (2,-1):room((2,-1),"battle",[[-1,0],[0,-1]],["tree","tree"]),
        (2,-2):room((2,-2),"battle",[[-1,0],[0,1]],["tree","tree"]),
        (1,-2):room((1,-2),"bronzekey",[[1,0]],None),
        (-1,-1):room((-1,-1),"bronzelock",[[1,0],[-1,0]],None),
        (-2,-1):room((-2,-1),"battle",[[1,0],[0,-1]],["tree","tree","tree"]),
        (-2,-2):room((-2,-2),"battle",[[1,0],[0,1]],["tree","tree","tree"]),
        (-1,-2):room((-1,-2),"silverkey",[[-1,0]],None),
        (0,-2):room((0,-2),"silverlock",[[0,1],[0,-1]],None),
        (0,-3):room((0,-3),"boss",[[0,1]],["tree","tree","tree","treeking"])}),

    dungeon("forest8","tree",17,2,[288,8393],[280,180],{
        (0,0):room((0,0),"door",[[-1,0]],None),
        (-1,0):room((-1,0),"battle",[[1,0],[0,1],[0,-1]],["treeworm","treeworm"]),
        (-1,-1):room((-1,-1),"battle",[[1,0],[0,1]],["treeworm","treeworm"]),
        (0,-1):room((0,-1),"battle",[[-1,0],[0,-1]],["treeworm","treeworm"]),
        (0,-2):room((0,-2),"battle",[[-1,0],[0,1]],["treeworm","soldiertreeworm"]),
        (-1,-2):room((-1,-2),"bronzekey",[[1,0]],None),

        (-1,1):room((-1,1),"bronzelock",[[1,0],[-1,0],[0,-1]],None),
        (-2,1):room((-2,1),"battle",[[1,0],[0,1]],["treeworm","treeworm"]),
        (-2,2):room((-2,2),"battle",[[-1,0],[0,-1]],["treeworm","treeworm"]),
        (-3,2):room((-3,2),"battle",[[1,0],[0,1]],["treeworm","soldiertreeworm"]),
        (-3,3):room((-3,3),"silverkey",[[0,-1]],None),

        (0,1):room((0,1),"silverlock",[[1,0],[-1,0]],None),
        (1,1):room((1,1),"battle",[[-1,0],[0,1]],["treeworm","treeworm"]),
        (1,2):room((1,2),"battle",[[1,0],[0,-1]],["treeworm","soldiertreeworm"]),
        (2,2):room((2,2),"game",[[-1,0],[0,1]],None),
        (2,3):room((2,3),"boss",[[0,-1]],["soldiertreeworm","soldiertreeworm","soldiertreeworm","treewormqueen"])}),

    dungeon("swamp1","swamp",18,1,[398,8177],[300,100],{
        (0,0):room((0,0),"door",[[0,1]],None),
        (0,1):room((-1,0),"battle",[[-1,0],[0,-1]],["swampdeadtree","swampdeadtree","swampdeadtree"]),
        (-1,1):room((-1,1),"battle",[[-1,0],[1,0],[0,1]],["swampdeadtree","swampdeadtree","swampdeadtree"]),
        (-2,1):room((-2,1),"battle",[[1,0],[0,-1]],["swampdeadtree","swampdeadtree","swampdeadtree"]),
        (-2,0):room((-2,0),"bronzekey",[[0,1]],None),
        (-1,2):room((-1,2),"bronzelock",[[0,1],[0,-1]],None),
        (-1,3):room((-1,3),"battle",[[1,0],[-1,0],[0,-1]],["swampdeadtree","swampdeadtree","swampdeadtree"]),
        (0,3):room((0,3),"battle",[[-1,0],[0,1]],["swampdeadtree","swampdeadtree","swampdeadtree"]),
        (0,4):room((0,4),"silverkey",[[0,-1]],None),
        (-2,3):room((-2,3),"silverlock",[[1,0],[0,1]],None),
        (-2,4):room((-2,4),"boss",[[0,-1]],["swampdeadtree","swampdeadtree","swampdeadtree","swampdeadtreeking"])}),

    dungeon("swamp2","swamp",19,1,[297,8116],[260,220],{
        (0,0):room((0,0),"door",[[0,-1]],None),
        (0,-1):room((0,-1),"battle",[[0,-1],[0,1]],["swampmushroom","swampmushroom","swampmushroom"]),
        (0,-2):room((0,-2),"battle",[[0,1],[1,0],[-1,0]],["swampmushroom","swampmushroom","swampmushroom"]),
        (1,-2):room((1,-2),"battle",[[1,0],[-1,0]],["swampmushroom","swampmushroom","swampmushroom"]),
        (2,-2):room((2,-2),"battle",[[-1,0],[0,1]],["swampmushroom","swampmushroom","swampmushroom"]),
        (2,-1):room((2,-1),"bronzekey",[[0,-1]],None),
        (-1,-2):room((-1,-2),"battle",[[-1,0],[1,0]],["swampmushroom","swampmushroom","swampmushroom"]),
        (-2,-2):room((-2,-2),"bronzelock",[[1,0],[0,1]],None),
        (-2,-1):room((-2,-1),"boss",[[0,-1]],["swampmushroom","swampmushroom","swampmushroom","swampmushroomking"])}),

    dungeon("swamp3","swamp",20,1,[198,8077],[260,240],{
        (0,0):room((0,0),"door",[[0,-1]],None),
        (0,-1):room((0,-1),"battle",[[0,-1],[0,1]],["swampmushroom","swampmushroom","poisonmushroom"]),
        (0,-2):room((0,-2),"battle",[[0,1],[1,0]],["swampmushroom","poisonmushroom","poisonmushroom"]),
        (1,-2):room((1,-2),"battle",[[1,0],[-1,0],[0,-1]],["swampmushroom","swampmushroom","poisonmushroom"]),
        (2,-2):room((2,-2),"battle",[[-1,0],[0,1]],["swampmushroom","swampmushroom","poisonmushroom"]),
        (2,-1):room((2,-1),"bronzekey",[[0,-1]],None),
        (1,-3):room((1,-3),"bronzelock",[[-1,0],[0,1]],None),
        (0,-3):room((0,-3),"battle",[[1,0],[-1,0]],["swampmushroom","poisonmushroom","poisonmushroom"]),
        (-1,-3):room((-1,-3),"battle",[[1,0],[0,1]],["swampmushroom","swampmushroom","poisonmushroom"]),
        (-1,-2):room((-1,-2),"battle",[[-1,0],[0,-1]],["swampmushroom","swampmushroom","poisonmushroom"]),
        (-2,-2):room((-2,-2),"heal",[[1,0],[0,1]],None),
        (-2,-1):room((-2,-1),"boss",[[0,-1]],["swampmushroom","poisonmushroom","poisonmushroom","swampmushroomking"])}),

    dungeon("swamp4","poisonmushroom",21,1,[145,8025],[260,240],{
        (0,0):room((0,0),"door",[[0,-1]],None),
        (0,-1):room((0,-1),"battle",[[0,-1],[0,1]],["poisonmushroom","poisonmushroom","poisonmushroom"]),
        (0,-2):room((0,-2),"battle",[[0,1],[0,-1]],["poisonmushroom","poisonmushroom","poisonmushroom"]),
        (1,-2):room((1,-2),"battle",[[1,0],[-1,0],[0,-1]],["poisonmushroom","poisonmushroom","poisonmushroom"]),
        (2,-2):room((2,-2),"battle",[[-1,0],[0,1]],["poisonmushroom","poisonmushroom","poisonmushroom"]),
        (2,-1):room((2,-1),"battle",[[-1,0],[0,-1]],["poisonmushroom","poisonmushroom","poisonmushroom"]),
        (1,-1):room((1,-1),"bronzekey",[[1,0]],None),
        (1,-3):room((1,-3),"battle",[[-1,0],[0,1]],["poisonmushroom","poisonmushroom","poisonmushroom"]),
        (0,-3):room((0,-3),"battle",[[1,0],[-1,0],[0,1]],["poisonmushroom","poisonmushroom","poisonmushroom"]),
        (-1,-3):room((-1,-3),"bronzelock",[[1,0],[0,1]],None),
        (-1,-2):room((-1,-2),"battle",[[-1,0],[0,-1]],["poisonmushroom","poisonmushroom","poisonmushroom"]),
        (-2,-2):room((-2,-2),"battle",[[1,0],[0,1]],["poisonmushroom","poisonmushroom","poisonmushroom"]),
        (-2,-1):room((-2,-1),"game",[[1,0],[0,-1]],None),
        (-1,-1):room((-1,-1),"boss",[[-1,0]],["poisonmushroom","poisonmushroom","poisonmushroom","poisonmushroomking"])}),

    dungeon("swamp5","swamp",22,1,[193,7899],[220,220],{
        (0,0):room((0,0),"door",[[0,-1]],None),
        (0,-1):room((0,-1),"battle",[[0,1],[0,-1]],["snail","snail"]),
        (0,-2):room((0,-2),"battle",[[0,1],[1,0]],["snail","snail"]),
        (1,-2):room((1,-2),"battle",[[-1,0],[1,0]],["snail","snail"]),
        (2,-2):room((2,-2),"battle",[[-1,0],[0,1]],["snail","snail"]),
        (2,-1):room((2,-1),"battle",[[0,1],[0,-1]],["snail","snail"]),
        (2,0):room((2,0),"battle",[[-1,0],[0,-1]],["snail","snail"]),
        (1,0):room((1,0),"battle",[[1,0],[0,-1]],["snail","snail"]),
        (1,-1):room((1,-1),"boss",[[0,1]],["snail","snail","snailking"])}),

    dungeon("swamp6","swamp",23,1,[293,7873],[160,200],{
        (0,0):room((0,0),"door",[[1,0]],None),
        (1,0):room((1,0),"battle",[[-1,0],[0,-1]],["mudmonster","mudmonster"]),
        (1,-1):room((1,-1),"battle",[[1,0],[0,1]],["mudmonster"]),
        (2,-1):room((2,-1),"battle",[[-1,0],[0,1]],["mudmonster","mudmonster"]),
        (2,0):room((2,0),"battle",[[1,0],[0,-1]],["mudmonster","mudmonster"]),
        (3,0):room((3,0),"battle",[[-1,0],[0,-1]],["mudmonster","mudmonster","mudmonster"]),
        (3,-1):room((3,-1),"battle",[[1,0],[0,1]],["mudmonster"]),
        (4,-1):room((4,-1),"battle",[[-1,0],[0,1]],["mudmonster"]),
        (4,0):room((4,0),"battle",[[1,0],[0,-1]],["mudmonster","mudmonster"]),
        (5,0):room((5,0),"boss",[[-1,0]],["mudmonster","mudmonster","mudmonster","mudking"])}),

    dungeon("swamp7","swamp",24,1,[410,7823],[160,220],{
        (0,0):room((0,0),"door",[[1,0]],None),
        (1,0):room((1,0),"battle",[[-1,0],[1,0],[0,-1]],["mudmonster","mudmonster"]),
        (1,-1):room((1,-1),"battle",[[1,0],[0,1]],["mudmonster"]),
        (2,-1):room((2,-1),"battle",[[-1,0],[0,-1]],["mudmonster","mudmonster","mudmonster"]),
        (2,-2):room((2,-2),"battle",[[0,1],[1,0]],["mudmonster","mudmonster"]),
        (3,-2):room((3,-2),"battle",[[-1,0],[0,1]],["mudmonster"]),
        (3,-1):room((3,-1),"battle",[[0,-1],[1,0]],["mudmonster","mudmonster"]),
        (4,-1):room((4,-1),"bronzekey",[[-1,0]],None),
        (2,0):room((2,0),"bronzelock",[[1,0],[-1,0]],None),
        (3,0):room((3,0),"battle",[[1,0],[-1,0]],["mudmonster","mudmonster","mudmonster"]),
        (4,0):room((4,0),"heal",[[1,0],[-1,0]],None),
        (5,0):room((5,0),"boss",[[-1,0]],["mudmonster","mudmonster","mudmound"])}),

    dungeon("swamp8","swamp",25,2,[398,7703],[180,180],{
        (0,0):room((0,0),"door",[[0,1]],None),
        (0,1):room((0,1),"battle",[[0,-1],[1,0]],["mudmonster","mudmonster"]),
        (1,1):room((1,1),"battle",[[1,0],[-1,0]],["mudmonster"]),
        (2,1):room((2,1),"battle",[[1,0],[-1,0]],["mudmonster","mudmonster","mudmonster"]),
        (3,1):room((3,1),"battle",[[1,0],[-1,0]],["mudmonster","mudmonster"]),
        (4,1):room((4,1),"battle",[[0,-1],[-1,0]],["mudmonster"]),
        (4,0):room((4,0),"battle",[[0,1],[-1,0]],["mudmonster","mudmonster"]),
        (3,0):room((3,0),"battle",[[1,0],[-1,0]],["mudmonster","mudmonster","mudmonster"]),
        (2,0):room((2,0),"battle",[[1,0],[-1,0]],["mudmonster","mudmonster"]),
        (1,0):room((1,0),"battle",[[1,0],[0,-1]],["mudmonster"]),
        (1,-1):room((1,-1),"battle",[[1,0],[0,1]],["mudmonster","mudmonster"]),
        (2,-1):room((2,-1),"heal",[[1,0],[-1,0]],None),
        (3,-1):room((3,-1),"boss",[[-1,0]],["mudhill"])}),

    dungeon("cave1","cave",26,1,[375,7440],[260,240],{
        (0,0):room((0,0),"door",[[0,-1]],None),
        (0,-1):room((0,-1),"battle",[[1,0],[-1,0],[0,1],[0,-1]],["bat","bat","bat"]),
        (0,-2):room((0,-2),"silverlock",[[0,1],[0,-1]],None),
        (0,-3):room((0,-3),"boss",[[0,1]],["bat","bat","bat","batking"]),
        (1,-1):room((1,-1),"battle",[[-1,0],[0,-1]],["bat","bat","bat"]),
        (1,-2):room((1,-2),"battle",[[1,0],[0,1]],["bat","bat","bat"]),
        (2,-2):room((2,-2),"battle",[[-1,0],[0,1]],["bat","bat","bat"]),
        (2,-1):room((2,-1),"bronzekey",[[0,-1]],["bat","bat","bat"]),
        (-1,-1):room((-1,-1),"bronzelock",[[1,0],[0,-1]],["bat","bat","bat"]),
        (-1,-2):room((-1,-2),"battle",[[-1,0],[0,1]],["bat","bat","bat"]),
        (-2,-2):room((-2,-2),"battle",[[1,0],[0,1]],["bat","bat","bat"]),
        (-2,-1):room((-2,-1),"silverkey",[[0,-1]],["bat","bat","bat"])}),

    dungeon("cave2","cave",27,1,[252,7386],[220,220],{
        (0,0):room((0,0),"door",[[1,0]],None),
        (1,0):room((1,0),"battle",[[-1,0],[1,0]],["rockmonster","rockmonster"]),
        (2,0):room((2,0),"battle",[[-1,0],[0,-1]],["rockmonster","rockmonster"]),
        (2,-1):room((2,-1),"battle",[[-1,0],[0,1]],["rockmonster","rockmonster"]),
        (1,-1):room((1,-1),"battle",[[-1,0],[1,0]],["rockmonster","rockmonster"]),
        (0,-1):room((0,-1),"battle",[[1,0],[0,-1]],["rockmonster","rockmonster"]),
        (0,-2):room((0,-2),"battle",[[1,0],[0,1]],["rockmonster","rockmonster"]),
        (1,-2):room((1,-2),"battle",[[1,0],[-1,0]],["rockmonster","rockmonster"]),
        (2,-2):room((2,-2),"boss",[[-1,0]],["rockmonster","rockmonster","rockmonster","rockking"])}),

    dungeon("cave3","cave",28,1,[133,7337],[320,220],{
        (0,0):room((0,0),"door",[[-1,0]],None),
        (-1,0):room((-1,0),"battle",[[1,0],[-1,0]],["bouldermonster","bouldermonster"]),
        (-2,0):room((-2,0),"battle",[[1,0],[-1,0]],["bouldermonster","bouldermonster"]),
        (-3,0):room((-3,0),"battle",[[1,0],[0,-1]],["bouldermonster","bouldermonster"]),
        (-3,-1):room((-3,-1),"battle",[[0,1],[0,-1]],["bouldermonster","bouldermonster"]),
        (-3,-2):room((-3,-2),"battle",[[1,0],[0,1]],["bouldermonster","bouldermonster"]),
        (-2,-2):room((-2,-2),"battle",[[1,0],[-1,0]],["bouldermonster","bouldermonster"]),
        (-1,-2):room((-1,-2),"battle",[[1,0],[-1,0]],["bouldermonster","bouldermonster"]),
        (0,-2):room((0,-2),"boss",[[-1,0]],["bouldermonster","bouldermonster","bouldermonster","boulderking"])}),

    dungeon("cave4","cave",29,1,[45,7214],[260,220],{
        (0,0):room((0,0),"door",[[0,-1]],None),
        (0,-1):room((0,-1),"battle",[[0,1],[0,-1]],["driller","driller"]),
        (0,-2):room((0,-2),"battle",[[1,0],[-1,0],[0,1]],["driller","driller"]),
        (-1,-2):room((-1,-2),"battle",[[1,0],[-1,0]],["driller","driller"]),
        (-2,-2):room((-2,-2),"battle",[[1,0],[0,1]],["driller","driller"]),
        (-2,-1):room((-2,-1),"battle",[[1,0],[0,-1]],["driller","driller"]),
        (-1,-1):room((-1,-1),"battle",[[-1,0],[0,1]],["driller","driller"]),
        (-1,0):room((-1,0),"battle",[[-1,0],[0,-1]],["driller","driller"]),
        (-2,0):room((-2,0),"bronzekey",[[1,0]],None),
        (1,-2):room((1,-2),"bronzelock",[[-1,0],[1,0]],None),
        (2,-2):room((2,-2),"battle",[[-1,0],[0,1]],["driller","driller"]),
        (2,-1):room((2,-1),"battle",[[-1,0],[0,-1]],["driller","driller"]),
        (1,-1):room((1,-1),"battle",[[1,0],[0,1]],["driller","driller"]),
        (1,0):room((1,0),"game",[[1,0],[0,-1]],None),
        (2,0):room((2,0),"boss",[[-1,0]],["driller","driller","driller","drillerking"])}),

    dungeon("cave5","hauntedmineshaft",30,1,[45,7077],[340,100],{
        (0,0):room((0,0),"door",[[-1,0]],None),
        (-1,0):room((-1,0),"battle",[[1,0],[-1,0]],["skeletonminer","skeletonminer"]),
        (-2,0):room((-2,0),"battle",[[1,0],[-1,0],[0,1]],["skeletonminer","skeletonminer"]),
        (-3,0):room((-3,0),"battle",[[1,0],[-1,0]],["skeletonminer","skeletonminer"]),
        (-4,0):room((-4,0),"bronzekey",[[1,0]],["skeletonminer","skeletonminer"]),
        (-2,1):room((-2,1),"bronzelock",[[0,1],[0,-1]],["skeletonminer","skeletonminer"]),
        (-2,2):room((-2,2),"battle",[[0,1],[0,-1]],["skeletonminer","skeletonminer"]),
        (-2,3):room((-2,3),"battle",[[0,1],[0,-1]],["skeletonminer","skeletonminer"]),
        (-2,4):room((-2,4),"boss",[[0,-1]],["skeletonminer","skeletonminer","skeletonminer","rockskeleton"])}),

    dungeon("cave6","mineshaft",31,1,[52,6971],[340,100],{
        (0,0):room((0,0),"door",[[-1,0]],None),
        (-1,0):room((-1,0),"battle",[[1,0],[-1,0]],["mole","mole"]),
        (-2,0):room((-2,0),"battle",[[1,0],[-1,0],[0,1]],["mole","mole"]),
        (-3,0):room((-3,0),"battle",[[1,0],[-1,0]],["mole","mole"]),
        (-4,0):room((-4,0),"bronzekey",[[1,0]],["mole","mole"]),
        (-2,1):room((-2,1),"bronzelock",[[0,1],[0,-1]],["mole","mole"]),
        (-2,2):room((-2,2),"battle",[[0,1],[0,-1]],["mole","mole"]),
        (-2,3):room((-2,3),"battle",[[0,1],[0,-1]],["mole","mole"]),
        (-2,4):room((-2,4),"battle",[[-1,0],[0,-1]],["mole","mole"]),
        (-3,4):room((-3,4),"battle",[[-1,0],[1,0]],["mole","mole"]),
        (-4,4):room((-4,4),"boss",[[1,0]],["mole","mole","mole","moleknight"])}),

    dungeon("cave7","cavecity",32,1,[178,6885],[260,260],{
        (0,0):room((0,0),"door",[[0,-1]],None),
        (0,-1):room((0,-1),"battle",[[0,-1],[0,1]],["moleguard","moleguard"]),
        (0,-2):room((0,-2),"battle",[[1,0],[-1,0],[0,1],[0,-1]],["moleguard","moleguard"]),
        (0,-3):room((0,-3),"silverlock",[[0,1],[0,-1]],None),
        (0,-4):room((0,-4),"boss",[[0,1]],["moleguard","moleguard","moleguard","moleknight"]),
        (-1,-2):room((-1,-2),"battle",[[1,0],[0,1]],["moleguard","moleguard"]),
        (-1,-1):room((-1,-1),"battle",[[-1,0],[0,-1]],["moleguard","moleguard"]),
        (-2,-1):room((-2,-1),"battle",[[1,0],[0,-1]],["moleguard","moleguard"]),
        (-2,-2):room((-2,-2),"battle",[[0,1],[0,-1]],["moleguard","moleguard"]),
        (-2,-3):room((-2,-3),"bronzekey",[[0,1]],None),
        (1,-2):room((1,-2),"bronzelock",[[-1,0],[0,-1]],None),
        (1,-3):room((1,-3),"battle",[[1,0],[0,1]],["moleguard","moleguard"]),
        (2,-3):room((2,-3),"battle",[[-1,0],[0,-1]],["moleguard","moleguard"]),
        (2,-4):room((2,-4),"silverkey",[[0,1]],None)}),

    dungeon("cave8","cavecity",33,2,[350,6868],[220,240],{
        (0,0):room((0,0),"door",[[0,-1]],None),
        (-2,-3):room((-2,-3),"bronzekey",[[0,1]],None),
        (0,-3):room((0,-3),"boss",[[0,1]],["moleguard","moleguard","moleguard","moleking"]),
        (1,-3):room((1,-3),"battle",[[1,0],[0,1]],["moleguard","moleguard"]),
        (2,-3):room((2,-3),"battle",[[-1,0],[0,1]],["moleguard","moleguard"]),
        (3,-3):room((3,-3),"battle",[[1,0],[0,1]],["moleguard","moleguard"]),
        (4,-3):room((4,-3),"goldkey",[[-1,0]],None),
        (-2,-2):room((-2,-2),"battle",[[0,1],[0,-1]],["moleguard","moleguard"]),
        (-1,-2):room((-1,-2),"goldlock",[[1,0],[0,1]],None),
        (0,-2):room((0,-2),"game",[[-1,0],[0,-1]],None),
        (1,-2):room((1,-2),"battle",[[0,1],[0,-1]],["moleguard","moleguard"]),
        (2,-2):room((2,-2),"silverkey",[[0,-1]],None),
        (3,-2):room((3,-2),"battle",[[0,1],[0,-1]],["moleguard","moleguard"]),
        (-2,-1):room((-2,-1),"battle",[[1,0],[0,-1]],["moleguard","moleguard"]),
        (-1,-1):room((-1,-1),"battle",[[1,0],[-1,0],[0,-1]],["moleguard","moleguard"]),
        (0,-1):room((0,-1),"battle",[[1,0],[-1,0],[0,1]],["moleguard","moleguard"]),
        (1,-1):room((1,-1),"bronzelock",[[1,0],[-1,0],[0,-1]],["moleguard","moleguard"]),
        (2,-1):room((2,-1),"silverlock",[[1,0],[-1,0]],None),
        (3,-1):room((3,-1),"battle",[[-1,0],[0,-1]],["moleguard","moleguard"])}),

    dungeon("desert1","desert",34,1,[405,6602],[260,280],{
        (0,0):room((0,0),"door",[[0,-1]],None),
        (0,-1):room((0,-1),"battle",[[0,1],[0,-1]],["cactus","cactus","cactus"]),
        (0,-2):room((0,-2),"battle",[[0,1],[0,-1],[1,0],[-1,0]],["cactus","cactus","cactus"]),
        (0,-3):room((0,-3),"bronzelock",[[0,1],[0,-1]],None),
        (0,-4):room((0,-4),"bronzelock",[[0,1],[0,-1]],None),
        (0,-5):room((0,-5),"boss",[[0,1]],["cactus","cactus","cactusking",]),
        (1,-2):room((1,-2),"battle",[[1,0],[-1,0]],["cactus","cactus","cactus"]),
        (2,-2):room((2,-2),"battle",[[-1,0],[0,-1]],["cactus","cactus","cactus"]),
        (2,-3):room((2,-3),"battle",[[0,1],[0,-1]],["cactus","cactus","cactus"]),
        (2,-4):room((2,-4),"bronzekey",[[0,1]],None),
        (-1,-2):room((-1,-2),"battle",[[1,0],[-1,0]],["cactus","cactus","cactus"]),
        (-2,-2):room((-2,-2),"battle",[[1,0],[0,-1]],["cactus","cactus","cactus"]),
        (-2,-3):room((-2,-3),"battle",[[0,1],[0,-1]],["cactus","cactus","cactus"]),
        (-2,-4):room((-2,-4),"bronzekey",[[0,1]],None)}),

    dungeon("desert2","desert",35,1,[335,6483],[140,220],{
        (0,0):room((0,0),"door",[[1,0]],None),
        (1,0):room((1,0),"battle",[[-1,0],[0,-1]],["skeleton","skeleton","skeleton"]),
        (1,-1):room((1,-1),"battle",[[1,0],[0,1],[0,-1]],["skeleton","skeleton","skeleton"]),
        (1,-2):room((1,-2),"battle",[[-1,0],[0,1]],["skeleton","skeleton","skeleton"]),
        (0,-2):room((0,-2),"bronzekey",[[1,0]],None),
        (2,-1):room((2,-1),"bronzelock",[[1,0],[-1,0]],None),
        (3,-1):room((3,-1),"battle",[[1,0],[-1,0]],["skeleton","skeleton","skeleton"]),
        (4,-1):room((4,-1),"battle",[[1,0],[-1,0]],["skeleton","skeleton","skeleton"]),
        (5,-1):room((5,-1),"battle",[[-1,0],[0,1],[0,-1]],["skeleton","skeleton","skeleton"]),
        (5,-2):room((5,-2),"battle",[[1,0],[0,1]],["skeleton","skeleton","skeleton"]),
        (6,-2):room((6,-2),"silverkey",[[-1,0]],None),
        (5,0):room((5,0),"silverlock",[[0,-1],[1,0]],None),
        (6,0):room((6,0),"boss",[[-1,0]],["skeleton","skeleton","skeleton","skeletongiant"])}),

    dungeon("desert3","desert",36,1,[240,6406],[260,340],{
        (0,0):room((0,0),"door",[[0,-1]],None),
        (0,-1):room((0,-1),"battle",[[1,0],[-1,0],[0,1],[0,-1]],["skeleton","skeleton","skeleton"]),
        (-1,-1):room((-1,-1),"battle",[[1,0],[-1,0]],["skeleton","skeleton","skeleton"]),
        (-2,-1):room((-2,-1),"bronzekey",[[1,0]],None),
        (1,-1):room((1,-1),"battle",[[1,0],[-1,0]],["skeleton","skeleton","skeleton"]),
        (2,-1):room((2,-1),"bronzekey",[[-1,0]],None),
        (0,-2):room((0,-2),"bronzelock",[[0,1],[0,-1]],None),
        (0,-3):room((0,-3),"bronzelock",[[0,1],[0,-1]],None),
        (0,-4):room((0,-4),"battle",[[1,0],[-1,0],[0,1],[0,-1]],["skeleton","skeleton","skeleton"]),
        (-1,-4):room((-1,-4),"battle",[[1,0],[-1,0]],["skeleton","skeleton","skeleton"]),
        (-2,-4):room((-2,-4),"bronzekey",[[1,0]],None),
        (1,-4):room((1,-4),"battle",[[1,0],[-1,0]],["skeleton","skeleton","skeleton"]),
        (2,-4):room((2,-4),"bronzekey",[[-1,0]],None),
        (0,-5):room((0,-5),"bronzelock",[[0,1],[0,-1]],None),
        (0,-6):room((0,-6),"bronzelock",[[0,1],[0,-1]],None),
        (0,-7):room((0,-7),"battle",[[-1,0],[0,1]],["skeleton","skeleton","skeleton"]),
        (-1,-7):room((-1,-7),"battle",[[1,0],[0,-1]],["skeleton","skeleton","skeleton"]),
        (-1,-8):room((-1,-8),"battle",[[1,0],[0,1]],["skeleton","skeleton","skeleton"]),
        (0,-8):room((0,-8),"battle",[[1,0],[-1,0]],["skeleton","skeleton","skeleton"]),
        (1,-8):room((1,-8),"heal",[[-1,0],[0,1]],None),
        (1,-7):room((1,-7),"boss",[[0,-1]],["skeletonserpent"])}),

    dungeon("desert4","desert",37,1,[160,6300],[140,40],{
        (0,0):room((0,0),"door",[[0,1]],None),
        (0,1):room((0,1),"battle",[[1,0],[0,-1]],["scorpion","scorpion","scorpion"]),
        (1,1):room((1,1),"battle",[[1,0],[-1,0],[0,1]],["scorpion","scorpion","scorpion"]),
        (2,1):room((2,1),"silverlock",[[-1,0],[0,-1]],None),
        (2,0):room((2,0),"goldkey",[[0,1]],None),
        (1,2):room((1,2),"battle",[[0,1],[0,-1]],["scorpion","scorpion","scorpion"]),
        (1,3):room((1,3),"battle",[[1,0],[0,-1]],["scorpion","scorpion","scorpion"]),
        (2,3):room((2,3),"battle",[[1,0],[-1,0]],["scorpion","scorpion","scorpion"]),
        (3,3):room((3,3),"battle",[[1,0],[-1,0],[0,1]],["scorpion","scorpion","scorpion"]),
        (4,3):room((4,3),"battle",[[1,0],[-1,0]],["scorpion","scorpion","scorpion"]),
        (5,3):room((5,3),"battle",[[-1,0],[0,-1]],["scorpion","scorpion","scorpion"]),
        (5,2):room((5,2),"battle",[[0,1],[0,-1]],["scorpion","scorpion","scorpion"]),
        (5,1):room((5,1),"battle",[[1,0],[-1,0],[0,1]],["scorpion","scorpion","scorpion"]),
        (4,1):room((4,1),"battle",[[1,0],[0,-1]],["scorpion","scorpion","scorpion"]),
        (4,0):room((4,0),"bronzekey",[[0,1]],None),
        (6,1):room((6,1),"bronzelock",[[-1,0],[0,-1]],None),
        (6,0):room((6,0),"silverkey",[[0,1]],None),
        (3,4):room((3,4),"goldlock",[[0,1],[0,-1]],None),
        (3,5):room((3,5),"battle",[[0,1],[0,-1]],["scorpion","scorpion","scorpion"]),
        (3,6):room((3,6),"battle",[[-1,0],[0,-1]],["scorpion","scorpion","scorpion"]),
        (2,6):room((2,6),"battle",[[1,0],[0,1]],["scorpion","scorpion","scorpion"]),
        (2,7):room((2,7),"game",[[-1,0],[0,-1]],["scorpion","scorpion","scorpion"]),
        (1,7):room((1,7),"boss",[[1,0]],["scorpion","scorpion","scorpionking"])}),
        
    dungeon("desert5","bandithideout",39,1,[144,5947],[260,300],{
        (0,0):room((0,0),"door",[[0,-1]],None),
        (0,-1):room((0,-1),"battle",[[0,1],[0,-1]],["bandit","bandit","bandit"]),
        (0,-2):room((0,-2),"battle",[[1,0],[-1,0],[0,1],[0,-1]],["bandit","bandit","bandit"]),
        (-1,-2):room((-1,-2),"battle",[[1,0],[0,1]],["bandit","bandit","bandit"]),
        (-1,-1):room((-1,-1),"battle",[[-1,0],[0,-1]],["bandit","bandit","bandit"]),
        (-2,-1):room((-2,-1),"chest",[[1,0],[0,-1]],[9,["item",101],["item",101]]),
        (-2,-2):room((-2,-2),"bronzekey",[[0,1]],None),
        (1,-2):room((1,-2),"bronzelock",[[-1,0],[0,1]],None),
        (1,-1):room((1,-1),"battle",[[1,0],[0,-1]],["bandit","bandit","bandit","bandit"]),
        (2,-1):room((2,-1),"chest",[[-1,0],[0,-1]],[10,["money",100],["money",50]]),
        (2,-2):room((2,-2),"silverkey",[[0,1]],None),

        (0,-3):room((0,-3),"battle",[[0,1],[0,-1]],["bandit","bandit","bandit"]),
        (0,-4):room((0,-4),"battle",[[1,0],[-1,0],[0,1],[0,-1]],["bandit","bandit","bandit"]),
        (-1,-4):room((-1,-4),"silverlock",[[1,0],[0,1]],None),
        (-1,-3):room((-1,-3),"battle",[[-1,0],[0,-1]],["bandit","bandit","bandit"]),
        (-2,-3):room((-2,-3),"chest",[[1,0],[0,-1]],[11,["item",105],["item",105]]),
        (-2,-4):room((-2,-4),"goldkey",[[0,1]],None),
        (1,-4):room((1,-4),"goldlock",[[-1,0],[0,1]],None),
        (1,-3):room((1,-3),"battle",[[1,0],[0,-1]],["bandit","bandit","bandit","bandit"]),
        (2,-3):room((2,-3),"chest",[[-1,0],[0,-1]],[12,["item",97],["item",97]]),
        (2,-4):room((2,-4),"magickey",[[0,1]],None),

        (0,-5):room((0,-5),"magiclock",[[-1,0],[0,1]],None),
        (-1,-5):room((-1,-5),"battle",[[1,0],[0,-1]],["bandit","bandit","bandit"]),
        (-1,-6):room((-1,-6),"battle",[[1,0],[0,1]],["bandit","bandit","bandit"]),
        (0,-6):room((0,-6),"chest",[[1,0],[-1,0]],[13,["item",109],["item",109]]),
        (1,-6):room((1,-6),"game",[[-1,0],[0,1]],None),
        (1,-5):room((1,-5),"boss",[[0,-1]],["bandit","bandit","bandit","banditking"])}),

    dungeon("desert6","statueroad",40,1,[129,5826],[260,260],{
        (0,0):room((0,0),"door",[[0,-1]],None),
        (0,-1):room((0,-1),"battle",[[0,1],[0,-1]],["statue","statue"]),
        (0,-2):room((0,-2),"battle",[[0,1],[0,-1]],["statue","statue"]),
        (0,-3):room((0,-3),"battle",[[0,1],[0,-1]],["statue","statue"]),
        (0,-4):room((0,-4),"boss",[[0,1]],["statue","statueking"])}),

    dungeon("desert7","pyramid",41,1,[128,5758],[260,260],{
        (-2,-4):room((-2,-4),"battle",[[1,0],[0,1]],["mummy","mummy","mummy"]),
        (-1,-4):room((-1,-4),"battle",[[1,0],[-1,0],[0,1]],["mummy","mummy","mummy"]),
        (0,-4):room((0,-4),"battle",[[-1,0],[0,1]],["mummy","mummy","mummy"]),
        (1,-4):room((1,-4),"battle",[[1,0],[0,1]],["mummy","mummy","mummy"]),
        (2,-4):room((2,-4),"battle",[[-1,0],[0,1]],["mummy","mummy","mummy"]),
        
        (-2,-3):room((-2,-3),"magickey",[[0,-1]],None),
        (-1,-3):room((-1,-3),"battle",[[0,1],[0,-1]],["mummy","mummy","mummy"]),
        (0,-3):room((0,-3),"magiclock",[[0,1],[0,-1]],None),
        (1,-3):room((1,-3),"silverlock",[[0,1],[0,-1]],None),
        (2,-3):room((2,-3),"goldkey",[[0,-1]],None),
        
        (-2,-2):room((-2,-2),"goldlock",[[1,0],[0,1]],None),
        (-1,-2):room((-1,-2),"battle",[[-1,0],[0,-1]],["mummy","mummy","mummy"]),
        (0,-2):room((0,-2),"boss",[[0,-1]],["mummy","mummy","mummy","pharoh"]),
        (1,-2):room((1,-2),"battle",[[1,0],[0,1],[0,-1]],["mummy","mummy","mummy"]),
        (2,-2):room((2,-2),"battle",[[-1,0],[0,1]],["mummy","mummy","mummy"]),
        
        (-2,-1):room((-2,-1),"battle",[[1,0],[0,1],[0,-1]],["mummy","mummy","mummy"]),
        (-1,-1):room((-1,-1),"battle",[[1,0],[-1,0]],["mummy","mummy","mummy"]),
        (0,-1):room((0,-1),"battle",[[1,0],[-1,0],[0,1]],["mummy","mummy","mummy"]),
        (1,-1):room((1,-1),"bronzelock",[[-1,0],[0,-1]],None),
        (2,-1):room((2,-1),"battle",[[0,1],[0,-1]],["mummy","mummy","mummy"]),
        
        (-2,0):room((-2,0),"battle",[[1,0],[0,-1]],["mummy","mummy","mummy"]),
        (-1,0):room((-1,0),"bronzekey",[[-1,0]],None),
        (0,0):room((0,0),"door",[[0,-1]],None),
        (1,0):room((1,0),"silverkey",[[1,0]],None),
        (2,0):room((2,0),"battle",[[-1,0],[0,-1]],["mummy","mummy","mummy"])}),

    dungeon("desert8","pyramid",42,2,[52,5609],[260,320],{
        (0,0):room((0,0),"door",[[0,-1]],None),
        (0,-1):room((0,-1),"battle",[[1,0],[-1,0],[0,1],[0,-1]],["mummy","mummy","mummy"]),
        (-1,-1):room((-1,-1),"battle",[[1,0],[0,-1]],["mummy","mummy","mummy"]),
        (-1,-2):room((-1,-2),"battle",[[-1,0],[0,1],[0,-1]],["mummy","mummy","mummy"]),
        (-2,-2):room((-2,-2),"battle",[[1,0],[0,-1]],["mummy","mummy","mummy"]),
        (1,-1):room((1,-1),"battle",[[-1,0],[0,-1]],["mummy","mummy","mummy"]),
        (1,-2):room((1,-2),"battle",[[1,0],[0,1],[0,-1]],["mummy","mummy","mummy"]),
        (2,-2):room((2,-2),"battle",[[-1,0],[0,-1]],["mummy","mummy","mummy"]),
        (-2,-3):room((-2,-3),"battle",[[0,1],[0,-1]],["mummy","mummy","mummy"]),
        (-2,-4):room((-2,-4),"battle",[[0,1],[0,-1]],["mummy","mummy","mummy"]),
        (-2,-5):room((-2,-5),"battle",[[0,1],[0,-1]],["mummy","mummy","mummy"]),
        (-2,-6):room((-2,-6),"bronzekey",[[0,1]],None),
        (-1,-3):room((-1,-3),"battle",[[0,1],[0,-1]],["mummy","mummy","mummy"]),
        (-1,-4):room((-1,-4),"battle",[[0,1],[0,-1]],["mummy","mummy","mummy"]),
        (-1,-5):room((-1,-5),"battle",[[0,1],[0,-1]],["mummy","mummy","mummy"]),
        (-1,-6):room((-1,-6),"silverkey",[[0,1]],None),
        (1,-3):room((1,-3),"battle",[[0,1],[0,-1]],["mummy","mummy","mummy"]),
        (1,-4):room((1,-4),"battle",[[0,1],[0,-1]],["mummy","mummy","mummy"]),
        (1,-5):room((1,-5),"battle",[[0,1],[0,-1]],["mummy","mummy","mummy"]),
        (1,-6):room((1,-6),"goldkey",[[0,1]],None),
        (2,-3):room((2,-3),"battle",[[0,1],[0,-1]],["mummy","mummy","mummy"]),
        (2,-4):room((2,-4),"battle",[[0,1],[0,-1]],["mummy","mummy","mummy"]),
        (2,-5):room((2,-5),"battle",[[0,1],[0,-1]],["mummy","mummy","mummy"]),
        (2,-6):room((2,-6),"magickey",[[0,1]],None),
        (0,-2):room((0,-3),"bronzelock",[[0,1],[0,-1]],None),
        (0,-3):room((0,-3),"silverlock",[[0,1],[0,-1]],None),
        (0,-4):room((0,-4),"goldlock",[[0,1],[0,-1]],None),
        (0,-5):room((0,-5),"magiclock",[[0,1],[0,-1]],None),
        (0,-6):room((0,-6),"game",[[0,1],[0,-1]],None),
        (0,-7):room((0,-7),"boss",[[0,1]],["mummy","mummy","sphinx"])}),

    dungeon("beach1","beach",43,1,[44,5457],[320,260],{
        (0,0):room((0,0),"door",[[-1,0]],None),
        (-1,0):room((-1,0),"battle",[[1,0],[-1,0]],["hermitcrab","hermitcrab","hermitcrab"]),
        (-2,0):room((-2,0),"battle",[[1,0],[-1,0]],["hermitcrab","hermitcrab"]),
        (-3,0):room((-3,0),"battle",[[1,0],[0,-1]],["hermitcrab","hermitcrab"]),
        (-3,-1):room((-3,-1),"battle",[[1,0],[0,1]],["hermitcrab","hermitcrab","hermitcrab"]),
        (-2,-1):room((-2,-1),"battle",[[1,0],[-1,0]],["hermitcrab","hermitcrab","hermitcrab"]),
        (-1,-1):room((-1,-1),"battle",[[-1,0],[0,-1]],["hermitcrab","hermitcrab"]),
        (-1,-2):room((-1,-2),"battle",[[-1,0],[0,1]],["hermitcrab","hermitcrab","hermitcrab"]),
        (-2,-2):room((-2,-2),"battle",[[1,0],[0,-1]],["hermitcrab","hermitcrab"]),
        (-2,-3):room((-2,-3),"battle",[[1,0],[0,1]],["hermitcrab","hermitcrab"]),
        (-1,-3):room((-1,-3),"battle",[[-1,0],[0,-1]],["hermitcrab","hermitcrab"]),
        (-1,-4):room((-1,-4),"boss",[[0,1]],["hermitcrab","hermitcrab","hermitcrab","hermitcrabking"])}),

    dungeon("beach2","beach",44,1,[78,5411],[340,280],{
        (0,0):room((0,0),"door",[[-1,0]],None),
        (-1,0):room((-1,0),"battle",[[1,0],[0,-1]],["crab","crab"]),
        (-1,-1):room((-1,-1),"battle",[[1,0],[-1,0],[0,1]],["crab","hermitcrab"]),
        (0,-1):room((0,-1),"battle",[[-1,0],[0,-1]],["hermitcrab"]),
        (0,-2):room((0,-2),"battle",[[-1,0],[0,1],[0,-1]],["crab"]),
        (-1,-2):room((-1,-2),"battle",[[1,0],[0,-1]],["crab","crab"]),
        (-1,-3):room((-1,-3),"bronzekey",[[0,1]],None),
        (0,-3):room((0,-3),"battle",[[0,1],[0,-1]],["crab","crab"]),
        (0,-4):room((0,-4),"battle",[[-1,0],[0,1]],["crab","hermitcrab"]),
        (-1,-4):room((-1,-4),"battle",[[1,0],[-1,0],[0,-1]],["crab","crab"]),
        (-2,-4):room((-2,-4),"bronzekey",[[1,0]],None),
        (-1,-5):room((-1,-5),"battle",[[-1,0],[0,1]],["hermitcrab"]),
        (-2,-5):room((-2,-5),"battle",[[1,0],[-1,0]],["crab","crab"]),
        (-3,-5):room((-3,-5),"bronzekey",[[1,0]],None),
        (-2,-1):room((-2,-1),"bronzelock",[[1,0],[0,-1]],None),
        (-2,-2):room((-2,-2),"battle",[[-1,0],[0,1]],["crab","crab"]),
        (-3,-2):room((-3,-2),"bronzelock",[[1,0],[0,-1]],None),
        (-3,-3):room((-3,-3),"battle",[[-1,0],[0,1]],["crab","crab","hermitcrab"]),
        (-4,-3):room((-4,-3),"bronzelock",[[1,0],[0,-1]],None),
        (-4,-4):room((-4,-4),"boss",[[0,1]],["crab","hermitcrab","crab","crabking"])}),

    dungeon("beach3","beach",45,1,[115,5454],[120,120],{
        (0,0):room((0,0),"door",[[1,0]],None),
        (1,0):room((1,0),"battle",[[-1,0],[0,1]],["seagull","seagull"]),
        (1,1):room((1,1),"battle",[[1,0],[0,-1]],["seagull","crab"]),
        (2,1):room((2,1),"battle",[[-1,0],[0,1]],["seagull"]),
        (2,2):room((2,2),"battle",[[1,0],[0,-1]],["crab","hermitcrab"]),
        (3,2):room((3,2),"battle",[[-1,0],[0,1]],["seagull","crab","hermitcrab"]),
        (3,3):room((3,3),"battle",[[1,0],[0,-1]],["seagull","seagull"]),
        (4,3):room((4,3),"battle",[[-1,0],[0,-1]],["hermitcrab","seagull"]),
        (4,2):room((4,2),"battle",[[1,0],[0,1]],["seagull"]),
        (5,2):room((5,2),"battle",[[-1,0],[0,-1]],["seagull","seagull","seagull"]),
        (5,1):room((5,1),"battle",[[1,0],[0,1]],["crab","crab"]),
        (6,1):room((6,1),"battle",[[-1,0],[0,-1]],["seagull","hermitcrab"]),
        (6,0):room((6,0),"battle",[[1,0],[0,1]],["seagull","seagull","seagull"]),
        (7,0):room((7,0),"boss",[[-1,0]],["seagull","crab","seagull","seagullking"])}),

    dungeon("beach4","beach",46,1,[141,5408],[320,240],{
        (0,0):room((0,0),"door",[[-1,0]],None),
        (-1,0):room((-1,0),"battle",[[1,0],[-1,0]],["sandmonster","sandmonster"]),
        (-2,0):room((-2,0),"battle",[[1,0],[-1,0]],["sandmonster","sandmonster","sandmonster"]),
        (-3,0):room((-3,0),"battle",[[1,0],[0,-1]],["sandmonster","sandmonster"]),
        (-3,-1):room((-3,-1),"battle",[[1,0],[0,1]],["sandmonster","sandmonster"]),
        (-2,-1):room((-2,-1),"battle",[[1,0],[-1,0]],["sandmonster"]),
        (-1,-1):room((-1,-1),"battle",[[1,0],[-1,0]],["sandmonster","crab"]),
        (0,-1):room((0,-1),"battle",[[-1,0],[0,-1]],["sandmonster"]),
        (0,-2):room((0,-2),"battle",[[-1,0],[0,1]],["sandmonster","hermitcrab","crab"]),
        (-1,-2):room((-1,-2),"battle",[[1,0],[-1,0]],["seagull","seagull"]),
        (-2,-2):room((-2,-2),"battle",[[1,0],[-1,0]],["sandmonster","seagull"]),
        (-3,-2):room((-3,-2),"battle",[[1,0],[0,-1]],["sandmonster","sandmonster","sandmonster"]),
        (-3,-3):room((-3,-3),"battle",[[1,0],[0,1]],["sandmonster","hermitcrab"]),
        (-2,-3):room((-2,-3),"battle",[[1,0],[-1,0]],["sandmonster","crab","hermitcrab","seagull"]),
        (-1,-3):room((-1,-3),"battle",[[1,0],[-1,0]],["sandmonster","sandmonster","sandmonster"]),
        (0,-3):room((0,-3),"boss",[[-1,0]],["sandmonster","seagull","sandmonster","sandking"])}),

    dungeon("beach5","sandcastle",47,1,[189,5445],[260,300],{
        (-3,-6):room((-3,-6),"goldkey",[[0,1]],None),
        (-1,-6):room((-1,-6),"goldkey",[[0,1]],None),
        (1,-6):room((0,-6),"magickey",[[0,1]],None),
        (3,-6):room((3,-6),"magickey",[[0,1]],None),

        (-3,-5):room((-3,-5),"battle",[[1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (-2,-5):room((-2,-5),"battle",[[1,0],[-1,0]],["sandguard","sandguard","sandguard","sandguard"]),
        (-1,-5):room((-1,-5),"battle",[[-1,0],[0,1],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (0,-5):room((0,-5),"boss",[[0,1]],["sandguard","sandguard","sandguard","sandknight"]),
        (1,-5):room((1,-5),"battle",[[1,0],[0,1],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (2,-5):room((2,-5),"battle",[[1,0],[-1,0]],["sandguard","sandguard","sandguard","sandguard"]),
        (3,-5):room((3,-5),"battle",[[-1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        
        (-2,-4):room((-2,-4),"battle",[[1,0],[0,1]],["sandguard","sandguard","sandguard","sandguard"]),
        (-1,-4):room((-1,-4),"battle",[[-1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (0,-4):room((0,-4),"game",[[0,1],[0,-1]],None),
        (1,-4):room((1,-4),"battle",[[1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (2,-4):room((2,-4),"battle",[[-1,0],[0,1]],["sandguard","sandguard","sandguard","sandguard"]),

        (-2,-3):room((-2,-3),"battle",[[1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (-1,-3):room((-1,-3),"battle",[[-1,0],[0,1]],["sandguard","sandguard","sandguard","sandguard"]),
        (0,-3):room((0,-3),"magiclock",[[0,1],[0,-1]],None),
        (1,-3):room((1,-3),"battle",[[1,0],[0,1]],["sandguard","sandguard","sandguard","sandguard"]),
        (2,-3):room((2,-3),"battle",[[-1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),

        (-2,-2):room((-2,-2),"battle",[[1,0],[0,1]],["sandguard","sandguard","sandguard","sandguard"]),
        (-1,-2):room((-1,-2),"battle",[[-1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (0,-2):room((0,-2),"magiclock",[[0,1],[0,-1]],None),
        (1,-2):room((1,-2),"battle",[[1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (2,-2):room((2,-2),"battle",[[-1,0],[0,1]],["sandguard","sandguard","sandguard","sandguard"]),

        (-3,-1):room((-3,-1),"battle",[[1,0],[0,1]],["sandguard","sandguard","sandguard","sandguard"]),
        (-2,-1):room((-2,-1),"battle",[[-1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (-1,-1):room((-1,-1),"battle",[[1,0],[0,1]],["sandguard","sandguard","sandguard","sandguard"]),
        (0,-1):room((0,-1),"battle",[[1,0],[-1,0],[0,1],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (1,-1):room((1,-1),"goldlock",[[-1,0],[0,1]],None),
        (2,-1):room((2,-1),"battle",[[1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (3,-1):room((3,-1),"battle",[[-1,0],[0,1]],["sandguard","sandguard","sandguard","sandguard"]),

        (-3,0):room((-3,0),"battle",[[1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (-2,0):room((-2,0),"battle",[[1,0],[-1,0]],["sandguard","sandguard","sandguard","sandguard"]),
        (-1,0):room((-1,0),"battle",[[-1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (0,0):room((0,0),"door",[[0,-1]],None),
        (1,0):room((1,0),"goldlock",[[1,0],[0,-1]],None),
        (2,0):room((2,0),"battle",[[1,0],[-1,0]],["sandguard","sandguard","sandguard","sandguard"]),
        (3,0):room((3,0),"battle",[[-1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"])}),

    dungeon("beach6","sandcastle",48,1,[253,5445],[260,300],{
        (-5,-6):room((-5,-6),"goldkey",[[0,1]],None),
        (-3,-6):room((-3,-6),"goldkey",[[0,1]],None),
        (-1,-6):room((-1,-6),"goldkey",[[0,1]],None),
        (1,-6):room((1,-6),"goldkey",[[0,1]],None),
        (3,-6):room((3,-6),"goldkey",[[0,1]],None),
        (5,-6):room((5,-6),"goldkey",[[0,1]],None),

        (-5,-5):room((-5,-5),"battle",[[1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (-4,-5):room((-4,-5),"battle",[[1,0],[-1,0],[0,1]],["sandguard","sandguard","sandguard","sandguard"]),
        (-3,-5):room((-3,-5),"battle",[[1,0],[-1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (-2,-5):room((-2,-5),"battle",[[1,0],[-1,0]],["sandguard","sandguard","sandguard","sandguard"]),
        (-1,-5):room((-1,-5),"battle",[[-1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (1,-5):room((1,-5),"battle",[[1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (2,-5):room((2,-5),"battle",[[1,0],[-1,0],[0,1]],["sandguard","sandguard","sandguard","sandguard"]),
        (3,-5):room((3,-5),"battle",[[1,0],[-1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (4,-5):room((4,-5),"battle",[[1,0],[-1,0],[0,1]],["sandguard","sandguard","sandguard","sandguard"]),
        (5,-5):room((5,-5),"battle",[[-1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),

        (-4,-4):room((-4,-4),"battle",[[1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (-3,-4):room((-3,-4),"battle",[[1,0],[-1,0]],["sandguard","sandguard","sandguard","sandguard"]),
        (-2,-4):room((-2,-4),"battle",[[-1,0],[0,1]],["sandguard","sandguard","sandguard","sandguard"]),
        (2,-4):room((2,-4),"battle",[[1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (3,-4):room((3,-4),"battle",[[-1,0],[0,1]],["sandguard","sandguard","sandguard","sandguard"]),
        (4,-4):room((4,-4),"goldlock",[[0,1],[0,-1]],None),

        (-4,-3):room((-4,-3),"battle",[[1,0],[0,1]],["sandguard","sandguard","sandguard","sandguard"]),
        (-3,-3):room((-3,-3),"battle",[[1,0],[-1,0]],["sandguard","sandguard","sandguard","sandguard"]),
        (-2,-3):room((-2,-3),"battle",[[-1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (2,-3):room((2,-3),"battle",[[1,0],[0,1]],["sandguard","sandguard","sandguard","sandguard"]),
        (3,-3):room((3,-3),"battle",[[-1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (4,-3):room((4,-3),"goldlock",[[0,1],[0,-1]],None),

        (-4,-2):room((-4,-2),"battle",[[1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (-3,-2):room((-3,-2),"battle",[[1,0],[-1,0]],["sandguard","sandguard","sandguard","sandguard"]),
        (-2,-2):room((-2,-2),"battle",[[-1,0],[0,1]],["sandguard","sandguard","sandguard","sandguard"]),
        (-1,-2):room((-1,-2),"battle",[[1,0],[0,1]],["sandguard","sandguard","sandguard","sandguard"]),
        (0,-2):room((0,-2),"battle",[[1,0],[-1,0],[0,1]],["sandguard","sandguard","sandguard","sandguard"]),
        (1,-2):room((1,-2),"battle",[[-1,0],[0,1]],["sandguard","sandguard","sandguard","sandguard"]),
        (2,-2):room((2,-2),"battle",[[0,1],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (3,-2):room((3,-2),"goldlock",[[1,0],[0,1]],None),
        (4,-2):room((4,-2),"goldlock",[[-1,0],[0,-1]],None),

        (-4,-1):room((-4,-1),"battle",[[1,0],[0,1]],["sandguard","sandguard","sandguard","sandguard"]),
        (-3,-1):room((-3,-1),"battle",[[1,0],[-1,0]],["sandguard","sandguard","sandguard","sandguard"]),
        (-2,-1):room((-2,-1),"battle",[[-1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (-1,-1):room((-1,-1),"battle",[[0,1],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (0,-1):room((0,-1),"battle",[[0,1],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (1,-1):room((1,-1),"battle",[[0,1],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (2,-1):room((2,-1),"battle",[[0,1],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (3,-1):room((3,-1),"goldlock",[[1,0],[0,-1]],None),
        (4,-1):room((4,-1),"goldlock",[[-1,0],[0,1]],None),

        (-4,0):room((-4,0),"battle",[[1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (-3,0):room((-3,0),"battle",[[1,0],[-1,0]],["sandguard","sandguard","sandguard","sandguard"]),
        (-2,0):room((-2,0),"battle",[[1,0],[-1,0]],["sandguard","sandguard","sandguard","sandguard"]),
        (-1,0):room((-1,0),"battle",[[-1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (0,0):room((0,0),"door",[[0,-1]],None),
        (1,0):room((1,0),"battle",[[1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (2,0):room((2,0),"battle",[[-1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (3,0):room((3,0),"boss",[[1,0]],["sandguard","sandguard","sandguard","sandknight"]),
        (4,0):room((4,0),"game",[[-1,0],[0,-1]],None)}),

    dungeon("beach7","sandcastle",49,1,[315,5441],[260,300],{
        (-2,-6):room((-2,-6),"magickey",[[0,1]],None),
        (0,-6):room((0,-6),"boss",[[0,1]],["sandguard","sandguard","sandguard","sandknight"]),
        (2,-6):room((2,-6),"magickey",[[0,1]],None),

        (-5,-5):room((-5,-5),"battle",[[1,0],[0,1]],["sandguard","sandguard","sandguard","sandguard"]),
        (-4,-5):room((-4,-5),"goldkey",[[-1,0]],None),
        (-2,-5):room((-2,-5),"battle",[[1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (-1,-5):room((-1,-5),"battle",[[-1,0],[0,1]],["sandguard","sandguard","sandguard","sandguard"]),
        (0,-5):room((0,-5),"game",[[0,1],[0,-1]],None),
        (1,-5):room((1,-5),"battle",[[1,0],[0,1]],["sandguard","sandguard","sandguard","sandguard"]),
        (2,-5):room((2,-5),"battle",[[-1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (4,-5):room((4,-5),"goldkey",[[1,0]],None),
        (5,-5):room((5,-5),"battle",[[-1,0],[0,1]],["sandguard","sandguard","sandguard","sandguard"]),

        (-5,-4):room((-5,-4),"battle",[[1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (-4,-4):room((-4,-4),"battle",[[-1,0],[0,1]],["sandguard","sandguard","sandguard","sandguard"]),
        (-1,-4):room((-1,-4),"battle",[[0,1],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (0,-4):room((0,-4),"magiclock",[[0,1],[0,-1]],None),
        (1,-4):room((1,-4),"battle",[[0,1],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (4,-4):room((4,-4),"battle",[[1,0],[0,1]],["sandguard","sandguard","sandguard","sandguard"]),
        (5,-4):room((5,-4),"battle",[[-1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),

        (-5,-3):room((-5,-3),"battle",[[1,0],[0,1]],["sandguard","sandguard","sandguard","sandguard"]),
        (-4,-3):room((-4,-3),"battle",[[-1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (-1,-3):room((-1,-3),"battle",[[0,1],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (0,-3):room((0,-3),"magiclock",[[0,1],[0,-1]],None),
        (1,-3):room((1,-3),"battle",[[0,1],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (4,-3):room((4,-3),"battle",[[1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (5,-3):room((5,-3),"battle",[[-1,0],[0,1]],["sandguard","sandguard","sandguard","sandguard"]),

        (-5,-2):room((-5,-2),"battle",[[1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (-4,-2):room((-4,-2),"battle",[[-1,0],[0,1]],["sandguard","sandguard","sandguard","sandguard"]),
        (-3,-2):room((-3,-2),"battle",[[1,0],[0,1]],["sandguard","sandguard","sandguard","sandguard"]),
        (-2,-2):room((-2,-2),"battle",[[-1,0],[0,1]],["sandguard","sandguard","sandguard","sandguard"]),
        (-1,-2):room((-1,-2),"goldlock",[[0,1],[0,-1]],None),
        (0,-2):room((0,-2),"battle",[[0,1],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (1,-2):room((1,-2),"goldlock",[[0,1],[0,-1]],None),
        (2,-2):room((2,-2),"battle",[[1,0],[0,1]],["sandguard","sandguard","sandguard","sandguard"]),
        (3,-2):room((3,-2),"battle",[[-1,0],[0,1]],["sandguard","sandguard","sandguard","sandguard"]),
        (4,-2):room((4,-2),"battle",[[1,0],[0,1]],["sandguard","sandguard","sandguard","sandguard"]),
        (5,-2):room((5,-2),"battle",[[-1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),

        (-5,-1):room((-5,-1),"battle",[[1,0],[0,1]],["sandguard","sandguard","sandguard","sandguard"]),
        (-4,-1):room((-4,-1),"battle",[[-1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (-3,-1):room((-3,-1),"battle",[[0,1],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (-2,-1):room((-2,-1),"battle",[[0,1],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (-1,-1):room((-1,-1),"battle",[[1,0],[0,1],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (0,-1):room((0,-1),"battle",[[1,0],[-1,0],[0,1],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (1,-1):room((1,-1),"battle",[[-1,0],[0,1],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (2,-1):room((2,-1),"battle",[[0,1],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (3,-1):room((3,-1),"battle",[[0,1],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (4,-1):room((4,-1),"battle",[[1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (5,-1):room((5,-1),"battle",[[-1,0],[0,1]],["sandguard","sandguard","sandguard","sandguard"]),

        (-5,0):room((-5,0),"battle",[[1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (-4,0):room((-4,0),"battle",[[1,0],[-1,0]],["sandguard","sandguard","sandguard","sandguard"]),
        (-3,0):room((-3,0),"battle",[[-1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (-2,0):room((-2,0),"battle",[[1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (-1,0):room((-1,0),"battle",[[-1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (0,0):room((0,0),"door",[[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (1,0):room((1,0),"battle",[[1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (2,0):room((2,0),"battle",[[-1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (3,0):room((3,0),"battle",[[1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (4,0):room((4,0),"battle",[[1,0],[-1,0]],["sandguard","sandguard","sandguard","sandguard"]),
        (5,0):room((5,0),"battle",[[-1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"])}),

    dungeon("beach8","sandcastle",50,2,[365,5441],[260,340],{
        (0,-8):room((0,-8),"boss",[[0,1]],["sandguard","sandguard","sandmazorov"]),

        (-5,-7):room((-5,-7),"heal",[[1,0],[0,1]],["sandguard","sandguard","sandguard","sandguard"]),
        (-4,-7):room((-4,-7),"bronzekey",[[-1,0]],None),
        (-1,-7):room((-3,-7),"goldkey",[[0,1]],None),
        (0,-7):room((-2,-7),"game",[[0,1],[0,-1]],None),
        (1,-7):room((-1,-7),"magickey",[[0,1]],None),
        (4,-7):room((0,-7),"silverkey",[[1,0]],None),
        (5,-7):room((5,-7),"heal",[[-1,0],[0,1]],["sandguard","sandguard","sandguard","sandguard"]),

        (-5,-6):room((-5,-6),"battle",[[1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (-4,-6):room((-4,-6),"battle",[[-1,0],[0,1]],["sandguard","sandguard","sandguard","sandguard"]),
        (-2,-6):room((-2,-6),"battle",[[1,0],[0,1]],["sandguard","sandguard","sandguard","sandguard"]),
        (-1,-6):room((-1,-6),"battle",[[-1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (0,-6):room((0,-6),"magiclock",[[0,1],[0,-1]],None),
        (1,-6):room((1,-6),"battle",[[1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (2,-6):room((2,-6),"battle",[[-1,0],[0,1]],["sandguard","sandguard","sandguard","sandguard"]),
        (4,-6):room((4,-6),"battle",[[1,0],[0,1]],["sandguard","sandguard","sandguard","sandguard"]),
        (5,-6):room((5,-6),"battle",[[-1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),

        (-5,-5):room((-5,-5),"battle",[[1,0],[0,1]],["sandguard","sandguard","sandguard","sandguard"]),
        (-4,-5):room((-4,-5),"battle",[[-1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (-2,-5):room((-2,-5),"battle",[[1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (-1,-5):room((-1,-5),"battle",[[-1,0],[0,1]],["sandguard","sandguard","sandguard","sandguard"]),
        (0,-5):room((0,-5),"goldlock",[[0,1],[0,-1]],None),
        (1,-5):room((1,-5),"battle",[[1,0],[0,1]],["sandguard","sandguard","sandguard","sandguard"]),
        (2,-5):room((2,-5),"battle",[[-1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (4,-5):room((4,-5),"battle",[[1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (5,-5):room((5,-5),"battle",[[-1,0],[0,1]],["sandguard","sandguard","sandguard","sandguard"]),

        (-5,-4):room((-5,-4),"battle",[[1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (-4,-4):room((-4,-4),"battle",[[-1,0],[0,1]],["sandguard","sandguard","sandguard","sandguard"]),
        (-1,-4):room((-1,-4),"battle",[[0,1],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (0,-4):room((0,-4),"silverlock",[[0,1],[0,-1]],None),
        (1,-4):room((1,-4),"battle",[[0,1],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (4,-4):room((4,-4),"battle",[[1,0],[0,1]],["sandguard","sandguard","sandguard","sandguard"]),
        (5,-4):room((5,-4),"battle",[[-1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),

        (-5,-3):room((-5,-3),"battle",[[1,0],[0,1]],["sandguard","sandguard","sandguard","sandguard"]),
        (-4,-3):room((-4,-3),"battle",[[-1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (-1,-3):room((-1,-3),"battle",[[0,1],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (0,-3):room((0,-3),"bronzelock",[[0,1],[0,-1]],None),
        (1,-3):room((1,-3),"battle",[[0,1],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (4,-3):room((4,-3),"battle",[[1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (5,-3):room((5,-3),"battle",[[-1,0],[0,1]],["sandguard","sandguard","sandguard","sandguard"]),

        (-5,-2):room((-5,-2),"battle",[[1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (-4,-2):room((-4,-2),"battle",[[1,0],[-1,0]],["sandguard","sandguard","sandguard","sandguard"]),
        (-3,-2):room((-3,-2),"battle",[[1,0],[-1,0]],["sandguard","sandguard","sandguard","sandguard"]),
        (-2,-2):room((-2,-2),"battle",[[-1,0],[0,1]],["sandguard","sandguard","sandguard","sandguard"]),
        (-1,-2):room((-1,-2),"battle",[[0,1],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (0,-2):room((0,-2),"battle",[[0,1],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (1,-2):room((1,-2),"battle",[[0,1],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (2,-2):room((2,-2),"battle",[[1,0],[0,1]],["sandguard","sandguard","sandguard","sandguard"]),
        (3,-2):room((3,-2),"battle",[[1,0],[-1,0]],["sandguard","sandguard","sandguard","sandguard"]),
        (4,-2):room((4,-2),"battle",[[1,0],[-1,0]],["sandguard","sandguard","sandguard","sandguard"]),
        (5,-2):room((5,-2),"battle",[[-1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),

        (-5,-1):room((-5,-1),"battle",[[1,0],[0,1]],["sandguard","sandguard","sandguard","sandguard"]),
        (-4,-1):room((-4,-1),"battle",[[1,0],[-1,0]],["sandguard","sandguard","sandguard","sandguard"]),
        (-3,-1):room((-3,-1),"battle",[[1,0],[-1,0]],["sandguard","sandguard","sandguard","sandguard"]),
        (-2,-1):room((-2,-1),"battle",[[-1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (-1,-1):room((-1,-1),"battle",[[1,0],[0,1],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (0,-1):room((0,-1),"battle",[[1,0],[-1,0],[0,1],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (1,-1):room((1,-1),"battle",[[-1,0],[0,1],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (2,-1):room((2,-1),"battle",[[1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (3,-1):room((3,-1),"battle",[[1,0],[-1,0]],["sandguard","sandguard","sandguard","sandguard"]),
        (4,-1):room((4,-1),"battle",[[1,0],[-1,0]],["sandguard","sandguard","sandguard","sandguard"]),
        (5,-1):room((5,-1),"battle",[[-1,0],[0,1]],["sandguard","sandguard","sandguard","sandguard"]),

        (-5,0):room((-5,0),"battle",[[1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (-4,0):room((-4,0),"battle",[[1,0],[-1,0]],["sandguard","sandguard","sandguard","sandguard"]),
        (-3,0):room((-3,0),"battle",[[1,0],[-1,0]],["sandguard","sandguard","sandguard","sandguard"]),
        (-2,0):room((-2,0),"battle",[[1,0],[-1,0]],["sandguard","sandguard","sandguard","sandguard"]),
        (-1,0):room((-1,0),"battle",[[-1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (0,0):room((0,0),"door",[[0,-1]],None),
        (1,0):room((1,0),"battle",[[1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"]),
        (2,0):room((2,0),"battle",[[1,0],[-1,0]],["sandguard","sandguard","sandguard","sandguard"]),
        (3,0):room((3,0),"battle",[[1,0],[-1,0]],["sandguard","sandguard","sandguard","sandguard"]),
        (4,0):room((4,0),"battle",[[1,0],[-1,0]],["sandguard","sandguard","sandguard","sandguard"]),
        (5,0):room((5,0),"battle",[[-1,0],[0,-1]],["sandguard","sandguard","sandguard","sandguard"])}),

    dungeon("ocean1","ocean",51,1,[346,5139],[160,160],{
        (0,0):room((0,0),"door",[[0,1]],None),
        (0,1):room((0,1),"battle",[[0,1],[0,-1]],["fish","fish","fish"]),
        (0,2):room((0,2),"battle",[[1,0],[0,-1]],["fish","fish","fish"]),
        (1,2):room((1,2),"battle",[[-1,0],[0,-1]],["fish","fish","fish"]),
        (1,1):room((1,1),"battle",[[1,0],[0,1]],["fish","fish","fish"]),
        (2,1):room((2,1),"battle",[[1,0],[-1,0],[0,1],[0,-1]],["fish","fish","fish"]),
        (3,1):room((3,1),"battle",[[1,0],[-1,0]],["fish","fish","fish"]),
        (4,1):room((4,1),"battle",[[-1,0],[0,1],[0,-1]],["fish","fish","fish"]),
        (4,0):room((4,0),"battle",[[1,0],[0,1]],["fish","fish","fish"]),
        (5,0):room((5,0),"battle",[[-1,0],[0,-1]],["fish","fish","fish"]),
        (5,-1):room((5,-1),"bronzekey",[[0,1]],None),
        (4,2):room((4,2),"battle",[[1,0],[0,-1]],["fish","fish","fish"]),
        (5,2):room((5,2),"battle",[[-1,0],[0,1]],["fish","fish","fish"]),
        (5,3):room((5,3),"bronzekey",[[0,-1]],None),
        (2,2):room((2,2),"battle",[[0,1],[0,-1]],["fish","fish","fish"]),
        (2,3):room((2,3),"battle",[[-1,0],[0,-1]],["fish","fish","fish"]),
        (1,3):room((1,3),"bronzekey",[[1,0]],None),
        (2,0):room((2,0),"bronzelock",[[0,1],[0,-1]],None),
        (2,-1):room((2,-1),"bronzelock",[[-1,0],[0,1]],None),
        (1,-1):room((1,-1),"bronzelock",[[1,0],[0,1]],None),
        (1,0):room((1,0),"boss",[[0,-1]],["fish","fish","fish","giantfish"])}),

    dungeon("ocean2","ocean",52,1,[210,5058],[140,160],{
        (0,0):room((0,0),"door",[[1,0]],None),
        (1,0):room((1,0),"battle",[[1,0],[-1,0]],["fish","fish","fish"]),
        (2,0):room((2,0),"battle",[[-1,0],[0,-1]],["fish","fish","fish"]),
        (2,-1):room((2,-1),"battle",[[1,0],[0,1]],["fish","fish","fish"]),
        (3,-1):room((3,-1),"battle",[[-1,0],[0,1]],["fish","fish","fish"]),
        (3,0):room((3,0),"battle",[[1,0],[0,-1]],["fish","fish","fish"]),
        (4,0):room((4,0),"battle",[[-1,0],[0,-1]],["fish","fish","fish"]),
        (4,-1):room((4,-1),"battle",[[1,0],[0,1],[0,-1]],["fish","fish","fish"]),
        (5,-1):room((5,-1),"battle",[[1,0],[-1,0]],["fish","fish","fish"]),
        (6,-1):room((6,-1),"battle",[[-1,0],[0,1]],["fish","fish","fish"]),
        (6,0):room((6,0),"bronzekey",[[0,-1]],None),
        (4,-2):room((4,-2),"battle",[[1,0],[0,1],[0,-1]],["fish","fish","fish"]),
        (5,-2):room((5,-2),"battle",[[1,0],[-1,0]],["fish","fish","fish"]),
        (6,-2):room((6,-2),"battle",[[-1,0],[0,-1]],["fish","fish","fish"]),
        (6,-3):room((6,-3),"bronzekey",[[0,1]],None),
        (4,-3):room((4,-3),"battle",[[-1,0],[0,1]],["fish","fish","fish"]),
        (3,-3):room((3,-3),"battle",[[1,0],[0,1]],["fish","fish","fish"]),
        (3,-2):room((3,-2),"battle",[[-1,0],[0,-1]],["fish","fish","fish"]),
        (2,-2):room((2,-2),"battle",[[1,0],[0,-1]],["fish","fish","fish"]),
        (2,-3):room((2,-3),"battle",[[-1,0],[0,1]],["fish","fish","fish"]),
        (1,-3):room((1,-3),"bronzelock",[[1,0],[0,1]],None),
        (1,-2):room((1,-2),"bronzelock",[[-1,0],[0,-1]],None),
        (0,-2):room((0,-2),"boss",[[1,0]],["fish","fish","fish","giantfish"])}),

    dungeon("ocean3","ocean",53,1,[86,4938],[340,260],{
        (-4,-4):room((-4,-4),"battle",[[1,0],[0,1]],["fish","fish","fish"]),
        (-3,-4):room((-3,-4),"battle",[[1,0],[-1,0]],["fish","fish","fish"]),
        (-2,-4):room((-2,-4),"battle",[[1,0],[-1,0]],["fish","fish","fish"]),
        (-1,-4):room((-1,-4),"battle",[[1,0],[-1,0]],["fish","fish","fish"]),
        (0,-4):room((0,-4),"battle",[[-1,0],[0,1]],["fish","fish","fish"]),

        (-4,-3):room((-4,-3),"battle",[[0,1],[0,-1]],["fish","fish","fish"]),
        (-3,-3):room((-3,-3),"battle",[[1,0],[0,1]],["fish","fish","fish"]),
        (-2,-3):room((-2,-3),"battle",[[1,0],[-1,0]],["fish","fish","fish"]),
        (-1,-3):room((-1,-3),"battle",[[-1,0],[0,1]],["fish","fish","fish"]),
        (0,-3):room((0,-3),"battle",[[0,1],[0,-1]],["fish","fish","fish"]),

        (-4,-2):room((-4,-2),"battle",[[0,1],[0,-1]],["fish","fish","fish"]),
        (-3,-2):room((-3,-2),"battle",[[0,1],[0,-1]],["fish","fish","fish"]),
        (-2,-2):room((-2,-2),"boss",[[1,0]],["fish","fish","fish","octopus"]),
        (-1,-2):room((-1,-2),"battle",[[-1,0],[0,-1]],["fish","fish","fish"]),
        (0,-2):room((0,-2),"battle",[[0,1],[0,-1]],["fish","fish","fish"]),

        (-4,-1):room((-4,-1),"battle",[[0,1],[0,-1]],["fish","fish","fish"]),
        (-3,-1):room((-3,-1),"battle",[[1,0],[0,-1]],["fish","fish","fish"]),
        (-2,-1):room((-2,-1),"battle",[[1,0],[-1,0]],["fish","fish","fish"]),
        (-1,-1):room((-1,-1),"battle",[[1,0],[-1,0]],["fish","fish","fish"]),
        (0,-1):room((0,-1),"battle",[[-1,0],[0,-1]],["fish","fish","fish"]),

        (-4,0):room((-4,0),"battle",[[1,0],[0,-1]],["fish","fish","fish"]),
        (-3,0):room((-3,0),"battle",[[1,0],[-1,0]],["fish","fish","fish"]),
        (-2,0):room((-2,0),"battle",[[1,0],[-1,0]],["fish","fish","fish"]),
        (-1,0):room((-1,0),"battle",[[1,0],[-1,0]],["fish","fish","fish"]),
        (0,0):room((0,0),"door",[[-1,0]],None)}),

    dungeon("ocean4","pirateship",54,1,[290,4822],[340,220],{
        (0,0):room((0,0),"door",[[-1,0]],None),
        (-1,0):room((-1,0),"battle",[[1,0],[-1,0],[0,-1]],["pirate","pirate","pirate"]),
        (-2,0):room((-2,0),"bronzekey",[[1,0]],None),
        (-5,-2):room((-5,-2),"boss",[[1,0]],["pirate","pirate","pirate","captain"]),
        (-4,-2):room((-4,-2),"battle",[[1,0],[-1,0]],["pirate","pirate","pirate"]),
        (-3,-2):room((-3,-2),"battle",[[1,0],[-1,0]],["pirate","pirate","pirate"]),
        (-2,-2):room((-2,-2),"battle",[[1,0],[-1,0]],["pirate","pirate","pirate"]),
        (-1,-2):room((-1,-2),"battle",[[1,0],[-1,0]],["pirate","pirate","pirate"]),
        (0,-2):room((0,-2),"battle",[[1,0],[-1,0]],["pirate","pirate","pirate"]),
        (1,-2):room((1,-2),"silverlock",[[-1,0],[0,1]],None),
        (-3,-1):room((-3,-1),"silverkey",[[1,0]],None),
        (-2,-1):room((-2,-1),"battle",[[1,0],[-1,0]],["pirate","pirate","pirate"]),
        (-1,-1):room((-1,-1),"bronzelock",[[1,0],[-1,0],[0,1]],None),
        (0,-1):room((0,-1),"chest",[[1,0],[-1,0]],[14,["money",200],["money",20]]),
        (1,-1):room((1,-1),"battle",[[-1,0],[0,-1]],["pirate","pirate","pirate"])}),

    dungeon("ocean5","coralreef",55,1,[434,4571],[140,260],{
        (0,0):room((0,0),"door",[[1,0]],None),
        (1,0):room((1,0),"battle",[[1,0],[-1,0]],["coral","coral","tropicalfish"]),
        (2,0):room((2,0),"battle",[[1,0],[-1,0],[0,-1]],["tropicalfish","coral","coral"]),
        (3,0):room((3,0),"battle",[[1,0],[-1,0]],["coral","tropicalfish","tropicalfish"]),
        (4,0):room((4,0),"battle",[[1,0],[-1,0]],["coral","coral","tropicalfish"]),
        (5,0):room((5,0),"battle",[[1,0],[-1,0]],["tropicalfish","tropicalfish","tropicalfish"]),
        (6,0):room((6,0),"battle",[[-1,0],[0,-1]],["coral","coral","coral"]),
        (6,-1):room((6,-1),"bronzelock",[[0,1],[0,-1]],None),
        (6,-2):room((6,-2),"bronzelock",[[0,1],[0,-1]],None),
        (6,-3):room((6,-3),"bronzelock",[[0,1],[0,-1]],None),
        (6,-4):room((6,-4),"boss",[[0,1]],["tropicalfish","coral","coral","coralmonster"]),
        (2,-1):room((2,-1),"battle",[[0,1],[0,-1]],["coral","coral"]),
        (2,-2):room((2,-2),"battle",[[1,0],[0,1],[0,-1]],["tropicalfish","coral"]),
        (3,-2):room((3,-2),"battle",[[1,0],[-1,0]],["coral","coral","tropicalfish"]),
        (4,-2):room((4,-2),"battle",[[-1,0],[0,-1]],["coral","tropicalfish","tropicalfish"]),
        (4,-3):room((4,-3),"battle",[[0,1],[0,-1]],["coral","coral","coral"]),
        (4,-4):room((4,-4),"bronzekey",[[0,1]],None),
        (2,-3):room((2,-3),"battle",[[-1,0],[0,1],[0,-1]],["tropicalfish","tropicalfish","tropicalfish"]),
        (1,-3):room((1,-3),"battle",[[1,0],[-1,0]],["coral","coral","tropicalfish"]),
        (0,-3):room((0,-3),"battle",[[1,0],[0,-1]],["coral","coral","coral"]),
        (0,-4):room((0,-4),"bronzekey",[[0,1]],None),
        (2,-4):room((2,-4),"bronzekey",[[0,1]],None)}),

    dungeon("ocean6","coralreef",56,1,[305,4550],[160,260],{
        (0,0):room((0,0),"door",[[1,0]],None),
        (1,0):room((1,0),"battle",[[-1,0],[0,1]],["tropicalfish","tropicalfish","tropicalfish"]),
        (1,1):room((1,1),"battle",[[1,0],[0,-1]],["tropicalfish","coral","tropicalfish"]),
        (2,1):room((2,1),"battle",[[1,0],[-1,0],[0,-1]],["oyster","coral","oyster"]),
        (2,0):room((2,0),"bronzelock",[[0,1],[0,-1]],None),
        (2,-1):room((2,-1),"boss",[[0,1]],["tropicalfish","oyster","oyster","giantoyster"]),
        (3,1):room((3,1),"battle",[[-1,0],[0,-1]],["tropicalfish","coral","oyster"]),
        (3,0):room((3,0),"battle",[[1,0],[0,1]],["tropicalfish","coral"]),
        (4,0):room((4,0),"battle",[[-1,0],[0,-1]],["tropicalfish","oyster"]),
        (4,-1):room((4,-1),"battle",[[0,1],[0,-1]],["oyster","oyster"]),
        (4,-2):room((4,-2),"battle",[[1,0],[0,1]],["tropicalfish","tropicalfish"]),
        (5,-2):room((5,-2),"battle",[[-1,0],[0,-1]],["coral","oyster"]),
        (5,-3):room((5,-3),"battle",[[-1,0],[0,1],[0,-1]],["tropicalfish","oyster","oyster"]),
        (4,-3):room((4,-3),"chest",[[1,0]],[15,["money",300],["money",30]]),
        (5,-4):room((5,-4),"battle",[[-1,0],[0,1]],["tropicalfish","oyster","oyster"]),
        (4,-4):room((4,-4),"battle",[[1,0],[0,-1]],["oyster","oyster","oyster"]),
        (4,-5):room((4,-5),"bronzekey",[[0,1]],None)}),

    dungeon("ocean7","oceancastle",57,1,[179,4517],[400,240],{
        (-6,-3):room((-6,-3),"bronzekey",[[0,1]],None),
        (-7,-2):room((-7,-2),"battle",[[1,0],[0,1]],["fishguard","fishguard","fishguard"]),
        (-6,-2):room((-6,-2),"battle",[[-1,0],[0,-1]],["fishguard","fishguard","fishguard"]),
        (-7,-1):room((-7,-1),"battle",[[1,0],[0,-1]],["fishguard","fishguard","fishguard"]),
        (-6,-1):room((-6,-1),"battle",[[-1,0],[0,1]],["fishguard","fishguard","fishguard"]),
        (-7,0):room((-7,0),"bronzekey",[[1,0]],None),
        (-6,0):room((-6,0),"battle",[[1,0],[-1,0],[0,-1]],["fishguard","fishguard","fishguard"]),
        (-5,0):room((-5,0),"battle",[[1,0],[-1,0]],["fishguard","fishguard","fishguard"]),
        (-4,0):room((-4,0),"battle",[[1,0],[-1,0]],["fishguard","fishguard","fishguard"]),
        (-3,0):room((-3,0),"battle",[[1,0],[-1,0],[0,-1]],["fishguard","fishguard","fishguard"]),
        (-2,0):room((-2,0),"battle",[[1,0],[-1,0]],["fishguard","fishguard","fishguard"]),
        (-1,0):room((-1,0),"battle",[[1,0],[-1,0],[0,-1]],["fishguard","fishguard","fishguard"]),
        (0,0):room((0,0),"door",[[-1,0]],None),
        (-4,-3):room((-4,-3),"boss",[[1,0]],["fishguard","fishguard","fishguard","fishknight"]),
        (-3,-3):room((-3,-3),"game",[[-1,0],[0,1]],None),
        (-4,-2):room((-4,-2),"bronzelock",[[1,0],[0,1]],None),
        (-3,-2):room((-3,-2),"battle",[[-1,0],[0,-1]],["fishguard","fishguard","fishguard"]),
        (-4,-1):room((-4,-1),"bronzelock",[[1,0],[0,-1]],None),
        (-3,-1):room((-3,-1),"bronzelock",[[-1,0],[0,1]],None),
        (-1,-3):room((-7,-2),"bronzekey",[[0,1]],None),
        (-1,-2):room((-1,-2),"battle",[[1,0],[0,-1]],["fishguard","fishguard","fishguard"]),
        (0,-2):room((0,-2),"battle",[[-1,0],[0,1]],["fishguard","fishguard","fishguard"]),
        (-1,-1):room((-1,-1),"battle",[[1,0],[0,1]],["fishguard","fishguard","fishguard"]),
        (0,-1):room((0,-1),"battle",[[-1,0],[0,-1]],["fishguard","fishguard","fishguard"])}),

    dungeon("ocean8","oceancastle",58,2,[45,4467],[260,300],{
        (-3,-4):room((-3,-4),"magickey",[[0,1]],["fishguard","fishguard","fishguard"]),
        (-4,-3):room((-4,-3),"battle",[[1,0],[0,1]],["fishguard","fishguard","fishguard"]),
        (-3,-3):room((-3,-3),"battle",[[-1,0],[0,-1]],["fishguard","fishguard","fishguard"]),
        (-4,-2):room((-4,-2),"battle",[[1,0],[0,-1]],["fishguard","fishguard","fishguard"]),
        (-3,-2):room((-3,-2),"battle",[[-1,0],[0,1]],["fishguard","fishguard","fishguard"]),
        (-4,-1):room((-4,-1),"battle",[[1,0],[0,1]],["fishguard","fishguard","fishguard"]),
        (-3,-1):room((-3,-1),"battle",[[-1,0],[0,-1]],["fishguard","fishguard","fishguard"]),
        (-4,0):room((-4,0),"battle",[[1,0],[0,-1]],["fishguard","fishguard","fishguard"]),
        (-3,0):room((-3,0),"battle",[[1,0],[-1,0]],["fishguard","fishguard","fishguard"]),
        (-2,0):room((-2,0),"battle",[[1,0],[-1,0]],["fishguard","fishguard","fishguard"]),
        (-1,0):room((-1,0),"battle",[[-1,0],[0,-1]],["fishguard","fishguard","fishguard"]),
        (0,0):room((0,0),"door",[[0,-1]],None),
        (1,0):room((1,0),"battle",[[1,0],[0,-1]],["fishguard","fishguard","fishguard"]),
        (2,0):room((2,0),"battle",[[1,0],[-1,0]],["fishguard","fishguard","fishguard"]),
        (3,0):room((3,0),"battle",[[1,0],[-1,0]],["fishguard","fishguard","fishguard"]),
        (4,0):room((4,0),"battle",[[-1,0],[0,-1]],["fishguard","fishguard","fishguard"]),
        (0,-6):room((0,-6),"boss",[[0,1]],["fishguard","fishguard","fishguard","fishking"]),
        (-1,-5):room((-1,-5),"goldlock",[[1,0],[0,1]],None),
        (0,-5):room((0,-5),"game",[[-1,0],[0,-1]],None),
        (1,-5):room((1,-5),"goldkey",[[0,1]],None),
        (-1,-4):room((-1,-4),"goldlock",[[1,0],[0,-1]],None),
        (0,-4):room((0,-4),"battle",[[1,0],[-1,0],[0,1]],["fishguard","fishguard","fishguard"]),
        (1,-4):room((1,-4),"battle",[[-1,0],[0,1],[0,-1]],["fishguard","fishguard","fishguard"]),
        (-1,-3):room((-1,-3),"battle",[[1,0],[0,1]],["fishguard","fishguard","fishguard"]),
        (0,-3):room((0,-3),"battle",[[-1,0],[0,-1]],["fishguard","fishguard","fishguard"]),
        (1,-3):room((1,-3),"battle",[[0,1],[0,-1]],["fishguard","fishguard","fishguard"]),
        (-1,-2):room((-1,-2),"magiclock",[[1,0],[0,-1]],None),
        (0,-2):room((0,-2),"magiclock",[[-1,0],[0,1]],None),
        (1,-2):room((1,-2),"goldkey",[[0,-1]],None),
        (-1,-1):room((-1,-1),"battle",[[1,0],[0,1]],["fishguard","fishguard","fishguard"]),
        (0,-1):room((0,-1),"battle",[[1,0],[-1,0],[0,1],[0,-1]],["fishguard","fishguard","fishguard"]),
        (1,-1):room((1,-1),"battle",[[-1,0],[0,1]],["fishguard","fishguard","fishguard"]),
        (3,-4):room((3,-4),"magickey",[[0,1]],None),
        (3,-3):room((3,-3),"battle",[[1,0],[0,-1]],["fishguard","fishguard","fishguard"]),
        (4,-3):room((4,-3),"battle",[[-1,0],[0,1]],["fishguard","fishguard","fishguard"]),
        (3,-2):room((3,-2),"battle",[[1,0],[0,1]],["fishguard","fishguard","fishguard"]),
        (4,-2):room((4,-2),"battle",[[-1,0],[0,-1]],["fishguard","fishguard","fishguard"]),
        (3,-1):room((3,-1),"battle",[[1,0],[0,-1]],["fishguard","fishguard","fishguard"]),
        (4,-1):room((4,-1),"battle",[[-1,0],[0,1]],["fishguard","fishguard","fishguard"])}),

    dungeon("jungle1","jungle",60,1,[191,3976],[300,240],{
        (-4,-3):room((-4,-3),"boss",[[1,0]],["evilplant","evilplant","evilplant","giantvine"]),
        (-3,-3):room((-3,-3),"battle",[[1,0],[-1,0]],["evilplant","evilplant","evilplant"]),
        (-2,-3):room((-2,-3),"battle",[[1,0],[-1,0]],["evilplant","evilplant"]),
        (-1,-3):room((-1,-3),"battle",[[1,0],[-1,0]],["evilplant","evilplant","evilplant"]),
        (0,-3):room((0,-3),"battle",[[-1,0],[0,1]],["evilplant"]),

        (-4,-2):room((-4,-2),"battle",[[1,0],[0,1]],["evilplant","evilplant","evilplant"]),
        (-3,-2):room((-3,-2),"battle",[[1,0],[-1,0]],["evilplant","evilplant"]),
        (-2,-2):room((-2,-2),"battle",[[-1,0],[0,1],],["evilplant","evilplant","evilplant"]),
        (0,-2):room((0,-2),"battle",[[0,1],[0,-1]],["evilplant","evilplant"]),

        (-4,-1):room((-4,-1),"battle",[[0,1],[0,-1]],["evilplant"]),
        (-2,-1):room((-2,-1),"battle",[[1,0],[0,-1]],["evilplant","evilplant"]),
        (-1,-1):room((-1,-1),"battle",[[1,0],[-1,0]],["evilplant","evilplant","evilplant"]),
        (0,-1):room((0,-1),"battle",[[-1,0],[0,-1]],["evilplant","evilplant"]),

        (-4,0):room((-4,0),"battle",[[1,0],[0,-1]],["evilplant"]),
        (-3,0):room((-3,0),"battle",[[1,0],[-1,0]],["evilplant","evilplant"]),
        (-2,0):room((-2,0),"battle",[[1,0],[-1,0]],["evilplant","evilplant","evilplant"]),
        (-1,0):room((-1,0),"battle",[[1,0],[-1,0]],["evilplant","evilplant"]),
        (0,0):room((0,0),"door",[[-1,0]],None)}),

    dungeon("jungle2","jungle",61,1,[93,3917],[300,260],{
        (-4,-4):room((-4,-4),"battle",[[1,0],[0,1]],["evilplant","muncher","muncher"]),
        (-3,-4):room((-3,-4),"battle",[[-1,0],[0,1]],["evilplant","evilplant"]),
        (-2,-4):room((-2,-4),"battle",[[1,0],[0,1]],["muncher","muncher"]),
        (-1,-4):room((-1,-4),"battle",[[-1,0],[0,1]],["evilplant","evilplant","muncher"]),
        (0,-4):room((0,-4),"boss",[[0,1]],["evilplant","muncher","muncher","devourer"]),

        (-4,-3):room((-4,-3),"battle",[[0,1],[0,-1]],["evilplant","evilplant","muncher"]),
        (-3,-3):room((-3,-3),"battle",[[0,1],[0,-1]],["evilplant","evilplant","muncher"]),
        (-2,-3):room((-2,-3),"battle",[[0,1],[0,-1]],["muncher","muncher","muncher"]),
        (-1,-3):room((-1,-3),"battle",[[1,0],[0,-1]],["evilplant","evilplant","evilplant"]),
        (0,-3):room((0,-3),"battle",[[-1,0],[0,-1]],["muncher","muncher","muncher"]),

        (-4,-2):room((-4,-2),"battle",[[0,1],[0,-1]],["muncher","evilplant","evilplant"]),
        (-3,-2):room((-3,-2),"battle",[[0,1],[0,-1]],["evilplant","muncher","evilplant"]),
        (-2,-2):room((-2,-2),"battle",[[1,0],[0,-1]],["evilplant","evilplant","muncher","evilplant"]),
        (-1,-2):room((-1,-2),"battle",[[1,0],[-1,0]],["muncher","muncher","muncher"]),
        (0,-2):room((0,-2),"battle",[[-1,0],[0,1]],["muncher"]),

        (-4,-1):room((-4,-1),"battle",[[0,1],[0,-1]],["evilplant","muncher","muncher"]),
        (-3,-1):room((-3,-1),"battle",[[1,0],[0,-1]],["evilplant"]),
        (-2,-1):room((-2,-1),"battle",[[1,0],[-1,0]],["muncher","evilplant","muncher"]),
        (-1,-1):room((-1,-1),"battle",[[1,0],[-1,0]],["evilplant","muncher"]),
        (0,-1):room((0,-1),"battle",[[-1,0],[0,-1]],["muncher","evilplant","muncher"]),

        (-4,0):room((-4,0),"battle",[[1,0],[0,-1]],["evilplant","evilplant"]),
        (-3,0):room((-3,0),"battle",[[1,0],[-1,0]],["evilplant","muncher","muncher"]),
        (-2,0):room((-2,0),"battle",[[1,0],[-1,0]],["evilplant","muncher"]),
        (-1,0):room((-1,0),"battle",[[1,0],[-1,0]],["evilplant","evilplant","muncher"]),
        (0,0):room((0,0),"door",[[-1,0]],None)}),

    dungeon("jungle3","jungle",62,1,[183,3860],[240,180],{
        (0,0):room((0,0),"door",[[0,1]],None),
        (0,1):room((0,1),"battle",[[1,0],[-1,0],[0,1],[0,-1]],["evilplant","muncher","spider"]),
        (1,1):room((1,1),"battle",[[1,0],[-1,0]],["evilplant","muncher","muncher"]),
        (2,1):room((2,1),"battle",[[-1,0],[0,-1]],["muncher","spider","spider"]),
        (2,0):room((2,0),"battle",[[1,0],[0,1]],["spider","spider"]),
        (3,0):room((3,0),"battle",[[1,0],[-1,0]],["muncher","muncher","evilplant"]),
        (4,0):room((4,0),"magickey",[[-1,0]],None),
        (0,2):room((0,2),"battle",[[1,0],[-1,0],[0,-1]],["evilplant","spider","spider"]),
        (1,2):room((1,2),"battle",[[1,0],[-1,0]],["spider","muncher","spider"]),
        (2,2):room((2,2),"battle",[[-1,0],[0,1]],["spider","spider","spider","spider"]),
        (2,3):room((2,3),"battle",[[1,0],[0,-1]],["evilplant","evilplant","muncher","muncher"]),
        (3,3):room((3,3),"battle",[[1,0],[-1,0]],["muncher","spider","spider"]),
        (4,3):room((4,3),"bronzekey",[[-1,0]],None),
        (-1,1):room((-1,1),"battle",[[1,0],[-1,0],[0,1],[0,-1]],["evilplant","muncher","muncher"]),
        (-2,1):room((-2,1),"battle",[[1,0],[-1,0]],["evilplant","evilplant","muncher"]),
        (-3,1):room((-3,1),"battle",[[1,0],[0,-1]],["spider","muncher","spider"]),
        (-3,0):room((-3,0),"battle",[[-1,0],[0,1]],["evilplant","muncher","spider","spider"]),
        (-4,0):room((-4,0),"battle",[[1,0],[-1,0]],["muncher","spider","spider"]),
        (-5,0):room((-5,0),"goldkey",[[1,0]],None),
        (-1,2):room((-1,2),"battle",[[1,0],[-1,0],[0,-1]],["muncher","spider","muncher"]),
        (-2,2):room((-2,2),"battle",[[1,0],[-1,0]],["evilplant","muncher","evilplant"]),
        (-3,2):room((-3,2),"battle",[[1,0],[0,1]],["evilplant","spider","spider"]),
        (-3,3):room((-3,3),"battle",[[-1,0],[0,-1]],["evilplant","muncher","evilplant"]),
        (-4,3):room((-4,3),"battle",[[1,0],[-1,0]],["spider","spider","spider"]),
        (-5,3):room((-5,3),"silverkey",[[1,0]],None),
        (-1,0):room((-1,0),"bronzelock",[[0,1],[0,-1]],None),
        (-1,-1):room((-1,-1),"silverlock",[[1,0],[0,1]],None),
        (0,-1):room((0,-1),"goldlock",[[1,0],[-1,0]],None),
        (1,-1):room((1,-1),"magiclock",[[-1,0],[0,-1]],None),
        (1,-2):room((1,-2),"battle",[[-1,0],[0,1]],["evilplant","muncher","spider"]),
        (0,-2):room((0,-2),"battle",[[1,0],[0,-1]],["spider","muncher","spider"]),
        (0,-3):room((0,-3),"battle",[[-1,0],[0,1]],["spider","muncher","spider"]),
        (-1,-3):room((-1,-3),"battle",[[1,0],[0,1]],["spider","spider","muncher","evilplant"]),
        (-1,-2):room((-1,-2),"battle",[[-1,0],[0,-1]],["spider","spider","spider","spider"]),
        (-2,-2):room((-2,-2),"game",[[1,0],[0,1]],None),
        (-2,-1):room((-2,-1),"boss",[[0,-1]],["evilplant","spider","spider","giantspider"])}),

    dungeon("jungle4","jungle",63,1,[296,3847],[220,260],{
        (-2,-4):room((-2,-4),"battle",[[1,0],[0,1]],["snake","snake","spider"]),
        (-1,-4):room((-1,-4),"battle",[[1,0],[-1,0]],["muncher","snake","snake"]),
        (0,-4):room((0,-4),"battle",[[1,0],[-1,0]],["muncher","muncher","snake","muncher"]),
        (1,-4):room((1,-4),"battle",[[1,0],[-1,0]],["muncher","snake","evilplant","snake"]),
        (2,-4):room((2,-4),"battle",[[-1,0],[0,1]],["spider","muncher","snake","spider"]),

        (-2,-3):room((-2,-3),"battle",[[1,0],[0,-1]],["snake","muncher","muncher","snake"]),
        (-1,-3):room((-1,-3),"boss",[[-1,0]],["muncher","snake","snake","snakeking"]),
        (0,-3):room((0,-3),"battle",[[1,0],[0,1]],["snake","snake","snake","spider"]),
        (1,-3):room((1,-3),"battle",[[-1,0],[0,1]],["muncher","evilplant","snake"]),
        (2,-3):room((2,-3),"battle",[[0,1],[0,-1]],["snake","snake","evilplant","muncher"]),

        (-2,-2):room((-2,-2),"battle",[[1,0],[0,1]],["muncher","muncher","spider"]),
        (-1,-2):room((-1,-2),"battle",[[-1,0],[0,1]],["snake","evilplant"]),
        (0,-2):room((0,-2),"battle",[[0,1],[0,-1]],["snake","evilplant","snake","snake"]),
        (1,-2):room((1,-2),"battle",[[0,1],[0,-1]],["spider","muncher","spider"]),
        (2,-2):room((2,-2),"battle",[[0,1],[0,-1]],["muncher","spider","spider","snake"]),

        (-2,-1):room((-2,-1),"battle",[[0,1],[0,-1]],["muncher","spider","snake"]),
        (-1,-1):room((-1,-1),"battle",[[1,0],[0,-1]],["muncher","snake","snake","snake"]),
        (0,-1):room((0,-1),"battle",[[-1,0],[0,-1]],["spider","spider","snake","snake"]),
        (1,-1):room((1,-1),"battle",[[0,1],[0,-1]],["spider","evilplant","muncher","evilplant"]),
        (2,-1):room((2,-1),"battle",[[0,1],[0,-1]],["spider","snake","snake","spider"]),

        (-2,0):room((-2,0),"battle",[[1,0],[0,-1]],["muncher","spider","snake","muncher"]),
        (-1,0):room((-1,0),"battle",[[1,0],[-1,0]],["snake","spider","evilplant","evilplant"]),
        (0,0):room((0,0),"door",[[-1,0]],None),
        (1,0):room((1,0),"battle",[[1,0],[0,-1]],["muncher","snake","snake"]),
        (2,0):room((2,0),"battle",[[-1,0],[0,-1]],["snake","snake","snake","evilplant"])}),

    dungeon("jungle5","templeyard",64,1,[398,3830],[260,300],{
        (0,0):room((0,0),"door",[[0,-1]],None),
        (0,-1):room((0,-1),"battle",[[1,0],[-1,0],[0,1],[0,-1]],["snake","snake","spider"]),
        (1,-1):room((1,-1),"battle",[[1,0],[-1,0]],["snake","snake","spider"]),
        (2,-1):room((2,-1),"battle",[[1,0],[-1,0]],["snake","snake","spider"]),
        (3,-1):room((3,-1),"bronzekey",[[-1,0]],None),
        (-1,-1):room((-1,-1),"battle",[[1,0],[-1,0]],["snake","snake","spider"]),
        (-2,-1):room((-2,-1),"battle",[[1,0],[-1,0]],["snake","snake","spider"]),
        (-3,-1):room((-3,-1),"silverkey",[[1,0]],None),
        (0,-2):room((0,-2),"battle",[[0,1],[0,-1]],["snake","snake","spider"]),
        (0,-3):room((0,-3),"battle",[[1,0],[-1,0],[0,1],[0,-1]],["snake","snake","spider"]),
        (1,-3):room((1,-3),"battle",[[1,0],[-1,0]],["snake","snake","spider"]),
        (2,-3):room((2,-3),"battle",[[1,0],[-1,0]],["snake","snake","spider"]),
        (3,-3):room((3,-3),"goldkey",[[-1,0]],None),
        (-1,-3):room((-1,-3),"battle",[[1,0],[-1,0]],["snake","snake","spider"]),
        (-2,-3):room((-2,-3),"battle",[[1,0],[-1,0]],["snake","snake","spider"]),
        (-3,-3):room((-3,-3),"magickey",[[1,0]],None),
        (0,-4):room((0,-4),"battle",[[0,1],[0,-1]],["snake","snake","spider"]),
        (0,-5):room((0,-5),"bronzelock",[[-1,0],[0,1]],None),
        (-1,-5):room((-1,-5),"silverlock",[[1,0],[0,-1]],None),
        (-1,-6):room((-1,-6),"goldlock",[[1,0],[0,1]],None),
        (0,-6):room((0,-6),"magiclock",[[1,0],[-1,0]],None),
        (1,-6):room((1,-6),"game",[[-1,0],[0,1]],None),
        (1,-5):room((1,-5),"boss",[[0,-1]],["snake","snake","tiger"])}),

    dungeon("jungle6","temple",65,1,[398,3767],[260,260],{
        (-3,-5):room((-3,-5),"battle",[[1,0],[0,1]],["snake","snake","spider"]),
        (-2,-5):room((-2,-5),"battle",[[-1,0],[0,1]],["snake","snake","spider"]),
        (2,-5):room((2,-5),"battle",[[1,0],[0,1]],["snake","snake","spider"]),
        (3,-5):room((3,-5),"battle",[[-1,0],[0,1]],["snake","snake","spider"]),

        (-3,-4):room((-3,-4),"goldkey",[[0,-1]],None),
        (-2,-4):room((-2,-4),"battle",[[1,0],[0,1],[0,-1]],["snake","snake","spider"]),
        (-1,-4):room((-1,-4),"battle",[[1,0],[-1,0]],["snake","snake","spider"]),
        (0,-4):room((0,-4),"battle",[[1,0],[-1,0]],["snake","snake","spider"]),
        (1,-4):room((1,-4),"battle",[[1,0],[-1,0]],["snake","snake","spider"]),
        (2,-4):room((2,-4),"battle",[[-1,0],[0,1],[0,-1]],["snake","snake","spider"]),
        (3,-4):room((3,-4),"magickey",[[0,-1]],None),

        (-2,-3):room((-2,-3),"battle",[[0,1],[0,-1]],["snake","snake","spider"]),
        (-1,-3):room((-1,-3),"goldlock",[[1,0],[0,1]],None),
        (0,-3):room((0,-3),"battle",[[1,0],[-1,0]],["snake","snake","spider"]),
        (1,-3):room((1,-3),"magiclock",[[-1,0],[0,1]],None),
        (2,-3):room((2,-3),"battle",[[0,1],[0,-1]],["snake","snake","spider"]),

        (-2,-2):room((-2,-2),"battle",[[0,1],[0,-1]],["snake","snake","spider"]),
        (-1,-2):room((-1,-2),"battle",[[0,1],[0,-1]],["snake","snake","spider"]),
        (0,-2):room((0,-2),"boss",[[0,1]],["snake","snake","spider","templeguardian"]),
        (1,-2):room((1,-2),"battle",[[0,1],[0,-1]],["snake","snake","spider"]),
        (2,-2):room((2,-2),"battle",[[0,1],[0,-1]],["snake","snake","spider"]),

        (-2,-1):room((-2,-1),"battle",[[0,1],[0,-1]],["snake","snake","spider"]),
        (-1,-1):room((-1,-1),"silverlock",[[1,0],[0,-1]],None),
        (0,-1):room((0,-1),"battle",[[-1,0],[0,-1]],["snake","snake","spider"]),
        (1,-1):room((1,-1),"bronzelock",[[0,1],[0,-1]],None),
        (2,-1):room((2,-1),"battle",[[0,1],[0,-1]],["snake","snake","spider"]),

        (-3,0):room((-3,0),"silverkey",[[0,1]],None),
        (-2,0):room((-2,0),"battle",[[1,0],[0,1],[0,-1]],["snake","snake","spider"]),
        (-1,0):room((-1,0),"battle",[[1,0],[-1,0]],["snake","snake","spider"]),
        (0,0):room((0,0),"door",[[-1,0]],None),
        (1,0):room((1,0),"battle",[[1,0],[0,-1]],["snake","snake","spider"]),
        (2,0):room((2,0),"battle",[[-1,0],[0,1],[0,-1]],["snake","snake","spider"]),
        (3,0):room((3,0),"bronzekey",[[0,1]],None),

        (-3,1):room((-3,1),"battle",[[1,0],[0,-1]],["snake","snake","spider"]),
        (-2,1):room((-2,1),"battle",[[-1,0],[0,-1]],["snake","snake","spider"]),
        (2,1):room((2,1),"battle",[[1,0],[0,-1]],["snake","snake","spider"]),
        (3,1):room((3,1),"battle",[[-1,0],[0,-1]],["snake","snake","spider"])}),

    dungeon("jungle7","jungle",66,1,[330,3652],[260,300],{
        (0,0):room((0,0),"door",[[0,-1]],None),
        (0,-1):room((0,-1),"battle",[[1,0],[-1,0],[0,1],[0,-1]],["snake","snake","snake"]),
        (-1,-1):room((-1,-1),"battle",[[1,0],[0,-1]],["snake","snake","raptor"]),
        (-1,-2):room((-1,-2),"battle",[[0,1],[0,-1]],["raptor","raptor"]),
        (-1,-3):room((-1,-3),"battle",[[-1,0],[0,1],[0,-1]],["snake","snake"]),
        (-1,-4):room((-1,-4),"bronzekey",[[0,1]],None),
        (-2,-3):room((-2,-3),"battle",[[1,0],[0,-1]],["snake","raptor","raptor"]),
        (-2,-4):room((-2,-4),"battle",[[0,1],[0,-1]],["snake","raptor"]),
        (-2,-5):room((-2,-5),"bronzekey",[[0,1]],None),
        (1,-1):room((1,-1),"battle",[[-1,0],[0,-1]],["snake","snake"]),
        (1,-2):room((1,-2),"battle",[[0,1],[0,-1]],["snake","raptor"]),
        (1,-3):room((1,-3),"battle",[[1,0],[0,1],[0,-1]],["snake","snake","snake"]),
        (1,-4):room((1,-4),"bronzekey",[[0,1]],None),
        (2,-3):room((2,-3),"battle",[[-1,0],[0,-1]],["snake","raptor","raptor"]),
        (2,-4):room((2,-4),"battle",[[0,1],[0,-1]],["raptor","raptor"]),
        (2,-5):room((2,-5),"bronzekey",[[0,1]],None),
        (0,-2):room((0,-2),"bronzelock",[[0,1],[0,-1]],None),
        (0,-3):room((0,-3),"bronzelock",[[0,1],[0,-1]],None),
        (0,-4):room((0,-4),"bronzelock",[[0,1],[0,-1]],None),
        (0,-5):room((0,-5),"bronzelock",[[0,1],[0,-1]],None),
        (0,-6):room((0,-6),"boss",[[0,1]],["snake","raptor","tyrannosaurusrex"])}),

    dungeon("jungle8","jungle",67,2,[216,3578],[260,260],{
        (0,0):room((0,0),"door",[[0,-1]],None),
        (0,-1):room((0,-1),"battle",[[1,0],[-1,0],[0,1],[0,-1]],["snake","raptor"]),
        (-1,-1):room((-1,-1),"battle",[[1,0],[0,-1]],["raptor","raptor"]),
        (-1,-2):room((-1,-2),"battle",[[-1,0],[0,1]],["snake","snake","raptor"]),
        (-2,-2):room((-2,-2),"battle",[[1,0],[0,-1]],["snake","snake"]),
        (-2,-3):room((-2,-3),"battle",[[-1,0],[0,1]],["snake","raptor","raptor"]),
        (-3,-3):room((-3,-3),"magickey",[[1,0]],None),
        (1,-1):room((1,-1),"battle",[[-1,0],[0,-1]],["snake","raptor"]),
        (1,-2):room((1,-2),"battle",[[1,0],[0,1]],["snake","raptor","raptor"]),
        (2,-2):room((2,-2),"battle",[[-1,0],[0,-1]],["raptor"]),
        (2,-3):room((2,-3),"battle",[[1,0],[0,1]],["raptor","raptor"]),
        (3,-3):room((3,-3),"magickey",[[-1,0]],None),
        (0,-2):room((0,-2),"magiclock",[[0,1],[0,-1]],None),
        (0,-3):room((0,-3),"magiclock",[[0,1],[0,-1]],None),
        (0,-4):room((0,-4),"boss",[[0,1]],["snake","raptor","raptor","pterodactyl"])}),

     dungeon("sky1","sky",68,1,[237,3454],[260,220],{
         (0,-3):room((0,-3),"boss",[[0,1]],["bird","bird","bird","albatross"]),

         (-4,-2):room((-4,-2),"bronzekey",[[1,0]],None),
         (-3,-2):room((-3,-2),"battle",[[-1,0],[0,1]],["bird","bird","bird"]),
         (-2,-2):room((-2,-2),"silverkey",[[1,0]],["bird","bird","bird"]),
         (-1,-2):room((-1,-2),"battle",[[-1,0],[0,1]],["bird","bird","bird"]),
         (0,-2):room((0,-2),"silverlock",[[0,1],[0,-1]],None),
         (1,-2):room((1,-2),"bronzelock",[[1,0],[0,1]],None),
         (2,-2):room((2,-2),"bronzelock",[[1,0],[-1,0]],None),
         (3,-2):room((3,-2),"battle",[[1,0],[-1,0],[0,1]],["bird","bird","bird"]),
         (4,-2):room((4,-2),"bronzekey",[[-1,0]],None),

         (-3,-1):room((-3,-1),"battle",[[1,0],[0,-1]],["bird","bird","bird","bird"]),
         (-2,-1):room((-2,-1),"battle",[[-1,0],[0,1]],["bird","bird","bird"]),
         (-1,-1):room((-1,-1),"battle",[[1,0],[0,-1]],["bird","bird"]),
         (0,-1):room((0,-1),"battle",[[1,0],[-1,0],[0,-1]],["bird","bird","bird"]),
         (1,-1):room((1,-1),"battle",[[-1,0],[0,-1]],["bird","bird","bird"]),
         (2,-1):room((2,-1),"battle",[[1,0],[0,1]],["bird","bird"]),
         (3,-1):room((3,-1),"battle",[[-1,0],[0,-1]],["bird","bird","bird"]),

         (-2,0):room((-2,0),"battle",[[1,0],[0,-1]],["bird","bird","bird"]),
         (-1,0):room((-1,0),"battle",[[-1,0],[0,1]],["bird","bird","bird","bird"]),
         (0,0):room((0,0),"door",[[0,1]],None),
         (1,0):room((1,0),"battle",[[1,0],[0,1]],["bird","bird","bird"]),
         (2,0):room((2,0),"battle",[[-1,0],[0,-1]],["bird","bird"]),

         (-1,1):room((-1,1),"battle",[[1,0],[0,-1]],["bird","bird","bird"]),
         (0,1):room((0,1),"battle",[[1,0],[-1,0],[0,-1]],["bird","bird","bird"]),
         (1,1):room((1,1),"battle",[[-1,0],[0,-1]],["bird","bird"])}),

    dungeon("sky2","sky",69,1,[129,3396],[180,160],{
        (1,-1):room((1,-1),"battle",[[1,0],[0,1]],["bird","cloud","cloud"]),
        (2,-1):room((2,-1),"battle",[[1,0],[-1,0]],["bird","cloud"]),
        (3,-1):room((3,-1),"battle",[[-1,0],[0,1]],["cloud","cloud"]),

        (0,0):room((0,0),"door",[[0,1]],None),
        (1,0):room((1,0),"battle",[[0,1],[0,-1]],["bird","bird"]),
        (2,0):room((2,0),"bronzekey",[[0,1]],["cloud","cloud","cloud"]),
        (3,0):room((3,0),"battle",[[1,0],[0,-1]],["bird","cloud"]),
        (4,0):room((4,0),"battle",[[-1,0],[0,1]],["cloud","bird"]),

        (-1,1):room((-1,1),"battle",[[1,0],[0,1]],["cloud","bird"]),
        (0,1):room((0,1),"battle",[[-1,0],[0,-1]],["cloud","cloud","bird"]),
        (1,1):room((1,1),"battle",[[1,0],[0,-1]],["cloud","cloud"]),
        (2,1):room((2,1),"battle",[[-1,0],[0,-1]],["bird","bird","bird"]),
        (3,1):room((3,1),"battle",[[1,0],[0,1]],["bird","cloud"]),
        (4,1):room((4,1),"battle",[[-1,0],[0,-1]],["bird","cloud","cloud"]),
        (5,1):room((5,1),"boss",[[0,1]],["bird","cloud","giantcloud"]),

        (-1,2):room((-1,2),"battle",[[1,0],[0,-1]],["bird","cloud"]),
        (0,2):room((0,2),"battle",[[1,0],[-1,0]],["cloud","cloud"]),
        (1,2):room((1,2),"battle",[[1,0],[-1,0]],["bird","bird","cloud"]),
        (2,2):room((2,2),"battle",[[1,0],[-1,0]],["bird","bird"]),
        (3,2):room((3,2),"battle",[[1,0],[-1,0],[0,-1]],["cloud","cloud"]),
        (4,2):room((4,2),"battle",[[1,0],[-1,0]],["bird","cloud"]),
        (5,2):room((5,2),"bronzelock",[[-1,0],[0,-1]],["cloud","bird"])}),

    dungeon("sky3","fog",70,1,[78,3297],[260,260],{
        (-2,-4):room((-2,-4),"battle",[[1,0],[0,1]],["fogspector","fogspector"]),
        (-1,-4):room((-1,-4),"battle",[[1,0],[-1,0]],["fogspector","fogspector"]),
        (0,-4):room((0,-4),"boss",[[-1,0]],["fogspector","fogspector","fogspector","fogmonster"]),
        (1,-4):room((1,-4),"battle",[[1,0],[0,1]],["fogspector","fogspector"]),
        (2,-4):room((2,-4),"battle",[[-1,0],[0,1]],["fogspector","fogspector","fogspector"]),

        (-2,-3):room((-2,-3),"battle",[[1,0],[0,-1]],["fogspector","fogspector"]),
        (-1,-3):room((-1,-3),"battle",[[1,0],[-1,0]],["fogspector","fogspector"]),
        (0,-3):room((0,-3),"battle",[[1,0],[-1,0]],["fogspector","fogspector"]),
        (1,-3):room((1,-3),"battle",[[-1,0],[0,-1]],["fogspector","fogspector","fogspector"]),
        (2,-3):room((1,-3),"battle",[[0,1],[0,-1]],["fogspector","fogspector"]),

        (-2,-2):room((-2,-2),"battle",[[1,0],[0,1]],["fogspector","fogspector"]),
        (-1,-2):room((-1,-2),"battle",[[1,0],[-1,0]],["fogspector"]),
        (0,-2):room((0,-2),"battle",[[1,0],[-1,0]],["fogspector"]),
        (1,-2):room((1,-2),"battle",[[-1,0],[0,1]],["fogspector","fogspector"]),
        (2,-2):room((1,-2),"battle",[[0,1],[0,-1]],["fogspector","fogspector"]),

        (-2,-1):room((-2,-1),"battle",[[0,1],[0,-1]],["fogspector"]),
        (-1,-1):room((-1,-1),"battle",[[1,0],[0,1]],["fogspector","fogspector"]),
        (0,-1):room((0,-1),"battle",[[-1,0],[0,1]],["fogspector"]),
        (1,-1):room((1,-1),"battle",[[0,1],[0,-1]],["fogspector","fogspector"]),
        (2,-1):room((1,-1),"battle",[[0,1],[0,-1]],["fogspector","fogspector"]),

        (-2,0):room((-2,0),"battle",[[1,0],[0,-1]],["fogspector","fogspector"]),
        (-1,0):room((-1,0),"battle",[[-1,0],[0,-1]],["fogspector","fogspector","fogspector"]),
        (0,0):room((0,0),"door",[[0,-1]],None),
        (1,0):room((1,0),"battle",[[1,0],[0,-1]],["fogspector"]),
        (2,0):room((1,0),"battle",[[-1,0],[0,-1]],["fogspector","fogspector"])}),

    dungeon("sky4","thunder",71,1,[211,3192],[340,120],{
        (0,0):room((0,0),"door",[[0,1]],None),
        (0,1):room((0,1),"battle",[[-1,0],[0,-1]],["cloud","cloud","thundercloud"]),
        (-1,1):room((-1,1),"battle",[[1,0],[0,-1]],["bird","cloud","cloud"]),
        (-1,0):room((-1,0),"battle",[[0,1],[0,-1]],["bird","bird","cloud"]),
        (-1,-1):room((-1,-1),"battle",[[-1,0],[0,1]],["cloud","cloud","cloud"]),
        (-2,-1):room((-2,-1),"battle",[[1,0],[-1,0],[0,1]],["cloud","cloud","cloud","thundercloud"]),
        (-3,-1):room((-3,-1),"battle",[[1,0],[0,1]],["cloud","cloud","thundercloud"]),
        (-3,0):room((-3,0),"battle",[[0,1],[0,-1]],["cloud","cloud","cloud"]),
        (-3,1):room((-3,1),"battle",[[-1,0],[0,-1]],["cloud","cloud"]),
        (-4,1):room((-4,1),"battle",[[1,0],[0,-1]],["bird","thundercloud","thundercloud"]),
        (-4,0):room((-4,0),"magickey",[[0,1]],None),
        (-2,0):room((-2,0),"battle",[[0,1],[0,-1]],["bird","bird","cloud","cloud"]),
        (-2,1):room((-2,1),"battle",[[0,1],[0,-1]],["cloud","cloud","thundercloud"]),
        (-2,2):room((-2,2),"magiclock",[[0,1],[0,-1]],None),
        (-2,3):room((-2,3),"battle",[[-1,0],[0,-1]],["cloud","thundercloud","thundercloud"]),
        (-3,3):room((-3,3),"game",[[1,0],[0,1]],None),
        (-3,4):room((-3,4),"boss",[[0,-1]],["thundercloud","thundercloud","cumulonimbus"])}),

    dungeon("sky5","thunder",72,1,[427,3028],[140,100],{
        (0,0):room((0,0),"door",[[0,1]],None),
        (0,1):room((0,1),"battle",[[0,1],[0,-1]],["bird","cloud","thundercloud"]),
        (0,2):room((0,2),"battle",[[0,1],[0,-1]],["bird","cloud"]),
        (0,3):room((0,3),"battle",[[1,0],[0,-1]],["bird","cloud","cloud"]),
        (1,3):room((1,3),"battle",[[1,0],[-1,0]],["cloud","cloud"]),
        (2,3):room((2,3),"battle",[[1,0],[-1,0]],["bird","bird"]),
        (3,3):room((3,3),"battle",[[1,0],[-1,0]],["cloud","cloud","thundercloud"]),
        (4,3):room((4,3),"battle",[[-1,0],[0,1],[0,-1]],["cloud"]),
        (4,4):room((4,4),"battle",[[0,1],[0,-1]],["thundercloud"]),
        (4,5):room((4,5),"battle",[[-1,0],[0,-1]],["bird","bird","bird"]),
        (3,5):room((3,5),"battle",[[1,0],[-1,0]],["thundercloud","thundercloud"]),
        (2,5):room((2,5),"battle",[[1,0],[-1,0]],["bird","cloud","thundercloud"]),
        (1,5):room((1,5),"bronzekey",[[1,0]],None),
        (4,2):room((4,2),"bronzelock",[[0,1],[0,-1]],None),
        (4,1):room((4,1),"battle",[[1,0],[-1,0],[0,1]],["bird","cloud","thundercloud"]),
        (5,1):room((5,1),"battle",[[1,0],[-1,0]],["bird","cloud","thundercloud"]),
        (6,1):room((6,1),"battle",[[-1,0],[0,1]],["cloud","cloud","cloud"]),
        (6,2):room((6,2),"battle",[[0,1],[0,-1]],["bird","cloud"]),
        (6,3):room((6,3),"battle",[[0,1],[0,-1]],["bird","bird","cloud"]),
        (6,4):room((6,4),"silverkey",[[0,-1]],None),
        (3,1):room((3,1),"silverlock",[[1,0],[-1,0]],None),
        (2,1):room((2,1),"battle",[[1,0],[0,1],[0,-1]],["bird","cloud"]),
        (2,0):room((2,0),"battle",[[0,1],[0,-1]],["bird","bird"]),
        (2,-1):room((2,-1),"battle",[[1,0],[0,1]],["bird","cloud","cloud"]),
        (3,-1):room((3,-1),"battle",[[1,0],[-1,0]],["thundercloud"]),
        (4,-1):room((4,-1),"battle",[[1,0],[-1,0]],["cloud","cloud","thundercloud"]),
        (5,-1):room((5,-1),"magickey",[[-1,0]],None),
        (2,2):room((2,2),"magiclock",[[1,0],[0,-1]],None),
        (3,2):room((3,2),"boss",[[-1,0]],["cloud","thundercloud","thundercloud","eyeofthestorm"])}),

    dungeon("sky6","sky",73,1,[342,2898],[300,280],{
        (0,0):room((0,0),"door",[[-1,0]],["bird","cloud"]),
        (-1,0):room((-1,0),"battle",[[1,0],[-1,0]],["bird","bird"]),
        (-2,0):room((-2,0),"battle",[[1,0],[0,-1]],["bird","cloud"]),
        (-2,-1):room((-2,-1),"battle",[[-1,0],[0,1]],["bird","cloud"]),
        (-3,-1):room((-3,-1),"battle",[[1,0],[0,-1]],["cloud","cloud"]),
        (-3,-2):room((-3,-2),"battle",[[1,0],[0,1]],["bird","cloud"]),
        (-2,-2):room((-2,-2),"battle",[[-1,0],[0,-1]],["bird","cloud"]),
        (-2,-3):room((-2,-3),"battle",[[-1,0],[0,1]],["bird","cloud","cloud"]),
        (-3,-3):room((-3,-3),"battle",[[1,0],[0,-1]],["cloud","cloud"]),
        (-3,-4):room((-3,-4),"battle",[[1,0],[0,1]],["bird","cloud"]),
        (-2,-4):room((-2,-4),"battle",[[1,0],[-1,0]],["bird"]),
        (-1,-4):room((-1,-4),"battle",[[1,0],[-1,0]],["bird","cloud"]),
        (0,-4):room((0,-4),"battle",[[1,0],[-1,0],[0,-1]],["bird","cloud"]),
        (0,-5):room((0,-5),"battle",[[-1,0],[0,1]],["cloud"]),
        (-1,-5):room((-1,-5),"battle",[[1,0],[-1,0]],["bird","bird"]),
        (-2,-5):room((-2,-5),"magickey",[[1,0]],None),
        (1,-4):room((1,-4),"battle",[[-1,0],[0,1]],["bird","cloud"]),
        (1,-3):room((1,-3),"battle",[[-1,0],[0,-1]],["bird","bird"]),
        (0,-3):room((0,-3),"battle",[[1,0],[0,1]],["bird","cloud"]),
        (0,-2):room((0,-2),"battle",[[1,0],[0,-1]],["cloud","cloud"]),
        (1,-2):room((1,-2),"battle",[[-1,0],[0,1]],["cloud","cloud"]),
        (1,-1):room((1,-1),"battle",[[-1,0],[0,-1]],["bird","cloud"]),
        (0,-1):room((0,-1),"battle",[[1,0],[-1,0]],["bird","bird","cloud"]),
        (-1,-1):room((-1,-1),"battle",[[1,0],[0,-1]],["bird","cloud"]),
        (-1,-2):room((-1,-2),"magiclock",[[0,1],[0,-1]],None),
        (-1,-3):room((-1,-3),"boss",[[0,1]],["bird","cloud","skydragon"])}),

    dungeon("sky7","sky",74,1,[280,2818],[440,200],{
        (0,0):room((0,0),"door",[[0,-1]],None),
        (0,-1):room((0,-1),"battle",[[-1,0],[0,1]],["bird","bird","cloud","cloud"]),
        (-1,-1):room((-1,-1),"battle",[[1,0],[0,1]],["bird","cloud","cloud","cloud"]),
        (-1,0):room((-1,0),"battle",[[0,1],[0,-1]],["cloud","cloud","cloud","cloud"]),
        (-1,1):room((-1,1),"battle",[[-1,0],[0,-1]],["bird","cloud","thundercloud","cloud"]),
        (-2,1):room((-2,1),"battle",[[1,0],[0,-1]],["bird","bird","bird","cloud"]),
        (-2,0):room((-2,0),"battle",[[-1,0],[0,1]],["bird","cloud","cloud"]),
        (-3,0):room((-3,0),"battle",[[1,0],[0,1]],["bird","bird","bird","bird"]),
        (-3,1):room((-3,1),"battle",[[-1,0],[0,-1]],["bird","bird","cloud","cloud"]),
        (-4,1):room((-4,1),"battle",[[1,0],[0,-1]],["cloud","thundercloud","cloud"]),
        (-4,0):room((-4,0),"battle",[[0,1],[0,-1]],["bird","cloud","cloud","cloud"]),
        (-4,-1):room((-4,-1),"battle",[[-1,0],[0,1]],["bird","bird","cloud","cloud"]),
        (-5,-1):room((-5,-1),"battle",[[1,0],[0,1]],["bird","bird","bird"]),
        (-5,0):room((-5,0),"battle",[[-1,0],[0,-1]],["bird","bird","bird","cloud"]),
        (-6,0):room((-6,0),"battle",[[1,0],[-1,0],[0,1],[0,-1]],["bird","cloud","cloud"]),
        (-6,-1):room((-6,-1),"battle",[[0,1],[0,-1]],["bird","bird","thundercloud","cloud"]),
        (-6,-2):room((-6,-2),"battle",[[-1,0],[0,1]],["bird","bird","bird","cloud"]),
        (-7,-2):room((-7,-2),"magickey",[[1,0]],None),
        (-7,0):room((-7,0),"battle",[[1,0],[0,-1]],["cloud","cloud","cloud","cloud"]),
        (-7,-1):room((-7,-1),"battle",[[-1,0],[0,1]],["cloud","cloud","cloud"]),
        (-8,-1):room((-8,-1),"battle",[[1,0],[-1,0]],["bird","cloud","thundercloud","cloud"]),
        (-9,-1):room((-9,-1),"magickey",[[1,0]],None),
        (-6,1):room((-6,1),"magiclock",[[-1,0],[0,-1]],None),
        (-7,1):room((-7,1),"magiclock",[[1,0],[-1,0]],None),
        (-8,1):room((-8,1),"game",[[1,0],[-1,0]],None),
        (-9,1):room((-9,1),"boss",[[1,0]],["bird","cloud","skyserpent"])}),

    dungeon("sky8","skycastle",75,2,[241,2695],[260,260],{
        (-5,-4):room((-5,-4),"bronzekey",[[0,1]],None),
        (-3,-4):room((-3,-4),"bronzekey",[[0,1]],None),
        (-1,-4):room((-1,-4),"bronzekey",[[0,1]],None),
        (1,-4):room((1,-4),"boss",[[0,1]],["skyguard","skyguard","skyguard","skyknight"]),
        (3,-4):room((3,-4),"silverkey",[[0,1]],None),
        (5,-4):room((5,-4),"silverkey",[[0,1]],None),

        (-5,-3):room((-5,-3),"battle",[[1,0],[0,-1]],["skyguard","skyguard","skyguard","skyguard"]),
        (-4,-3):room((-4,-3),"battle",[[1,0],[-1,0],[0,1]],["skyguard","skyguard","skyguard","skyguard"]),
        (-3,-3):room((-3,-3),"battle",[[1,0],[-1,0],[0,-1]],["skyguard","skyguard","skyguard","skyguard"]),
        (-2,-3):room((-2,-3),"battle",[[1,0],[-1,0]],["skyguard","skyguard","skyguard","skyguard"]),
        (-1,-3):room((-1,-3),"battle",[[-1,0],[0,-1]],["skyguard","skyguard","skyguard","skyguard"]),
        (1,-3):room((1,-3),"game",[[1,0],[0,-1]],None),
        (2,-3):room((2,-3),"silverlock",[[1,0],[-1,0]],["skyguard","skyguard","skyguard","skyguard"]),
        (3,-3):room((3,-3),"silverlock",[[1,0],[-1,0],[0,-1]],["skyguard","skyguard","skyguard","skyguard"]),
        (4,-3):room((4,-3),"battle",[[1,0],[-1,0],[0,1]],["skyguard","skyguard","skyguard","skyguard"]),
        (5,-3):room((5,-3),"battle",[[-1,0],[0,-1]],["skyguard","skyguard","skyguard","skyguard"]),

        (-4,-2):room((-4,-2),"battle",[[1,0],[0,-1]],["skyguard","skyguard","skyguard","skyguard"]),
        (-3,-2):room((-3,-2),"battle",[[1,0],[-1,0]],["skyguard","skyguard","skyguard","skyguard"]),
        (-2,-2):room((-2,-2),"battle",[[-1,0],[0,1]],["skyguard","skyguard","skyguard","skyguard"]),
        (2,-2):room((2,-2),"battle",[[1,0],[0,1]],["skyguard","skyguard","skyguard","skyguard"]),
        (3,-2):room((3,-2),"battle",[[1,0],[-1,0]],["skyguard","skyguard","skyguard","skyguard"]),
        (4,-2):room((4,-2),"battle",[[-1,0],[0,-1]],["skyguard","skyguard","skyguard","skyguard"]),

        (-4,-1):room((-4,-1),"battle",[[1,0],[0,1]],["skyguard","skyguard","skyguard","skyguard"]),
        (-3,-1):room((-3,-1),"battle",[[1,0],[-1,0]],["skyguard","skyguard","skyguard","skyguard"]),
        (-2,-1):room((-2,-1),"battle",[[-1,0],[0,-1]],["skyguard","skyguard","skyguard","skyguard"]),
        (-1,-1):room((-1,-1),"battle",[[1,0],[0,1]],["skyguard","skyguard","skyguard","skyguard"]),
        (0,-1):room((0,-1),"battle",[[1,0],[-1,0],[0,1]],["skyguard","skyguard","skyguard","skyguard"]),
        (1,-1):room((1,-1),"battle",[[-1,0],[0,1]],["skyguard","skyguard","skyguard","skyguard"]),
        (2,-1):room((2,-1),"battle",[[1,0],[0,-1]],["skyguard","skyguard","skyguard","skyguard"]),
        (3,-1):room((3,-1),"battle",[[1,0],[-1,0]],["skyguard","skyguard","skyguard","skyguard"]),
        (4,-1):room((4,-1),"battle",[[-1,0],[0,1]],["skyguard","skyguard","skyguard","skyguard"]),

        (-4,0):room((-4,0),"battle",[[1,0],[0,-1]],["skyguard","skyguard","skyguard","skyguard"]),
        (-3,0):room((-3,0),"battle",[[1,0],[-1,0]],["skyguard","skyguard","skyguard","skyguard"]),
        (-2,0):room((-2,0),"battle",[[1,0],[-1,0]],["skyguard","skyguard","skyguard","skyguard"]),
        (-1,0):room((-1,0),"battle",[[-1,0],[0,-1]],["skyguard","skyguard","skyguard","skyguard"]),
        (0,0):room((0,0),"door",[[0,-1]],None),
        (1,0):room((1,0),"battle",[[1,0],[0,-1]],["skyguard","skyguard","skyguard","skyguard"]),
        (2,0):room((2,0),"bronzelock",[[1,0],[-1,0]],None),
        (3,0):room((3,0),"bronzelock",[[1,0],[-1,0]],None),
        (4,0):room((4,0),"bronzelock",[[-1,0],[0,-1]],None)}),

    dungeon("mountain1","mountain",76,1,[300,2379],[180,280],{
        (0,0):room((0,0),"door",[[1,0]],None),
        (1,0):room((1,0),"battle",[[1,0],[-1,0]],["stonemonster","stonemonster","goat","goat"]),
        (2,0):room((2,0),"battle",[[1,0],[-1,0]],["goat","stonemonster","stonemonster"]),
        (3,0):room((3,0),"battle",[[1,0],[-1,0]],["goat","goat","goat","stonemonster"]),
        (4,0):room((4,0),"battle",[[-1,0],[0,-1]],["goat","goat","stonemonster","stonemonster"]),
        (4,-1):room((4,-1),"battle",[[-1,0],[0,1]],["goat","stonemonster","stonemonster","goat"]),
        (3,-1):room((3-1),"battle",[[1,0],[-1,0]],["stonemonster","goat","stonemonster","goat"]),
        (2,-1):room((2,-1),"battle",[[1,0],[-1,0]],["goat","goat","stonemonster","goat"]),
        (1,-1):room((1,-1),"battle",[[1,0],[-1,0]],["goat","goat","goat","stonemonster"]),
        (0,-1):room((0,-1),"battle",[[1,0],[0,-1]],["goat","goat","goat","goat"]),
        (0,-2):room((0,-2),"battle",[[1,0],[0,1]],["goat","goat","stonemonster","stonemonster"]),
        (1,-2):room((1,-2),"battle",[[1,0],[-1,0],[0,-1]],["stonemonster","goat","goat","goat"]),
        (2,-2):room((2,-2),"battle",[[1,0],[-1,0]],["goat","stonemonster","stonemonster","goat"]),
        (3,-2):room((3,-2),"battle",[[1,0],[-1,0]],["stonemonster","stonemonster","stonemonster","stonemonster"]),
        (4,-2):room((4,-2),"bronzekey",[[-1,0]],None),
        (1,-3):room((1,-3),"bronzelock",[[1,0],[0,1],[0,-1]],None),
        (2,-3):room((2,-3),"battle",[[1,0],[-1,0]],["goat","stonemonster","stonemonster","stonemonster"]),
        (3,-3):room((3,-3),"battle",[[-1,0],[0,-1]],["stonemonster","stonemonster","goat","goat"]),
        (3,-4):room((3,-4),"silverkey",[[0,1]],None),
        (1,-4):room((1,-4),"battle",[[1,0],[0,1]],["stonemonster","stonemonster","stonemonster","goat"]),
        (2,-4):room((2,-4),"silverlock",[[-1,0],[0,-1]],None),
        (2,-5):room((2,-5),"boss",[[0,1]],["goat","stonemonster","stonemonster","stoneking"])}),

    dungeon("mountain2","mountain",77,1,[258,2267],[160,280],{
        (0,0):room((0,0),"door",[[1,0]],None),
        (1,0):room((1,0),"battle",[[1,0],[-1,0]],["stonemonster","stonemonster","goat","mountainwolf"]),
        (2,0):room((2,0),"battle",[[1,0],[-1,0]],["mountainwolf","mountainwolf","stonemonster","goat"]),
        (3,0):room((3,0),"battle",[[1,0],[-1,0]],["goat","goat","goat","mountainwolf"]),
        (4,0):room((4,0),"battle",[[1,0],[-1,0]],["goat","stonemonster","stonemonster","mountainwolf"]),
        (5,0):room((5,0),"battle",[[-1,0],[0,-1]],["goat","mountainwolf","stonemonster","stonemonster"]),

        (0,-1):room((0,-1),"bronzekey",[[1,0]],None),
        (1,-1):room((1,-1),"battle",[[1,0],[-1,0]],["mountainwolf","stonemonster","stonemonster","stonemonster"]),
        (2,-1):room((2,-1),"battle",[[1,0],[-1,0]],["goat","goat","stonemonster","stonemonster"]),
        (3,-1):room((3,-1),"battle",[[1,0],[-1,0]],["goat","mountainwolf","mountainwolf","goat"]),
        (4,-1):room((4,-1),"battle",[[1,0],[-1,0],[0,-1]],["stonemonster","mountainwolf","goat","goat"]),
        (5,-1):room((5,-1),"battle",[[-1,0],[0,1]],["stonemonster","mountainwolf","stonemonster","mountainwolf"]),

        (1,-2):room((1,-2),"battle",[[1,0],[0,-1]],["mountainwolf","goat","stonemonster","stonemonster"]),
        (2,-2):room((2,-2),"battle",[[1,0],[-1,0]],["mountainwolf","mountainwolf","goat","mountainwolf"]),
        (3,-2):room((3,-2),"battle",[[1,0],[-1,0]],["stonemonster","goat","mountainwolf","mountainwolf"]),
        (4,-2):room((4,-2),"bronzelock",[[-1,0],[0,1]],None),

        (1,-3):room((1,-3),"battle",[[1,0],[0,1]],["stonemonster","goat","mountainwolf","mountainwolf"]),
        (2,-3):room((2,-3),"battle",[[1,0],[-1,0],[0,-1]],["stonemonster","goat","mountainwolf","mountainwolf"]),
        (3,-3):room((3,-3),"battle",[[1,0],[-1,0]],["goat","mountainwolf","mountainwolf","goat"]),
        (4,-3):room((4,-3),"silverkey",[[-1,0]],None),

        (2,-4):room((2,-4),"silverlock",[[1,0],[0,1]],None),
        (3,-4):room((3,-4),"battle",[[-1,0],[0,-1]],["goat","goat","stonemonster","stonemonster"]),

        (2,-5):room((2,-5),"boss",[[1,0]],["stonemonster","mountainwolf","alpha"]),
        (3,-5):room((3,-5),"battle",[[-1,0],[0,1]],["stonemonster","goat","mountainwolf","mountainwolf"])}),

    dungeon("mountain3","mountain",78,1,[197,2184],[140,280],{
        (0,0):room((0,0),"door",[[1,0]],None),
        (1,0):room((1,0),"battle",[[1,0],[-1,0],[0,-1]],["goat","goat","stonemonster","stonemonster"] ),
        (2,0):room((2,0),"battle",[[1,0],[-1,0]],["goat","goat","goat","goat"] ),
        (3,0):room((3,0),"battle",[[1,0],[-1,0]],["goat","mountainwolf","goat","stonemonster"]),
        (4,0):room((4,0),"battle",[[1,0],[-1,0]],["goat","goat","mountainwolf","stonemonster"] ),
        (5,0):room((5,0),"battle",[[1,0],[-1,0]],["goat","mountainwolf","mountainwolf","mountainwolf"]),
        (6,0):room((6,0),"bronzekey",[[-1,0]],None),

        (1,-1):room((1,-1),"bronzelock",[[1,0],[0,1]],None),
        (2,-1):room((2,-1),"battle",[[1,0],[-1,0]],["stonemonster","goat","mountainwolf","stonemonster"]),
        (3,-1):room((3,-1),"battle",[[1,0],[-1,0]],["goat","mountainwolf","mountainwolf","stonemonster"]),
        (4,-1):room((4,-1),"battle",[[1,0],[-1,0]],["stonemonster","mountainwolf","mountainwolf","mountainwolf"]),
        (5,-1):room((5,-1),"battle",[[-1,0],[0,-1]],["stonemonster","goat","stonemonster","mountainwolf"]),

        (1,-2):room((1,-2),"silverkey",[[1,0]],None),
        (2,-2):room((2,-2),"battle",[[1,0],[-1,0]],["stonemonster","stonemonster","stonemonster","stonemonster"]),
        (3,-2):room((3,-2),"battle",[[1,0],[-1,0]],["stonemonster","goat","mountainwolf","goat"]),
        (4,-2):room((4,-2),"battle",[[1,0],[-1,0],[0,-1]],["goat","goat","goat","stonemonster"]),
        (5,-2):room((5,-2),"battle",[[-1,0],[0,1]],["stonemonster","stonemonster","goat","mountainwolf"]),

        (2,-3):room((2,-3),"battle",[[1,0],[0,-1]],["mountainwolf","goat","goat","stonemonster"]),
        (3,-3):room((3,-3),"battle",[[1,0],[-1,0]],["stonemonster","stonemonster","stonemonster","goat"]),
        (4,-3):room((4,-3),"silverlock",[[-1,0],[0,1],[0,-1]],None),

        (2,-4):room((2,-4),"goldkey",[[0,1]],None),
        (3,-4):room((3,-4),"goldlock",[[1,0],[0,-1]],None),
        (4,-4):room((4,-4),"battle",[[-1,0],[0,1]],["goat","goat","mountainwolf","stonemonster"]),

        (3,-5):room((3,-5),"boss",[[0,1]],["stonemonster","goat","mountainlion"])}),

    dungeon("mountain4","mountain",79,1,[118,2118],[140,80],{
        (0,0):room((0,0),"door",[[0,1]],None),
        (6,0):room((0,0),"boss",[[0,1]],["stonemonster","goat","mountainwolf","griffin"]),
        
        (0,1):room((0,1),"battle",[[1,0],[0,-1]],["stonemonster","goat","mountainwolf","mountainwolf"]),
        (1,1):room((1,1),"battle",[[-1,0],[0,1]],["mountainwolf","stonemonster","goat","goat"]),
        (5,1):room((5,1),"battle",[[1,0],[0,1]],["stonemonster","goat","goat","goat"]),
        (6,1):room((6,1),"battle",[[-1,0],[0,-1]],["stonemonster","stonemonster","goat","goat"]),

        (0,2):room((0,2),"battle",[[1,0],[0,1]],["mountainwolf","mountainwolf","stonemonster","goat"]),
        (1,2):room((1,2),"battle",[[-1,0],[0,-1]],["goat","stonemonster","goat","mountainwolf"]),
        (5,2):room((5,2),"battle",[[1,0],[0,-1]],["mountainwolf","mountainwolf","mountainwolf","stonemonster"]),
        (6,2):room((6,2),"battle",[[-1,0],[0,1]],["stonemonster","goat","goat","goat"]),

        (0,3):room((0,3),"battle",[[1,0],[0,-1]],["mountainwolf","goat","stonemonster","mountainwolf"]),
        (1,3):room((1,3),"battle",[[1,0],[-1,0]],["mountainwolf","stonemonster","stonemonster","mountainwolf"]),
        (2,3):room((2,3),"battle",[[-1,0],[0,1]],["stonemonster","goat","mountainwolf","stonemonster"]),
        (4,3):room((4,3),"battle",[[1,0],[0,1]],["mountainwolf","mountainwolf","stonemonster","mountainwolf"]),
        (5,3):room((5,3),"battle",[[1,0],[-1,0]],["mountainwolf","goat","goat","goat"]),
        (6,3):room((6,3),"battle",[[-1,0],[0,-1]],["mountainwolf","mountainwolf","mountainwolf","mountainwolf"]),

        (0,4):room((0,4),"battle",[[1,0],[0,1]],["goat","stonemonster","mountainwolf","mountainwolf"]),
        (1,4):room((1,4),"battle",[[1,0],[-1,0]],["stonemonster","stonemonster","mountainwolf","stonemonster"]),
        (2,4):room((2,4),"battle",[[-1,0],[0,-1]],["mountainwolf","stonemonster","stonemonster","goat"]),
        (4,4):room((4,4),"battle",[[1,0],[0,-1]],["goat","goat","goat","mountainwolf"]),
        (5,4):room((5,4),"battle",[[1,0],[-1,0]],["mountainwolf","goat","goat","stonemonster"]),
        (6,4):room((6,4),"battle",[[-1,0],[0,1]],["goat","goat","mountainwolf","mountainwolf"]),

        (0,5):room((0,5),"battle",[[1,0],[0,-1]],["mountainwolf","stonemonster","stonemonster","stonemonster"]),
        (1,5):room((1,5),"battle",[[1,0],[-1,0]],["mountainwolf","stonemonster","stonemonster","mountainwolf"]),
        (2,5):room((2,5),"battle",[[1,0],[-1,0]],["mountainwolf","goat","mountainwolf","mountainwolf"]),
        (3,5):room((3,5),"battle",[[1,0],[-1,0]],["stonemonster","mountainwolf","mountainwolf","goat"]),
        (4,5):room((4,5),"battle",[[1,0],[-1,0]],["stonemonster","stonemonster","mountainwolf","stonemonster"]),
        (5,5):room((5,5),"battle",[[1,0],[-1,0]],["mountainwolf","mountainwolf","stonemonster","mountainwolf"]),
        (6,5):room((6,5),"battle",[[-1,0],[0,-1]],["stonemonster","goat","mountainwolf","goat"])}),

    dungeon("mountain5","mountain",80,1,[34,2027],[140,300],{
        (0,0):room((0,0),"door",[[1,0]],None),
        (1,0):room((1,0),"battle",[[1,0],[-1,0]],["stonemonster","mountainwolf","mountainwolf","goat"]),
        (2,0):room((2,0),"battle",[[1,0],[-1,0]],["mountainwolf","goat","goat","mountainwolf"]),
        (3,0):room((3,0),"battle",[[1,0],[-1,0]],["goat","stonemonster","stonethrower","mountainwolf"]),
        (4,0):room((4,0),"battle",[[1,0],[-1,0]],["goat","stonemonster","stonethrower","stonemonster"]),
        (5,0):room((5,0),"battle",[[1,0],[-1,0]],["goat","stonemonster","stonemonster","mountainwolf"]),
        (6,0):room((6,0),"battle",[[-1,0],[0,-1]],["mountainwolf","stonemonster","mountainwolf","stonethrower"]),

        (1,-1):room((1,-1),"battle",[[1,0],[0,-1]],["goat","goat","mountainwolf","stonethrower"] ),
        (2,-1):room((2,-1),"battle",[[1,0],[-1,0]],["goat","goat","stonethrower","stonemonster"] ),
        (3,-1):room((3,-1),"battle",[[1,0],[-1,0]],["goat","stonethrower","goat","goat"]),
        (4,-1):room((4,-1),"battle",[[1,0],[-1,0]],["goat","mountainwolf","mountainwolf","mountainwolf"]),
        (5,-1):room((5,-1),"battle",[[1,0],[-1,0]],["stonethrower","stonethrower","mountainwolf","stonethrower"]),
        (6,-1):room((6,-1),"battle",[[-1,0],[0,1]],["goat","stonethrower","goat","stonethrower"]),

        (1,-2):room((1,-2),"battle",[[1,0],[0,1]],["goat","mountainwolf","stonethrower","mountainwolf"]),
        (2,-2):room((2,-2),"battle",[[1,0],[-1,0]],["mountainwolf","goat","goat","goat"]),
        (3,-2):room((3,-2),"battle",[[1,0],[-1,0]],["goat","goat","stonemonster","goat"]),
        (4,-2):room((4,-2),"battle",[[1,0],[-1,0]],["goat","goat","stonemonster","goat"]),
        (5,-2):room((5,-2),"battle",[[-1,0],[0,-1]],["goat","mountainwolf","mountainwolf","stonemonster"]),

        (2,-3):room((2,-3),"battle",[[1,0],[0,-1]],["mountainwolf","stonethrower","stonethrower","stonethrower"]),
        (3,-3):room((3,-3),"battle",[[1,0],[-1,0]],["mountainwolf","mountainwolf","mountainwolf","stonethrower"]),
        (4,-3):room((4,-3),"battle",[[1,0],[-1,0]],["goat","goat","mountainwolf","stonemonster"]),
        (5,-3):room((5,-3),"battle",[[-1,0],[0,1]],["stonemonster","goat","goat","stonethrower"]),

        (2,-4):room((2,-4),"battle",[[1,0],[0,1]],["goat","stonethrower","goat","stonemonster"]),
        (3,-4):room((3,-4),"battle",[[1,0],[-1,0]],["mountainwolf","stonemonster","mountainwolf","mountainwolf"]),
        (4,-4):room((4,-4),"battle",[[-1,0],[0,-1]],["stonethrower","goat","stonemonster","stonemonster"]),

        (3,-5):room((3,-5),"battle",[[1,0],[0,-1]],["stonethrower","goat","goat","mountainwolf"]),
        (4,-5):room((4,-5),"battle",[[-1,0],[0,1]],["mountainwolf","stonemonster","mountainwolf","stonemonster"]),

        (3,-6):room((3,-6),"boss",[[0,1]],["mountainwolf","stonethrower","yeti"])}),

    dungeon("mountain6","glacier",81,1,[130,1991],[200,300],{
        (0,-6):room((0,-6),"battle",[[1,0],[0,1]],["stonethrower","icemonster","icemonster","mountainwolf"]),
        (1,-6):room((1,-6),"battle",[[1,0],[-1,0]],["stonethrower","icemonster","goat","icemonster"]),
        (2,-6):room((2,-6),"battle",[[1,0],[-1,0]],["mountainwolf","icemonster","mountainwolf","goat"]),
        (3,-6):room((3,-6),"boss",[[-1,0]],["icemonster","icemonster","stonethrower","icedragon"]),
        (0,-5):room((0,-5),"battle",[[1,0],[0,-1]],["goat","icemonster","goat","mountainwolf"]),
        (1,-5):room((1,-5),"battle",[[1,0],[-1,0]],["goat","icemonster","icemonster","icemonster"]),
        (2,-5):room((2,-5),"battle",[[1,0],[-1,0]],["icemonster","icemonster","icemonster","stonethrower"]),
        (3,-5):room((3,-5),"battle",[[-1,0],[0,1]],["goat","icemonster","icemonster","stonethrower"]),
        (0,-4):room((0,-4),"battle",[[1,0],[0,1]],["goat","goat","icemonster","mountainwolf"]),
        (1,-4):room((1,-4),"battle",[[1,0],[-1,0]],["icemonster","icemonster","icemonster","mountainwolf"]),
        (2,-4):room((2,-4),"battle",[[1,0],[-1,0]],["goat","icemonster","icemonster","icemonster"]),
        (3,-4):room((3,-4),"battle",[[-1,0],[0,-1]],["icemonster","mountainwolf","goat","icemonster"]),
        (0,-3):room((0,-3),"battle",[[1,0],[0,-1]],["goat","mountainwolf","mountainwolf","mountainwolf"]),
        (1,-3):room((1,-3),"battle",[[1,0],[-1,0]],["icemonster","mountainwolf","icemonster","goat"]),
        (2,-3):room((2,-3),"battle",[[1,0],[-1,0]],["mountainwolf","goat","stonethrower","icemonster"]),
        (3,-3):room((3,-3),"battle",[[-1,0],[0,1]],["icemonster","icemonster","icemonster","icemonster"]),
        (0,-2):room((0,-2),"battle",[[1,0],[0,1]],["icemonster","mountainwolf","icemonster","goat"]),
        (1,-2):room((1,-2),"battle",[[1,0],[-1,0]],["mountainwolf","stonethrower","mountainwolf","icemonster"]),
        (2,-2):room((2,-2),"battle",[[1,0],[-1,0]],["goat","icemonster","mountainwolf","icemonster"]),
        (3,-2):room((3,-2),"battle",[[-1,0],[0,-1]],["icemonster","mountainwolf","icemonster","mountainwolf"]),
        (0,-1):room((0,-1),"battle",[[1,0],[0,-1]],["icemonster","icemonster","goat","stonethrower"]),
        (1,-1):room((1,-1),"battle",[[1,0],[-1,0]],["icemonster","icemonster","goat","mountainwolf"]),
        (2,-1):room((2,-1),"battle",[[1,0],[-1,0]],["goat","mountainwolf","icemonster","icemonster"]),
        (3,-1):room((3,-1),"battle",[[-1,0],[0,1]],["mountainwolf","icemonster","goat","stonethrower"]),
        (0,0):room((0,0),"door",[[1,0]],["icemonster","mountainwolf","mountainwolf","mountainwolf"]),
        (1,0):room((1,0),"battle",[[1,0],[-1,0]],["goat","goat","icemonster","goat"]),
        (2,0):room((2,0),"battle",[[1,0],[-1,0]],["goat","icemonster","goat","mountainwolf"]),
        (3,0):room((3,0),"battle",[[-1,0],[0,-1]],["goat","goat","goat","mountainwolf"])}),

    dungeon("mountain7","treasurecave",82,1,[203,1948],[120,80],{
        (0,0):room((0,0),"door",[[0,1]],None),
        (1,0):room((1,0),"battle",[[1,0],[0,1]],["stonemonster","goldcrab","goldcrab","stonemonster"]),
        (2,0):room((2,0),"battle",[[-1,0],[0,1]],["stonemonster","goldcrab","goldbat","goldsnake"]),
        (3,0):room((3,0),"magickey",[[0,1]],None),
        (0,1):room((0,1),"battle",[[1,0],[0,-1]],["goldcrab","goldsnake","goldcrab","goldcrab"]),
        (1,1):room((1,1),"battle",[[-1,0],[0,-1]],["goldsnake","goldcrab","stonemonster","goldbat"] ),
        (2,1):room((2,1),"battle",[[0,1],[0,-1]],["goldsnake","goldbat","goldcrab","goldcrab"] ),
        (3,1):room((3,1),"chest",[[1,0],[0,-1]],[16,["item",99],["item",99]]),
        (4,1):room((4,1),"battle",[[-1,0],[0,1]],["stonemonster","goldbat","goldsnake","goldsnake"] ),
        (2,2):room((2,2),"battle",[[1,0],[0,-1]],["goldsnake","goldcrab","goldbat","goldcrab"] ),
        (3,2):room((3,2),"battle",[[-1,0],[0,1]],["stonemonster","goldbat","goldcrab","goldcrab"] ),
        (4,2):room((4,2),"battle",[[1,0],[0,-1]],["goldcrab","goldcrab","goldbat","goldsnake"] ),
        (5,2):room((5,2),"battle",[[1,0],[-1,0]],["goldbat","stonemonster","goldcrab","goldcrab"] ),
        (6,2):room((6,2),"battle",[[1,0],[-1,0]],["goldcrab","goldcrab","goldcrab","goldcrab"] ),
        (7,2):room((7,2),"silverlock",[[-1,0],[0,1]],None),
        (3,3):room((3,3),"battle",[[1,0],[0,-1]],["goldcrab","goldcrab","goldbat","goldbat"] ),
        (4,3):room((4,3),"battle",[[1,0],[-1,0]],["goldcrab","goldcrab","stonemonster","goldbat"] ),
        (5,3):room((5,3),"battle",[[1,0],[-1,0]],["goldcrab","goldcrab","goldcrab","goldbat"] ),
        (6,3):room((6,3),"battle",[[1,0],[-1,0]],["stonemonster","goldbat","goldcrab","goldbat"] ),
        (7,3):room((7,3),"battle",[[-1,0],[0,1],[0,-1]],["goldcrab","goldbat","goldcrab","goldcrab"]),
        (4,4):room((4,4),"chest",[[1,0],[0,1]],[17,["item",103],["item",103]]),
        (5,4):room((5,4),"battle",[[1,0],[-1,0]],["goldcrab","stonemonster","goldbat","goldsnake"]),
        (6,4):room((6,4),"battle",[[1,0],[-1,0]],["goldbat","stonemonster","goldsnake","goldsnake"]),
        (7,4):room((7,4),"battle",[[-1,0],[0,-1]],["goldcrab","goldcrab","stonemonster","stonemonster"]),
        (4,5):room((4,5),"silverkey",[[1,0],[0,-1]],None),
        (5,5):room((5,5),"magiclock",[[1,0],[-1,0]],None),
        (6,5):room((6,5),"game",[[1,0],[-1,0]],None),
        (7,5):room((7,5),"boss",[[-1,0]],["goldcrab","goldsnake","hoarderdragon"])}),

    dungeon("mountain8","mountain",83,2,[279,1911],[120,320],{
        (0,0):room((0,0),"door",[[1,0]],None),
        (1,0):room((1,0),"battle",[[1,0],[-1,0]],["goat","goat","mountainwolf","stonemonster"]),
        (2,0):room((2,0),"battle",[[1,0],[-1,0]],["mountainwolf","stonethrower","stonemonster","mountainwolf"]),
        (3,0):room((3,0),"battle",[[1,0],[-1,0]],["goat","stonethrower","mountainwolf","goat"]),
        (4,0):room((4,0),"battle",[[1,0],[-1,0]],["goat","goat","mountainwolf","mountainwolf"]),
        (5,0):room((5,0),"battle",[[1,0],[-1,0]],["mountainwolf","mountainwolf","mountainwolf","stonemonster"]),
        (6,0):room((6,0),"battle",[[1,0],[-1,0]],["stonethrower","stonethrower","goat","mountainwolf"]),
        (7,0):room((7,0),"battle",[[-1,0],[0,-1]],["goat","stonemonster","stonemonster","mountainwolf"]),

        (1,-1):room((1,-1),"battle",[[1,0],[0,-1]],["stonemonster","stonethrower","stonemonster","stonemonster"]),
        (2,-1):room((2,-1),"battle",[[1,0],[-1,0]],["stonemonster","stonethrower","stonethrower","goat"]),
        (3,-1):room((3,-1),"battle",[[1,0],[-1,0]],["stonemonster","mountainwolf","mountainwolf","mountainwolf"]),
        (4,-1):room((4,-1),"battle",[[1,0],[-1,0]],["mountainwolf","stonemonster","mountainwolf","stonethrower"]),
        (5,-1):room((5,-1),"battle",[[1,0],[-1,0]],["stonethrower","mountainwolf","stonemonster","mountainwolf"]),
        (6,-1):room((6,-1),"battle",[[1,0],[-1,0]],["stonemonster","goat","stonemonster","stonemonster"]),
        (7,-1):room((7,-1),"battle",[[-1,0],[0,1]],["stonemonster","goat","stonemonster","stonemonster"]),

        (1,-2):room((1,-2),"battle",[[1,0],[0,1]],["mountainwolf","stonemonster","goat","mountainwolf"] ),
        (2,-2):room((2,-2),"battle",[[1,0],[-1,0]],["mountainwolf","stonethrower","mountainwolf","mountainwolf"]),
        (3,-2):room((3,-2),"battle",[[1,0],[-1,0]],["mountainwolf","stonemonster","stonethrower","stonemonster"]),
        (4,-2):room((4,-2),"battle",[[1,0],[-1,0]],["stonemonster","mountainwolf","mountainwolf","stonemonster"]),
        (5,-2):room((5,-2),"battle",[[1,0],[-1,0]],["stonethrower","mountainwolf","stonemonster","mountainwolf"]),
        (6,-2):room((6,-2),"battle",[[-1,0],[0,-1]],["stonemonster","mountainwolf","stonethrower","stonemonster"]),

        (2,-3):room((2,-3),"battle",[[1,0],[0,-1]],["mountainwolf","goat","stonemonster","stonethrower"]),
        (3,-3):room((3,-3),"battle",[[1,0],[-1,0]],["goat","stonethrower","stonemonster","stonethrower"]),
        (4,-3):room((4,-3),"battle",[[1,0],[-1,0]],["stonethrower","stonemonster","goat","stonethrower"]),
        (5,-3):room((5,-3),"battle",[[1,0],[-1,0]],["goat","mountainwolf","mountainwolf","stonemonster"]),
        (6,-3):room((6,-3),"battle",[[-1,0],[0,1]],["stonemonster","goat","stonethrower","stonethrower"]),

        (2,-4):room((2,-4),"battle",[[1,0],[0,1]],["stonemonster","stonemonster","stonemonster","mountainwolf"]),
        (3,-4):room((3,-4),"battle",[[1,0],[-1,0]],["goat","stonemonster","stonethrower","goat"]),
        (4,-4):room((4,-4),"battle",[[1,0],[-1,0]],["stonethrower","goat","mountainwolf","mountainwolf"]),
        (5,-4):room((5,-4),"battle",[[-1,0],[0,-1]],["stonemonster","stonethrower","stonemonster","stonethrower"]),

        (3,-5):room((3,-5),"battle",[[1,0],[0,-1]],["stonemonster","stonemonster","stonemonster","stonemonster"]),
        (4,-5):room((4,-5),"battle",[[1,0],[-1,0]],["mountainwolf","stonemonster","stonemonster","goat"]),
        (5,-5):room((5,-5),"battle",[[-1,0],[0,1]],["mountainwolf","mountainwolf","mountainwolf","goat"]),

        (3,-6):room((3,-6),"battle",[[1,0],[0,1]],["goat","stonethrower","stonethrower","mountainwolf"]),
        (4,-6):room((4,-6),"battle",[[-1,0],[0,-1]],["stonemonster","stonemonster","stonethrower","stonethrower"]),

        (3,-7):room((3,-7),"boss",[[1,0]],["stonemonster","stonethrower","mountainbird"]),
        (4,-7):room((4,-7),"game",[[-1,0],[0,1]],None)}),

    dungeon("volcano1","volcano",84,1,[246,1854],[160,260],{
        (0,0):room((0,0),"door",[[1,0]],None),
        (1,0):room((1,0),"battle",[[1,0],[-1,0]],["pyroclast","pyroclast","pyroclast","lavamonster"]),
        (2,0):room((2,0),"battle",[[1,0],[-1,0]],["pyroclast","pyroclast","pyroclast","lavamonster"]),
        (3,0):room((3,0),"battle",[[1,0],[-1,0]],["pyroclast","pyroclast","babydragon","pyroclast"]),
        (4,0):room((4,0),"battle",[[1,0],[-1,0]],["pyroclast","pyroclast","lavamonster","lavamonster"]),
        (5,0):room((5,0),"battle",[[-1,0],[0,-1]],["babydragon","pyroclast","lavamonster","babydragon"]),
        (5,-1):room((5,-1),"battle",[[-1,0],[0,1]],["pyroclast","lavamonster","pyroclast","pyroclast"]),
        (4,-1):room((4,-1),"battle",[[1,0],[-1,0]],["pyroclast","lavamonster","pyroclast","pyroclast"]),
        (3,-1):room((3,-1),"battle",[[1,0],[-1,0],[0,-1]],["pyroclast","babydragon","lavamonster","pyroclast"]),
        (2,-1):room((2,-1),"battle",[[1,0],[-1,0]],["babydragon","pyroclast","lavamonster","babydragon"]),
        (1,-1):room((1,-1),"battle",[[1,0],[-1,0]],["pyroclast","pyroclast","lavamonster","babydragon"]),
        (0,-1):room((0,-1),"battle",[[1,0],[0,-1]],["pyroclast","pyroclast","lavamonster","babydragon"]),
        (0,-2):room((0,-2),"bronzekey",[[0,1]],None),
        (3,-2):room((3,-2),"bronzelock",[[-1,0],[0,1],[0,-1]],None),
        (3,-3):room((3,-3),"battle",[[1,0],[0,1]],["pyroclast","pyroclast","babydragon","pyroclast"]),
        (4,-3):room((4,-3),"battle",[[-1,0],[0,1]],["lavamonster","pyroclast","lavamonster","pyroclast"]),
        (4,-2):room((4,-2),"battle",[[1,0],[0,-1]],["pyroclast","pyroclast","pyroclast","pyroclast"]),
        (5,-2):room((5,-2),"silverkey",[[-1,0]],None),
        (2,-2):room((2,-2),"battle",[[1,0],[-1,0]],["pyroclast","lavamonster","pyroclast","lavamonster"]),
        (1,-2):room((1,-2),"battle",[[1,0],[0,-1]],["pyroclast","pyroclast","lavamonster","lavamonster"]),
        (1,-3):room((1,-3),"silverlock",[[1,0],[0,1]],None),
        (2,-3):room((2,-3),"battle",[[-1,0],[0,-1]],["pyroclast","pyroclast","pyroclast","pyroclast"]),
        (2,-4):room((2,-4),"battle",[[1,0],[0,1]],["babydragon","pyroclast","lavamonster","pyroclast"]),
        (3,-4):room((3,-4),"boss",[[-1,0]],["pyroclast","pyroclast","lavamonster","pyroclastking"])}),

    dungeon("volcano2","volcano",85,1,[364,1782],[260,260],{
        (-4,-4):room((-4,-4),"battle",[[1,0],[0,1]],["pyroclast","lavamonster","babydragon","lavamonster"]),
        (-3,-4):room((-3,-4),"battle",[[-1,0],[0,1]],["lavamonster","lavamonster","lavamonster","pyroclast"]),
        (0,-4):room((0,-4),"boss",[[0,1]],["babydragon","lavamonster","dragon"]),
        (3,-4):room((3,-4),"battle",[[1,0],[0,1]],["lavamonster","pyroclast","babydragon","babydragon"]),
        (4,-4):room((4,-4),"battle",[[-1,0],[0,1]],["babydragon","lavamonster","babydragon","babydragon"]),

        (-4,-3):room((-4,-3),"battle",[[0,1],[0,-1]],["lavamonster","babydragon","babydragon","pyroclast"]),
        (-3,-3):room((-3,-3),"battle",[[1,0],[0,-1]],["babydragon","pyroclast","pyroclast","babydragon"]),
        (-2,-3):room((-2,-3),"battle",[[1,0],[-1,0]],["pyroclast","pyroclast","lavamonster","pyroclast"]),
        (-1,-3):room((-1,-3),"goldkey",[[-1,0]],None),
        (0,-3):room((0,-3),"goldlock",[[1,0],[0,-1]],None),
        (1,-3):room((1,-3),"battle",[[1,0],[-1,0]],["babydragon","lavamonster","babydragon","babydragon"]),
        (2,-3):room((2,-3),"battle",[[1,0],[-1,0]],["babydragon","babydragon","pyroclast","lavamonster"]),
        (3,-3):room((3,-3),"battle",[[-1,0],[0,-1]],["babydragon","babydragon","pyroclast","lavamonster"]),
        (4,-3):room((4,-3),"battle",[[0,1],[0,-1]],["babydragon","lavamonster","babydragon","babydragon"]),

        (-4,-2):room((-4,-2),"battle",[[1,0],[0,-1]],["babydragon","babydragon","babydragon","babydragon"]),
        (-3,-2):room((-3,-2),"battle",[[-1,0],[0,1]],["lavamonster","babydragon","lavamonster","pyroclast"]),
        (-2,-2):room((-2,-2),"battle",[[1,0],[0,1]],["babydragon","babydragon","babydragon","lavamonster"]),
        (-1,-2):room((-1,-2),"battle",[[1,0],[-1,0]],["lavamonster","babydragon","lavamonster","babydragon"]),
        (0,-2):room((0,-2),"battle",[[1,0],[-1,0],[0,1]],["lavamonster","babydragon","babydragon","pyroclast"]),
        (1,-2):room((1,-2),"battle",[[1,0],[-1,0]],["pyroclast","babydragon","babydragon","babydragon"]),
        (2,-2):room((2,-2),"battle",[[-1,0],[0,1]],["lavamonster","pyroclast","babydragon","lavamonster"]),
        (3,-2):room((3,-2),"battle",[[1,0],[0,1]],["babydragon","lavamonster","babydragon","lavamonster"]),
        (4,-2):room((4,-2),"battle",[[-1,0],[0,-1]],["lavamonster","babydragon","pyroclast","pyroclast"]),

        (-3,-1):room((-3,-1),"battle",[[1,0],[0,-1]],["babydragon","babydragon","lavamonster","babydragon"]),
        (-2,-1):room((-2,-1),"battle",[[-1,0],[0,-1]],["lavamonster","pyroclast","babydragon","pyroclast"]),
        (0,-1):room((0,-1),"battle",[[0,1],[0,-1]],["lavamonster","lavamonster","pyroclast","lavamonster"]),
        (2,-1):room((2,-1),"battle",[[1,0],[0,-1]],["babydragon","pyroclast","pyroclast","babydragon"]),
        (3,-1):room((3,-1),"battle",[[-1,0],[0,-1]],["babydragon","lavamonster","pyroclast","babydragon"]),

        (0,0):room((0,0),"door",[[0,-1]],None)}),

    dungeon("volcano3","volcano",86,1,[445,1672],[260,60],{
        (0,0):room((0,0),"door",[[0,1]],None),

        (-1,1):room((-1,1),"battle",[[1,0],[0,1]],["lavamonster","babydragon","lavamonster","lavamonster"]),
        (0,1):room((0,1),"battle",[[1,0],[-1,0],[0,1],[0,-1]],["babydragon","babydragon","babydragon","lavamonster"]),
        (1,1):room((1,1),"battle",[[-1,0],[0,1]],["lavamonster","lavamonster","pyroclast","lavamonster"]),
        
        (-2,2):room((-2,2),"battle",[[1,0],[0,1]],["pyroclast","babydragon","lavamonster","babydragon"]),
        (-1,2):room((-1,2),"battle",[[-1,0],[0,-1]],["lavamonster","lavamonster","lavamonster","lavamonster"]),
        (0,2):room((0,2),"bronzelock",[[0,1],[0,-1]],None),
        (1,2):room((1,2),"battle",[[1,0],[0,-1]],["pyroclast","pyroclast","pyroclast","babydragon"]),
        (2,2):room((2,2),"battle",[[-1,0],[0,1]],["pyroclast","babydragon","pyroclast","babydragon"]),

        (-2,3):room((-2,3),"battle",[[0,1],[0,-1]],["pyroclast","lavamonster","lavamonster","lavamonster"]),
        (-1,3):room((-1,3),"battle",[[1,0],[0,1]],["pyroclast","babydragon","pyroclast","lavamonster"]),
        (0,3):room((0,3),"bronzelock",[[1,0],[-1,0],[0,1],[0,-1]],None),
        (1,3):room((1,3),"battle",[[-1,0],[0,1]],["pyroclast","pyroclast","lavamonster","lavamonster"]),
        (2,3):room((2,3),"battle",[[0,1],[0,-1]],["pyroclast","lavamonster","pyroclast","lavamonster"]),

        (-2,4):room((-2,4),"battle",[[0,1],[0,-1]],["lavamonster","lavamonster","lavamonster","pyroclast"]),
        (-1,4):room((-1,4),"battle",[[0,1],[0,-1]],["lavamonster","pyroclast","babydragon","lavamonster"]),
        (0,4):room((0,4),"silverlock",[[0,1],[0,-1]],None),
        (1,4):room((1,4),"battle",[[0,1],[0,-1]],["pyroclast","babydragon","babydragon","lavamonster"]),
        (2,4):room((2,4),"battle",[[0,1],[0,-1]],["lavamonster","pyroclast","pyroclast","babydragon"]),

        (-2,5):room((-2,5),"battle",[[0,1],[0,-1]],["lavamonster","babydragon","babydragon","lavamonster"]),
        (-1,5):room((-1,5),"battle",[[0,1],[0,-1]],["pyroclast","pyroclast","lavamonster","pyroclast"]),
        (0,5):room((0,5),"silverlock",[[0,1],[0,-1]],None),
        (1,5):room((1,5),"battle",[[0,1],[0,-1]],["pyroclast","lavamonster","lavamonster","babydragon"]),
        (2,5):room((2,5),"battle",[[0,1],[0,-1]],["pyroclast","lavamonster","lavamonster","babydragon"]),

        (-2,6):room((-2,6),"bronzekey",[[0,-1]],None),
        (-1,6):room((-1,6),"silverkey",[[0,-1]],None),
        (0,6):room((0,6),"boss",[[0,-1]],["pyroclast","lavamonster","lavamonster","lavaking"]),
        (1,6):room((1,6),"silverkey",[[0,-1]],None),
        (2,6):room((2,6),"bronzekey",[[0,-1]],None)}),

    dungeon("volcano4","volcano",87,1,[383,1654],[260,20],{
        (0,0):room((0,0),"door",[[0,1]],None),

        (-1,1):room((-1,1),"battle",[[1,0],[0,1]],["pyroclast","pyroclast","babydragon","pyroclast"]),
        (0,1):room((0,1),"battle",[[1,0],[-1,0],[0,1],[0,-1]],["pyroclast","lavamonster","pyroclast","lavamonster"]),
        (1,1):room((1,1),"battle",[[-1,0],[0,1]],["lavamonster","lavamonster","pyroclast","lavamonster"]),

        (-2,2):room((-2,2),"battle",[[1,0],[0,1]],["pyroclast","pyroclast","pyroclast","lavamonster"]),
        (-1,2):room((-1,2),"battle",[[-1,0],[0,-1]],["babydragon","pyroclast","lavamonster","lavamonster"]),
        (0,2):room((0,2),"bronzelock",[[0,1],[0,-1]],["lavamonster","lavamonster","babydragon","pyroclast"]),
        (1,2):room((1,2),"battle",[[1,0],[0,-1]],["babydragon","babydragon","babydragon","lavamonster"]),
        (2,2):room((2,2),"battle",[[-1,0],[0,1]],["pyroclast","pyroclast","lavamonster","lavamonster"]),

        (-3,3):room((-3,3),"battle",[[1,0],[0,1]],["pyroclast","lavamonster","babydragon","lavamonster"]),
        (-2,3):room((-2,3),"battle",[[-1,0],[0,-1]],["pyroclast","lavamonster","babydragon","lavamonster"]),
        (-1,3):room((-1,3),"battle",[[1,0],[0,1]],["babydragon","babydragon","pyroclast","pyroclast"]),
        (0,3):room((0,3),"bronzelock",[[1,0],[-1,0],[0,1],[0,-1]],["lavamonster","lavamonster","lavamonster","lavamonster"]),
        (1,3):room((1,3),"battle",[[-1,0],[0,1]],["lavamonster","lavamonster","lavamonster","babydragon"]),
        (2,3):room((2,3),"battle",[[1,0],[0,-1]],["babydragon","pyroclast","babydragon","lavamonster"]),
        (3,3):room((3,3),"battle",[[-1,0],[0,1]],["lavamonster","babydragon","babydragon","pyroclast"]),

        (-4,4):room((-4,4),"battle",[[1,0],[0,1]],["pyroclast","babydragon","babydragon","lavamonster"]),
        (-3,4):room((-3,4),"battle",[[-1,0],[0,-1]],["pyroclast","pyroclast","pyroclast","pyroclast"]),
        (-2,4):room((-2,4),"battle",[[1,0],[0,1]],["lavamonster","lavamonster","pyroclast","pyroclast"]),
        (-1,4):room((-1,4),"battle",[[-1,0],[0,-1]],["lavamonster","pyroclast","babydragon","pyroclast"]),
        (0,4):room((0,4),"silverlock",[[0,1],[0,-1]],["pyroclast","babydragon","lavamonster","lavamonster"]),
        (1,4):room((1,4),"battle",[[1,0],[0,-1]],["pyroclast","lavamonster","babydragon","pyroclast"]),
        (2,4):room((2,4),"battle",[[-1,0],[0,1]],["pyroclast","pyroclast","pyroclast","lavamonster"]),
        (3,4):room((3,4),"battle",[[1,0],[0,-1]],["pyroclast","lavamonster","pyroclast","lavamonster"]),
        (4,4):room((4,4),"battle",[[-1,0],[0,1]],["babydragon","pyroclast","lavamonster","lavamonster"]),

        (-4,5):room((-4,5),"bronzekey",[[0,-1]],["lavamonster","babydragon","lavamonster","babydragon"]),
        (-3,5):room((-3,5),"silverkey",[[1,0]],["lavamonster","pyroclast","babydragon","lavamonster"]),
        (-2,5):room((-2,5),"battle",[[-1,0],[0,-1]],["lavamonster","lavamonster","lavamonster","lavamonster"]),
        (-1,5):room((-1,5),"battle",[[1,0],[0,1]],["pyroclast","babydragon","lavamonster","lavamonster"]),
        (0,5):room((0,5),"silverlock",[[1,0],[-1,0],[0,1],[0,-1]],["babydragon","lavamonster","lavamonster","lavamonster"]),
        (1,5):room((1,5),"battle",[[-1,0],[0,1]],["lavamonster","babydragon","babydragon","lavamonster"]),
        (2,5):room((2,5),"battle",[[1,0],[0,-1]],["lavamonster","lavamonster","lavamonster","babydragon"]),
        (3,5):room((3,5),"silverkey",[[-1,0]],["pyroclast","lavamonster","lavamonster","babydragon"]),
        (4,5):room((4,5),"bronzekey",[[0,-1]],["lavamonster","lavamonster","lavamonster","babydragon"]),

        (-1,6):room((-1,6),"goldkey",[[0,-1]],["lavamonster","lavamonster","babydragon","pyroclast"]),
        (0,6):room((0,6),"goldlock",[[0,1],[0,-1]],["lavamonster","pyroclast","lavamonster","pyroclast"]),
        (1,6):room((1,6),"goldkey",[[0,-1]],["pyroclast","pyroclast","pyroclast","babydragon"]),

        (0,7):room((0,7),"goldlock",[[0,1],[0,-1]],["lavamonster","lavamonster","lavamonster","babydragon"]),

        (0,8):room((0,8),"boss",[[0,-1]],["lavamonster","babydragon","lavaspider"])}),

    dungeon("volcano5","volcano",88,1,[241,1660],[260,40],{
        (0,0):room((0,0),"door",[[0,1]],None),

        (-2,1):room((-2,1),"battle",[[1,0],[0,1]],["lavamonster","pyroclast","lavamonster","lavamonster"]),
        (-1,1):room((-1,1),"battle",[[1,0],[-1,0]],["lavamonster","babydragon","lavamonster","pyroclast"]),
        (0,1):room((0,1),"battle",[[1,0],[-1,0],[0,1],[0,-1]],["lavamonster","lavamonster","lavamonster","pyroclast"]),
        (1,1):room((1,1),"battle",[[1,0],[-1,0]],["babydragon","lavamonster","babydragon","lavamonster"]),
        (2,1):room((2,1),"battle",[[-1,0],[0,1]],["lavamonster","babydragon","babydragon","lavamonster"]),

        (-3,2):room((-3,2),"battle",[[1,0],[0,1]],["babydragon","pyroclast","lavamonster","lavamonster"]),
        (-2,2):room((-2,2),"battle",[[-1,0],[0,-1]],["pyroclast","pyroclast","babydragon","lavamonster"]),
        (-1,2):room((-1,2),"bronzelock",[[1,0],[0,1]],None),
        (0,2):room((0,2),"battle",[[1,0],[-1,0],[0,1],[0,-1]],["lavamonster","lavamonster","pyroclast","lavamonster"]),
        (1,2):room((1,2),"bronzelock",[[-1,0],[0,1]],None),
        (2,2):room((2,2),"battle",[[1,0],[0,-1]],["pyroclast","lavamonster","lavamonster","lavamonster"]),
        (3,2):room((3,2),"battle",[[-1,0],[0,1]],["pyroclast","babydragon","lavamonster","lavamonster"]),

        (-3,3):room((-3,3),"battle",[[0,1],[0,-1]],["babydragon","lavamonster","lavamonster","lavamonster"]),
        (-2,3):room((-2,3),"battle",[[1,0],[0,1]],["pyroclast","babydragon","lavamonster","lavamonster"]),
        (-1,3):room((-1,3),"battle",[[-1,0],[0,-1]],["babydragon","pyroclast","lavamonster","lavamonster"]),
        (0,3):room((0,3),"silverlock",[[0,1],[0,-1]],None),
        (1,3):room((1,3),"battle",[[1,0],[0,-1]],["pyroclast","babydragon","lavamonster","lavamonster"]),
        (2,3):room((2,3),"battle",[[-1,0],[0,1]],["pyroclast","pyroclast","lavamonster","babydragon"]),
        (3,3):room((3,3),"battle",[[0,1],[0,-1]],["lavamonster","pyroclast","lavamonster","babydragon"]),

        (-3,4):room((-3,4),"bronzekey",[[0,-1]],None),
        (-2,4):room((-2,4),"battle",[[0,1],[0,-1]],["lavamonster","lavamonster","pyroclast","lavamonster"]),
        (-1,4):room((-1,4),"battle",[[1,0],[0,1]],["babydragon","pyroclast","babydragon","lavamonster"]),
        (0,4):room((0,4),"silverlock",[[1,0],[-1,0],[0,1],[0,-1]],None),
        (1,4):room((1,4),"battle",[[-1,0],[0,1]],["lavamonster","pyroclast","lavamonster","pyroclast"]),
        (2,4):room((2,4),"battle",[[0,1],[0,-1]],["lavamonster","pyroclast","lavamonster","lavamonster"]),
        (3,4):room((3,4),"bronzekey",[[0,-1]],None),

        (-2,5):room((-2,5),"silverkey",[[0,-1]],None),
        (-1,5):room((-1,5),"battle",[[0,1],[0,-1]],["lavamonster","lavamonster","babydragon","pyroclast"]),
        (0,5):room((0,5),"goldlock",[[0,1],[0,-1]],None),
        (1,5):room((1,5),"battle",[[0,1],[0,-1]],["lavamonster","lavamonster","lavamonster","lavamonster"]),
        (2,5):room((2,5),"silverkey",[[0,-1]],None),

        (-1,6):room((-1,6),"goldkey",[[0,-1]],None),
        (0,6):room((0,6),"goldlock",[[0,1],[0,-1]],None),
        (1,6):room((1,6),"goldkey",[[0,-1]],None),

        (0,7):room((0,7),"boss",[[0,-1]],["lavamonster","lavaseamonster"])}),

    dungeon("volcano6","volcano",89,1,[49,1578],[260,260],{
        (-5,-4):room((-5,-4),"bronzekey",[[1,0]],None),
        (-4,-4):room((-4,-4),"battle",[[-1,0],[0,1]],["pyroclast","pyroclast","pyroclast","lavamonster"]),
        (-3,-4):room((-3,-4),"goldkey",[[1,0]],None),
        (-2,-4):room((-2,-4),"battle",[[-1,0],[0,1]],["lavamonster","pyroclast","pyroclast","babydragon"]),
        (0,-4):room((0,-4),"boss",[[0,1]],["lavamonster","lavamonster","lavamonster","phoenix"]),
        (2,-4):room((2,-4),"battle",[[1,0],[0,1]],["lavamonster","pyroclast","pyroclast","lavamonster"]),
        (3,-4):room((3,-4),"magickey",[[-1,0]],None),
        (4,-4):room((4,-4),"battle",[[1,0],[0,1]],["pyroclast","lavamonster","lavamonster","lavamonster"]),
        (5,-4):room((5,-4),"bronzekey",[[-1,0]],None),

        (-4,-3):room((-4,-3),"battle",[[1,0],[0,-1]],["babydragon","pyroclast","lavamonster","lavamonster"]),
        (-3,-3):room((-3,-3),"battle",[[-1,0],[0,1]],["pyroclast","lavamonster","lavamonster","lavamonster"]),
        (-2,-3):room((-2,-3),"battle",[[1,0],[0,-1]],["babydragon","babydragon","babydragon","pyroclast"]),
        (-1,-3):room((-1,-3),"battle",[[-1,0],[0,1]],["pyroclast","pyroclast","lavamonster","lavamonster"]),
        (0,-3):room((0,-3),"magiclock",[[0,1],[0,-1]],None),
        (1,-3):room((1,-3),"battle",[[1,0],[0,1]],["pyroclast","pyroclast","pyroclast","lavamonster"]),
        (2,-3):room((2,-3),"battle",[[-1,0],[0,-1]],["babydragon","babydragon","lavamonster","pyroclast"]),
        (3,-3):room((3,-3),"battle",[[1,0],[0,1]],["pyroclast","pyroclast","lavamonster","lavamonster"]),
        (4,-3):room((4,-3),"battle",[[-1,0],[0,-1]],["lavamonster","lavamonster","lavamonster","babydragon"]),

        (-3,-2):room((-3,-2),"battle",[[1,0],[0,-1]],["babydragon","pyroclast","pyroclast","pyroclast"]),
        (-2,-2):room((-2,-2),"battle",[[-1,0],[0,1]],["pyroclast","pyroclast","lavamonster","babydragon"]),
        (-1,-2):room((-1,-2),"bronzelock",[[1,0],[0,-1]],None),
        (0,-2):room((0,-2),"bronzelock",[[1,0],[-1,0],[0,1],[0,-1]],None),
        (1,-2):room((1,-2),"goldlock",[[-1,0],[0,-1]],None),
        (2,-2):room((2,-2),"battle",[[1,0],[0,1]],["pyroclast","lavamonster","lavamonster","pyroclast"]),
        (3,-2):room((3,-2),"battle",[[-1,0],[0,-1]],["lavamonster","lavamonster","lavamonster","lavamonster"]),

        (-2,-1):room((-2,-1),"battle",[[1,0],[0,-1]],["babydragon","lavamonster","babydragon","pyroclast"]),
        (-1,-1):room((-1,-1),"battle",[[1,0],[-1,0]],["lavamonster","lavamonster","pyroclast","lavamonster"]),
        (0,-1):room((0,-1),"battle",[[1,0],[-1,0],[0,1],[0,-1]],["pyroclast","lavamonster","pyroclast","pyroclast"]),
        (1,-1):room((1,-1),"battle",[[1,0],[-1,0]],["pyroclast","pyroclast","babydragon","lavamonster"]),
        (2,-1):room((2,-1),"battle",[[-1,0],[0,-1]],["lavamonster","lavamonster","pyroclast","pyroclast"]),

        (0,0):room((0,0),"door",[[0,-1]],None)}),

    dungeon("volcano7","volcano",90,1,[66,1469],[260,280],{
        (-5,-5):room((-5,-5),"battle",[[1,0],[0,1]],["lavamonster","lavamonster","lavamonster","pyroclast"]),
        (-4,-5):room((-4,-5),"battle",[[1,0],[-1,0]],["pyroclast","pyroclast","babydragon","pyroclast"]),
        (-3,-5):room((-3,-5),"silverkey",[[-1,0]],None),
        (0,-5):room((0,-5),"boss",[[0,1]],["lavamonster","babydragon","babydragon","firedragon"]),
        (3,-5):room((3,-5),"silverkey",[[1,0]],None),
        (4,-5):room((4,-5),"battle",[[1,0],[-1,0]],["babydragon","lavamonster","babydragon","babydragon"]),
        (5,-5):room((5,-5),"battle",[[-1,0],[0,1]],["lavamonster","babydragon","lavamonster","babydragon"]),

        (-5,-4):room((-5,-4),"battle",[[1,0],[0,1],[0,-1]],["babydragon","babydragon","lavamonster","pyroclast"]),
        (-4,-4):room((-4,-4),"battle",[[1,0],[-1,0]],["pyroclast","lavamonster","lavamonster","pyroclast"]),
        (-3,-4):room((-3,-4),"battle",[[1,0],[-1,0]],["lavamonster","lavamonster","pyroclast","babydragon"]),
        (-2,-4):room((-2,-4),"battle",[[1,0],[-1,0]],["pyroclast","pyroclast","pyroclast","pyroclast"]),
        (-1,-4):room((-1,-4),"battle",[[-1,0],[0,1]],["babydragon","pyroclast","lavamonster","pyroclast"]),
        (0,-4):room((0,-4),"battle",[[1,0],[0,-1]],["babydragon","pyroclast","lavamonster","pyroclast"]),
        (1,-4):room((1,-4),"silverlock",[[1,0],[-1,0]],["lavamonster","lavamonster","lavamonster","babydragon"]),
        (2,-4):room((2,-4),"silverlock",[[1,0],[-1,0]],["babydragon","babydragon","babydragon","lavamonster"]),
        (3,-4):room((3,-4),"silverlock",[[1,0],[-1,0]],["lavamonster","lavamonster","pyroclast","babydragon"]),
        (4,-4):room((4,-4),"silverlock",[[1,0],[-1,0]],["pyroclast","pyroclast","babydragon","lavamonster"]),
        (5,-4):room((5,-4),"battle",[[-1,0],[0,1],[0,-1]],["babydragon","pyroclast","babydragon","lavamonster"]),

        (-5,-3):room((-5,-3),"battle",[[1,0],[0,-1]],["lavamonster","babydragon","pyroclast","lavamonster"]),
        (-4,-3):room((-4,-3),"battle",[[-1,0],[0,1]],["babydragon","lavamonster","lavamonster","lavamonster"]),
        (-3,-3):room((-3,-3),"battle",[[1,0],[0,1]],["lavamonster","lavamonster","lavamonster","babydragon"]),
        (-2,-3):room((-2,-3),"battle",[[-1,0],[0,1]],["pyroclast","lavamonster","lavamonster","lavamonster"]),
        (-1,-3):room((-1,-3),"battle",[[1,0],[0,-1]],["lavamonster","lavamonster","babydragon","pyroclast"]),
        (0,-3):room((0,-3),"battle",[[1,0],[-1,0],[0,1]],["pyroclast","lavamonster","lavamonster","pyroclast"]),
        (1,-3):room((1,-3),"battle",[[1,0],[-1,0]],["pyroclast","lavamonster","pyroclast","babydragon"]),
        (2,-3):room((2,-3),"battle",[[1,0],[-1,0]],["lavamonster","pyroclast","lavamonster","lavamonster"]),
        (3,-3):room((3,-3),"battle",[[1,0],[-1,0]],["babydragon","pyroclast","pyroclast","pyroclast"]),
        (4,-3):room((4,-3),"battle",[[1,0],[-1,0],[0,1]],["lavamonster","pyroclast","lavamonster","lavamonster"]),
        (5,-3):room((5,-3),"battle",[[-1,0],[0,-1]],["babydragon","lavamonster","lavamonster","pyroclast"]),

        (-4,-2):room((-4,-2),"battle",[[1,0],[0,-1]],["pyroclast","babydragon","babydragon","lavamonster"]),
        (-3,-2):room((-3,-2),"battle",[[-1,0],[0,-1]],["lavamonster","pyroclast","lavamonster","babydragon"]),
        (-2,-2):room((-2,-2),"silverkey",[[0,-1]],None),
        (0,-2):room((0,-2),"battle",[[0,1],[0,-1]],["pyroclast","lavamonster","lavamonster","pyroclast"]),
        (2,-2):room((2,-2),"silverkey",[[1,0]],None),
        (3,-2):room((3,-2),"battle",[[1,0],[-1,0]],["pyroclast","pyroclast","babydragon","pyroclast"]),
        (4,-2):room((4,-2),"battle",[[-1,0],[0,-1]],["pyroclast","lavamonster","pyroclast","babydragon"]),

        (0,-1):room((0,-1),"battle",[[0,1],[0,-1]],["babydragon","pyroclast","pyroclast","babydragon"]),

        (0,0):room((0,0),"door",[[0,-1]],None)}),

    dungeon("volcano8","firecastle",91,2,[252,1524],[260,280],{
        (-5,-5):room((-5,-5),"bronzekey",[[0,1]],None),
        (-3,-5):room((-3,-5),"bronzekey",[[0,1]],None),
        (-1,-5):room((-1,-5),"bronzekey",[[0,1]],None),
        (1,-5):room((1,-5),"goldkey",[[0,1]],None),
        (3,-5):room((3,-5),"goldkey",[[0,1]],None),
        (5,-5):room((5,-5),"boss",[[0,1]],["fireguard","fireguard","fireguard","fireknight"]),

        (-5,-4):room((-5,-4),"battle",[[1,0],[0,-1]],["fireguard","fireguard","fireguard","fireguard"]),
        (-4,-4):room((-4,-4),"battle",[[1,0],[-1,0]],["fireguard","fireguard","fireguard","fireguard"]),
        (-3,-4):room((-3,-4),"battle",[[1,0],[-1,0],[0,-1]],["fireguard","fireguard","fireguard","fireguard"]),
        (-2,-4):room((-2,-4),"battle",[[1,0],[-1,0],[0,1]],["fireguard","fireguard","fireguard","fireguard"]),
        (-1,-4):room((-1,-4),"battle",[[-1,0],[0,-1]],["fireguard","fireguard","fireguard","fireguard"]),
        (1,-4):room((1,-4),"battle",[[1,0],[0,-1]],["fireguard","fireguard","fireguard","fireguard"]),
        (2,-4):room((2,-4),"battle",[[1,0],[-1,0],[0,1]],["fireguard","fireguard","fireguard","fireguard"]),
        (3,-4):room((3,-4),"goldlock",[[1,0],[-1,0],[0,-1]],None),
        (4,-4):room((4,-4),"goldlock",[[1,0],[-1,0]],None),
        (5,-4):room((5,-4),"game",[[-1,0],[0,-1]],None),

        (-4,-3):room((-4,-3),"battle",[[1,0],[0,1]],["fireguard","fireguard","fireguard","fireguard"]),
        (-3,-3):room((-3,-3),"battle",[[1,0],[-1,0]],["fireguard","fireguard","fireguard","fireguard"]),
        (-2,-3):room((-2,-3),"battle",[[-1,0],[0,-1]],["fireguard","fireguard","fireguard","fireguard"]),
        (2,-3):room((2,-3),"battle",[[1,0],[0,-1]],["fireguard","fireguard","fireguard","fireguard"]),
        (3,-3):room((3,-3),"battle",[[1,0],[-1,0]],["fireguard","fireguard","fireguard","fireguard"]),
        (4,-3):room((4,-3),"battle",[[-1,0],[0,1]],["fireguard","fireguard","fireguard","fireguard"]),

        (-4,-2):room((-4,-2),"battle",[[1,0],[0,-1]],["fireguard","fireguard","fireguard","fireguard"]),
        (-3,-2):room((-3,-2),"battle",[[1,0],[-1,0]],["fireguard","fireguard","fireguard","fireguard"]),
        (-2,-2):room((-2,-2),"battle",[[-1,0],[0,1]],["fireguard","fireguard","fireguard","fireguard"]),
        (-1,-2):room((-1,-2),"battle",[[1,0],[0,1]],["fireguard","fireguard","fireguard","fireguard"]),
        (0,-2):room((0,-2),"battle",[[1,0],[-1,0],[0,1]],["fireguard","fireguard","fireguard","fireguard"]),
        (1,-2):room((1,-2),"battle",[[-1,0],[0,1]],["fireguard","fireguard","fireguard","fireguard"]),
        (2,-2):room((2,-2),"battle",[[1,0],[0,1]],["fireguard","fireguard","fireguard","fireguard"]),
        (3,-2):room((3,-2),"battle",[[1,0],[-1,0]],["fireguard","fireguard","fireguard","fireguard"]),
        (4,-2):room((4,-2),"battle",[[-1,0],[0,-1]],["fireguard","fireguard","fireguard","fireguard"]),

        (-4,-1):room((-4,-1),"battle",[[1,0],[0,1]],["fireguard","fireguard","fireguard","fireguard"]),
        (-3,-1):room((-3,-1),"battle",[[1,0],[-1,0]],["fireguard","fireguard","fireguard","fireguard"]),
        (-2,-1):room((-2,-1),"battle",[[-1,0],[0,-1]],["fireguard","fireguard","fireguard","fireguard"]),
        (-1,-1):room((-1,-1),"battle",[[0,1],[0,-1]],["fireguard","fireguard","fireguard","fireguard"]),
        (0,-1):room((0,-1),"battle",[[0,1],[0,-1]],["fireguard","fireguard","fireguard","fireguard"]),
        (1,-1):room((1,-1),"battle",[[0,1],[0,-1]],["fireguard","fireguard","fireguard","fireguard"]),
        (2,-1):room((2,-1),"battle",[[1,0],[0,-1]],["fireguard","fireguard","fireguard","fireguard"]),
        (3,-1):room((3,-1),"battle",[[1,0],[-1,0]],["fireguard","fireguard","fireguard","fireguard"]),
        (4,-1):room((4,-1),"battle",[[-1,0],[0,1]],["fireguard","fireguard","fireguard","fireguard"]),

        (-4,0):room((-4,0),"battle",[[1,0],[0,-1]],["fireguard","fireguard","fireguard","fireguard"]),
        (-3,0):room((-3,0),"battle",[[1,0],[-1,0]],["fireguard","fireguard","fireguard","fireguard"]),
        (-2,0):room((-2,0),"battle",[[1,0],[-1,0]],["fireguard","fireguard","fireguard","fireguard"]),
        (-1,0):room((-1,0),"battle",[[-1,0],[0,-1]],["fireguard","fireguard","fireguard","fireguard"]),
        (0,0):room((0,0),"door",[[0,-1]],None),
        (1,0):room((1,0),"battle",[[1,0],[0,-1]],["fireguard","fireguard","fireguard","fireguard"]),
        (2,0):room((2,0),"bronzelock",[[1,0],[-1,0]],None),
        (3,0):room((3,0),"bronzelock",[[1,0],[-1,0]],None),
        (4,0):room((4,0),"bronzelock",[[-1,0],[0,-1]],None)}),

    dungeon("graveyard1","graveyard",92,1,[263,1251],[240,280],{
        (-2,-5):room((-2,-5),"battle",[[1,0],[0,1]],["ghosttree","raven","ghosttree","ghosttree"]),
        (-1,-5):room((-1,-5),"battle",[[1,0],[-1,0]],["ghosttree","ghosttree","ghosttree","raven"]),
        (0,-5):room((0,-5),"battle",[[1,0],[-1,0]],["ghosttree","ghosttree","ghosttree","raven"]),
        (1,-5):room((1,-5),"battle",[[1,0],[-1,0]],["raven","ghosttree","ghosttree","ghosttree"]),
        (2,-5):room((2,-5),"battle",[[1,0],[-1,0]],["raven","ghosttree","ghosttree","ghosttree"]),
        (3,-5):room((3,-5),"boss",[[-1,0]],["ghosttree","ghosttree","raven","spiritmist"]),

        (-2,-4):room((-2,-4),"battle",[[1,0],[0,-1]],["ghosttree","raven","ghosttree","raven"]),
        (-1,-4):room((-1,-4),"battle",[[1,0],[-1,0]],["ghosttree","raven","ghosttree","ghosttree"]),
        (0,-4):room((0,-4),"battle",[[1,0],[-1,0]],["ghosttree","ghosttree","ghosttree","ghosttree"]),
        (1,-4):room((1,-4),"battle",[[1,0],[-1,0]],["ghosttree","ghosttree","ghosttree","ghosttree"]),
        (2,-4):room((2,-4),"battle",[[-1,0],[0,1]],["ghosttree","ghosttree","ghosttree","raven"]),

        (-1,-3):room((-1,-3),"battle",[[1,0],[0,1]],["raven","ghosttree","ghosttree","ghosttree"]),
        (0,-3):room((0,-3),"battle",[[1,0],[-1,0]],["ghosttree","raven","ghosttree","raven"]),
        (1,-3):room((1,-3),"battle",[[1,0],[-1,0]],["ghosttree","ghosttree","ghosttree","ghosttree"]),
        (2,-3):room((2,-3),"battle",[[-1,0],[0,-1]],["ghosttree","ghosttree","ghosttree","ghosttree"]),

        (-1,-2):room((-1,-2),"battle",[[1,0],[0,-1]],["raven","ghosttree","ghosttree","ghosttree"]),
        (0,-2):room((0,-2),"battle",[[1,0],[-1,0]],["ghosttree","ghosttree","raven","ghosttree"]),
        (1,-2):room((1,-2),"battle",[[-1,0],[0,1]],["ghosttree","ghosttree","ghosttree","ghosttree"]),

        (0,-1):room((0,-1),"battle",[[1,0],[0,1]],["ghosttree","ghosttree","raven","ghosttree"]),
        (1,-1):room((1,-1),"battle",[[-1,0],[0,-1]],["ghosttree","ghosttree","ghosttree","raven"]),

        (0,0):room((0,0),"door",[[0,-1]],None)}),

    dungeon("graveyard2","graveyard",93,1,[144,1191],[260,280],{
        (-1,-5):room((-1,-5),"boss",[[1,0]],["raven","ghosttree","ghosttree","bigghost"]),
        (0,-5):room((0,-5),"silverlock",[[1,0],[-1,0]],None),
        (1,-5):room((1,-5),"bronzelock",[[-1,0],[0,1]],None),

        (-2,-4):room((-2,-4),"bronzekey",[[1,0]],None),
        (-1,-4):room((-1,-4),"battle",[[1,0],[-1,0]],["ghosttree","raven","ghosttree","ghosttree"]),
        (0,-4):room((0,-4),"battle",[[1,0],[-1,0]],["raven","raven","ghosttree","ghosttree"]),
        (1,-4):room((1,-4),"battle",[[1,0],[-1,0],[0,-1]],["raven","raven","ghosttree","raven"]),
        (2,-4):room((2,-4),"bronzelock",[[-1,0],[0,1]],None),

        (-2,-3):room((-2,-3),"bronzekey",[[1,0]],None),
        (-1,-3):room((-1,-3),"battle",[[1,0],[-1,0]],["raven","ghosttree","ghosttree","ghosttree"]),
        (0,-3):room((0,-3),"battle",[[1,0],[-1,0]],["ghosttree","raven","raven","ghosttree"]),
        (1,-3):room((1,-3),"battle",[[1,0],[-1,0]],["ghosttree","raven","raven","ghosttree"]),
        (2,-3):room((2,-3),"bronzelock",[[-1,0],[0,1],[0,-1]],None),

        (-2,-2):room((-2,-2),"bronzekey",[[1,0]],None),
        (-1,-2):room((-1,-2),"battle",[[1,0],[-1,0]],["ghosttree","ghosttree","raven","ghosttree"]),
        (0,-2):room((0,-2),"battle",[[1,0],[-1,0]],["ghosttree","ghosttree","raven","ghosttree"]),
        (1,-2):room((1,-2),"battle",[[1,0],[-1,0]],["ghosttree","ghosttree","ghosttree","raven"]),
        (2,-2):room((2,-2),"bronzelock",[[-1,0],[0,1],[0,-1]],None),

        (-2,-1):room((-2,-1),"battle",[[1,0],[0,1]],["ghosttree","ghosttree","ghosttree","raven"]),
        (-1,-1):room((-1,-1),"battle",[[1,0],[-1,0]],["ghosttree","ghosttree","ghosttree","ghosttree"]),
        (0,-1):room((0,-1),"battle",[[1,0],[-1,0],[0,1]],["raven","raven","ghosttree","ghosttree"]),
        (1,-1):room((1,-1),"battle",[[1,0],[-1,0]],["raven","ghosttree","raven","ghosttree"]),
        (2,-1):room((2,-1),"battle",[[-1,0],[0,1],[0,-1]],["ghosttree","ghosttree","raven","ghosttree"]),

        (-2,0):room((-2,0),"silverkey",[[0,-1]],None),
        (0,0):room((0,0),"door",[[0,-1]],None),
        (2,0):room((2,0),"bronzekey",[[0,-1]],None)}),

    dungeon("graveyard3","graveyard",94,1,[39,1118],[100,280],{
        (0,-5):room((0,-5),"battle",[[1,0],[0,1]],["ghost","ghost","ghost","ghosttree"]),
        (1,-5):room((1,-5),"battle",[[1,0],[-1,0]],["ghost","ghost","ghosttree","ghost"]),
        (2,-5):room((2,-5),"battle",[[-1,0],[0,1]],["raven","ghosttree","raven","ghosttree"]),
        (4,-5):room((4,-5),"silverkey",[[0,1]],None),
        (6,-5):room((6,-5),"battle",[[1,0],[0,1]],["ghost","ghost","raven","raven"]),
        (7,-5):room((7,-5),"battle",[[1,0],[-1,0]],["ghosttree","raven","ghost","ghosttree"]),
        (8,-5):room((8,-5),"battle",[[-1,0],[0,1]],["ghost","ghost","ghosttree","raven"]),

        (0,-4):room((0,-4),"battle",[[0,1],[0,-1]],["ghost","ghost","ghost","ghost"]),
        (2,-4):room((2,-4),"battle",[[0,1],[0,-1]],["ghost","ghost","ghost","ghost"]),
        (4,-4):room((4,-4),"battle",[[0,1],[0,-1]],["ghost","ghost","ghost","raven"]),
        (6,-4):room((6,-4),"battle",[[0,1],[0,-1]],["raven","raven","raven","ghost"]),
        (8,-4):room((8,-4),"battle",[[0,1],[0,-1]],["ghost","ghost","ghost","ghost"]),

        (0,-3):room((0,-3),"battle",[[0,1],[0,-1]],["ghosttree","ghosttree","ghost","ghost"]),
        (1,-3):room((1,-3),"bronzekey",[[1,0]],None),
        (2,-3):room((2,-3),"battle",[[-1,0],[0,-1]],["ghosttree","raven","ghost","raven"]),
        (4,-3):room((4,-3),"battle",[[0,1],[0,-1]],["raven","raven","ghosttree","raven"]),
        (6,-3):room((6,-3),"battle",[[0,1],[0,-1]],["ghost","ghost","ghost","raven"]),
        (7,-3):room((7,-3),"boss",[[1,0]],["ghost","ghost","raven","shadowghost"]),
        (8,-3):room((8,-3),"battle",[[-1,0],[0,-1]],["ghosttree","ghosttree","ghost","ghost"]),

        (0,-2):room((0,-2),"battle",[[1,0],[0,1],[0,-1]],["ghosttree","ghosttree","ghost","ghost"]),
        (1,-2):room((1,-2),"bronzelock",[[1,0],[-1,0]],None),
        (2,-2):room((2,-2),"battle",[[-1,0],[0,1]],["ghost","ghost","ghosttree","ghost"]),
        (4,-2):room((4,-2),"battle",[[0,1],[0,-1]],["ghost","ghosttree","ghost","raven"]),
        (6,-2):room((6,-2),"battle",[[0,1],[0,-1]],["ghosttree","ghost","ghost","raven"]),

        (0,-1):room((0,-1),"battle",[[0,1],[0,-1]],["raven","raven","ghosttree","ghosttree"]),
        (2,-1):room((2,-1),"battle",[[0,1],[0,-1]],["ghost","ghost","ghost","raven"]),
        (4,-1):room((4,-1),"battle",[[0,1],[0,-1]],["ghost","raven","raven","ghost"]),
        (6,-1):room((6,-1),"battle",[[0,1],[0,-1]],["raven","ghost","ghost","ghost"]),

        (0,0):room((0,0),"door",[[0,-1]],None),
        (2,0):room((2,0),"battle",[[1,0],[0,-1]],["ghost","ghosttree","ghosttree","ghost"]),
        (3,0):room((3,0),"battle",[[1,0],[-1,0]],["ghost","ghosttree","ghosttree","ghosttree"]),
        (4,0):room((4,0),"battle",[[1,0],[-1,0],[0,-1]],["raven","ghost","ghosttree","ghosttree"]),
        (5,0):room((5,0),"silverlock",[[1,0],[-1,0]],["ghost","raven","ghost","ghosttree"]),
        (6,0):room((6,0),"battle",[[-1,0],[0,-1]],["ghost","ghosttree","ghosttree","ghost"])}),

    dungeon("graveyard4","graveyard",95,1,[166,1052],[280,280],{
        (-3,-5):room((-3,-5),"battle",[[1,0],[0,1]],["ghost","ghost","ghost","ghost"]),
        (-2,-5):room((-2,-5),"battle",[[1,0],[-1,0]],["specter","specter","ghost","ghost"]),
        (-1,-5):room((-1,-5),"battle",[[-1,0],[0,1]],["specter","specter","ghost","specter"]),
        (0,-5):room((0,-5),"battle",[[1,0],[0,1]],["specter","specter","ghost","ghost"]),
        (1,-5):room((1,-5),"battle",[[-1,0],[0,1]],["specter","ghost","specter","specter"]),
        (2,-5):room((2,-5),"boss",[[0,1]],["ghost","specter","specter","shadowspecter"]),

        (-3,-4):room((-3,-4),"battle",[[1,0],[0,-1]],["ghost","specter","ghost","specter"]),
        (-2,-4):room((-2,-4),"battle",[[-1,0],[0,1]],["ghost","ghost","ghost","ghost"]),
        (-1,-4):room((-1,-4),"battle",[[1,0],[0,-1]],["ghost","ghost","ghost","ghost"]),
        (0,-4):room((0,-4),"battle",[[-1,0],[0,-1]],["ghost","specter","ghost","ghost"]),
        (1,-4):room((1,-4),"battle",[[0,1],[0,-1]],["ghost","ghost","specter","ghost"]),
        (2,-4):room((2,-4),"heal",[[0,1],[0,-1]],None),

        (-3,-3):room((-3,-3),"battle",[[1,0],[0,1]],["ghost","specter","ghost","specter"]),
        (-2,-3):room((-2,-3),"battle",[[-1,0],[0,-1]],["ghost","specter","specter","ghost"]),
        (-1,-3):room((-1,-3),"battle",[[1,0],[0,1]],["ghost","ghost","ghost","specter"]),
        (0,-3):room((0,-3),"battle",[[-1,0],[0,1]],["specter","ghost","specter","specter"]),
        (1,-3):room((1,-3),"battle",[[0,1],[0,-1]],["specter","ghost","ghost","ghost"]),
        (2,-3):room((2,-3),"battle",[[0,1],[0,-1]],["ghost","ghost","ghost","specter"]),

        (-3,-2):room((-3,-2),"battle",[[0,1],[0,-1]],["ghost","specter","ghost","specter"]),
        (-2,-2):room((-2,-2),"battle",[[1,0],[0,1]],["ghost","ghost","ghost","ghost"]),
        (-1,-2):room((-1,-2),"battle",[[-1,0],[0,-1]],["specter","ghost","specter","ghost"]),
        (0,-2):room((0,-2),"battle",[[0,1],[0,-1]],["ghost","specter","ghost","specter"]),
        (1,-2):room((1,-2),"battle",[[0,1],[0,-1]],["ghost","ghost","specter","ghost"]),
        (2,-2):room((2,-2),"battle",[[0,1],[0,-1]],["ghost","ghost","specter","ghost"]),

        (-3,-1):room((-3,-1),"battle",[[0,1],[0,-1]],["ghost","ghost","ghost","ghost"]),
        (-2,-1):room((-2,-1),"battle",[[0,1],[0,-1]],["specter","ghost","specter","specter"]),
        (-1,-1):room((-1,-1),"battle",[[1,0],[0,1]],["ghost","ghost","specter","ghost"]),
        (0,-1):room((0,-1),"battle",[[-1,0],[0,-1]],["ghost","ghost","ghost","ghost"]),
        (1,-1):room((1,-1),"battle",[[0,1],[0,-1]],["ghost","specter","specter","specter"]),
        (2,-1):room((2,-1),"battle",[[0,1],[0,-1]],["ghost","specter","ghost","ghost"]),

        (-3,0):room((-3,0),"battle",[[1,0],[0,-1]],["ghost","ghost","ghost","specter"]),
        (-2,0):room((-2,0),"battle",[[-1,0],[0,-1]],["ghost","ghost","specter","ghost"]),
        (-1,0):room((-1,0),"battle",[[1,0],[0,-1]],["ghost","ghost","ghost","ghost"]),
        (0,0):room((0,0),"door",[[-1,0]],None),
        (1,0):room((1,0),"battle",[[1,0],[0,-1]],["ghost","ghost","ghost","specter"]),
        (2,0):room((2,0),"battle",[[-1,0],[0,-1]],["ghost","ghost","ghost","ghost"])}),

    dungeon("graveyard5","graveyard",96,1,[333,1025],[300,300],{
        (-2,-6):room((-2,-6),"battle",[[1,0],[0,1]],["angryghost","angryghost","ghost","angryghost"]),
        (-1,-6):room((-1,-6),"battle",[[1,0],[-1,0],[0,1]],["ghost","ghost","ghost","ghost"]),
        (0,-6):room((0,-6),"battle",[[-1,0],[0,1]],["ghost","ghost","angryghost","ghost"]),

        (-3,-5):room((-3,-5),"battle",[[1,0],[0,1]],["angryghost","ghost","ghost","ghost"]),
        (-2,-5):room((-2,-5),"battle",[[-1,0],[0,-1]],["ghost","angryghost","ghost","angryghost"]),
        (-1,-5):room((-1,-5),"battle",[[0,1],[0,-1]],["ghost","angryghost","ghost","ghost"]),
        (0,-5):room((0,-5),"battle",[[1,0],[0,-1]],["ghost","ghost","ghost","ghost"]),
        (1,-5):room((1,-5),"battle",[[-1,0],[0,1]],["angryghost","ghost","angryghost","ghost"]),

        (-3,-4):room((-3,-4),"battle",[[0,1],[0,-1]],["ghost","ghost","ghost","ghost"]),
        (-1,-4):room((-1,-4),"magickey",[[0,-1]],None),
        (1,-4):room((1,-4),"magickey",[[0,-1]],None),

        (-3,-3):room((-3,-3),"battle",[[0,1],[0,-1]],["ghost","angryghost","ghost","ghost"]),
        (-2,-3):room((-2,-3),"battle",[[1,0],[0,1]],["ghost","ghost","ghost","angryghost"]),
        (-1,-3):room((-1,-3),"battle",[[1,0],[-1,0]],["ghost","angryghost","angryghost","ghost"]),
        (0,-3):room((0,-3),"battle",[[1,0],[-1,0]],["ghost","ghost","ghost","angryghost"]),
        (1,-3):room((1,-3),"battle",[[-1,0],[0,1]],["ghost","angryghost","ghost","angryghost"]),

        (-3,-2):room((-3,-2),"battle",[[1,0],[0,-1]],["ghost","ghost","ghost","ghost"]),
        (-2,-2):room((-2,-2),"battle",[[-1,0],[0,-1]],["ghost","ghost","ghost","ghost"]),
        (0,-2):room((0,-2),"battle",[[1,0],[0,1]],["angryghost","ghost","ghost","ghost"]),
        (1,-2):room((1,-2),"battle",[[-1,0],[0,-1]],["ghost","ghost","ghost","ghost"]),

        (-2,-1):room((-2,-1),"magiclock",[[1,0],[0,1]],None),
        (-1,-1):room((-1,-1),"magiclock",[[1,0],[-1,0]],None),
        (0,-1):room((0,-1),"battle",[[-1,0],[0,1],[0,-1]],["ghost","ghost","ghost","ghost"]),

        (-2,0):room((-2,0),"boss",[[0,-1]],["ghost","ghost","phantom"]),
        (0,0):room((0,0),"door",[[0,-1]],None)}),

    dungeon("graveyard6","graveyard",97,1,[478,965],[320,300],{
        (-3,-6):room((-3,-6),"battle",[[1,0],[0,1]],["ghost","angryghost","ghost","angryghost"]),
        (-2,-6):room((-2,-6),"battle",[[-1,0],[0,1]],["angryghost","ghost","angryghost","angryghost"]),
        (-1,-6):room((-1,-6),"battle",[[1,0],[0,1]],["ghost","ghost","angryghost","angryghost"]),
        (0,-6):room((0,-6),"battle",[[-1,0],[0,1]],["ghost","angryghost","ghost","ghost"]),

        (-4,-5):room((-4,-5),"battle",[[1,0],[0,1]],["ghost","ghost","angryghost","ghost"]),
        (-3,-5):room((-3,-5),"battle",[[-1,0],[0,-1]],["ghost","angryghost","ghost","ghost"]),
        (-2,-5):room((-2,-5),"battle",[[1,0],[0,-1]],["ghost","ghost","angryghost","ghost"]),
        (-1,-5):room((-1,-5),"battle",[[-1,0],[0,-1]],["ghost","ghost","angryghost","ghost"]),
        (0,-5):room((0,-5),"battle",[[1,0],[0,-1]],["ghost","ghost","ghost","ghost"]),
        (1,-5):room((1,-5),"battle",[[-1,0],[0,1]],["ghost","ghost","ghost","ghost"]),

        (-4,-4):room((-4,-4),"battle",[[0,1],[0,-1]],["ghost","ghost","angryghost","angryghost"]),
        (-2,-4):room((-2,-4),"battle",[[1,0],[0,1]],["ghost","ghost","angryghost","ghost"]),
        (-1,-4):room((-1,-4),"battle",[[-1,0],[0,1]],["angryghost","ghost","ghost","ghost"]),
        (1,-4):room((1,-4),"battle",[[0,1],[0,-1]],["ghost","angryghost","angryghost","angryghost"]),

        (-4,-3):room((-4,-3),"battle",[[0,1],[0,-1]],["ghost","ghost","angryghost","angryghost"]),
        (-3,-3):room((-3,-3),"battle",[[1,0],[0,1]],["ghost","ghost","angryghost","ghost"]),
        (-2,-3):room((-2,-3),"battle",[[-1,0],[0,-1]],["ghost","ghost","angryghost","ghost"]),
        (-1,-3):room((-1,-3),"battle",[[1,0],[0,-1]],["ghost","angryghost","angryghost","angryghost"]),
        (0,-3):room((0,-3),"magickey",[[-1,0]],None),
        (1,-3):room((1,-3),"battle",[[0,1],[0,-1]],["ghost","ghost","angryghost","ghost"]),

        (-4,-2):room((-4,-2),"battle",[[1,0],[0,-1]],["ghost","ghost","ghost","ghost"]),
        (-3,-2):room((-3,-2),"battle",[[-1,0],[0,-1]],["ghost","ghost","ghost","ghost"]),
        (0,-2):room((0,-2),"battle",[[1,0],[0,1]],["angryghost","angryghost","ghost","ghost"]),
        (1,-2):room((1,-2),"battle",[[-1,0],[0,-1]],["ghost","ghost","ghost","angryghost"]),

        (-3,-1):room((-3,-1),"game",[[1,0],[0,1]],["ghost","ghost","angryghost","ghost"]),
        (-2,-1):room((-2,-1),"battle",[[1,0],[-1,0]],["ghost","ghost","ghost","ghost"]),
        (-1,-1):room((-1,-1),"magiclock",[[1,0],[-1,0]],["ghost","ghost","ghost","angryghost"]),
        (0,-1):room((0,-1),"battle",[[-1,0],[0,1],[0,-1]],["ghost","ghost","angryghost","ghost"]),

        (-3,0):room((-3,0),"boss",[[0,-1]],["ghost","ghost","angryphantom"]),
        (0,0):room((0,0),"door",[[0,-1]],None)}),

    dungeon("graveyard7","graveyard",98,1,[368,896],[300,300],{
        (-3,-6):room((-3,-6),"silverkey",[[1,0]],None),
        (-2,-6):room((-2,-6),"battle",[[1,0],[-1,0],[0,1]],["angryghost","ghost","ghost","ghost"]),
        (-1,-6):room((-1,-6),"silverlock",[[1,0],[-1,0]],["ghost","angryghost","ghost","ghost"]),
        (0,-6):room((0,-6),"game",[[1,0],[-1,0]],None),
        (1,-6):room((1,-6),"boss",[[-1,0]],["ghost","angryghost","frightfulphantom"]),

        (-4,-5):room((-4,-5),"magickey",[[0,1]],None),
        (-2,-5):room((-2,-5),"silverlock",[[1,0],[0,-1]],None),
        (-1,-5):room((-1,-5),"battle",[[1,0],[-1,0],[0,1]],["ghost","ghost","ghost","angryghost"]),
        (0,-5):room((0,-5),"silverkey",[[-1,0]],None),
        (2,-5):room((2,-5),"magickey",[[0,1]],None),

        (-4,-4):room((-4,-4),"battle",[[0,1],[0,-1]],["angryghost","ghost","ghost","ghost"]),
        (-1,-4):room((-1,-4),"magiclock",[[0,1],[0,-1]],None),
        (2,-4):room((2,-4),"battle",[[0,1],[0,-1]],["angryghost","angryghost","ghost","ghost"]),

        (-4,-3):room((-4,-3),"battle",[[0,1],[0,-1]],["angryghost","angryghost","angryghost","ghost"]),
        (-3,-3):room((-3,-3),"battle",[[1,0],[0,1]],["ghost","ghost","ghost","angryghost"]),
        (-2,-3):room((-2,-3),"battle",[[-1,0],[0,1]],["angryghost","angryghost","ghost","ghost"]),
        (-1,-3):room((-1,-3),"magiclock",[[1,0],[0,-1]],None),
        (0,-3):room((0,-3),"magiclock",[[1,0],[-1,0],[0,1]],None),
        (1,-3):room((1,-3),"battle",[[-1,0],[0,1]],["angryghost","ghost","ghost","ghost"]),
        (2,-3):room((2,-3),"battle",[[0,1],[0,-1]],["ghost","ghost","ghost","angryghost"]),

        (-4,-2):room((-4,-2),"battle",[[1,0],[0,-1]],["angryghost","ghost","ghost","ghost"]),
        (-3,-2):room((-3,-2),"battle",[[-1,0],[0,-1]],["angryghost","ghost","ghost","ghost"]),
        (-2,-2):room((-2,-2),"battle",[[0,1],[0,-1]],["ghost","ghost","angryghost","ghost"]),
        (0,-2):room((0,-2),"battle",[[0,1],[0,-1]],["ghost","ghost","ghost","angryghost"]),
        (1,-2):room((1,-2),"battle",[[1,0],[0,-1]],["angryghost","ghost","ghost","ghost"]),
        (2,-2):room((2,-2),"battle",[[-1,0],[0,-1]],["ghost","ghost","angryghost","ghost"]),

        (-2,-1):room((-2,-1),"battle",[[1,0],[0,1],[0,-1]],["ghost","angryghost","ghost","angryghost"]),
        (-1,-1):room((-1,-1),"battle",[[1,0],[-1,0]],["ghost","ghost","ghost","ghost"]),
        (0,-1):room((0,-1),"battle",[[-1,0],[0,1],[0,-1]],["ghost","ghost","ghost","angryghost"]),

        (-2,0):room((-2,0),"magickey",[[0,-1]],None),
        (0,0):room((0,0),"door",[[0,-1]],None)}),

    dungeon("graveyard8","graveyard",99,2,[236,851],[300,340],{
        (-3,-8):room((-3,-8),"battle",[[1,0],[0,1]],["ghost","ghost","angryghost","ghost"]),
        (-2,-8):room((-2,-8),"battle",[[1,0],[-1,0]],["angryghost","ghost","ghost","ghost"]),
        (-1,-8):room((-1,-8),"battle",[[1,0],[-1,0]],["ghost","ghost","ghost","ghost"]),
        (0,-8):room((0,-8),"battle",[[1,0],[-1,0]],["ghost","angryghost","ghost","ghost"]),
        (1,-8):room((1,-8),"battle",[[-1,0],[0,1]],["angryghost","angryghost","ghost","ghost"]),

        (-4,-7):room((-4,-7),"battle",[[1,0],[0,1]],["ghost","ghost","angryghost","angryghost"]),
        (-3,-7):room((-3,-7),"battle",[[-1,0],[0,-1]],["ghost","ghost","ghost","ghost"]),
        (-2,-7):room((-2,-7),"battle",[[1,0],[0,1]],["ghost","ghost","angryghost","ghost"]),
        (-1,-7):room((-1,-7),"battle",[[1,0],[-1,0]],["ghost","ghost","angryghost","ghost"]),
        (0,-7):room((0,-7),"battle",[[-1,0],[0,1]],["ghost","angryghost","angryghost","ghost"]),
        (1,-7):room((1,-7),"battle",[[1,0],[0,-1]],["ghost","ghost","angryghost","ghost"]),
        (2,-7):room((2,-7),"battle",[[-1,0],[0,1]],["ghost","angryghost","ghost","angryghost"]),

        (-4,-6):room((-4,-6),"battle",[[0,1],[0,-1]],["ghost","ghost","ghost","ghost"]),
        (-2,-6):room((-2,-6),"battle",[[1,0],[0,-1]],["ghost","angryghost","ghost","ghost"]),
        (-1,-6):room((-1,-6),"battle",[[-1,0],[0,1]],["ghost","ghost","ghost","angryghost"]),
        (0,-6):room((0,-6),"magickey",[[0,-1]],["ghost","angryghost","ghost","ghost"]),
        (2,-6):room((2,-6),"battle",[[0,1],[0,-1]],["ghost","angryghost","ghost","angryghost"]),

        (-4,-5):room((-4,-5),"battle",[[0,1],[0,-1]],["ghost","ghost","angryghost","ghost"]),
        (-1,-5):room((-1,-5),"battle",[[0,1],[0,-1]],["angryghost","angryghost","ghost","ghost"]),
        (2,-5):room((2,-5),"battle",[[0,1],[0,-1]],["ghost","ghost","angryghost","angryghost"]),

        (-4,-4):room((-4,-4),"battle",[[1,0],[0,-1]],["ghost","angryghost","ghost","ghost"]),
        (-3,-4):room((-3,-4),"battle",[[-1,0],[0,1]],["angryghost","ghost","ghost","ghost"]),
        (-2,-4):room((-2,-4),"battle",[[1,0],[0,1]],["ghost","ghost","angryghost","ghost"]),
        (-1,-4):room((-1,-4),"battle",[[-1,0],[0,-1]],["ghost","ghost","angryghost","angryghost"]),
        (0,-4):room((0,-4),"battle",[[1,0],[0,1]],["ghost","ghost","ghost","ghost"]),
        (1,-4):room((1,-4),"battle",[[1,0],[-1,0]],["angryghost","ghost","angryghost","ghost"]),
        (2,-4):room((2,-4),"battle",[[-1,0],[0,-1]],["ghost","ghost","angryghost","ghost"]),

        (-3,-3):room((-3,-3),"battle",[[0,1],[0,-1]],["angryghost","ghost","ghost","ghost"]),
        (-2,-3):room((-2,-3),"battle",[[0,1],[0,-1]],["angryghost","ghost","ghost","ghost"]),
        (0,-3):room((0,-3),"battle",[[1,0],[0,-1]],["angryghost","ghost","angryghost","ghost"]),
        (1,-3):room((1,-3),"battle",[[-1,0],[0,1]],["angryghost","angryghost","ghost","ghost"]),

        (-3,-2):room((-3,-2),"battle",[[1,0],[0,-1]],["ghost","ghost","ghost","ghost"]),
        (-2,-2):room((-2,-2),"battle",[[-1,0],[0,-1]],["angryghost","ghost","ghost","angryghost"]),
        (0,-2):room((0,-2),"battle",[[1,0],[0,1]],["ghost","ghost","ghost","ghost"]),
        (1,-2):room((1,-2),"battle",[[-1,0],[0,-1]],["ghost","ghost","ghost","ghost"]),

        (-2,-1):room((-2,-1),"game",[[1,0],[0,1]],None),
        (-1,-1):room((-1,-1),"magiclock",[[1,0],[-1,0]],None),
        (0,-1):room((0,-1),"battle",[[-1,0],[0,1],[0,-1]],["ghost","angryghost","ghost","ghost"]),

        (-2,0):room((-2,0),"boss",[[0,-1]],["ghost","angryghost","shadowphantom"]),
        (0,0):room((0,0),"door",[[0,-1]],None)}),

    dungeon("darkcastle1","darkcastle",100,1,[261,655],[260,300],{
        (-3,-6):room((-3,-6),"goldkey",[[0,1]],None),
        (-1,-6):room((-1,-6),"goldkey",[[0,1]],None),
        (1,-6):room((0,-6),"magickey",[[0,1]],None),
        (3,-6):room((3,-6),"magickey",[[0,1]],None),

        (-3,-5):room((-3,-5),"battle",[[1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (-2,-5):room((-2,-5),"battle",[[1,0],[-1,0]],["darkguard","darkguard","darkguard","darkguard"]),
        (-1,-5):room((-1,-5),"battle",[[-1,0],[0,1],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (0,-5):room((0,-5),"boss",[[0,1]],["darkguard","darkguard","darkguard","darkknight"]),
        (1,-5):room((1,-5),"battle",[[1,0],[0,1],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (2,-5):room((2,-5),"battle",[[1,0],[-1,0]],["darkguard","darkguard","darkguard","darkguard"]),
        (3,-5):room((3,-5),"battle",[[-1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        
        (-2,-4):room((-2,-4),"battle",[[1,0],[0,1]],["darkguard","darkguard","darkguard","darkguard"]),
        (-1,-4):room((-1,-4),"battle",[[-1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (0,-4):room((0,-4),"game",[[0,1],[0,-1]],None),
        (1,-4):room((1,-4),"battle",[[1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (2,-4):room((2,-4),"battle",[[-1,0],[0,1]],["darkguard","darkguard","darkguard","darkguard"]),

        (-2,-3):room((-2,-3),"battle",[[1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (-1,-3):room((-1,-3),"battle",[[-1,0],[0,1]],["darkguard","darkguard","darkguard","darkguard"]),
        (0,-3):room((0,-3),"magiclock",[[0,1],[0,-1]],None),
        (1,-3):room((1,-3),"battle",[[1,0],[0,1]],["darkguard","darkguard","darkguard","darkguard"]),
        (2,-3):room((2,-3),"battle",[[-1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),

        (-2,-2):room((-2,-2),"battle",[[1,0],[0,1]],["darkguard","darkguard","darkguard","darkguard"]),
        (-1,-2):room((-1,-2),"battle",[[-1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (0,-2):room((0,-2),"magiclock",[[0,1],[0,-1]],None),
        (1,-2):room((1,-2),"battle",[[1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (2,-2):room((2,-2),"battle",[[-1,0],[0,1]],["darkguard","darkguard","darkguard","darkguard"]),

        (-3,-1):room((-3,-1),"battle",[[1,0],[0,1]],["darkguard","darkguard","darkguard","darkguard"]),
        (-2,-1):room((-2,-1),"battle",[[-1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (-1,-1):room((-1,-1),"battle",[[1,0],[0,1]],["darkguard","darkguard","darkguard","darkguard"]),
        (0,-1):room((0,-1),"battle",[[1,0],[-1,0],[0,1],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (1,-1):room((1,-1),"goldlock",[[-1,0],[0,1]],None),
        (2,-1):room((2,-1),"battle",[[1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (3,-1):room((3,-1),"battle",[[-1,0],[0,1]],["darkguard","darkguard","darkguard","darkguard"]),

        (-3,0):room((-3,0),"battle",[[1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (-2,0):room((-2,0),"battle",[[1,0],[-1,0]],["darkguard","darkguard","darkguard","darkguard"]),
        (-1,0):room((-1,0),"battle",[[-1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (0,0):room((0,0),"door",[[0,-1]],None),
        (1,0):room((1,0),"goldlock",[[1,0],[0,-1]],None),
        (2,0):room((2,0),"battle",[[1,0],[-1,0]],["darkguard","darkguard","darkguard","darkguard"]),
        (3,0):room((3,0),"battle",[[-1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"])}),

    dungeon("darkcastle2","darkcastle",101,1,[103,534],[260,300],{
        (-5,-6):room((-5,-6),"goldkey",[[0,1]],None),
        (-3,-6):room((-3,-6),"goldkey",[[0,1]],None),
        (-1,-6):room((-1,-6),"goldkey",[[0,1]],None),
        (1,-6):room((1,-6),"goldkey",[[0,1]],None),
        (3,-6):room((3,-6),"goldkey",[[0,1]],None),
        (5,-6):room((5,-6),"goldkey",[[0,1]],None),

        (-5,-5):room((-5,-5),"battle",[[1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (-4,-5):room((-4,-5),"battle",[[1,0],[-1,0],[0,1]],["darkguard","darkguard","darkguard","darkguard"]),
        (-3,-5):room((-3,-5),"battle",[[1,0],[-1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (-2,-5):room((-2,-5),"battle",[[1,0],[-1,0]],["darkguard","darkguard","darkguard","darkguard"]),
        (-1,-5):room((-1,-5),"battle",[[-1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (1,-5):room((1,-5),"battle",[[1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (2,-5):room((2,-5),"battle",[[1,0],[-1,0],[0,1]],["darkguard","darkguard","darkguard","darkguard"]),
        (3,-5):room((3,-5),"battle",[[1,0],[-1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (4,-5):room((4,-5),"battle",[[1,0],[-1,0],[0,1]],["darkguard","darkguard","darkguard","darkguard"]),
        (5,-5):room((5,-5),"battle",[[-1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),

        (-4,-4):room((-4,-4),"battle",[[1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (-3,-4):room((-3,-4),"battle",[[1,0],[-1,0]],["darkguard","darkguard","darkguard","darkguard"]),
        (-2,-4):room((-2,-4),"battle",[[-1,0],[0,1]],["darkguard","darkguard","darkguard","darkguard"]),
        (2,-4):room((2,-4),"battle",[[1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (3,-4):room((3,-4),"battle",[[-1,0],[0,1]],["darkguard","darkguard","darkguard","darkguard"]),
        (4,-4):room((4,-4),"goldlock",[[0,1],[0,-1]],None),

        (-4,-3):room((-4,-3),"battle",[[1,0],[0,1]],["darkguard","darkguard","darkguard","darkguard"]),
        (-3,-3):room((-3,-3),"battle",[[1,0],[-1,0]],["darkguard","darkguard","darkguard","darkguard"]),
        (-2,-3):room((-2,-3),"battle",[[-1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (2,-3):room((2,-3),"battle",[[1,0],[0,1]],["darkguard","darkguard","darkguard","darkguard"]),
        (3,-3):room((3,-3),"battle",[[-1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (4,-3):room((4,-3),"goldlock",[[0,1],[0,-1]],None),

        (-4,-2):room((-4,-2),"battle",[[1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (-3,-2):room((-3,-2),"battle",[[1,0],[-1,0]],["darkguard","darkguard","darkguard","darkguard"]),
        (-2,-2):room((-2,-2),"battle",[[-1,0],[0,1]],["darkguard","darkguard","darkguard","darkguard"]),
        (-1,-2):room((-1,-2),"battle",[[1,0],[0,1]],["darkguard","darkguard","darkguard","darkguard"]),
        (0,-2):room((0,-2),"battle",[[1,0],[-1,0],[0,1]],["darkguard","darkguard","darkguard","darkguard"]),
        (1,-2):room((1,-2),"battle",[[-1,0],[0,1]],["darkguard","darkguard","darkguard","darkguard"]),
        (2,-2):room((2,-2),"battle",[[0,1],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (3,-2):room((3,-2),"goldlock",[[1,0],[0,1]],None),
        (4,-2):room((4,-2),"goldlock",[[-1,0],[0,-1]],None),

        (-4,-1):room((-4,-1),"battle",[[1,0],[0,1]],["darkguard","darkguard","darkguard","darkguard"]),
        (-3,-1):room((-3,-1),"battle",[[1,0],[-1,0]],["darkguard","darkguard","darkguard","darkguard"]),
        (-2,-1):room((-2,-1),"battle",[[-1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (-1,-1):room((-1,-1),"battle",[[0,1],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (0,-1):room((0,-1),"battle",[[0,1],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (1,-1):room((1,-1),"battle",[[0,1],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (2,-1):room((2,-1),"battle",[[0,1],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (3,-1):room((3,-1),"goldlock",[[1,0],[0,-1]],None),
        (4,-1):room((4,-1),"goldlock",[[-1,0],[0,1]],None),

        (-4,0):room((-4,0),"battle",[[1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (-3,0):room((-3,0),"battle",[[1,0],[-1,0]],["darkguard","darkguard","darkguard","darkguard"]),
        (-2,0):room((-2,0),"battle",[[1,0],[-1,0]],["darkguard","darkguard","darkguard","darkguard"]),
        (-1,0):room((-1,0),"battle",[[-1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (0,0):room((0,0),"door",[[0,-1]],None),
        (1,0):room((1,0),"battle",[[1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (2,0):room((2,0),"battle",[[-1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (3,0):room((3,0),"boss",[[1,0]],["darkguard","darkguard","darkguard","darkknight"]),
        (4,0):room((4,0),"game",[[-1,0],[0,-1]],None)}),

    dungeon("darkcastle3","darkcastle",102,1,[424,510],[260,300],{
        (-2,-6):room((-2,-6),"magickey",[[0,1]],None),
        (0,-6):room((0,-6),"boss",[[0,1]],["darkguard","darkguard","darkguard","darkknight"]),
        (2,-6):room((2,-6),"magickey",[[0,1]],None),

        (-5,-5):room((-5,-5),"battle",[[1,0],[0,1]],["darkguard","darkguard","darkguard","darkguard"]),
        (-4,-5):room((-4,-5),"goldkey",[[-1,0]],None),
        (-2,-5):room((-2,-5),"battle",[[1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (-1,-5):room((-1,-5),"battle",[[-1,0],[0,1]],["darkguard","darkguard","darkguard","darkguard"]),
        (0,-5):room((0,-5),"game",[[0,1],[0,-1]],None),
        (1,-5):room((1,-5),"battle",[[1,0],[0,1]],["darkguard","darkguard","darkguard","darkguard"]),
        (2,-5):room((2,-5),"battle",[[-1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (4,-5):room((4,-5),"goldkey",[[1,0]],None),
        (5,-5):room((5,-5),"battle",[[-1,0],[0,1]],["darkguard","darkguard","darkguard","darkguard"]),

        (-5,-4):room((-5,-4),"battle",[[1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (-4,-4):room((-4,-4),"battle",[[-1,0],[0,1]],["darkguard","darkguard","darkguard","darkguard"]),
        (-1,-4):room((-1,-4),"battle",[[0,1],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (0,-4):room((0,-4),"magiclock",[[0,1],[0,-1]],None),
        (1,-4):room((1,-4),"battle",[[0,1],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (4,-4):room((4,-4),"battle",[[1,0],[0,1]],["darkguard","darkguard","darkguard","darkguard"]),
        (5,-4):room((5,-4),"battle",[[-1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),

        (-5,-3):room((-5,-3),"battle",[[1,0],[0,1]],["darkguard","darkguard","darkguard","darkguard"]),
        (-4,-3):room((-4,-3),"battle",[[-1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (-1,-3):room((-1,-3),"battle",[[0,1],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (0,-3):room((0,-3),"magiclock",[[0,1],[0,-1]],None),
        (1,-3):room((1,-3),"battle",[[0,1],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (4,-3):room((4,-3),"battle",[[1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (5,-3):room((5,-3),"battle",[[-1,0],[0,1]],["darkguard","darkguard","darkguard","darkguard"]),

        (-5,-2):room((-5,-2),"battle",[[1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (-4,-2):room((-4,-2),"battle",[[-1,0],[0,1]],["darkguard","darkguard","darkguard","darkguard"]),
        (-3,-2):room((-3,-2),"battle",[[1,0],[0,1]],["darkguard","darkguard","darkguard","darkguard"]),
        (-2,-2):room((-2,-2),"battle",[[-1,0],[0,1]],["darkguard","darkguard","darkguard","darkguard"]),
        (-1,-2):room((-1,-2),"goldlock",[[0,1],[0,-1]],None),
        (0,-2):room((0,-2),"battle",[[0,1],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (1,-2):room((1,-2),"goldlock",[[0,1],[0,-1]],None),
        (2,-2):room((2,-2),"battle",[[1,0],[0,1]],["darkguard","darkguard","darkguard","darkguard"]),
        (3,-2):room((3,-2),"battle",[[-1,0],[0,1]],["darkguard","darkguard","darkguard","darkguard"]),
        (4,-2):room((4,-2),"battle",[[1,0],[0,1]],["darkguard","darkguard","darkguard","darkguard"]),
        (5,-2):room((5,-2),"battle",[[-1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),

        (-5,-1):room((-5,-1),"battle",[[1,0],[0,1]],["darkguard","darkguard","darkguard","darkguard"]),
        (-4,-1):room((-4,-1),"battle",[[-1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (-3,-1):room((-3,-1),"battle",[[0,1],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (-2,-1):room((-2,-1),"battle",[[0,1],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (-1,-1):room((-1,-1),"battle",[[1,0],[0,1],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (0,-1):room((0,-1),"battle",[[1,0],[-1,0],[0,1],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (1,-1):room((1,-1),"battle",[[-1,0],[0,1],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (2,-1):room((2,-1),"battle",[[0,1],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (3,-1):room((3,-1),"battle",[[0,1],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (4,-1):room((4,-1),"battle",[[1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (5,-1):room((5,-1),"battle",[[-1,0],[0,1]],["darkguard","darkguard","darkguard","darkguard"]),

        (-5,0):room((-5,0),"battle",[[1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (-4,0):room((-4,0),"battle",[[1,0],[-1,0]],["darkguard","darkguard","darkguard","darkguard"]),
        (-3,0):room((-3,0),"battle",[[-1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (-2,0):room((-2,0),"battle",[[1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (-1,0):room((-1,0),"battle",[[-1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (0,0):room((0,0),"door",[[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (1,0):room((1,0),"battle",[[1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (2,0):room((2,0),"battle",[[-1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (3,0):room((3,0),"battle",[[1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (4,0):room((4,0),"battle",[[1,0],[-1,0]],["darkguard","darkguard","darkguard","darkguard"]),
        (5,0):room((5,0),"battle",[[-1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"])}),

    dungeon("darkcastle4","darkcastle",103,2,[244,425],[260,340],{
        (0,-8):room((0,-8),"boss",[[0,1]],["darkguard","darkguard","mazorov"]),

        (-5,-7):room((-5,-7),"heal",[[1,0],[0,1]],["darkguard","darkguard","darkguard","darkguard"]),
        (-4,-7):room((-4,-7),"bronzekey",[[-1,0]],None),
        (-1,-7):room((-3,-7),"goldkey",[[0,1]],None),
        (0,-7):room((-2,-7),"game",[[0,1],[0,-1]],None),
        (1,-7):room((-1,-7),"magickey",[[0,1]],None),
        (4,-7):room((0,-7),"silverkey",[[1,0]],None),
        (5,-7):room((5,-7),"heal",[[-1,0],[0,1]],["darkguard","darkguard","darkguard","darkguard"]),

        (-5,-6):room((-5,-6),"battle",[[1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (-4,-6):room((-4,-6),"battle",[[-1,0],[0,1]],["darkguard","darkguard","darkguard","darkguard"]),
        (-2,-6):room((-2,-6),"battle",[[1,0],[0,1]],["darkguard","darkguard","darkguard","darkguard"]),
        (-1,-6):room((-1,-6),"battle",[[-1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (0,-6):room((0,-6),"magiclock",[[0,1],[0,-1]],None),
        (1,-6):room((1,-6),"battle",[[1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (2,-6):room((2,-6),"battle",[[-1,0],[0,1]],["darkguard","darkguard","darkguard","darkguard"]),
        (4,-6):room((4,-6),"battle",[[1,0],[0,1]],["darkguard","darkguard","darkguard","darkguard"]),
        (5,-6):room((5,-6),"battle",[[-1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),

        (-5,-5):room((-5,-5),"battle",[[1,0],[0,1]],["darkguard","darkguard","darkguard","darkguard"]),
        (-4,-5):room((-4,-5),"battle",[[-1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (-2,-5):room((-2,-5),"battle",[[1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (-1,-5):room((-1,-5),"battle",[[-1,0],[0,1]],["darkguard","darkguard","darkguard","darkguard"]),
        (0,-5):room((0,-5),"goldlock",[[0,1],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (1,-5):room((1,-5),"battle",[[1,0],[0,1]],["darkguard","darkguard","darkguard","darkguard"]),
        (2,-5):room((2,-5),"battle",[[-1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (4,-5):room((4,-5),"battle",[[1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (5,-5):room((5,-5),"battle",[[-1,0],[0,1]],["darkguard","darkguard","darkguard","darkguard"]),

        (-5,-4):room((-5,-4),"battle",[[1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (-4,-4):room((-4,-4),"battle",[[-1,0],[0,1]],["darkguard","darkguard","darkguard","darkguard"]),
        (-1,-4):room((-1,-4),"battle",[[0,1],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (0,-4):room((0,-4),"silverlock",[[0,1],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (1,-4):room((1,-4),"battle",[[0,1],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (4,-4):room((4,-4),"battle",[[1,0],[0,1]],["darkguard","darkguard","darkguard","darkguard"]),
        (5,-4):room((5,-4),"battle",[[-1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),

        (-5,-3):room((-5,-3),"battle",[[1,0],[0,1]],["darkguard","darkguard","darkguard","darkguard"]),
        (-4,-3):room((-4,-3),"battle",[[-1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (-1,-3):room((-1,-3),"battle",[[0,1],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (0,-3):room((0,-3),"bronzelock",[[0,1],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (1,-3):room((1,-3),"battle",[[0,1],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (4,-3):room((4,-3),"battle",[[1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (5,-3):room((5,-3),"battle",[[-1,0],[0,1]],["darkguard","darkguard","darkguard","darkguard"]),

        (-5,-2):room((-5,-2),"battle",[[1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (-4,-2):room((-4,-2),"battle",[[1,0],[-1,0]],["darkguard","darkguard","darkguard","darkguard"]),
        (-3,-2):room((-3,-2),"battle",[[1,0],[-1,0]],["darkguard","darkguard","darkguard","darkguard"]),
        (-2,-2):room((-2,-2),"battle",[[-1,0],[0,1]],["darkguard","darkguard","darkguard","darkguard"]),
        (-1,-2):room((-1,-2),"battle",[[0,1],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (0,-2):room((0,-2),"battle",[[0,1],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (1,-2):room((1,-2),"battle",[[0,1],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (2,-2):room((2,-2),"battle",[[1,0],[0,1]],["darkguard","darkguard","darkguard","darkguard"]),
        (3,-2):room((3,-2),"battle",[[1,0],[-1,0]],["darkguard","darkguard","darkguard","darkguard"]),
        (4,-2):room((4,-2),"battle",[[1,0],[-1,0]],["darkguard","darkguard","darkguard","darkguard"]),
        (5,-2):room((5,-2),"battle",[[-1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),

        (-5,-1):room((-5,-1),"battle",[[1,0],[0,1]],["darkguard","darkguard","darkguard","darkguard"]),
        (-4,-1):room((-4,-1),"battle",[[1,0],[-1,0]],["darkguard","darkguard","darkguard","darkguard"]),
        (-3,-1):room((-3,-1),"battle",[[1,0],[-1,0]],["darkguard","darkguard","darkguard","darkguard"]),
        (-2,-1):room((-2,-1),"battle",[[-1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (-1,-1):room((-1,-1),"battle",[[1,0],[0,1],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (0,-1):room((0,-1),"battle",[[1,0],[-1,0],[0,1],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (1,-1):room((1,-1),"battle",[[-1,0],[0,1],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (2,-1):room((2,-1),"battle",[[1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (3,-1):room((3,-1),"battle",[[1,0],[-1,0]],["darkguard","darkguard","darkguard","darkguard"]),
        (4,-1):room((4,-1),"battle",[[1,0],[-1,0]],["darkguard","darkguard","darkguard","darkguard"]),
        (5,-1):room((5,-1),"battle",[[-1,0],[0,1]],["darkguard","darkguard","darkguard","darkguard"]),

        (-5,0):room((-5,0),"battle",[[1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (-4,0):room((-4,0),"battle",[[1,0],[-1,0]],["darkguard","darkguard","darkguard","darkguard"]),
        (-3,0):room((-3,0),"battle",[[1,0],[-1,0]],["darkguard","darkguard","darkguard","darkguard"]),
        (-2,0):room((-2,0),"battle",[[1,0],[-1,0]],["darkguard","darkguard","darkguard","darkguard"]),
        (-1,0):room((-1,0),"battle",[[-1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (0,0):room((0,0),"door",[[0,-1],[0,-8]],None),
        (1,0):room((1,0),"battle",[[1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"]),
        (2,0):room((2,0),"battle",[[1,0],[-1,0]],["darkguard","darkguard","darkguard","darkguard"]),
        (3,0):room((3,0),"battle",[[1,0],[-1,0]],["darkguard","darkguard","darkguard","darkguard"]),
        (4,0):room((4,0),"battle",[[1,0],[-1,0]],["darkguard","darkguard","darkguard","darkguard"]),
        (5,0):room((5,0),"battle",[[-1,0],[0,-1]],["darkguard","darkguard","darkguard","darkguard"])})
    ]


total = 0
for d in dungeons:
    count = 0
    for r in d.inside:
        if d.inside[r].contents == "battle" or d.inside[r].contents == "boss":
            for e in d.inside[r].extra:
                count += (enemylist[e][8][0] + enemylist[e][8][1]) / 2
        if d.inside[r].contents == "chest":
            if d.inside[r].extra[1][0] == "money":
                count += d.inside[r].extra[1][1]
    total += count
    print d.name,count,total






    
              
