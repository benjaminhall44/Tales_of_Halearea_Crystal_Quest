import random,pygame,pickle
pygame.init()
#pygame.mixer.init()
#soundeffectchannel = pygame.mixer.Channel(1)
#musicchannel = pygame.mixer.Channel(2)
linefont = pygame.font.Font(None,30)
screen = pygame.display.set_mode([560,400])
def playsound(name):
    pass
    #sfile = open("assets/audio/player/%s" % name)
    #soundeffectchannel.queue(pygame.mixer.Sound(sfile))
    #sfile.close()
maptexture = pygame.image.load("assets/graphics/extra/map.png")
clouds1texture = pygame.image.load("assets/graphics/extra/clouds1.png")
clouds2texture = pygame.image.load("assets/graphics/extra/clouds2.png")
clouds3texture = pygame.image.load("assets/graphics/extra/clouds3.png")
clouds4texture = pygame.image.load("assets/graphics/extra/clouds4.png")
clouds5texture = pygame.image.load("assets/graphics/extra/clouds5.png")
clouds6texture = pygame.image.load("assets/graphics/extra/clouds6.png")
clouds7texture = pygame.image.load("assets/graphics/extra/clouds7.png")
clouds8texture = pygame.image.load("assets/graphics/extra/clouds8.png")
clouds9texture = pygame.image.load("assets/graphics/extra/clouds9.png")
clouds10texture = pygame.image.load("assets/graphics/extra/clouds10.png")
clouds11texture = pygame.image.load("assets/graphics/extra/clouds11.png")
clouds12texture = pygame.image.load("assets/graphics/extra/clouds12.png")
def animatemap():
    global direction
    screen.blit(pygame.transform.chop(maptexture,[560,0,560,scroll]),[0,0])
    for d in dungeons:
        if mouseposition[0] > d.position[0] and mouseposition[0] < d.position[0] - 10 + 40 * d.size and mouseposition[1] > d.position[1] - scroll and mouseposition[1] < d.position[1] - 10 + 40 * d.size - scroll:
            if d.value <= progress:
                if d.size == 1:
                    screen.blit(pygame.image.load("assets/graphics/extra/glowsmallpin.png"),[d.position[0],d.position[1] - scroll])
                else:
                    screen.blit(pygame.image.load("assets/graphics/extra/glowbigpin.png"),[d.position[0],d.position[1] - scroll])
            elif d.value > progress + 1:
                if d.size == 1:
                    screen.blit(pygame.image.load("assets/graphics/extra/glowsmalllockpin.png"),[d.position[0],d.position[1] - scroll])
                else:
                    screen.blit(pygame.image.load("assets/graphics/extra/glowbiglockpin.png"),[d.position[0],d.position[1] - scroll])
            else:
                if d.size == 1:
                    screen.blit(pygame.image.load("assets/graphics/extra/glowsmallpin.png"),[d.position[0],d.position[1] - scroll])
                else:
                    screen.blit(pygame.image.load("assets/graphics/extra/glowbigpin.png"),[d.position[0],d.position[1] - scroll])
        else:
            if d.value <= progress:
                if d.size == 1:
                    screen.blit(pygame.image.load("assets/graphics/extra/smallpin.png"),[d.position[0],d.position[1] - scroll])
                else:
                    screen.blit(pygame.image.load("assets/graphics/extra/bigpin.png"),[d.position[0],d.position[1] - scroll])
            elif d.value > progress + 1:
                if d.size == 1:
                    screen.blit(pygame.image.load("assets/graphics/extra/smalllockpin.png"),[d.position[0],d.position[1] - scroll])
                else:
                    screen.blit(pygame.image.load("assets/graphics/extra/biglockpin.png"),[d.position[0],d.position[1] - scroll])
            else:
                if d.size == 1:
                    screen.blit(pygame.image.load("assets/graphics/extra/smallpin.png"),[d.position[0],d.position[1] - scroll])
                else:
                    screen.blit(pygame.image.load("assets/graphics/extra/bigpin.png"),[d.position[0],d.position[1] - scroll])
    if (positions[position + direction][0] - positions[position][0]) >= 0 or positions[position][2] == "sky":
        if positions[position][2] == "sky":
            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/extra/team%s%s.png" % (len(team),positions[position][2])),direction < 0,direction < 0),[positionuse[0],positionuse[1] - scroll])
        else:
            screen.blit(pygame.image.load("assets/graphics/extra/team%s%s.png" % (len(team),positions[position][2])),[positionuse[0],positionuse[1] - scroll])
    else:
        screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/extra/team%s%s.png" % (len(team),positions[position][2])),True,False),[positionuse[0],positionuse[1] - scroll])
    if progress < 8:
        screen.blit(pygame.transform.chop(clouds1texture,[560,0,560,scroll]),[0,0])
    elif progress < 17:
        screen.blit(pygame.transform.chop(clouds2texture,[560,0,560,scroll]),[0,0])
    elif progress < 25:
        screen.blit(pygame.transform.chop(clouds3texture,[560,0,560,scroll]),[0,0])
    elif progress < 33:
        screen.blit(pygame.transform.chop(clouds4texture,[560,0,560,scroll]),[0,0])
    elif progress < 42:
        screen.blit(pygame.transform.chop(clouds5texture,[560,0,560,scroll]),[0,0])
    elif progress < 50:
        screen.blit(pygame.transform.chop(clouds6texture,[560,0,560,scroll]),[0,0])
    elif progress < 58:
        screen.blit(pygame.transform.chop(clouds7texture,[560,0,560,scroll]),[0,0])
    elif progress < 67:
        screen.blit(pygame.transform.chop(clouds8texture,[560,0,560,scroll]),[0,0])
    elif progress < 75:
        screen.blit(pygame.transform.chop(clouds9texture,[560,0,560,scroll]),[0,0])
    elif progress < 83:
        screen.blit(pygame.transform.chop(clouds10texture,[560,0,560,scroll]),[0,0])
    elif progress < 91:
        screen.blit(pygame.transform.chop(clouds11texture,[560,0,560,scroll]),[0,0])
    elif progress < 99:
        screen.blit(pygame.transform.chop(clouds12texture,[560,0,560,scroll]),[0,0])
    if mouseposition[0] > 510 and mouseposition[0] < 550 and mouseposition[1] > 310 and mouseposition[1] < 350:
        screen.blit(pygame.image.load("assets/graphics/extra/gear2.png"),[510,310])
    else:
        screen.blit(pygame.image.load("assets/graphics/extra/gear1.png"),[510,310])
    if mouseposition[0] > 510 and mouseposition[0] < 550 and mouseposition[1] > 350 and mouseposition[1] < 390:
        screen.blit(pygame.image.load("assets/graphics/extra/bag2.png"),[510,350])
    else:
        screen.blit(pygame.image.load("assets/graphics/extra/bag1.png"),[510,350])
colors = [[50,50,50],[0,130,0],[55,181,255],[255,100,0],[200,0,255],[255,232,70]]
class item:
    def __init__(self,name,level,itemtype,equipt,health,attack,defence,speed,luck,itemid):
        self.name = name
        self.texture = pygame.image.load("assets/graphics/items/%s.png" % name)
        self.level = level
        self.itemtype = itemtype
        self.equipt = equipt
        self.health = health
        self.attack = attack
        self.defence = defence
        self.speed = speed
        self.luck = luck
        self.itemid = itemid
    def description(self):
        panel = pygame.image.load("assets/graphics/extra/description1.png")
        panel.blit(linefont.render("%s" % self.name,0,colors[self.level - 1]),[10,10])
        if "ring" in self.itemtype:
            panel.blit(linefont.render("ring Lv.%s" % (self.level),0,colors[self.level - 1]),[30,40])
        else:
            panel.blit(linefont.render("%s Lv.%s" % (self.itemtype,self.level),0,colors[self.level - 1]),[30,40])
        panel.blit(linefont.render(" + %s" % self.health,0,colors[self.level - 1]),[40,70])
        panel.blit(linefont.render(" + %s" % self.attack,0,colors[self.level - 1]),[40,96])
        panel.blit(linefont.render(" + %s" % self.defence,0,colors[self.level - 1]),[40,122])
        panel.blit(linefont.render(" + %s" % self.speed,0,colors[self.level - 1]),[40,148])
        panel.blit(linefont.render(" + %s" % self.luck,0,colors[self.level - 1]),[40,174])
        panelpos = mouseposition[:]
        if mouseposition[1] > 190:
            panelpos = (panelpos[0],190)
        if mouseposition[0] > 390:
            panelpos = (390,panelpos[1])
        screen.blit(panel,panelpos)
        pygame.display.flip()
        ###############
        #Golden Sword #
        #  Sword Lv.6 #
        #health + 0   #
        #attack + 400 #
        #defence + 0  #
        #speed + 100  #
        #luck + 0     #
        ###############
        #position on mouse
        #account for when mouse is near edge
class ingredient:
    def __init__(self,name,level,potiontype,itemid):
        self.name = name
        self.texture = pygame.image.load("assets/graphics/items/%s.png" % name)
        self.level = level
        self.itemtype = "ingredient"
        self.equipt = "ingredient"
        self.potiontype = potiontype
        self.itemid = itemid
    def description(self):
        panel = pygame.image.load("assets/graphics/extra/description2.png")
        panel.blit(linefont.render("%s" % self.name,0,colors[self.level - 1]),[10,10])
        panel.blit(linefont.render("%s Lv.%s" % (self.itemtype,self.level),0,colors[self.level - 1]),[10,40])
        panel.blit(linefont.render("Used to make",0,colors[self.level - 1]),[10,70])
        panel.blit(linefont.render("%s" % self.potiontype,0,colors[self.level - 1]),[10,96])
        panel.blit(linefont.render("Potions",0,colors[self.level - 1]),[10,122])
        panelpos = mouseposition[:]
        if mouseposition[1] > 190:
            panelpos = (panelpos[0],190)
        if mouseposition[0] > 390:
            panelpos = (390,panelpos[1])
        screen.blit(panel,panelpos)
        pygame.display.flip()
class potion:
    def __init__(self,name,level,power,itemid):
        self.name = name
        self.texture = pygame.image.load("assets/graphics/items/%s.png" % name)
        self.level = level
        self.itemtype = "potion"
        self.equipt = "potion"
        self.power = power
        self.potiontype = "healing"
        self.itemid = itemid
    def description(self):
        panel = pygame.image.load("assets/graphics/extra/description2.png")
        panel.blit(linefont.render("%s" % self.name,0,colors[self.level - 1]),[10,10])
        panel.blit(linefont.render("Potion Lv.%s" % (self.level),0,colors[self.level - 1]),[30,40])
        panel.blit(linefont.render("Used to heal",0,colors[self.level - 1]),[10,70])
        panel.blit(linefont.render("%s damage" % self.power,0,colors[self.level - 1]),[10,96])
        panel.blit(linefont.render("in a battle",0,colors[self.level - 1]),[10,122])
        panelpos = mouseposition[:]
        if mouseposition[1] > 190:
            panelpos = (panelpos[0],190)
        if mouseposition[0] > 390:
            panelpos = (390,panelpos[1])
        screen.blit(panel,panelpos)
        pygame.display.flip()
    def update(self,hud,team,enemies):
        return hud,team,enemies
    def use(self,hud,team,enemies,decor):
        hud.health += self.power
        if hud.health > hud.maxhealth:
            hud.health = hud.maxhealth
        hud.carry = None
        return hud,team,enemies
class potion2:
    def __init__(self,name,level,potiontype,power,duration,itemid):
        self.name = name
        self.texture = pygame.image.load("assets/graphics/items/%s.png" % name)
        self.level = level
        self.itemtype = "potion"
        self.equipt = "potion"
        self.power = power
        self.duration = duration
        self.potiontype = potiontype
        self.itemid = itemid
    def description(self):
        panel = pygame.image.load("assets/graphics/extra/description2.png")
        panel.blit(linefont.render("%s" % self.name,0,colors[self.level - 1]),[10,10])
        panel.blit(linefont.render("Potion Lv.%s" % (self.level),0,colors[self.level - 1]),[30,40])
        panel.blit(linefont.render("Used to give",0,colors[self.level - 1]),[10,70])
        panel.blit(linefont.render("+%s %s" % (self.power,self.potiontype),0,colors[self.level - 1]),[10,96])
        panel.blit(linefont.render("for %s seconds" % int(self.duration / 100),0,colors[self.level - 1]),[10,122])
        panel.blit(linefont.render("in a battle",0,colors[self.level - 1]),[10,148])
        panelpos = mouseposition[:]
        if mouseposition[1] > 190:
            panelpos = (panelpos[0],190)
        if mouseposition[0] > 390:
            panelpos = (390,panelpos[1])
        screen.blit(panel,panelpos)
        pygame.display.flip()
    def update(self,hud,team,enemies):
        return hud,team,enemies
    def use(self,hud,team,enemies,decor):
        hud.effect = [self.potiontype,self.power,self.duration]
        #if self.potiontype == "swiftness":
        #    hud.speed += self.power
        hud.carry = None
        hud.delay = int(6000 / (hud.speed + hud.effect[1] * (hud.effect[0] == "swiftness")))
        return hud,team,enemies
class spell:
    def __init__(self,name,delay,power,description,color,attack,itemid):
        self.name = name
        self.texture = pygame.image.load("assets/graphics/items/%s.png" % name)
        self.offtexture = pygame.image.load("assets/graphics/items/%scharge.png" % name)
        self.itemtype = "spell"
        self.equipt = "bag"
        self.itemid = itemid
        self.lore = description
        self.level = color
        self.attack = attack
        self.delay = delay
        self.power = power
    def description(self):
        panel = pygame.image.load("assets/graphics/extra/description2.png")
        panel.blit(linefont.render("%s" % self.name,0,colors[self.level - 1]),[10,10])
        px = 40
        for line in self.lore:
            panel.blit(linefont.render("%s" % line,0,colors[self.level - 1]),[10,px])
            px += 30
        panelpos = mouseposition[:]
        if mouseposition[1] > 190:
            panelpos = (panelpos[0],190)
        if mouseposition[0] > 390:
            panelpos = (390,panelpos[1])
        screen.blit(panel,panelpos)
        pygame.display.flip()
    def update(self,hud,team,enemies):
        if not "spellcharge" in dir(hud):
            hud.spellcharge = 0
        if hud.spellcharge < self.delay:
            hud.spellcharge += 1
        return hud,team,enemies
    def use(self,hud,team,enemies,decor):
        global mouseposition
        if hud.spellcharge == self.delay:
            if self.attack == "area" or self.attack == "heal" or self.attack == "wind":
                if self.attack == "area":
                    if self.name == "quake":
                        if doanimations:
                            animatebattle(enemies,decor,hud)
                            screen.blit(pygame.image.load("assets/graphics/spells/quake1.png"),[10 + battleside * 310,130])
                            pygame.display.flip()
                            pygame.time.delay(1000)
                            animatebattle(enemies,decor,hud)
                            screen.blit(pygame.image.load("assets/graphics/spells/quake2.png"),[10 + battleside * 310,130])
                            pygame.display.flip()
                        for d in enemies:
                            d.health -= self.power
                            if d.health < 0:
                                d.health = 0
                        if doanimations:
                            animatebattle(enemies,decor,hud)
                            screen.blit(pygame.image.load("assets/graphics/spells/quake2.png"),[10 + battleside * 310,130])
                            pygame.display.flip()
                            pygame.time.delay(1000)
                    elif self.name == "meteorstrike":
                        if doanimations:
                            if battleside:
                                arrpos = [30,230 - 300 - 100]
                            else:
                                arrpos = [430,230 - 300 - 100]
                            while arrpos[1] < 130:
                                arrpos[0] += -15 + 30 * battleside
                                arrpos[1] += 15
                                animatebattle(enemies,decor,hud)
                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/spells/meteor.png"),not battleside,False),arrpos)
                                pygame.display.flip()
                                pygame.time.delay(15)
                            animatebattle(enemies,decor,hud)
                            if battleside:
                                screen.blit(pygame.image.load("assets/graphics/spells/meteorcrash.png"),[430 - 50,130])
                            else:
                                screen.blit(pygame.image.load("assets/graphics/spells/meteorcrash.png"),[130 - 50,130])
                            pygame.display.flip()
                            pygame.time.delay(150)
                        for d in enemies:
                            d.health -= self.power
                            if d.health < 0:
                                d.health = 0
                elif self.attack == "heal":
                    if doanimations:
                        for f in range(1,5):
                            animatebattle(enemies,decor,hud)
                            if battleside:
                                screen.blit(pygame.image.load("assets/graphics/spells/heal%s.png" % f),[10,130])
                            else:
                                screen.blit(pygame.image.load("assets/graphics/spells/heal%s.png" % f),[310,130])
                            pygame.display.flip()
                            pygame.time.delay(100)
                    for d in team:
                        d.health += self.power
                        if d.health > d.maxhealth:
                            d.health = d.maxhealth
                elif self.attack == "wind":
                    if doanimations:
                        for f in range(1,7):
                            animatebattle(enemies,decor,hud,enemies)
                            """p = 0
                            for d in team:
                                if mouseposition[0] > 430 - 30 * len(team) + p and mouseposition[0] < 490 - 30 * len(team) + p and mouseposition[1] > 130 and mouseposition[1] < 230:
                                    screen.blit(pygame.image.load("assets/graphics/extra/characterhighlight.png"),[430 - 30 * len(team) + p,130])
                                if d.health > 0:
                                    if d.shield != None:
                                        screen.blit(pygame.image.load("assets/graphics/characters/%s.png" % d.shield.name),[430 - 30 * len(team) + p,130])
                                    screen.blit(pygame.image.load("assets/graphics/characters/%s.png" % d.name),[430 - 30 * len(team) + p,130])
                                    if d.armor != None:
                                        screen.blit(pygame.image.load("assets/graphics/characters/%s.png" % d.armor.name),[430 - 30 * len(team) + p,130])
                                    if d.weapon != None:
                                        screen.blit(pygame.image.load("assets/graphics/characters/%s.png" % d.weapon.name),[430 - 30 * len(team) + p,130])
                                    screen.blit(pygame.image.load("assets/graphics/characters/%sarm.png" % d.name),[430 - 30 * len(team) + p,130])
                                    pygame.draw.rect(screen,[200,200,200],[430 - 30 * len(team) + p,170,60,20])
                                    pygame.draw.rect(screen,[0,255,0],[430 - 30 * len(team) + p,170,60 * (float(d.health) / d.maxhealth),20])
                                    pygame.draw.arc(screen,[220,220,0],[430 - 30 * len(team) + p,65,30,30],1.570,7.853 * (float(d.charge) / d.delay),15)
                                    if d.effect[0] != None:
                                        screen.blit(pygame.image.load("assets/graphics/extra/%s.png" % d.effect[0]),[430 - 30 * len(team) + p,30])
                                        screen.blit(linefont.render("%s:%s" % (int(effect[2] / 6000),int(effect[2] / 100)),0,[0,0,150]),[460 - 30 * len(team) + p,30])
                                else:
                                    screen.blit(pygame.image.load("assets/graphics/characters/%ssleep.png" % d.name),[430 - 30 * len(team) + p,130])
                                p += 60"""
                            screen.blit(pygame.image.load("assets/graphics/spells/tornado%s.png" % f),[10 + battleside * 310,0])
                            pygame.display.flip()
                            pygame.time.delay(100)
                    enem = []
                    while len(enemies) > 0:
                        d = random.choice(enemies)
                        enem.append(d)
                        enemies.remove(d)
                        d.health -= self.power
                        if d.health < 0:
                            d.health = 0
                    enemies = enem[:]
                    animatebattle(enemies,decor,hud)
                    pygame.display.flip()
            else:
                read = True
                while read:
                    mouse = mouseposition[:]
                    mouseposition = [490,360]
                    animatebattle(enemies,decor,hud)
                    mouseposition = mouse[:]
                    screen.blit(pygame.image.load("assets/graphics/extra/target.png"),[mouseposition[0] - 25,mouseposition[1] - 25])
                    pygame.display.flip()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            read = False
                            running = False
                            playing = False
                            battle = False
                            return
                            break
                        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            entvol = 0
                            for d in enemies:
                                entvol += d.size[0] / 2
                            p = 0
                            for d in enemies:
                                if ((battleside and mouseposition[0] > 430 - entvol + p and mouseposition[0] < 430 + d.size[0] - entvol + p) or (not battleside and mouseposition[0] > 130 + entvol - p - d.size[0] and mouseposition[0] < 130 + entvol - p)) and mouseposition[1] > 230 - d.size[1] and mouseposition[1] < 230:
                                    target = d
                                    read = False
                                    break
                                p += d.size[0]
                            if not read:
                                break
                            if mouseposition[0] > 450 and mouseposition[0] < 490 and mouseposition[1] > 343 and mouseposition[1] < 383 and hud.good:
                                read = False
                                return hud,team,enemies
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_4:
                                if len(enemies) > 0 + 3*battleside:
                                    target = enemies[0 + 3*battleside]
                                    read = False
                                    break
                            elif event.key == pygame.K_3:
                                if len(enemies) > 1 + 1*battleside:
                                    target = enemies[1 + 1*battleside]
                                    read = False
                                    break
                            elif event.key == pygame.K_2:
                                if len(enemies) > 2 - 1*battleside:
                                    target = enemies[2 - 1*battleside]
                                    read = False
                                    break
                            elif event.key == pygame.K_1:
                                if len(enemies) > 3 - 3*battleside:
                                    target = enemies[3 - 3*battleside]
                                    read = False
                                    break
                            elif event.key == pygame.K_v:
                                read = False
                                return hud,team,enemies
                        elif event.type == pygame.MOUSEMOTION:
                            mouseposition = event.pos[:]
                            mouse = mouseposition[:]
                            mouseposition = [490,360]
                            animatebattle(enemies,decor,hud)
                            mouseposition = mouse[:]
                            screen.blit(pygame.image.load("assets/graphics/extra/target.png"),[mouseposition[0] - 25,mouseposition[1] - 25])
                            pygame.display.flip()
                if self.attack == "bomb":
                    #animation
                    if doanimations:
                        if battleside:
                            arrpos = [(130 + 30 * len(team) - 60 - 60 * team.index(hud)) - 37 + 74 * battleside,130]
                        else:
                            arrpos = [(430 - 30 * len(team) + 60 * team.index(hud)) - 37 + 74 * battleside,130]
                        p = 0
                        entvol = 0
                        for d in enemies:
                            entvol += d.size[0] / 2
                            if d == target:
                                pv = p
                            p += d.size[0]
                        while (battleside and arrpos[0] + 30 < 430 - entvol + pv) or ((not battleside) and arrpos[0] > 130 + entvol - pv):
                            arrpos[0] += -15 + 30 * battleside
                            animatebattle(enemies,decor,hud)
                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/spells/fireball.png"),not battleside,False),arrpos)
                            pygame.display.flip()
                            pygame.time.delay(15)
                        for f in range(1,5):
                            screen.blit(pygame.image.load("assets/graphics/spells/fireball%s.png" % f),[arrpos[0] + 60 * battleside - 120,90])
                            pygame.display.flip()
                            pygame.time.delay(50)
                    target.health -= self.power - (target.defence + target.effect[1] * (target.effect[0] == "resistance"))
                    if target.health < 0:
                        target.health = 0
                    if enemies.index(target) > 0:
                        enemies[enemies.index(target) - 1].health -= self.power / 2 - (enemies[enemies.index(target) - 1].defence + enemies[enemies.index(target) - 1].effect[1] * (enemies[enemies.index(target) - 1].effect[0] == "resistance"))
                        if enemies[enemies.index(target) - 1].health < 0:
                            enemies[enemies.index(target) - 1].health = 0
                    if enemies.index(target) < len(enemies) - 1:
                        enemies[enemies.index(target) + 1].health -= self.power / 2 - (enemies[enemies.index(target) + 1].defence + enemies[enemies.index(target) - 1].effect[1] * (enemies[enemies.index(target) - 1].effect[0] == "resistance"))
                        if enemies[enemies.index(target) + 1].health < 0:
                            enemies[enemies.index(target) + 1].health = 0
                elif self.attack == "strike":
                    if doanimations:
                        if self.name == "lightning":
                            animatebattle(enemies,decor,hud)
                            p = 0
                            entvol = 0
                            for d in enemies:
                                entvol += d.size[0] / 2
                                if d == target:
                                    pv = p
                                    pvi = p + d.size[0]
                                p += d.size[0]
                            if battleside:
                                screen.blit(pygame.image.load("assets/graphics/spells/lightning.png"),[430 - entvol + pv + (target.size[0] - 60) / 2,0])
                            else:
                                screen.blit(pygame.image.load("assets/graphics/spells/lightning.png"),[130 + entvol - pvi - (target.size[0] - 60) / 2,0])
                            pygame.display.flip()
                            pygame.time.delay(50)
                    target.health -= self.power - (target.defence + target.effect[1] * (target.effect[0] == "resistance"))
                    if target.health < 0:
                        target.health = 0
                    animatebattle(enemies,decor,hud)
                elif self.attack == "fang":
                    #animation
                    target.effect = self.power[:]
                elif self.attack == "leech":
                    if doanimations:
                        if battleside:
                            arrpos = [(130 + 30 * len(team) - 60 - 60 * team.index(hud)) - 37 + 74 * battleside,130 + 39]
                        else:
                            arrpos = [(430 - 30 * len(team) + 60 * team.index(hud)) - 37 + 74 * battleside,130 + 39]
                        p = 0
                        entvol = 0
                        for d in enemies:
                            entvol += d.size[0] / 2
                            if d == target:
                                pv = p
                            p += d.size[0]
                        while (battleside and arrpos[0] + 30 - 15 < 430 - entvol + pv) or ((not battleside) and arrpos[0] + 15 > 130 + entvol - pv):
                            arrpos[0] += -15 + 30 * battleside
                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/spells/leechvine.png"),not battleside,False),arrpos)
                            pygame.display.flip()
                            pygame.time.delay(15)
                        pygame.time.delay(500)
                    #animation
                    h = target.health
                    target.health -= self.power - (target.defence + target.effect[1] * (target.effect[0] == "resistance"))
                    if target.health < 0:
                        target.health = 0
                    hud.health += h - target.health
                    if hud.health > hud.maxhealth:
                        hud.health = hud.maxhealth
                    animatebattle(enemies,decor,hud)
                elif self.attack == "arrow":
                    if hud.weapon.itemtype == "bow":
                        #animation
                        if doanimations:
                            if battleside:
                                arrpos = [(130 + 30 * len(team) - 60 - 60 * team.index(hud)) - 37 + 74 * battleside,130 + 39]
                            else:
                                arrpos = [(430 - 30 * len(team) + 60 * team.index(hud)) - 37 + 74 * battleside,130 + 39]
                            p = 0
                            entvol = 0
                            for d in enemies:
                                entvol += d.size[0] / 2
                                if d == target:
                                    pv = p
                                p += d.size[0]
                            while (battleside and arrpos[0] + 30 - 15 < 430 - entvol + pv) or ((not battleside) and arrpos[0] + 15 > 130 + entvol - pv):
                                arrpos[0] += -15 + 30 * battleside
                                animatebattle(enemies,decor,hud)
                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/spells/brilliantarrow.png"),not battleside,False),arrpos)
                                pygame.display.flip()
                                pygame.time.delay(15)
                        target.health -= self.power - (target.defence + target.effect[1] * (target.effect[0] == "resistance"))
                        if target.health < 0:
                            target.health = 0
                    else:
                        return hud,team,enemies
            hud.spellcharge = 0
        return hud,team,enemies

smallsword = item("smallsword",1,"sword","weapon",0,10,0,2 * 5 - 1,0,0)
ironsword = item("ironsword",2,"sword","weapon",0,20,0,10 - 1,0,1)
steelsword = item("steelsword",3,"sword","weapon",0,30,0,15 - 1,0,2)
greatsword = item("greatsword",4,"sword","weapon",0,50,0,20 - 1,0,3)
silversword = item("silversword",5,"sword","weapon",0,70,0,25 - 1,0,4)
goldensword = item("goldensword",6,"sword","weapon",0,100,0,30 - 1,0,5)

twigbow = item("twigbow",1,"bow","weapon",0,12,0,4 - 1,0,6)
basicbow = item("basicbow",2,"bow","weapon",0,24,0,8 - 1,0,7)
goodbow = item("goodbow",3,"bow","weapon",0,36,0,12 - 1,0,8)
longbow = item("longbow",4,"bow","weapon",0,60,0,16 - 1,0,9)
hunterbow = item("hunterbow",5,"bow","weapon",0,94,0,20 - 1,0,10)
masterbow = item("masterbow",6,"bow","weapon",0,120,0,24 - 1,0,11)

stonehammer = item("stonehammer",1,"hammer","weapon",0,15,0,3 - 1,0,12)
sludgehammer = item("sludgehammer",2,"hammer","weapon",0,30,0,6 - 1,0,13)
ironmallet = item("ironmallet",3,"hammer","weapon",0,45,0,9 - 1,0,14)
steelhammer = item("steelhammer",4,"hammer","weapon",0,75,0,12 - 1,0,15)
silverhammer = item("silverhammer",5,"hammer","weapon",0,105,0,15 - 1,0,16)
goldenhammer = item("goldenhammer",6,"hammer","weapon",0,150,0,18 - 1,0,17)

basicwand = item("basicwand",1,"wand","weapon",0,7,0,8 - 1,0,18)
starwand = item("starwand",2,"wand","weapon",0,14,0,15 - 1,0,19)
enchantedwand = item("enchantedwand",3,"wand","weapon",0,21,0,23 - 1,0,20)
basicstaff = item("basicstaff",4,"wand","weapon",0,35,0,30 - 1,0,21)
masterstaff = item("masterstaff",5,"wand","weapon",0,49,0,38 - 1,0,22)
crystalstaff = item("crystalstaff",6,"wand","weapon",0,70,0,45 - 1,0,23)

leatherarmor = item("leatherarmor",1,"armor","armor",50,0,0,0,0,24)
platedarmor = item("platedarmor",2,"armor","armor",100,0,0,0,0,25)
chainarmor = item("chainarmor",3,"armor","armor",200,0,0,0,0,26)
steelarmor = item("steelarmor",4,"armor","armor",400,0,0,0,0,27)
silverarmor = item("silverarmor",5,"armor","armor",600,0,0,0,0,28)
goldenarmor = item("goldenarmor",6,"armor","armor",900,0,0,0,0,29)

woodenshield = item("woodenshield",1,"shield","shield",0,0,2,0,0,30)
circularshield = item("circularshield",2,"shield","shield",0,0,4,0,0,31)#reinforcedshield
ironshield = item("ironshield",3,"shield","shield",0,0,6,0,0,32)
wideshield = item("wideshield",4,"shield","shield",0,0,10,0,0,33)
silvershield = item("silvershield",5,"shield","shield",0,0,14,0,0,34)
goldenshield = item("goldenshield",6,"shield","shield",0,0,20,0,0,35)

greenring = item("greenring",1,"healthring","ring",75,0,0,0,0,36)#75
greenjewel = item("greenjewel",2,"healthring","ring",100,0,0,0,0,37)#100
greennecklace = item("greennecklace",3,"healthring","ring",150,0,0,0,0,38)#150
greenamulet = item("greenamulet",4,"healthring","ring",250,0,0,0,0,39)#250
greengoblet = item("greengoblet",5,"healthring","ring",350,0,0,0,0,40)#350
greencrown = item("greencrown",6,"healthring","ring",500,0,0,0,0,41)#500
redring = item("redring",1,"attackring","ring",0,5,0,0,0,42)
redjewel = item("redjewel",2,"attackring","ring",0,10,0,0,0,43)
rednecklace = item("rednecklace",3,"attackring","ring",0,15,0,0,0,44)
redamulet = item("redamulet",4,"attackring","ring",0,25,0,0,0,45)
redgoblet = item("redgoblet",5,"attackring","ring",0,35,0,0,0,46)
redcrown = item("redcrown",6,"attackring","ring",0,50,0,0,0,47)
bluering = item("bluering",1,"defencering","ring",0,0,1,0,0,48)
bluejewel = item("bluejewel",2,"defencering","ring",0,0,2,0,0,49)
bluenecklace = item("bluenecklace",3,"defencering","ring",0,0,3,0,0,50)
blueamulet = item("blueamulet",4,"defencering","ring",0,0,5,0,0,51)
bluegoblet = item("bluegoblet",5,"defencering","ring",0,0,7,0,0,52)
bluecrown = item("bluecrown",6,"defencering","ring",0,0,10,0,0,53)
yellowring = item("yellowring",1,"speedring","ring",0,0,0,2 * 2,0,54)
yellowjewel = item("yellowjewel",2,"speedring","ring",0,0,0,5,0,55)
yellownecklace = item("yellownecklace",3,"speedring","ring",0,0,0,7,0,56)
yellowamulet = item("yellowamulet",4,"speedring","ring",0,0,0,10,0,57)
yellowgoblet = item("yellowgoblet",5,"speedring","ring",0,0,0,12,0,58)
yellowcrown = item("yellowcrown",6,"speedring","ring",0,0,0,15,0,59)
pinkring = item("pinkring",1,"luckring","ring",0,0,0,0,5,60)
pinkjewel = item("pinkjewel",2,"luckring","ring",0,0,0,0,10,61)
pinknecklace = item("pinknecklace",3,"luckring","ring",0,0,0,0,15,62)
pinkamulet = item("pinkamulet",4,"luckring","ring",0,0,0,0,20,63)
pinkgoblet = item("pinkgoblet",5,"luckring","ring",0,0,0,0,30,64)
pinkcrown = item("pinkcrown",6,"luckring","ring",0,0,0,0,45,65)

healthherbs = potion("healthherbs",1,100,66)
smallhealthpotion = potion("healthserum",2,200,67)#healthvial--serum
healthpotion = potion("healthpotion",3,500,68)
largehealthpotion = potion("healthjug",4,750,69)#healthjug
healthelixir = potion("healthtonic",5,1000,70)#healthtonic
largehealthelixir = potion("healthelixir",6,1900,71)#healthelixer

strengthherbs = potion2("strengthherbs",1,"strength",10,6000,72)
smallstrengthpotion = potion2("strengthserum",2,"strength",20,6000,73)
strengthpotion = potion2("strengthpotion",3,"strength",30,6000,74)
largestrengthpotion = potion2("strengthjug",4,"strength",50,6000,75)
strengthelixir = potion2("strengthtonic",5,"strength",70,6000,76)
largestrengthelixir = potion2("strengthelixir",6,"strength",100,6000,77)

defenceherbs = potion2("defenceherbs",1,"resistance",2,6000,78)
smalldefencepotion = potion2("defenceserum",2,"resistance",4,6000,79)
defencepotion = potion2("defencepotion",3,"resistance",6,6000,80)
largedefencepotion = potion2("defencejug",4,"resistance",10,6000,81)
defenceelixir = potion2("defencetonic",5,"resistance",14,6000,82)
largedefenceelixir = potion2("defenceelixir",6,"resistance",20,6000,83)

speedherbs = potion2("speedherbs",1,"swiftness",5 + 3,6000,84)
smallspeedpotion = potion2("speedserum",2,"swiftness",10,6000,85)
speedpotion = potion2("speedpotion",3,"swiftness",15,6000,86)
largespeedpotion = potion2("speedjug",4,"swiftness",20,6000,87)
speedelixir = potion2("speedtonic",5,"swiftness",25,6000,88)
largespeedelixir = potion2("speedelixir",6,"swiftness",30,6000,89)

luckherbs = potion2("luckherbs",1,"charm",10,6000,90)
smallluckpotion = potion2("luckserum",2,"charm",20,6000,91)
luckpotion = potion2("luckpotion",3,"charm",30,6000,92)
largeluckpotion = potion2("luckjug",4,"charm",40,6000,93)
luckelixir = potion2("lucktonic",5,"charm",60,6000,94)
largeluckelixir = potion2("luckelixir",6,"charm",90,6000,95)

healingbranch = ingredient("healingbranch",1,"healing",96)
greenspices = ingredient("greenspices",2,"healing",97)
greennector = ingredient("greennector",3,"healing",98)
greengem = ingredient("greengem",4,"healing",99)

emberleaf = ingredient("emberleaf",1,"strength",100)
redspices = ingredient("redspices",2,"strength",101)
rednector = ingredient("rednector",3,"strength",102)
redgem = ingredient("redgem",4,"strength",103)

toughgord = ingredient("toughgord",1,"resistance",104)
bluespices = ingredient("bluespices",2,"resistance",105)
bluenector = ingredient("bluenector",3,"resistance",106)
bluegem = ingredient("bluegem",4,"resistance",107)

seepyberries = ingredient("seepyberries",1,"swiftness",108)
yellowspices = ingredient("yellowspices",2,"swiftness",109)
yellownector = ingredient("yellownector",3,"swiftness",110)
yellowgem = ingredient("yellowgem",4,"swiftness",111)

cobanut = ingredient("cobanut",1,"charm",112)
pinkspices = ingredient("pinkspices",2,"charm",113)
pinknector = ingredient("pinknector",3,"charm",114)
pinkgem = ingredient("pinkgem",4,"charm",115)

fireball = spell("fireball",1000,400,["attack an","enemy and do","half damage to","surrounding","enemies"],2,"bomb",116)
lightning = spell("lightning",1000,600,["zap an","enemy"],2,"strike",117)
frost = spell("frost",2000,["frozen",50,300],["freeze an","enemy"],3,"fang",118)
poison = spell("poison",2000,["poison",100,1000],["poison an","enemy"],3,"fang",119)
leechvine = spell("leechvine",1500,250,["drain life from","an enemy"],3,"leech",120)
brilliantarrow = spell("brilliantarrow",2000,1500,["shoot a magic","arrow","(requires bow)"],4,"arrow",121)
healpulse = spell("healpulse",2000,50,["heal your team"],4,"heal",122)
whirlwind = spell("whirlwind",2000,200,["blow all the","enemies","around"],4,"wind",123)
quake = spell("quake",3000,1000,["attack all","enemies"],5,"area",124)
meteorstrike = spell("meteorstrike",6000,5000,["attack all","enemies"],6,"area",125)

items = [smallsword,ironsword,steelsword,greatsword,silversword,goldensword,#0-5
         twigbow,basicbow,goodbow,longbow,hunterbow,masterbow,#6-11
         stonehammer,sludgehammer,ironmallet,steelhammer,silverhammer,goldenhammer,#12-17
         basicwand,starwand,enchantedwand,basicstaff,masterstaff,crystalstaff,#18-23

         leatherarmor,platedarmor,chainarmor,steelarmor,silverarmor,goldenarmor,#24-29

         woodenshield,circularshield,ironshield,wideshield,silvershield,goldenshield,#30-35

         greenring,greenjewel,greennecklace,greenamulet,greengoblet,greencrown,#36-41
         redring,redjewel,rednecklace,redamulet,redgoblet,redcrown,#42-47
         bluering,bluejewel,bluenecklace,blueamulet,bluegoblet,bluecrown,#48-53
         yellowring,yellowjewel,yellownecklace,yellowamulet,yellowgoblet,yellowcrown,#54-59
         pinkring,pinkjewel,pinknecklace,pinkamulet,pinkgoblet,pinkcrown,#60-65

         healthherbs,smallhealthpotion,healthpotion,largehealthpotion,healthelixir,largehealthelixir,#66-71
         strengthherbs,smallstrengthpotion,strengthpotion,largestrengthpotion,strengthelixir,largestrengthelixir,#72-77
         defenceherbs,smalldefencepotion,defencepotion,largedefencepotion,defenceelixir,largedefenceelixir,#78-83
         speedherbs,smallspeedpotion,speedpotion,largespeedpotion,speedelixir,largespeedelixir,#84-89
         luckherbs,smallluckpotion,luckpotion,largeluckpotion,luckelixir,largeluckelixir,#90-95

         healingbranch,greenspices,greennector,greengem,#96-99
         emberleaf,redspices,rednector,redgem,#100-103
         toughgord,bluespices,bluenector,bluegem,#104-107
         seepyberries,yellowspices,yellownector,yellowgem,#108-111
         cobanut,pinkspices,pinknector,pinkgem,#112-115

         fireball,lightning,frost,poison,leechvine,brilliantarrow,healpulse,whirlwind,quake,meteorstrike#116-125
         

         ]

prices = [50,140,400,1000,2500,7000,#swords
          55,155,440,1100,2750,7700,#bows
          60,170,480,1200,3000,8400,#hammer
          55,155,440,1100,2750,7700,#wands

          75,210,600,1500,3750,10500,#armor
          
          60,170,480,1200,3000,8400,#shield

          100,280,800,2000,5000,14000,#rings
          100,280,800,2000,5000,14000,#rings
          100,280,800,2000,5000,14000,#rings
          100,280,800,2000,5000,14000,#rings
          100,280,800,2000,5000,14000,#rings

          15,40,100,250,700,2000,#potions
          15,40,100,250,700,2000,#potions
          15,40,100,250,700,2000,#potions
          15,40,100,250,700,2000,#potions
          15,40,100,250,700,2000,#potions

          5,15,40,100,#herbs
          5,15,40,100,#herbs
          5,15,40,100,#herbs
          5,15,40,100,#herbs
          5,15,40,100,#herbs

          2000,2000,5000,5000,6000,12000,12000,12000,18000,24000#spells


          ]
class character:
    def __init__(self,name,weapon,armor,shield,ring1,ring2,carry):
        self.name = name
        self.good = True
        self.texture = pygame.image.load("assets/graphics/characters/%s.png" % name)
        if weapon != None:
            self.weapon = items[weapon]
        else:
            self.weapon = None
        if armor != None:
            self.armor = items[armor]
        else:
            self.armor = None
        if shield != None:
            self.shield = items[shield]
        else:
            self.shield = None
        if ring1 != None:
            self.ring1 = items[ring1]
        else:
            self.ring1 = None
        if ring2 != None:
            self.ring2 = items[ring2]
        else:
            self.ring2 = None
        if carry != None:
            self.carry = items[carry]
        else:
            self.carry = None
        self.health = 100
        self.attack = 0
        self.defence = 0
        self.speed = 1
        self.luck = 10
        self.effect = [None,0,0]
        self.spellcharge = 0
        if self.weapon != None:
            self.health += self.weapon.health
            self.attack += self.weapon.attack
            self.defence += self.weapon.defence
            self.speed += self.weapon.speed
            self.luck += self.weapon.luck
        if self.armor != None:
            self.health += self.armor.health
            self.attack += self.armor.attack
            self.defence += self.armor.defence
            self.speed += self.armor.speed
            self.luck += self.armor.luck
        if self.shield != None:
            self.health += self.shield.health
            self.attack += self.shield.attack
            self.defence += self.shield.defence
            self.speed += self.shield.speed
            self.luck += self.shield.luck
        if self.ring1 != None:
            self.health += self.ring1.health
            self.attack += self.ring1.attack
            self.defence += self.ring1.defence
            self.speed += self.ring1.speed
            self.luck += self.ring1.luck
        if self.ring2 != None:
            self.health += self.ring2.health
            self.attack += self.ring2.attack
            self.defence += self.ring2.defence
            self.speed += self.ring2.speed
            self.luck += self.ring2.luck
        self.maxhealth = self.health
        self.delay = int(6000 / (self.speed + self.effect[1] * (self.effect[0] == "swiftness")))
        self.charge = 0
class enemy:
    def __init__(self,enlist):
        self.name = enlist[0]
        self.good = False
        self.texture = pygame.image.load("assets/graphics/enemies/%s.png" % enlist[0])
        self.health = enlist[1]
        self.attack = enlist[2]
        self.defence = enlist[3]
        self.speed = enlist[4]
        self.luck = enlist[5]
        self.effect = [None,0,0]
        self.maxhealth = self.health
        self.delay = int(6000 / (self.speed + self.effect[1] * (self.effect[0] == "swiftness")))
        self.charge = 0
        self.poisoncharge = 0
        self.attacktype = enlist[6]
        self.level = enlist[7]
        self.loot = enlist[8]
        self.boss = enlist[9]
        if len(enlist) == 11:
            self.size = enlist[10]
        else:
            self.size = [60,100]
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
class person:
    def __init__(self,name,value,position,size,quest,facing):
        self.name = name
        self.texture = pygame.image.load("assets/graphics/city/%s.png" % name)
        self.value = value
        self.position = position
        self.size = size
        self.quest = quest
        self.facing = facing
class city:
    def __init__(self,name,value,position,size,scharacter,people):
        self.name = name
        self.value = value
        self.position = position
        self.size = size
        self.character = scharacter
        self.people = []
        for p in people:
            self.people.append(person(p[0],p[1],p[2],p[3],p[4],p[5]))
    def visit(self):
        global mouseposition,progress,tutorial,money,inventory,quests
        if progress < self.value:
            progress += 1
            team.append(character(self.character[0],self.character[1],self.character[2],self.character[3],self.character[4],self.character[5],self.character[6]))
            screen.blit(pygame.image.load("assets/graphics/extra/teamadd.png"),[0,0])
            screen.blit(linefont.render("%s Has Decided To Join Your Team" % team[-1].name,0,[150,120,0]),[100,70])
            if team[-1].shield != None:
                screen.blit(pygame.transform.scale(pygame.image.load("assets/graphics/characters/%s.png" % team[-1].shield.name),[120,200]),[220,100])
            screen.blit(pygame.transform.scale(pygame.image.load("assets/graphics/characters/%s.png" % team[-1].name),[120,200]),[220,100])
            if team[-1].armor != None:
                screen.blit(pygame.transform.scale(pygame.image.load("assets/graphics/characters/%s.png" % team[-1].armor.name),[120,200]),[220,100])
            if team[-1].weapon != None:
                screen.blit(pygame.transform.scale(pygame.image.load("assets/graphics/characters/%s.png" % team[-1].weapon.name),[120,200]),[220,100])
            screen.blit(pygame.transform.scale(pygame.image.load("assets/graphics/characters/%sarm.png" % team[-1].name),[120,200]),[220,100])
            screenup = True
            pygame.display.flip()
            while screenup:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        playing = False
                        visit = False
                        screenup = False
                        break
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        screenup = False
                    if event.type == pygame.MOUSEMOTION:
                        mouseposition = event.pos[:]
        visit = True
        while visit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    playing = False
                    visit = False
                    break
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for d in self.people:
                        if quests[d.value] == False:
                            if mouseposition[0] > d.position[0] and mouseposition[0] < d.position[0] + d.size[0] and mouseposition[1] > d.position[1] and mouseposition[1] < d.position[1] + d.size[1]:
                                if d.quest[0] == "shop":
                                    shop(d.quest[1])
                                    if tutorial == 1 and team[0].weapon != None:
                                        tutorial == 0
                                        screen.blit(pygame.image.load("assets/graphics/city/%s.png" % self.name),[0,0])
                                        for d in self.people:
                                            if quests[d.value] == False:
                                                if mouseposition[0] > d.position[0] and mouseposition[0] < d.position[0] + d.size[0] and mouseposition[1] > d.position[1] and mouseposition[1] < d.position[1] + d.size[1]:
                                                    screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/city/%sglow.png" % d.name),d.facing,False),d.position)
                                                else:
                                                    screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/city/%s.png" % d.name),d.facing,False),d.position)
                                        pygame.display.flip()
                                        pygame.time.delay(500)
                                        readbox(["Visit my house at any time","for some instructions on combat"],"oldfox")
                                elif d.quest[0] == "talk":
                                    readbox(d.quest[1],d.name)
                                elif d.quest[0] == "teach":
                                    teach(d.quest[1])
                                elif d.quest[0] == "bag":
                                    inventoryopen()
                                elif d.quest[0] == "exit":
                                    if team[0].weapon != None or progress > 1:
                                        visit = False
                                        tutorial = 0
                                    elif team[0].weapon == None:
                                        readbox(["You ought to equip a sword before","you leave"],"oldfox")
                                elif d.quest[0] == "quest":
                                    readbox(d.quest[1][:-1],d.name)
                                    if questionbox(d.quest[1][-1]):
                                        num = 0
                                        cle = []
                                        for i in range(len(inventory)):
                                            if inventory[i] == d.quest[2]:
                                                num += 1
                                                cle.append(i)
                                        if num >= d.quest[3]:
                                            for s in cle:
                                                inventory[s] = None
                                            readbox(d.quest[4],d.name)
                                            if d.quest[5] == "money":
                                                money += d.quest[6]
                                            elif d.quest[5] == "item":
                                                if None in inventory[:15 * len(team)]:
                                                    inventory[inventory.index(None)] = d.quest[6]
                                            quests[d.value] = True
                                break
                    screen.blit(pygame.image.load("assets/graphics/city/%s.png" % self.name),[0,0])
                    for d in self.people:
                        if quests[d.value] == False:
                            if mouseposition[0] > d.position[0] and mouseposition[0] < d.position[0] + d.size[0] and mouseposition[1] > d.position[1] and mouseposition[1] < d.position[1] + d.size[1]:
                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/city/%sglow.png" % d.name),d.facing,False),d.position)
                            else:
                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/city/%s.png" % d.name),d.facing,False),d.position)
                    pygame.display.flip()
                if event.type == pygame.MOUSEMOTION:
                    mouseposition = event.pos[:]
                    screen.blit(pygame.image.load("assets/graphics/city/%s.png" % self.name),[0,0])
                    for d in self.people:
                        if quests[d.value] == False:
                            if mouseposition[0] > d.position[0] and mouseposition[0] < d.position[0] + d.size[0] and mouseposition[1] > d.position[1] and mouseposition[1] < d.position[1] + d.size[1]:
                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/city/%sglow.png" % d.name),d.facing,False),d.position)
                            else:
                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/city/%s.png" % d.name),d.facing,False),d.position)
                    pygame.display.flip()
def readbox(words,name):
    read = True
    speaker = pygame.image.load("assets/graphics/city/%s.png" % name)
    specord = speaker.get_rect()
    speaker = pygame.transform.scale(speaker,[specord[2] * 2,specord[3] * 2])
    screen.blit(speaker,[63,282 - specord[3] * 2])
    screen.blit(pygame.image.load("assets/graphics/extra/readbox.png"),[0,0])
    y = 260
    for line in words:
        screen.blit(linefont.render(line,0,[0,0,0]),[70,y])
        y += 30
    pygame.display.flip()
    while read:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                read = False
                running = False
                playing = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                read = False
            if event.type == pygame.MOUSEMOTION:
                mouseposition = event.pos[:]
def questionbox(string):
    global mouseposition,mousedown
    read = True
    screen.blit(pygame.image.load("assets/graphics/extra/readbox.png"),[0,0])
    screen.blit(linefont.render(string,0,[0,0,0]),[70,260])
    screen.blit(linefont.render("Yes",0,[255,0,0]),[70,290])
    screen.blit(linefont.render("No",0,[255,0,0]),[70,320])
    pygame.display.flip()
    while read:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                read = False
                running = False
                playing = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if mouseposition[0] > 60 and mouseposition[0] < 500 and mouseposition[1] > 280 and mouseposition[1] < 310:
                    return True
                else:
                    return False
            if event.type == pygame.MOUSEMOTION:
                mouseposition = event.pos[:]
                screen.blit(pygame.image.load("assets/graphics/extra/readbox.png"),[0,0])
                screen.blit(linefont.render(string,0,[0,0,0]),[70,260])
                if mouseposition[0] > 70 and mouseposition[0] < 170 and mouseposition[1] > 290 and mouseposition[1] < 320:
                    screen.blit(linefont.render("Yes",0,[200,0,0]),[70,290])
                    screen.blit(linefont.render("No",0,[255,0,0]),[70,320])
                else:
                    screen.blit(linefont.render("Yes",0,[255,0,0]),[70,290])
                    if mouseposition[0] > 70 and mouseposition[0] < 170 and mouseposition[1] > 320 and mouseposition[1] < 350:
                        screen.blit(linefont.render("No",0,[200,0,0]),[70,320])
                    else:
                        screen.blit(linefont.render("No",0,[255,0,0]),[70,320])
                pygame.display.flip()
def teach(name):
    pygame.time.set_timer(pygame.USEREVENT + 2,50)
    frame = 1
    page = 1
    screen.blit(pygame.image.load("assets/graphics/extra/animations/tutorials/%s/page%s/frame%s.png" % (name,page,frame)),[0,0])
    pygame.display.flip()
    screenup = True
    while screenup:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                playing = False
                visit = False
                screenup = False
                break
            if event.type == pygame.USEREVENT + 2:
                frame += 1
                try:
                    screen.blit(pygame.image.load("assets/graphics/extra/animations/tutorials/%s/page%s/frame%s.png" % (name,page,frame)),[0,0])
                except:
                    frame = 1
                    screen.blit(pygame.image.load("assets/graphics/extra/animations/tutorials/%s/page%s/frame%s.png" % (name,page,frame)),[0,0])
                pygame.display.flip()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                page += 1
                frame = 1
                try:
                    pygame.image.load("assets/graphics/extra/animations/tutorials/%s/page%s/frame1.png" % (name,page))
                except:
                    return
                screen.blit(pygame.image.load("assets/graphics/extra/animations/tutorials/%s/page%s/frame%s.png" % (name,page,frame)),[0,0])
                pygame.display.flip()
            if event.type == pygame.MOUSEMOTION:
                mouseposition = event.pos[:]
        


enemylist = { "greengrobble":["greengrobble",20,5,0,2 * 3,10,"melee",1,[1,6],False],
              "greengrobbleking":["greengrobbleking",50,5,0,2 * 3,10,"melee",1,[7,12],True],
              "redgrobble":["redgrobble",30,6,0,2 * 3,10,"melee",1,[3,8],False],
              "redgrobbleking":["redgrobbleking",60,6,0,2 * 3,10,"melee",1,[9,14],True],
              "yellowgrobble":["yellowgrobble",40,7,0,2 * 3,10,"melee",1,[5,10],False],
              "yellowgrobbleking":["yellowgrobbleking",80,7,0,2 * 3,10,"melee",1,[13,18],True],
              "blackgrobble":["blackgrobble",50,8,0,2 * 3,10,"melee",1,[7,12],False],
              "blackgrobbleking":["blackgrobbleking",100,8,0,2 * 3,10,"melee",1,[17,22],True],
              
              "deadtree":["deadtree",40,6,4,7,10,"melee",2,[2,7],False],
              "deadtreeking":["deadtreeking",100,7,4,7,10,"melee",2,[10,15],True],
              "mushroom":["mushroom",50,6,1,8,10,"range",2,[2,7],False],
              "mushroomking":["mushroomking",120,10,1,8,10,"range",2,[10,15],True],
              "tree":["tree",40,8,10,7,10,"melee",2,[5,10],False],
              "treeking":["treeking",100,10,10,7,10,"melee",2,[16,21],True],
              "treeworm":["treeworm",70,8,2,17,10,"melee",2,[5,10],False],
              "soldiertreeworm":["soldiertreeworm",50,14,2,8,10,"melee",2,[8,13],False],
              "treewormqueen":["treewormqueen",300,16,2,20,10,"range",2,[30,35],True],
              
              "swampdeadtree":["deadtree",60,10,4,7,10,"melee",3,[1,6],False],
              "swampdeadtreeking":["deadtreeking",300,13,4,20,10,"melee",3,[7,12],True],
              "swampmushroom":["mushroom",75,7,1,8,10,"range",3,[1,6],False],
              "swampmushroomking":["mushroomking",240,12,1,20,10,"range",3,[7,12],True],
              "poisonmushroom":["poisonmushroom",70,9,1,8,10,"range",3,[1,6],False],
              "poisonmushroomking":["poisonmushroomking",300,14,1,20,10,"range",3,[2,7],True],
              "snail":["snail",50,20,10,5,10,"melee",3,[1,6],False],
              "snailking":["snailking",100,20,10,5,10,"melee",3,[25,30],True],
              "mudmonster":["mudmonster",100,16,0,7,10,"melee",3,[1,6],False],
              "mudking":["mudking",200,16,0,6,10,"melee",3,[3,8],True],
              "mudmound":["mudmound",1500,16,0,12,10,"range",3,[10,15],True,[240,100]],
              "mudhill":["mudmound",2000,16,0,16,10,"range",3,[12,17],True,[240,100]],
              
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
              "bandit":["bandit",50,18,15,15,10,"melee",5,[15,20],False],
              "banditking":["banditking",2000,25,15,22,10,"melee",5,[300,305],True],
              "statue":["statue",520,21,18,16,10,"melee",5,[21,26],False,[120,200]],
              "statueking":["statueking",1120,26,18,16,10,"melee",5,[36,41],True,[120,200]],
              "mummy":["mummy",85,18,9,14,10,"melee",5,[18,23],False],
              "pharoh":["pharoh",520,37,9,22,10,"melee",5,[27,32],True],
              "sphinx":["sphinx",1950,45,19,23,10,"range",5,[36,41],True,[90,150]],
              
              "hermitcrab":["hermitcrab",60,27,10,15,10,"melee",6,[7,12],False],
              "hermitcrabking":["hermitcrabking",400,36,10,15,10,"melee",6,[65,70],True],
              "crab":["crab",90,21,7,20,10,"melee",6,[10,15],False],
              "crabking":["crabking",600,27,7,20,10,"melee",6,[80,85],True],
              "seagull":["seagull",120,16,6,30,10,"melee",6,[13,18],False],
              "seagullking":["seagullking",800,20,6,30,10,"melee",6,[105,110],True],
              "sandmonster":["sandmonster",100,18,0,28,10,"melee",6,[11,16],False],
              "sandking":["sandking",800,42,0,28,10,"melee",6,[80,85],True,[120,120]],
              "sandguard":["sandguard",70,10,0,20,10,"melee",6,[7,12],False],
              "sandknight":["sandknight",2000,30,0,40,10,"melee",6,[200,205],True],
              "sandmazorov":["sandmazorov",4000,40,0,40,10,"range",6,[400,405],True,[150,120]],
              
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
              
              "evilplant":["evilplant",200,45,10,18,10,"melee",8,[30,35],False],
              "giantvine":["giantvine",700,56,10,18,10,"melee",8,[115,120],True],
              "muncher":["muncher",200,54,10,14,10,"melee",8,[30,35],False],
              "devourer":["devourer",800,80,10,14,10,"melee",8,[125,130],True],
              "spider":["spider",100,55,25,18,10,"melee",8,[20,25],False],
              "giantspider":["giantspider",2000,70,25,17,10,"melee",8,[515,520],True],
              "snake":["snake",240,30,4,22,10,"melee",8,[35,40],False],
              "snakeking":["snakeking",1000,75,4,12,10,"melee",8,[140,145],True],
              "tiger":["tiger",7000,60,10,30,10,"melee",8,[500,505],True,[100,100]],
              "templeguardian":["templeguardian",4000,120,0,24,10,"range",8,[1000,1005],True],
              "raptor":["raptor",400,80,18,22,10,"melee",8,[85,90],False],
              "tyrannosaurusrex":["tyrannosaurusrex",4000,160,10,17,10,"melee",8,[650,655],True,[120,200]],
              "pterodactyl":["pterodactyl",5000,85,12,55,10,"melee",8,[850,855],True],

              "bird":["bird",200,50,6,24,10,"melee",9,[47,52],False],
              "albatross":["albatross",1000,60,6,50,10,"melee",9,[195,200],True],
              "cloud":["cloud",300,40,0,20,10,"melee",9,[60,65],False],
              "giantcloud":["giantcloud",2000,100,0,24,10,"melee",9,[360,365],True,[120,200]],
              "fogspector":["fogspector",100,44,60,50,10,"melee",9,[120,125],False],
              "fogmonster":["fogmonster",1000,64,30,40,10,"melee",9,[310,315],True],
              "thundercloud":["thundercloud",300,60,0,15,10,"range",9,[60,65],False],
              "cumulonimbus":["cumulonimbus",6000,80,0,60,10,"range",9,[1070,1075],True,[120,200]],
              "eyeofthestorm":["eyeofthestorm",7000,70,0,50,10,"range",9,[1245,1250],True],
              "skydragon":["skydragon",5000,50,20,70,10,"range",9,[1245,1250],True,[90,150]],
              "skyserpent":["skyserpent",7000,70,0,50,10,"range",9,[1245,1250],True,[90,150]],
              "skyguard":["skyguard",100,50,14,25,10,"melee",9,[22,27],False],
              "skyknight":["skyknight",10000,55,14,50,10,"melee",9,[2230,2235],True],
              
              "stonemonster":["stonemonster",200,40,24,20,10,"melee",10,[50,55],False],
              "stoneking":["stoneking",1000,60,24,50,10,"melee",10,[225,230],True],
              "goat":["goat",240,30,12,34,10,"melee",10,[50,55],False],
              "mountainwolf":["mountainwolf",300,40,14,30,10,"melee",10,[60,65],False],
              "alpha":["alpha",3000,70,14,50,10,"melee",10,[555,560],True,[100,100]],
              "mountainlion":["mountainlion",4000,60,10,50,10,"melee",10,[685,690],True,[100,100]],
              "griffin":["griffin",5000,50,16,60,10,"melee",10,[955,960],True],
              "stonethrower":["stonethrower",500,100,20,10,10,"range",10,[100,105],False],
              "yeti":["yeti",3000,150,20,10,10,"melee",10,[615,620],True,[90,150]],
              "icemonster":["icemonster",200,32,24,20,10,"melee",10,[50,55],False],
              "icedragon":["icedragon",6000,60,20,50,10,"range",10,[1235,1240],True,[100,100]],
              "goldcrab":["goldcrab",420,40,0,20,10,"melee",10,[60,65],False],
              "goldbat":["goldbat",300,28,0,40,10,"melee",10,[50,55],False],
              "goldsnake":["goldsnake",360,60,0,10,10,"melee",10,[60,65],False],
              "hoarderdragon":["hoarderdragon",20000,70,22,45,10,"range",10,[3500,3505],True,[100,140]],
              "mountainbird":["mountainbird",25000,65,10,55,10,"melee",10,[4000,4005],True,[100,140]],
              
              "pyroclast":["pyroclast",240,45,18,25,10,"melee",11,[95,100],False],
              "pyroclastking":["pyroclastking",1200,75,12,60,10,"melee",11,[460,465],True],
              "babydragon":["babydragon",300,40,12,30,10,"range",11,[130,135],False],
              "dragon":["dragon",5000,70,14,70,10,"range",11,[1945,1950],True,[110,100]],
              "lavamonster":["lavamonster",180,50,5,20,10,"melee",11,[65,70],False],
              "lavaking":["lavaking",4000,80,5,50,10,"melee",11,[1415,1420],True],
              "lavaspider":["lavaspider",4000,70,18,60,10,"range",11,[1615,1620],True,[100,100]],
              "lavaseamonster":["lavaseamonster",6000,80,14,40,10,"range",11,[2300,2305],True,[160,140]],
              "phoenix":["phoenix",7000,70,10,70,10,"range",11,[2570,2575],True,[60,100]],
              "firedragon":["firedragon",6000,80,25,60,10,"range",11,[2640,2645],True,[120,110]],
              "fireguard":["fireguard",150,50,16,25,10,"melee",11,[65,70],False],
              "fireknight":["fireknight",20000,80,16,50,10,"melee",11,[7500,7505],True],
              
              "ghosttree":["ghosttree",300,60,22,20,10,"melee",12,[80,85],False],
              "raven":["raven",200,50,15,30,10,"melee",12,[90,95],False],
              "spiritmist":["spiritmist",2000,90,10,50,10,"melee",12,[660,665],True],
              "bigghost":["bigghost",3000,100,13,60,10,"melee",12,[1000,1005],True],
              "ghost":["ghost",350,70,10,22,10,"melee",12,[100,105],False],
              "shadowghost":["shadowghost",3000,100,24,60,10,"melee",12,[1150,1155],True],
              "specter":["specter",400,80,24,16,10,"melee",12,[170,175],False],
              "shadowspecter":["shadowspecter",8000,100,24,50,10,"melee",12,[3050,3055],True],
              "angryghost":["angryghost",200,100,10,20,10,"melee",12,[110,115],False],
              "phantom":["phantom",5000,100,15,60,10,"melee",12,[1695,1700],True,[80,100]],
              "angryphantom":["angryphantom",9000,120,15,60,10,"melee",12,[3050,3055],True,[80,100]],
              "frightfulphantom":["frightfulphantom",15000,140,15,60,10,"melee",12,[5095,5100],True,[80,100]],
              "shadowphantom":["shadowphantom",20000,150,15,60,10,"melee",12,[6795,6800],True,[80,100]],
              
              "darkguard":["darkguard",200,60,20,30,10,"melee",13,[100,105],False],
              "darkknight":["darkknight",20000,100,20,60,10,"melee",13,[8550,8555],True],
              "mazorov":["mazorov",30000,100,20,70,10,"range",13,[100000,100005],True,[150,120]]
}
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
panellawin = city("panellatowncrystal",0,[180,10030],[175,120],["Jason",0,None,None,None,None,None],
               [["bag",0,[510,310],[40,40],["bag"],False],
                ["map",0,[511,352],[40,40],["exit"],False],
                ["panellastore",0,[42,269],[150,100],["shop",[0,30,24,36,42,48,54,60]],False],
                ["foxcitizen3",0,[199,171],[40,75],["talk",["Our crystal is back!"]],False],
                ["foxcitizen4",0,[295,194],[40,75],["talk",["You saved the day!"]],True],
                ["oldfox",0,[312,309],[40,75],["talk",["Congratulations! You have","saved our village"]],True],
                ["panellahouse",0,[370,286],[150,100],["teach","combat"],False],
                ["bag",0,[510,310],[40,40],["bag"],False],
                ["map",0,[510,350],[40,40],["exit"],False]])
cities = [city("panellatown",0,[180,10030],[175,120],["Jason",0,None,None,None,None,None],
               [["bag",0,[510,310],[40,40],["bag"],False],
                ["map",0,[511,352],[40,40],["exit"],False],
                ["panellastore",0,[42,269],[150,100],["shop",[0,30,24,36,42,48,54,60]],False],
                ["foxcitizen1",0,[199,171],[40,75],["talk",["What will we ever do","without our crystal"]],False],
                ["foxcitizen2",0,[295,194],[40,75],["talk",["The hills around the city","are full of monsters"]],True],
                ["oldfox",0,[312,309],[40,75],["talk",["You must travel to Mazorov's","castle in the north to retrieve","our crystal"]],True],
                ["panellahouse",0,[370,286],[150,100],["teach","combat"],False],
                ["bag",0,[510,310],[40,40],["bag"],False],
                ["map",0,[511,352],[40,40],["exit"],False]]),
          city("serranavillage",13,[185,8714],[175,125],["Stella",6,None,None,None,None,None],
               [["bag",0,[510,310],[40,40],["bag"],False],
                ["map",0,[511,352],[40,40],["exit"],False],
                ["serranastore",0,[0,253],[179,129],["shop",[1,6,7,31,25,37,43,49,55,61]],False],
                ["deercitizen1",1,[218,177 - 25],[40,100],["quest",["I need some health herbs","Give herbs?"],66,1,["Thank You"],"money",30],False],
                ["deercitizen2",2,[316,111 - 25],[40,100],["quest",["I need a health potion","Give potion?"],68,1,["Thank You"],"item",8],False],
                ["deercitizen3",0,[470,76],[40,75],["talk",["There is a mountain range in the","north I do not know how you","will get past it"]],True],
                ["serranahouse",0,[319,216],[241,172],["teach","brewing"],False],
                ["bag",0,[510,310],[40,40],["bag"],False],
                ["map",0,[511,352],[40,40],["exit"],False]]),
          city("buhntacity",38,[70,6040],[220,165],["Marvin",12,None,None,None,None,None],
               [["bag",0,[510,310],[40,40],["bag"],False],
                ["map",0,[511,352],[40,40],["exit"],False],
                ["buhntastore",0,[0,272],[175,122],["shop",[2,8,12,13,32,26,38,44,50,56,62]],False],
                ["bullcitizen1",4,[191,130 - 30],[40,105],["quest",["I need a wide shield","Give shield?"],33,1,["Thank You"],"item",51],False],
                ["bullcitizen2",0,[186,221],[40,75],["talk",["In the North are some ancient ruins","but it is very dangerous to","go near them"]],False],
                ["bullcitizen3",0,[327,127],[40,75],["talk",["The route north is riddled with","bandits be careful"]],False],
                ["bullcitizen4",3,[331,225 - 30],[40,105],["quest",["I need some red spices","Give spices?"],101,1,["Thank You"],"money",40],False],
                ["buhntahouse",0,[385,269],[175,122],["teach","smithing"],False],
                ["bag",0,[510,310],[40,40],["bag"],False],
                ["map",0,[511,352],[40,40],["exit"],False]]),
          city("mavella",59,[114,4080],[300,190],["Luna",18,None,None,None,None,None],
               [["bag",0,[510,310],[40,40],["bag"],False],
                ["map",0,[511,352],[40,40],["exit"],False],
                ["mavellastore",0,[22,255],[118,94],["shop",[3,9,14,18,19,33,27,39,45,51,57,63,116,117,118,119,120,121,122,123,124,125]],False],
                ["birdcitizen2",5,[173,221 - 30],[40,105],["quest",["I need some yellow nector","Give nector?"],114,1,["Thank You"],"money",100],False],
                ["birdcitizen3",0,[300,182],[40,75],["talk",["The sea to the north is too","dangerous to navigate"]],True],
                ["birdcitizen4",6,[374,215 - 30],[40,105],["quest",["I need a pink gem","Give gem?"],115,1,["Thank You"],"money",250],True],
                ["mavellahouse",0,[451,242],[76,108],["teach","magic"],False],
                ["bag",0,[510,310],[40,40],["bag"],False],
                ["map",0,[511,352],[40,40],["exit"],False]])
          ]
positions = [
    [222,10065,"plain"],
    [244, 9948, 'plain'], [274, 9877, 'plain'], [270, 9785, 'plain'], [254, 9707, 'plain'], [310, 9643, 'plain'], [380, 9599, 'plain'], [392, 9503, 'plain'], [393, 9421, 'plain'],
    [401, 9243, 'plain'], [375, 9123, 'plain'], [346, 9030, 'plain'], [300, 8963, 'plain'],
    [227,8774,"plain"],
    [140, 8631, 'plain'], [93, 8511, 'plain'], [164, 8417, 'plain'], [278, 8435, 'plain'],
    [368, 8184, 'plain'], [267, 8123, 'plain'], [168, 8084, 'plain'], [115, 8032, 'plain'], [163, 7906, 'plain'], [263, 7880, 'plain'], [380, 7830, 'plain'], [388, 7745, 'plain'],
    [345, 7447, 'plain'], [222, 7393, 'plain'], [103, 7344, 'plain'], [15, 7221, 'plain'], [15, 7084, 'plain'], [22, 6978, 'plain'], [148, 6892, 'plain'], [340, 6910, 'plain'],
    [375, 6609, 'plain'], [305, 6490, 'plain'], [210, 6413, 'plain'], [130, 6307, 'plain'],
    [138,6136,"plain"],
    [114, 5954, 'plain'], [99, 5833, 'plain'], [98, 5765, 'plain'], [42, 5651, 'plain'],
    [14, 5464, 'plain'], [48, 5418, 'plain'], [85, 5461, 'plain'], [111, 5415, 'plain'], [159, 5452, 'plain'], [223, 5452, 'plain'], [285, 5448, 'plain'], [355, 5483, 'plain'],
    [303, 5095, 'ocean'], [167, 5014, 'ocean'], [43, 4894, 'ocean'], [247, 4778, 'ocean'], [391, 4527, 'ocean'], [262, 4506, 'ocean'], [136, 4473, 'ocean'], [22,4443, 'ocean'],
    [216,4245,"plain"],
    [161, 3983, 'plain'], [63, 3924, 'plain'], [153, 3867, 'plain'], [266, 3854, 'plain'], [368, 3837, 'plain'], [368, 3774, 'plain'], [300, 3659, 'plain'], [206, 3620, 'plain'],
    [207, 3461, 'sky'], [99, 3403, 'sky'], [48, 3304, 'sky'], [181, 3199, 'sky'], [397, 3035, 'sky'], [312, 2905, 'sky'], [250, 2825, 'sky'], [231, 2718, 'sky'],
    [270, 2386, 'plain'], [228, 2274, 'plain'], [167, 2191, 'plain'], [88, 2125, 'plain'], [4, 2034, 'plain'], [100, 1998, 'plain'], [173, 1955, 'plain'], [269, 1953, 'plain'],
    [216, 1861, 'plain'], [334, 1789, 'plain'], [415, 1679, 'plain'], [353, 1661, 'plain'], [211, 1667, 'plain'], [19, 1585, 'plain'], [36, 1476, 'plain'], [242, 1566, 'plain'],
    [233, 1258, 'plain'], [114, 1198, 'plain'], [9, 1125, 'plain'], [136, 1059, 'plain'], [303, 1032, 'plain'], [448, 972, 'plain'], [338, 903, 'plain'], [226, 893, 'plain'],
    [231, 662, 'plain'], [73, 541, 'plain'], [394, 517, 'plain'], [234, 467, 'plain'],
    [500,100, 'void']
]
clippoints = {
    }
def target(enemies,decor,hud):
    global mouseposition,mousedown
    huddle = [hud]
    read = True
    targeted = None
    while read:
        animatebattle(enemies,decor,hud)
        screen.blit(pygame.image.load("assets/graphics/extra/targetbuttonon.png"),[410,287])
        screen.blit(pygame.image.load("assets/graphics/extra/target.png"),[mouseposition[0] - 25,mouseposition[1] - 25])
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                read = False
                running = False
                playing = False
                battle = False
                return
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                p = 0
                entvol = 0
                if battleside:
                    for d in enemies:
                        entvol += d.size[0] / 2
                    for d in enemies:
                        #560 - 10 - 120 - 30 * len(enemies) + p
                        if mouseposition[0] > 430 - entvol - p and mouseposition[0] < 430 + d.size[0] - entvol - p and mouseposition[1] > 230 - d.size[1] and mouseposition[1] < 230:
                            targeted = d
                            read = False
                            break
                        p -= d.size[0]
                else:
                    for d in enemies:
                        entvol += d.size[0] / 2
                    for d in enemies:
                        #(10 + 120) + 30 * len(team) - p - size
                        if mouseposition[0] > 130 + entvol - p - d.size[0] and mouseposition[0] < 130 + entvol - p and mouseposition[1] > 230 - d.size[1] and mouseposition[1] < 230:
                            targeted = d
                            read = False
                            break
                        p += d.size[0]
                if not read:
                    break
                if mouseposition[0] > 430 and mouseposition[0] < 550 and mouseposition[1] > 295 and mouseposition[1] < 330:
                    read = False
                    break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_4:
                    if len(enemies) > 0 + 3*battleside:
                        targeted = enemies[0 + 3*battleside]
                        read = False
                        break
                elif event.key == pygame.K_3:
                    if len(enemies) > 1 + 1*battleside:
                        targeted = enemies[1 + 1*battleside]
                        read = False
                        break
                elif event.key == pygame.K_2:
                    if len(enemies) > 2 - 1*battleside:
                        targeted = enemies[2 - 1*battleside]
                        read = False
                        break
                elif event.key == pygame.K_1:
                    if len(enemies) > 3 - 3*battleside:
                        targeted = enemies[3 - 3*battleside]
                        read = False
                        break
                elif event.key == pygame.K_f:
                    read = False
                    break
            elif event.type == pygame.MOUSEMOTION:
                mouseposition = event.pos[:]
                p = 0
                entvol = 0
                if battleside:
                    for d in enemies:
                        entvol += d.size[0] / 2
                    for d in enemies:
                        #560 - 10 - 120 - 30 * len(enemies) + p
                        if mouseposition[0] > 430 - entvol - p and mouseposition[0] < 430 + d.size[0] - entvol - p and mouseposition[1] > 230 - d.size[1] and mouseposition[1] < 230:
                            hud = d
                            break
                        p -= d.size[0]
                else:
                    for d in enemies:
                        entvol += d.size[0] / 2
                    for d in enemies:
                        #(10 + 120) + 30 * len(team) - p - size
                        if mouseposition[0] > 130 + entvol - p - d.size[0] and mouseposition[0] < 130 + entvol - p and mouseposition[1] > 230 - d.size[1] and mouseposition[1] < 230:
                            hud = d
                            break
                        p += d.size[0]
                animatebattle(enemies,decor,hud)
                screen.blit(pygame.image.load("assets/graphics/extra/targetbuttonon.png"),[410,287])
                screen.blit(pygame.image.load("assets/graphics/extra/target.png"),[mouseposition[0] - 25,mouseposition[1] - 25])
                pygame.display.flip()
    return targeted
def moveteam(team,enemies,decor,hud):
    global mouseposition,mousedown
    read = True
    while read:
        animatebattle(enemies,decor,hud)
        screen.blit(pygame.image.load("assets/graphics/extra/movebuttonon.png"),[410,260])
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                read = False
                running = False
                playing = False
                battle = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if mouseposition[0] > 410 and mouseposition[0] < 530 and mouseposition[1] > 260 and mouseposition[1] < 286:
                    read = False
                    break
                if battleside:
                    p = -60
                    ins = 0
                    for d in team:
                            #10 + 120 + 30 * len(team) - 60 + p
                        if mouseposition[0] > 130 + 30 * len(team) + p and mouseposition[0] < 190 + 30 * len(team) + p and mouseposition[1] > 130 and mouseposition[1] < 230:
                            teama = hud
                            teamb = d
                            ta = team.index(hud)
                            tb = team.index(d)
                            team[ta] = teamb
                            team[tb] = teama
                            #team.remove(hud)
                            #team.insert(ins,hud)
                            read = False
                            break
                        ins += 1
                        p -= 60
                else:
                    p = 0
                    ins = 0
                    for d in team:
                            #10 + 120 + 30 * len(team) - 60 + p
                        if mouseposition[0] > 430 - 30 * len(team) + p and mouseposition[0] < 490 - 30 * len(team) + p and mouseposition[1] > 130 and mouseposition[1] < 230:
                            teama = hud
                            teamb = d
                            ta = team.index(hud)
                            tb = team.index(d)
                            team[ta] = teamb
                            team[tb] = teama
                            #team.remove(hud)
                            #team.insert(ins,hud)
                            read = False
                            break
                        ins += 1
                        p += 60
                if not read:
                    break
                animatebattle(enemies,decor,hud)
                screen.blit(pygame.image.load("assets/graphics/extra/movebuttonon.png"),[410,260])
                pygame.display.flip()
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    if len(team) > 0 + 3*battleside:
                        d = team[0 + 3*battleside]
                        teama = hud
                        teamb = d
                        ta = team.index(hud)
                        tb = team.index(d)
                        team[ta] = teamb
                        team[tb] = teama
                        #team.remove(hud)
                        #team.insert(ins,hud)
                        read = False
                        break
                elif event.key == pygame.K_2:
                    if len(team) > 1 + 1*battleside:
                        d = team[1 + 1*battleside]
                        teama = hud
                        teamb = d
                        ta = team.index(hud)
                        tb = team.index(d)
                        team[ta] = teamb
                        team[tb] = teama
                        #team.remove(hud)
                        #team.insert(ins,hud)
                        read = False
                        break
                elif event.key == pygame.K_3:
                    if len(team) > 2 - 1*battleside:
                        d = team[2 - 1*battleside]
                        teama = hud
                        teamb = d
                        ta = team.index(hud)
                        tb = team.index(d)
                        team[ta] = teamb
                        team[tb] = teama
                        #team.remove(hud)
                        #team.insert(ins,hud)
                        read = False
                        break
                elif event.key == pygame.K_4:
                    if len(team) > 3 - 3*battleside:
                        d = team[3 - 3*battleside]
                        teama = hud
                        teamb = d
                        ta = team.index(hud)
                        tb = team.index(d)
                        team[ta] = teamb
                        team[tb] = teama
                        #team.remove(hud)
                        #team.insert(ins,hud)
                        read = False
                        break
                elif event.key == pygame.K_r:
                    read = False
                    break
            elif event.type == pygame.MOUSEMOTION:
                mouseposition = event.pos[:]
                animatebattle(enemies,decor,hud)
                screen.blit(pygame.image.load("assets/graphics/extra/movebuttonon.png"),[410,260])
                pygame.display.flip()
    for e in enemies:
        if team[0].health > 0:
            e.target = team[0]
        elif team[1].health > 0:
            e.target = team[1]
        elif team[2].health > 0:
            e.target = team[2]
        else:
            e.target = team[3]
    return team
def battledelay(hud,team,enemies,decor,event):
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        p = 0
        entvol = 0
        for dt in enemies:
            entvol += dt.size[0] / 2
        for dt in enemies:#560 - 10 - 120 - 30 * len(enemies) + p #(10 + 120) + 30 * len(team) - p - size
            if ((battleside and mouseposition[0] > 430 - entvol + p and mouseposition[0] < 430 + dt.size[0] - entvol + p) or (not battleside and mouseposition[0] > 130 + entvol - p - dt.size[0] and mouseposition[0] < 130 + entvol - p)) and mouseposition[1] > 230 - dt.size[1] and mouseposition[1] < 230:
                hud = dt
                break
            p += dt.size[0]
        p = 0
        for dt in team:#10 + 120 + 30 * len(team) - 60 + p #10 + 120 + 30 * len(team) - 60 + p
            if ((battleside and mouseposition[0] > 130 + 30 * len(team) - p - 60 and mouseposition[0] < 190 + 30 * len(team) - p - 60) or (not battleside and mouseposition[0] > 430 - 30 * len(team) + p and mouseposition[0] < 490 - 30 * len(team) + p)) and mouseposition[1] > 130 and mouseposition[1] < 230:
                hud = dt
                break
            p += 60
        if mouseposition[0] > 410 and mouseposition[0] < 530 and mouseposition[1] > 260 and mouseposition[1] < 286 and hud.good:
            moveteam(team,enemies,decor,hud)
        elif mouseposition[0] > 410 and mouseposition[0] < 530 and mouseposition[1] > 287 and mouseposition[1] < 313 and hud.good:
            tard = target(enemies,decor,hud)
            if tard != None:
                hud.target = tard
        elif mouseposition[0] > 450 and mouseposition[0] < 490 and mouseposition[1] > 343 and mouseposition[1] < 383 and hud.good:
            if hud.carry != None:
                hud,team,enemies = hud.carry.use(hud,team,enemies,decor)
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_1:
            if len(team) > 0 + 3*battleside:
                hud = team[0 + 3*battleside]
        elif event.key == pygame.K_2:
            if len(team) > 1 + 1*battleside:
                hud = team[1 + 1*battleside]
        elif event.key == pygame.K_3:
            if len(team) > 2 - 1*battleside:
                hud = team[2 - 1*battleside]
        elif event.key == pygame.K_4:
            if len(team) > 3 - 3*battleside:
                hud = team[3 - 3*battleside]
        elif event.key == pygame.K_f:
            if hud.good:
                tard = target(enemies,decor,hud)
                if tard != None:
                    hud.target = tard
        elif event.key == pygame.K_r:
            if hud.good:
                moveteam(team,enemies,decor,hud)
        elif event.key == pygame.K_v:
            if hud.good:
                if hud.carry != None:
                    hud,team,enemies = hud.carry.use(hud,team,enemies,decor)
    return hud,team,enemies
def battle(enemies,decor):
    global money,mouseposition,mousedown,battlespeed,team
    hud = team[0]
    battle = True
    tick = 0
    for d in team:
        d.target = enemies[0]
    for d in enemies:
        d.target = team[0]
    for d in enemies:
        if d.target.health == 0:
            for e in team:
                if e.health > 0:
                    d.target = e
                    break
    #pygame.time.set_timer(pygame.USEREVENT + 3,10)
    if battlespeed == 1:
        pygame.time.set_timer(pygame.USEREVENT + 3,20)
    elif battlespeed == 2:
        pygame.time.set_timer(pygame.USEREVENT + 3,10)
    elif battlespeed == 3:
        pygame.time.set_timer(pygame.USEREVENT + 3,5)
    elif battlespeed == 4:
        pygame.time.set_timer(pygame.USEREVENT + 3,2)
    #pygame.time.set_timer(pygame.USEREVENT + 2 + 2,10)
    #pygame.time.set_timer(pygame.USEREVENT + 2 + 3,5)
    #pygame.time.set_timer(pygame.USEREVENT + 2 + 4,2)
    #animatebattle(enemies,decor,hud)
    pygame.display.flip()
    while battle:
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT + 3:
                tick += 1
                """if battlespeed == 1:
                    if tick == 20:
                        tick = 0
                elif battlespeed == 2:
                    if tick == 10:
                        tick = 0
                elif battlespeed == 3:
                    if tick == 5:
                        tick = 0
                elif battlespeed == 4:
                    if tick == 2:
                        tick = 0"""
                if tick == 10:
                    tick = 0
                if True:
                    for d in team:
                        if d.health > 0:
                            #d.charge += 1
                            #if d.charge == d.delay:
                            if random.randint(0,6000) < d.speed + d.effect[1] * (d.effect[0] == "swiftness"):
                                dtarget = d.target
                                if not random.randint(1,2000) < 100 * dtarget.luck / (float(d.luck + d.effect[1] * (d.effect[0] == "charm"))):
                                    if random.randint(1,2000) < 100 * (float(d.luck + d.effect[1] * (d.effect[0] == "charm")) / dtarget.luck):
                                        if doanimations:
                                            #animation critical
                                            enemyp,selfp = animatebattle(enemies,decor,hud,[d,dtarget])
                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/enemies/%s.png" % dtarget.name),not battleside,False),[enemyp[0],230 - dtarget.size[1]])
                                            if d.weapon == None or d.weapon.itemtype == "sword" or d.weapon.itemtype == "hammer":
                                                if d.weapon != None:
                                                    playsound("%scritical" % d.weapon.name)
                                                else:
                                                    playsound("fistcritical")
                                                selfp = animatebattle(enemies,decor,hud,[d])[0]
                                                yp = 20
                                                while yp < 140:
                                                    selfp = animatebattle(enemies,decor,hud,[d])[0]
                                                    if d.shield != None:
                                                        screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % d.shield.name),not battleside,False),[enemyp[0] + 60 - 120 * battleside - 10 * (not battleside),yp])
                                                    screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sattack.png" % d.name),not battleside,False),[enemyp[0] + 60 - 120 * battleside,yp])
                                                    if d.armor != None:
                                                        screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sattack.png" % d.armor.name),not battleside,False),[enemyp[0] + 60 - 120 * battleside,yp])
                                                    if d.weapon != None:
                                                        screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sattack.png" % d.weapon.name),not battleside,False),[enemyp[0] + 60 - 120 * battleside - 10 * (not battleside),yp])
                                                    screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sattackarm.png" % d.name),not battleside,False),[enemyp[0] + 60 - 120 * battleside,yp])
                                                    pygame.display.flip()
                                                    #hud,team,enemies = battledelay(20,hud,team,enemies,decor)
                                                    #yp += 10
                                                    for event in pygame.event.get():
                                                        if event.type == pygame.USEREVENT + 2 + 1:
                                                            yp += 4
                                                            if yp % 20 == 0 or yp > 140:
                                                                selfp = animatebattle(enemies,decor,hud,[d])[0]
                                                                if d.shield != None:
                                                                    screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % d.shield.name),not battleside,False),[enemyp[0] + 60 - 120 * battleside - 10 * (not battleside),yp])
                                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sattack.png" % d.name),not battleside,False),[enemyp[0] + 60 - 120 * battleside,yp])
                                                                if d.armor != None:
                                                                    screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sattack.png" % d.armor.name),not battleside,False),[enemyp[0] + 60 - 120 * battleside,yp])
                                                                if d.weapon != None:
                                                                    screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sattack.png" % d.weapon.name),not battleside,False),[enemyp[0] + 60 - 120 * battleside - 10 * (not battleside),yp])
                                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sattackarm.png" % d.name),not battleside,False),[enemyp[0] + 60 - 120 * battleside,yp])
                                                                pygame.display.flip()
                                                                if yp > 140:
                                                                    break
                                                        if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1) or event.type == pygame.KEYDOWN:
                                                            hud,team,enemies = battledelay(hud,team,enemies,decor,event)
                                                            selfp = animatebattle(enemies,decor,hud,[d])[0]
                                                            if d.shield != None:
                                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % d.shield.name),not battleside,False),[enemyp[0] + 60 - 120 * battleside - 10 * (not battleside),yp])
                                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sattack.png" % d.name),not battleside,False),[enemyp[0] + 60 - 120 * battleside,yp])
                                                            if d.armor != None:
                                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sattack.png" % d.armor.name),not battleside,False),[enemyp[0] + 60 - 120 * battleside,yp])
                                                            if d.weapon != None:
                                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sattack.png" % d.weapon.name),not battleside,False),[enemyp[0] + 60 - 120 * battleside - 10 * (not battleside),yp])
                                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sattackarm.png" % d.name),not battleside,False),[enemyp[0] + 60 - 120 * battleside,yp])
                                                            pygame.display.flip()
                                                        if event.type == pygame.MOUSEMOTION:
                                                            mouseposition = event.pos[:]
                                                            selfp = animatebattle(enemies,decor,hud,[d])[0]
                                                            if d.shield != None:
                                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % d.shield.name),not battleside,False),[enemyp[0] + 60 - 120 * battleside - 10 * (not battleside),yp])
                                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sattack.png" % d.name),not battleside,False),[enemyp[0] + 60 - 120 * battleside,yp])
                                                            if d.armor != None:
                                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sattack.png" % d.armor.name),not battleside,False),[enemyp[0] + 60 - 120 * battleside,yp])
                                                            if d.weapon != None:
                                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sattack.png" % d.weapon.name),not battleside,False),[enemyp[0] + 60 - 120 * battleside - 10 * (not battleside),yp])
                                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sattackarm.png" % d.name),not battleside,False),[enemyp[0] + 60 - 120 * battleside,yp])
                                                            pygame.display.flip()
                                            ####
                                            # bows and wands to be critical
                                            #
                                            ####
                                            elif d.weapon.itemtype == "bow" or d.weapon.itemtype == "wand":
                                                animatebattle(enemies,decor,hud)
                                                if d.weapon.itemtype == "bow":
                                                    playsound("%s" % d.weapon.name)
                                                    if d.shield != None:
                                                        screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % d.shield.name),not battleside,False),[selfp[0] - 10 * (not battleside),130])
                                                    screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sshoot.png" % d.name),not battleside,False),[selfp[0],130])
                                                    if d.armor != None:
                                                        screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sshoot.png" % d.armor.name),not battleside,False),[selfp[0],130])
                                                    if d.weapon != None:
                                                        screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sattack.png" % d.weapon.name),not battleside,False),[selfp[0] - 10 * (not battleside),130])
                                                    screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sshootarm.png" % d.name),not battleside,False),[selfp[0],130])
                                                    pygame.display.flip()
                                                    #arrow animation
                                                elif d.weapon.itemtype == "wand":
                                                    playsound("%s" % d.weapon.name)
                                                    if d.shield != None:
                                                        screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % d.shield.name),not battleside,False),[selfp[0] - 10 * (not battleside),130]) 
                                                    screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % d.name),not battleside,False),[selfp[0],130])
                                                    if d.armor != None:
                                                        screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % d.armor.name),not battleside,False),[selfp[0],130])
                                                    if d.weapon != None:
                                                        screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sattack.png" % d.weapon.name),not battleside,False),[selfp[0] - 10 * (not battleside),130])
                                                    screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sarm.png" % d.name),not battleside,False),[selfp[0],130])
                                                    pygame.display.flip()
                                                    #spell animation
                                                pygame.display.flip()
                                                yp = 0
                                                while yp < 5:
                                                    for event in pygame.event.get():
                                                        if event.type == pygame.USEREVENT + 2 + 1:
                                                            yp += 1
                                                        if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1) or event.type == pygame.KEYDOWN:
                                                            hud,team,enemies = battledelay(hud,team,enemies,decor,event)
                                                            animatebattle(enemies,decor,hud)
                                                            if d.weapon.itemtype == "bow":
                                                                playsound("%s" % d.weapon.name)
                                                                if d.shield != None:
                                                                    screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % d.shield.name),not battleside,False),[selfp[0] - 10 * (not battleside),130])
                                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sshoot.png" % d.name),not battleside,False),[selfp[0],130])
                                                                if d.armor != None:
                                                                    screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sshoot.png" % d.armor.name),not battleside,False),[selfp[0],130])
                                                                if d.weapon != None:
                                                                    screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sattack.png" % d.weapon.name),not battleside,False),[selfp[0] - 10 * (not battleside),130])
                                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sshootarm.png" % d.name),not battleside,False),[selfp[0],130])
                                                                pygame.display.flip()
                                                                #arrow animation
                                                            elif d.weapon.itemtype == "wand":
                                                                playsound("%s" % d.weapon.name)
                                                                if d.shield != None:
                                                                    screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % d.shield.name),not battleside,False),[selfp[0] - 10 * (not battleside),130]) 
                                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % d.name),not battleside,False),[selfp[0],130])
                                                                if d.armor != None:
                                                                    screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % d.armor.name),not battleside,False),[selfp[0],130])
                                                                if d.weapon != None:
                                                                    screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sattack.png" % d.weapon.name),not battleside,False),[selfp[0] - 10 * (not battleside),130])
                                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sarm.png" % d.name),not battleside,False),[selfp[0],130])
                                                                pygame.display.flip()
                                                                #spell animation
                                                            pygame.display.flip()
                                                        if event.type == pygame.MOUSEMOTION:
                                                            mouseposition = event.pos[:]
                                                            animatebattle(enemies,decor,hud)
                                                            if d.weapon.itemtype == "bow":
                                                                playsound("%s" % d.weapon.name)
                                                                if d.shield != None:
                                                                    screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % d.shield.name),not battleside,False),[selfp[0] - 10 * (not battleside),130])
                                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sshoot.png" % d.name),not battleside,False),[selfp[0],130])
                                                                if d.armor != None:
                                                                    screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sshoot.png" % d.armor.name),not battleside,False),[selfp[0],130])
                                                                if d.weapon != None:
                                                                    screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sattack.png" % d.weapon.name),not battleside,False),[selfp[0] - 10 * (not battleside),130])
                                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sshootarm.png" % d.name),not battleside,False),[selfp[0],130])
                                                                pygame.display.flip()
                                                                #arrow animation
                                                            elif d.weapon.itemtype == "wand":
                                                                playsound("%s" % d.weapon.name)
                                                                if d.shield != None:
                                                                    screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % d.shield.name),not battleside,False),[selfp[0] - 10 * (not battleside),130]) 
                                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % d.name),not battleside,False),[selfp[0],130])
                                                                if d.armor != None:
                                                                    screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % d.armor.name),not battleside,False),[selfp[0],130])
                                                                if d.weapon != None:
                                                                    screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sattack.png" % d.weapon.name),not battleside,False),[selfp[0] - 10 * (not battleside),130])
                                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sarm.png" % d.name),not battleside,False),[selfp[0],130])
                                                                pygame.display.flip()
                                                                #spell animation
                                                            pygame.display.flip()
                                                arrpos = [selfp[0] - 37 + 74 * battleside,130]
                                                animatebattle(enemies,decor,hud)
                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sarrowcritical.png" % d.weapon.name),not battleside,False),arrpos)
                                                pygame.display.flip()
                                                yp = 0
                                                while (battleside and arrpos[0] + 30 < enemyp[0]) or ((not battleside) and arrpos[0] > enemyp[0] + dtarget.size[0]):#abs((arrpos[0] + 30 * battleside) - enemyp[0]) > 30:
                                                    for event in pygame.event.get():
                                                        if not abs(arrpos[0] - enemyp[0]) > 30:
                                                            break
                                                        if event.type == pygame.USEREVENT + 2 + 1:
                                                            yp += 1
                                                            if yp == 5:
                                                                arrpos[0] += -15 + 30 * battleside
                                                                animatebattle(enemies,decor,hud)
                                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sarrowcritical.png" % d.weapon.name),not battleside,False),arrpos)
                                                                pygame.display.flip()
                                                                yp = 0
                                                        if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1) or event.type == pygame.KEYDOWN:
                                                            hud,team,enemies = battledelay(hud,team,enemies,decor,event)
                                                            animatebattle(enemies,decor,hud)
                                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sarrowcritical.png" % d.weapon.name),not battleside,False),arrpos)
                                                            pygame.display.flip()
                                                        if event.type == pygame.MOUSEMOTION:
                                                            mouseposition = event.pos[:]
                                                            animatebattle(enemies,decor,hud)
                                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sarrowcritical.png" % d.weapon.name),not battleside,False),arrpos)
                                                            pygame.display.flip()
                                                playsound("%shit" % d.weapon.name)
                                        if 2 * (d.attack + d.effect[1] * (d.effect[0] == "strength")) - (dtarget.defence + dtarget.effect[1] * (dtarget.effect[0] == "resistance")) > 0:
                                            dtarget.health -= 2 * (d.attack + d.effect[1] * (d.effect[0] == "strength")) - (dtarget.defence + dtarget.effect[1] * (dtarget.effect[0] == "resistance"))
                                        else:
                                            dtarget.health -= 1
                                        if dtarget.health < 0:
                                            dtarget.health = 0
                                        animatebattle(enemies,decor,hud)
                                        pygame.display.flip()
                                        yp = 0
                                        while yp < 10:
                                            for event in pygame.event.get():
                                                if event.type == pygame.USEREVENT + 2 + 1:
                                                    yp += 1
                                                if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1) or event.type == pygame.KEYDOWN:
                                                    hud,team,enemies = battledelay(hud,team,enemies,decor,event)
                                                    animatebattle(enemies,decor,hud)
                                                    pygame.display.flip()
                                                if event.type == pygame.MOUSEMOTION:
                                                    mouseposition = event.pos[:]
                                                    animatebattle(enemies,decor,hud)
                                                    pygame.display.flip()
                                    else:
                                        if doanimations:
                                            enemyp,selfp = animatebattle(enemies,decor,hud,[d,dtarget])
                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/enemies/%s.png" % dtarget.name),not battleside,False),[enemyp[0],230 - dtarget.size[1]])
                                            if  d.weapon == None or d.weapon.itemtype == "sword" or d.weapon.itemtype == "hammer":
                                                if d.weapon != None:
                                                    playsound("%shit" % d.weapon.name)
                                                else:
                                                    playsound("fisthit")
                                                if d.shield != None:
                                                    screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % d.shield.name),not battleside,False),[enemyp[0] + 60 - 120 * battleside - 10 * (not battleside),130])
                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sattack.png" % d.name),not battleside,False),[enemyp[0] + 60 - 120 * battleside,130])
                                                if d.armor != None:
                                                    screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sattack.png" % d.armor.name),not battleside,False),[enemyp[0] + 60 - 120 * battleside,130])
                                                if d.weapon != None:
                                                    screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sattack.png" % d.weapon.name),not battleside,False),[enemyp[0] + 60 - 120 * battleside - 10 * (not battleside),130])
                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sattackarm.png" % d.name),not battleside,False),[enemyp[0] + 60 - 120 * battleside,130])
                                                pygame.display.flip()
                                                yp = 0
                                                while yp < 20:
                                                    for event in pygame.event.get():
                                                        if event.type == pygame.USEREVENT + 2 + 1:
                                                            yp += 1
                                                        if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1) or event.type == pygame.KEYDOWN:
                                                            hud,team,enemies = battledelay(hud,team,enemies,decor,event)
                                                            enemyp,selfp = animatebattle(enemies,decor,hud,[d,dtarget])
                                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/enemies/%s.png" % dtarget.name),not battleside,False),[enemyp[0],230 - dtarget.size[1]])
                                                            if d.shield != None:
                                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % d.shield.name),not battleside,False),[enemyp[0] + 60 - 120 * battleside - 10 * (not battleside),130])
                                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sattack.png" % d.name),not battleside,False),[enemyp[0] + 60 - 120 * battleside,130])
                                                            if d.armor != None:
                                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sattack.png" % d.armor.name),not battleside,False),[enemyp[0] + 60 - 120 * battleside,130])
                                                            if d.weapon != None:
                                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sattack.png" % d.weapon.name),not battleside,False),[enemyp[0] + 60 - 120 * battleside - 10 * (not battleside),130])
                                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sattackarm.png" % d.name),not battleside,False),[enemyp[0] + 60 - 120 * battleside,130])
                                                            pygame.display.flip()
                                                        if event.type == pygame.MOUSEMOTION:
                                                            mouseposition = event.pos[:]
                                                            enemyp,selfp = animatebattle(enemies,decor,hud,[d,dtarget])
                                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/enemies/%s.png" % dtarget.name),not battleside,False),[enemyp[0],230 - dtarget.size[1]])
                                                            if d.shield != None:
                                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % d.shield.name),not battleside,False),[enemyp[0] + 60 - 120 * battleside - 10 * (not battleside),130])
                                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sattack.png" % d.name),not battleside,False),[enemyp[0] + 60 - 120 * battleside,130])
                                                            if d.armor != None:
                                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sattack.png" % d.armor.name),not battleside,False),[enemyp[0] + 60 - 120 * battleside,130])
                                                            if d.weapon != None:
                                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sattack.png" % d.weapon.name),not battleside,False),[enemyp[0] + 60 - 120 * battleside - 10 * (not battleside),130])
                                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sattackarm.png" % d.name),not battleside,False),[enemyp[0] + 60 - 120 * battleside,130])
                                                            pygame.display.flip()
                                            elif d.weapon.itemtype == "bow" or d.weapon.itemtype == "wand":
                                                animatebattle(enemies,decor,hud)
                                                if d.weapon.itemtype == "bow":
                                                    playsound("%s" % d.weapon.name)
                                                    if d.shield != None:
                                                        screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % d.shield.name),not battleside,False),[selfp[0] - 10 * (not battleside),130])
                                                    screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sshoot.png" % d.name),not battleside,False),[selfp[0],130])
                                                    if d.armor != None:
                                                        screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sshoot.png" % d.armor.name),not battleside,False),[selfp[0],130])
                                                    if d.weapon != None:
                                                        screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sattack.png" % d.weapon.name),not battleside,False),[selfp[0] - 10 * (not battleside),130])
                                                    screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sshootarm.png" % d.name),not battleside,False),[selfp[0],130])
                                                    pygame.display.flip()
                                                    #arrow animation
                                                elif d.weapon.itemtype == "wand":
                                                    playsound("%s" % d.weapon.name)
                                                    if d.shield != None:
                                                        screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % d.shield.name),not battleside,False),[selfp[0] - 10 * (not battleside),130]) 
                                                    screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % d.name),not battleside,False),[selfp[0],130])
                                                    if d.armor != None:
                                                        screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % d.armor.name),not battleside,False),[selfp[0],130])
                                                    if d.weapon != None:
                                                        screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sattack.png" % d.weapon.name),not battleside,False),[selfp[0] - 10 * (not battleside),130])
                                                    screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sarm.png" % d.name),not battleside,False),[selfp[0],130])
                                                    pygame.display.flip()
                                                    #spell animation
                                                pygame.display.flip()
                                                yp = 0
                                                while yp < 5:
                                                    for event in pygame.event.get():
                                                        if event.type == pygame.USEREVENT + 2 + 1:
                                                            yp += 1
                                                        if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1) or event.type == pygame.KEYDOWN:
                                                            hud,team,enemies = battledelay(hud,team,enemies,decor,event)
                                                            animatebattle(enemies,decor,hud)
                                                            if d.weapon.itemtype == "bow":
                                                                playsound("%s" % d.weapon.name)
                                                                if d.shield != None:
                                                                    screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % d.shield.name),not battleside,False),[selfp[0] - 10 * (not battleside),130])
                                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sshoot.png" % d.name),not battleside,False),[selfp[0],130])
                                                                if d.armor != None:
                                                                    screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sshoot.png" % d.armor.name),not battleside,False),[selfp[0],130])
                                                                if d.weapon != None:
                                                                    screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sattack.png" % d.weapon.name),not battleside,False),[selfp[0] - 10 * (not battleside),130])
                                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sshootarm.png" % d.name),not battleside,False),[selfp[0],130])
                                                                pygame.display.flip()
                                                                #arrow animation
                                                            elif d.weapon.itemtype == "wand":
                                                                playsound("%s" % d.weapon.name)
                                                                if d.shield != None:
                                                                    screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % d.shield.name),not battleside,False),[selfp[0] - 10 * (not battleside),130]) 
                                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % d.name),not battleside,False),[selfp[0],130])
                                                                if d.armor != None:
                                                                    screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % d.armor.name),not battleside,False),[selfp[0],130])
                                                                if d.weapon != None:
                                                                    screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sattack.png" % d.weapon.name),not battleside,False),[selfp[0] - 10 * (not battleside),130])
                                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sarm.png" % d.name),not battleside,False),[selfp[0],130])
                                                                pygame.display.flip()
                                                                #spell animation
                                                            pygame.display.flip()
                                                        if event.type == pygame.MOUSEMOTION:
                                                            mouseposition = event.pos[:]
                                                            animatebattle(enemies,decor,hud)
                                                            if d.weapon.itemtype == "bow":
                                                                playsound("%s" % d.weapon.name)
                                                                if d.shield != None:
                                                                    screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % d.shield.name),not battleside,False),[selfp[0] - 10 * (not battleside),130])
                                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sshoot.png" % d.name),not battleside,False),[selfp[0],130])
                                                                if d.armor != None:
                                                                    screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sshoot.png" % d.armor.name),not battleside,False),[selfp[0],130])
                                                                if d.weapon != None:
                                                                    screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sattack.png" % d.weapon.name),not battleside,False),[selfp[0] - 10 * (not battleside),130])
                                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sshootarm.png" % d.name),not battleside,False),[selfp[0],130])
                                                                pygame.display.flip()
                                                                #arrow animation
                                                            elif d.weapon.itemtype == "wand":
                                                                playsound("%s" % d.weapon.name)
                                                                if d.shield != None:
                                                                    screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % d.shield.name),not battleside,False),[selfp[0] - 10 * (not battleside),130]) 
                                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % d.name),not battleside,False),[selfp[0],130])
                                                                if d.armor != None:
                                                                    screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % d.armor.name),not battleside,False),[selfp[0],130])
                                                                if d.weapon != None:
                                                                    screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sattack.png" % d.weapon.name),not battleside,False),[selfp[0] - 10 * (not battleside),130])
                                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sarm.png" % d.name),not battleside,False),[selfp[0],130])
                                                                pygame.display.flip()
                                                                #spell animation
                                                            pygame.display.flip()
                                                #if d.weapon.itemtype == "bow":
                                                 #   arrpos = [selfp[0] - 37 + 74 * battleside,130 + 39]
                                                #elif d.weapon.itemtype == "wand":
                                                arrpos = [selfp[0] - 37 + 74 * battleside,130]
                                                animatebattle(enemies,decor,hud)
                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sarrow.png" % d.weapon.name),not battleside,False),arrpos)
                                                pygame.display.flip()
                                                yp = 0
                                                while (battleside and arrpos[0] + 30 < enemyp[0]) or ((not battleside) and arrpos[0] > enemyp[0] + dtarget.size[0]):#abs(arrpos[0] - enemyp[0]) > 30:
                                                    #arrpos[0] += -15 + 30 * battleside
                                                    #animatebattle(enemies,decor,hud)
                                                    #screen.blit(pygame.image.load("assets/graphics/characters/%sarrow.png" % d.weapon.name),arrpos)
                                                    #pygame.display.flip()
                                                    for event in pygame.event.get():
                                                        if event.type == pygame.USEREVENT + 2 + 1:
                                                            yp += 1
                                                            if yp == 5:
                                                                arrpos[0] += -15 + 30 * battleside
                                                                animatebattle(enemies,decor,hud)
                                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sarrow.png" % d.weapon.name),not battleside,False),arrpos)
                                                                pygame.display.flip()
                                                                if not abs(arrpos[0] - enemyp[0]) > 30:
                                                                    break
                                                                yp = 0
                                                        if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1) or event.type == pygame.KEYDOWN:
                                                            hud,team,enemies = battledelay(hud,team,enemies,decor,event)
                                                            animatebattle(enemies,decor,hud)
                                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sarrow.png" % d.weapon.name),not battleside,False),arrpos)
                                                            pygame.display.flip()
                                                        if event.type == pygame.MOUSEMOTION:
                                                            mouseposition = event.pos[:]
                                                            animatebattle(enemies,decor,hud)
                                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sarrow.png" % d.weapon.name),not battleside,False),arrpos)
                                                            pygame.display.flip()
                                        if (d.attack + d.effect[1] * (d.effect[0] == "strength")) - (dtarget.defence + dtarget.effect[1] * (dtarget.effect[0] == "resistance")) > 0:
                                            dtarget.health -= (d.attack + d.effect[1] * (d.effect[0] == "strength")) - (dtarget.defence + dtarget.effect[1] * (dtarget.effect[0] == "resistance"))
                                        else:
                                            dtarget.health -= 1
                                        if dtarget.health < 0:
                                            dtarget.health = 0
                                        animatebattle(enemies,decor,hud)
                                        pygame.display.flip()
                                        yp = 0
                                        while yp < 10:
                                            for event in pygame.event.get():
                                                if event.type == pygame.USEREVENT + 2 + 1:
                                                    yp += 1
                                                if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1) or event.type == pygame.KEYDOWN:
                                                    hud,team,enemies = battledelay(hud,team,enemies,decor,event)
                                                    animatebattle(enemies,decor,hud)
                                                    pygame.display.flip()
                                                if event.type == pygame.MOUSEMOTION:
                                                    mouseposition = event.pos[:]
                                                    animatebattle(enemies,decor,hud)
                                                    pygame.display.flip()
                                        #animation attack
                                    if dtarget.health <= 0:
                                        drop = []
                                        if random.randint(0,100) < d.luck + d.effect[1] * (d.effect[0] == "charm"):
                                            if dtarget.level == 2:
                                                drop = [96]
                                            elif dtarget.level == 3:
                                                drop = [random.choice([96,100])]
                                            elif dtarget.level == 4:
                                                drop = [random.choice([96,100,104])]
                                            elif dtarget.level == 5:
                                                drop = [random.choice([96,96,97,100,100,101,104,104,105,108,108,109])]
                                            elif dtarget.level == 6:
                                                drop = [random.choice([96,97,97,100,101,101,104,105,105,108,109,109,112,113,113])]
                                            elif dtarget.level == 7:
                                                drop = [random.choice([97,101,105,109,113])]
                                            elif dtarget.level == 8:
                                                drop = [random.choice([97,98,101,102,105,106,109,110,113,114])]
                                            elif dtarget.level == 9:
                                                drop = [random.choice([98,102,106,110,114])]
                                            elif dtarget.level == 10:
                                                drop = [random.choice([98,98,99,102,102,103,106,106,107,110,110,111,114,114,115])]
                                            elif dtarget.level == 11:
                                                drop = [random.choice([98,99,99,102,103,103,106,107,107,110,111,111,114,115,115])]
                                            elif dtarget.level == 12 or dtarget.level == 13:
                                                drop = [random.choice([99,103,107,111,115])]
                                        if doanimations:
                                            playsound("poof")
                                            for f in range(3):
                                                animatebattle(enemies,decor,hud)
                                                screen.blit(pygame.transform.scale(pygame.image.load("assets/graphics/extra/poof%s.png" % f),dtarget.size),enemyp)
                                                pygame.display.flip()
                                                yp = 0
                                                while yp < 20:
                                                    for event in pygame.event.get():
                                                        if event.type == pygame.USEREVENT + 2 + 1:
                                                            yp += 1
                                                        if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1) or event.type == pygame.KEYDOWN:
                                                            hud,team,enemies = battledelay(hud,team,enemies,decor,event)
                                                            animatebattle(enemies,decor,hud)
                                                            screen.blit(pygame.transform.scale(pygame.image.load("assets/graphics/extra/poof%s.png" % f),dtarget.size),enemyp)
                                                            pygame.display.flip()
                                                        if event.type == pygame.MOUSEMOTION:
                                                            mouseposition = event.pos[:]
                                                            animatebattle(enemies,decor,hud)
                                                            screen.blit(pygame.transform.scale(pygame.image.load("assets/graphics/extra/poof%s.png" % f),dtarget.size),enemyp)
                                                            pygame.display.flip()
                                                #rewards
                                            enemyp = animatebattle(enemies,decor,hud,[dtarget])[0]
                                            if drop != []:
                                                drpos = random.randint(0,20)
                                                screen.blit(pygame.image.load("assets/graphics/items/%s.png" % items[drop[0]].name),[enemyp[0] + drpos,190])
                                            pygame.display.flip()
                                            yp = 0
                                            while yp < 10:
                                                for event in pygame.event.get():
                                                    if event.type == pygame.USEREVENT + 2 + 1:
                                                        yp += 1
                                                    if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1) or event.type == pygame.KEYDOWN:
                                                        hud,team,enemies = battledelay(hud,team,enemies,decor,event)
                                                        enemyp = animatebattle(enemies,decor,hud,[dtarget])[0]
                                                        if drop != []:
                                                            screen.blit(pygame.image.load("assets/graphics/items/%s.png" % items[drop[0]].name),[enemyp[0] + drpos,190])
                                                        pygame.display.flip()
                                                    if event.type == pygame.MOUSEMOTION:
                                                        mouseposition = event.pos[:]
                                                        enemyp = animatebattle(enemies,decor,hud,[dtarget])[0]
                                                        if drop != []:
                                                            screen.blit(pygame.image.load("assets/graphics/items/%s.png" % items[drop[0]].name),[enemyp[0] + drpos,190])
                                                        pygame.display.flip()
                                            enemyp = animatebattle(enemies,decor,hud,[dtarget])[0]
                                            pygame.display.flip()
                                        enemies.remove(dtarget)
                                        animatebattle(enemies,decor,hud)
                                        pygame.display.flip()
                                        if drop != []:
                                            if None in inventory[:15 * len(team)]:
                                                inventory[inventory.index(None)] = drop[0]
                                        money += random.randint(dtarget.loot[0],dtarget.loot[1])
                                        #
                                        #REWARDS
                                        #
                                        #animation
                                        if len(enemies) == 0:
                                            return True
                                        else:
                                            for e in team:
                                                if not e.target in enemies:
                                                    e.target = enemies[0]
                                else:
                                    #dodge
                                    #animation
                                    if doanimations:
                                        
                                        enemyp,selfp = animatebattle(enemies,decor,hud,[d,dtarget])
                                        if d.weapon.itemtype == "sword" or d.weapon.itemtype == "hammer":
                                            screen.blit(pygame.transform.flip(dtarget.texture,not battleside,False),[enemyp[0] - 40 + 80 * battleside,230 - dtarget.size[1]])
                                            if d.shield != None:
                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % d.shield.name),not battleside,False),[enemyp[0] + 60 - 120 * battleside - 10 * (not battleside),130])
                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sattack.png" % d.name),not battleside,False),[enemyp[0] + 60 - 120 * battleside,130])
                                            if d.armor != None:
                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sattack.png" % d.armor.name),not battleside,False),[enemyp[0] + 60 - 120 * battleside,130])
                                            if d.weapon != None:
                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sattack.png" % d.weapon.name),not battleside,False),[enemyp[0] + 60 - 120 * battleside - 10 * (not battleside),130])
                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sattackarm.png" % d.name),not battleside,False),[enemyp[0] + 60 - 120 * battleside,130])
                                            pygame.display.flip()
                                            yp = 0
                                            while yp < 20:
                                                for event in pygame.event.get():
                                                    if event.type == pygame.USEREVENT + 2 + 1:
                                                        yp += 1
                                                    if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1) or event.type == pygame.KEYDOWN:
                                                        hud,team,enemies = battledelay(hud,team,enemies,decor,event)
                                                        enemyp,selfp = animatebattle(enemies,decor,hud,[d,dtarget])
                                                        screen.blit(pygame.transform.flip(dtarget.texture,not battleside,False),[enemyp[0] - 40 + 80 * battleside,230 - dtarget.size[1]])
                                                        if d.shield != None:
                                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % d.shield.name),not battleside,False),[enemyp[0] + 60 - 120 * battleside - 10 * (not battleside),130])
                                                        screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sattack.png" % d.name),not battleside,False),[enemyp[0] + 60 - 120 * battleside,130])
                                                        if d.armor != None:
                                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sattack.png" % d.armor.name),not battleside,False),[enemyp[0] + 60 - 120 * battleside,130])
                                                        if d.weapon != None:
                                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sattack.png" % d.weapon.name),not battleside,False),[enemyp[0] + 60 - 120 * battleside - 10 * (not battleside),130])
                                                        screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sattackarm.png" % d.name),not battleside,False),[enemyp[0] + 60 - 120 * battleside,130])
                                                        pygame.display.flip()
                                                    if event.type == pygame.MOUSEMOTION:
                                                        mouseposition = event.pos[:]
                                                        enemyp,selfp = animatebattle(enemies,decor,hud,[d,dtarget])
                                                        screen.blit(pygame.transform.flip(dtarget.texture,not battleside,False),[enemyp[0] - 40 + 80 * battleside,230 - dtarget.size[1]])
                                                        if d.shield != None:
                                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % d.shield.name),not battleside,False),[enemyp[0] + 60 - 120 * battleside - 10 * (not battleside),130])
                                                        screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sattack.png" % d.name),not battleside,False),[enemyp[0] + 60 - 120 * battleside,130])
                                                        if d.armor != None:
                                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sattack.png" % d.armor.name),not battleside,False),[enemyp[0] + 60 - 120 * battleside,130])
                                                        if d.weapon != None:
                                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sattack.png" % d.weapon.name),not battleside,False),[enemyp[0] + 60 - 120 * battleside - 10 * (not battleside),130])
                                                        screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sattackarm.png" % d.name),not battleside,False),[enemyp[0] + 60 - 120 * battleside,130])
                                                        pygame.display.flip()
                                        elif d.weapon.itemtype == "bow" or d.weapon.itemtype == "wand":
                                            animatebattle(enemies,decor,hud)
                                            if d.weapon.itemtype == "bow":
                                                playsound("%s" % d.weapon.name)
                                                if d.shield != None:
                                                    screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % d.shield.name),not battleside,False),[selfp[0] - 10 * (not battleside),130])
                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sshoot.png" % d.name),not battleside,False),[selfp[0],130])
                                                if d.armor != None:
                                                    screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sshoot.png" % d.armor.name),not battleside,False),[selfp[0],130])
                                                if d.weapon != None:
                                                    screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sattack.png" % d.weapon.name),not battleside,False),[selfp[0] - 10 * (not battleside),130])
                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sshootarm.png" % d.name),not battleside,False),[selfp[0],130])
                                                pygame.display.flip()
                                                #arrow animation
                                            elif d.weapon.itemtype == "wand":
                                                playsound("%s" % d.weapon.name)
                                                if d.shield != None:
                                                    screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % d.shield.name),not battleside,False),[selfp[0] - 10 * (not battleside),130]) 
                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % d.name),not battleside,False),[selfp[0],130])
                                                if d.armor != None:
                                                    screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % d.armor.name),not battleside,False),[selfp[0],130])
                                                if d.weapon != None:
                                                    screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sattack.png" % d.weapon.name),not battleside,False),[selfp[0] - 10 * (not battleside),130])
                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sarm.png" % d.name),not battleside,False),[selfp[0],130])
                                                pygame.display.flip()
                                                #spell animation
                                            pygame.display.flip()
                                            yp = 0
                                            while yp < 5:
                                                for event in pygame.event.get():
                                                    if event.type == pygame.USEREVENT + 2 + 1:
                                                        yp += 1
                                                    if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1) or event.type == pygame.KEYDOWN:
                                                        hud,team,enemies = battledelay(hud,team,enemies,decor,event)
                                                        animatebattle(enemies,decor,hud)
                                                        if d.weapon.itemtype == "bow":
                                                            playsound("%s" % d.weapon.name)
                                                            if d.shield != None:
                                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % d.shield.name),not battleside,False),[selfp[0] - 10 * (not battleside),130])
                                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sshoot.png" % d.name),not battleside,False),[selfp[0],130])
                                                            if d.armor != None:
                                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sshoot.png" % d.armor.name),not battleside,False),[selfp[0],130])
                                                            if d.weapon != None:
                                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sattack.png" % d.weapon.name),not battleside,False),[selfp[0] - 10 * (not battleside),130])
                                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sshootarm.png" % d.name),not battleside,False),[selfp[0],130])
                                                            pygame.display.flip()
                                                            #arrow animation
                                                        elif d.weapon.itemtype == "wand":
                                                            playsound("%s" % d.weapon.name)
                                                            if d.shield != None:
                                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % d.shield.name),not battleside,False),[selfp[0] - 10 * (not battleside),130]) 
                                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % d.name),not battleside,False),[selfp[0],130])
                                                            if d.armor != None:
                                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % d.armor.name),not battleside,False),[selfp[0],130])
                                                            if d.weapon != None:
                                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sattack.png" % d.weapon.name),not battleside,False),[selfp[0] - 10 * (not battleside),130])
                                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sarm.png" % d.name),not battleside,False),[selfp[0],130])
                                                            pygame.display.flip()
                                                            #spell animation
                                                        pygame.display.flip()
                                                    if event.type == pygame.MOUSEMOTION:
                                                        mouseposition = event.pos[:]
                                                        animatebattle(enemies,decor,hud)
                                                        if d.weapon.itemtype == "bow":
                                                            playsound("%s" % d.weapon.name)
                                                            if d.shield != None:
                                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % d.shield.name),not battleside,False),[selfp[0] - 10 * (not battleside),130])
                                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sshoot.png" % d.name),not battleside,False),[selfp[0],130])
                                                            if d.armor != None:
                                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sshoot.png" % d.armor.name),not battleside,False),[selfp[0],130])
                                                            if d.weapon != None:
                                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sattack.png" % d.weapon.name),not battleside,False),[selfp[0] - 10 * (not battleside),130])
                                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sshootarm.png" % d.name),not battleside,False),[selfp[0],130])
                                                            pygame.display.flip()
                                                            #arrow animation
                                                        elif d.weapon.itemtype == "wand":
                                                            playsound("%s" % d.weapon.name)
                                                            if d.shield != None:
                                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % d.shield.name),not battleside,False),[selfp[0] - 10 * (not battleside),130]) 
                                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % d.name),not battleside,False),[selfp[0],130])
                                                            if d.armor != None:
                                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % d.armor.name),not battleside,False),[selfp[0],130])
                                                            if d.weapon != None:
                                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sattack.png" % d.weapon.name),not battleside,False),[selfp[0] - 10 * (not battleside),130])
                                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sarm.png" % d.name),not battleside,False),[selfp[0],130])
                                                            pygame.display.flip()
                                                            #spell animation
                                                        pygame.display.flip()
                                            #if d.weapon.itemtype == "bow":
                                             #   arrpos = [selfp[0] - 37 + 74 * battleside,130 + 39]
                                            #elif d.weapon.itemtype == "wand":
                                            arrpos = [selfp[0] - 37 + 74 * battleside,130]
                                            yp = 0
                                            while arrpos[0] > -60 and arrpos[0] < 560:
                                                for event in pygame.event.get():
                                                    if event.type == pygame.USEREVENT + 2 + 1:
                                                        yp += 1
                                                        if yp == 5:
                                                            arrpos[0] += -15 + 30 * battleside
                                                            enemyp = animatebattle(enemies,decor,hud,[dtarget])[0]
                                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/enemies/%s.png" % dtarget.name),not battleside,False),[enemyp[0] - 40 + 80 * battleside,230 - dtarget.size[1]])
                                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sarrow.png" % d.weapon.name),not battleside,False),arrpos)
                                                            pygame.display.flip()
                                                            yp = 0
                                                            if arrpos[0] > -60 and arrpos[0] < 560:
                                                                break
                                                    if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1) or event.type == pygame.KEYDOWN:
                                                        hud,team,enemies = battledelay(hud,team,enemies,decor,event)
                                                        enemyp = animatebattle(enemies,decor,hud,[dtarget])[0]
                                                        screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/enemies/%s.png" % dtarget.name),not battleside,False),[enemyp[0] - 40 + 80 * battleside,230 - dtarget.size[1]])
                                                        screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sarrow.png" % d.weapon.name),not battleside,False),arrpos)
                                                        pygame.display.flip()
                                                    if event.type == pygame.MOUSEMOTION:
                                                        mouseposition = event.pos[:]
                                                        enemyp = animatebattle(enemies,decor,hud,[dtarget])[0]
                                                        screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/enemies/%s.png" % dtarget.name),not battleside,False),[enemyp[0] - 40 + 80 * battleside,230 - dtarget.size[1]])
                                                        screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sarrow.png" % d.weapon.name),not battleside,False),arrpos)
                                                        pygame.display.flip()
                                    animatebattle(enemies,decor,hud)
                                    pygame.display.flip()
                                    yp = 0
                                    while yp < 10:
                                        for event in pygame.event.get():
                                            if event.type == pygame.USEREVENT + 2 + 1:
                                                yp += 1
                                            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1) or event.type == pygame.KEYDOWN:
                                                hud,team,enemies = battledelay(hud,team,enemies,decor,event)
                                                animatebattle(enemies,decor,hud)
                                                pygame.display.flip()
                                            if event.type == pygame.MOUSEMOTION:
                                                mouseposition = event.pos[:]
                                                animatebattle(enemies,decor,hud)
                                                pygame.display.flip()
                                d.charge = 0
                            if d.effect[0] != None:
                                d.effect[2] -= 1
                                if d.effect[2] == 0:
                                    if d.effect[0] == "swiftness":
                                        d.delay = int(6000 / (d.speed + d.effect[1] * (d.effect[0] == "swiftness")))
                                    d.effect = [None,0,0]
                    for d in enemies:
                        if not d.effect[0] == "frozen" and d.health > 0:
                            #d.charge += 1
                            #if d.charge == d.delay:
                            if random.randint(0,6000) < d.speed + d.effect[1] * (d.effect[0] == "swiftness"):
                                dtarget = d.target
                                if not random.randint(1,2000) < 100 * ((dtarget.luck + dtarget.effect[1] * (dtarget.effect[0] == "charm")) / float(d.luck)):
                                    if random.randint(1,2000) < 100 * (float(d.luck) / (dtarget.luck + dtarget.effect[1] * (dtarget.effect[0] == "charm"))):
                                        if doanimations:#checkpoint
                                            #critical animation
                                            selfp,enemyp = animatebattle(enemies,decor,hud,[d,dtarget])
                                            if dtarget.shield != None:
                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % dtarget.shield.name),not battleside,False),[enemyp[0] - 10 * (not battleside),130])
                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % dtarget.name),not battleside,False),[enemyp[0],130])
                                            if dtarget.armor != None:
                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % dtarget.armor.name),not battleside,False),[enemyp[0],130])
                                            if dtarget.weapon != None:
                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % dtarget.weapon.name),not battleside,False),[enemyp[0] - 10 * (not battleside),130])
                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sarm.png" % dtarget.name),not battleside,False),[enemyp[0],130])
                                            if d.attacktype == "melee":
                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/enemies/%sattackcritical.png" % d.name),not battleside,False),[enemyp[0] - 60 + 120 * battleside,230 - d.size[1]])
                                                pygame.display.flip()
                                                yp = 0
                                                while yp < 20:
                                                    for event in pygame.event.get():
                                                        if event.type == pygame.USEREVENT + 2 + 1:
                                                            yp += 1
                                                        if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1) or event.type == pygame.KEYDOWN:
                                                            hud,team,enemies = battledelay(hud,team,enemies,decor,event)
                                                            animatebattle(enemies,decor,hud,[d])
                                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/enemies/%sattackcritical.png" % d.name),not battleside,False),[enemyp[0] - 60 + 120 * battleside,230 - d.size[1]])
                                                            pygame.display.flip()
                                                        if event.type == pygame.MOUSEMOTION:
                                                            mouseposition = event.pos[:]
                                                            animatebattle(enemies,decor,hud,[d])
                                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/enemies/%sattackcritical.png" % d.name),not battleside,False),[enemyp[0] - 60 + 120 * battleside,230 - d.size[1]])
                                                            pygame.display.flip()
                                            elif d.attacktype == "range":
                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/enemies/%sattackcritical.png" % d.name),not battleside,False),[selfp[0],230 - d.size[1]])
                                                #arrow animation
                                                arrpos = [selfp[0] + 37 - 74 * battleside,130]
                                                #while arrpos[0] < enemyp[0]:
                                                while ((not battleside) and arrpos[0] + 30 < enemyp[0]) or (battleside and arrpos[0] > enemyp[0] + 60):#abs(arrpos[0] - enemyp[0]) > 30:
                                                    for event in pygame.event.get():
                                                        if not abs(arrpos[0] - enemyp[0]) > 30:
                                                            break
                                                        if event.type == pygame.USEREVENT + 2 + 1:
                                                            arrpos[0] -= -10 + 20 * battleside
                                                            animatebattle(enemies,decor,hud)
                                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/enemies/%sattackcritical.png" % d.name),not battleside,False),arrpos)
                                                            pygame.display.flip()
                                                        if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1) or event.type == pygame.KEYDOWN:
                                                            hud,team,enemies = battledelay(hud,team,enemies,decor,event)
                                                            animatebattle(enemies,decor,hud)
                                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/enemies/%sattackcritical.png" % d.name),not battleside,False),arrpos)
                                                            pygame.display.flip()
                                                        if event.type == pygame.MOUSEMOTION:
                                                            mouseposition = event.pos[:]
                                                            animatebattle(enemies,decor,hud)
                                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/enemies/%sattackcritical.png" % d.name),not battleside,False),arrpos)
                                                            pygame.display.flip()
                                        if 2 * (d.attack + d.effect[1] * (d.effect[0] == "strength")) - (dtarget.defence + dtarget.effect[1] * (dtarget.effect[0] == "resistance")) > 0:
                                            dtarget.health -= 2 * (d.attack + d.effect[1] * (d.effect[0] == "strength")) - (dtarget.defence + dtarget.effect[1] * (dtarget.effect[0] == "resistance"))
                                        else:
                                            dtarget.health -= 1
                                        if dtarget.health < 0:
                                            dtarget.health = 0
                                        animatebattle(enemies,decor,hud)
                                        pygame.display.flip()
                                        yp = 0
                                        while yp < 10:
                                            for event in pygame.event.get():
                                                if event.type == pygame.USEREVENT + 2 + 1:
                                                    yp += 1
                                                if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1) or event.type == pygame.KEYDOWN:
                                                    hud,team,enemies = battledelay(hud,team,enemies,decor,event)
                                                    animatebattle(enemies,decor,hud)
                                                    pygame.display.flip()
                                                if event.type == pygame.MOUSEMOTION:
                                                    mouseposition = event.pos[:]
                                                    animatebattle(enemies,decor,hud)
                                                    pygame.display.flip()
                                    else:
                                        if doanimations:
                                            selfp,enemyp = animatebattle(enemies,decor,hud,[d,dtarget])
                                            if dtarget.shield != None:
                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % dtarget.shield.name),not battleside,False),[enemyp[0] - 10 * (not battleside),130])
                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % dtarget.name),not battleside,False),[enemyp[0],130])
                                            if dtarget.armor != None:
                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % dtarget.armor.name),not battleside,False),[enemyp[0],130])
                                            if dtarget.weapon != None:
                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % dtarget.weapon.name),not battleside,False),[enemyp[0] - 10 * (not battleside),130])
                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sarm.png" % dtarget.name),not battleside,False),[enemyp[0],130])
                                            if d.attacktype == "melee":
                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/enemies/%sattack.png" % d.name),not battleside,False),[enemyp[0] - 60 + 120 * battleside,230 - d.size[1]])
                                                pygame.display.flip()
                                                yp = 0
                                                while yp < 20:
                                                    for event in pygame.event.get():
                                                        if event.type == pygame.USEREVENT + 2 + 1:
                                                            yp += 1
                                                        if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1) or event.type == pygame.KEYDOWN:
                                                            hud,team,enemies = battledelay(hud,team,enemies,decor,event)
                                                            animatebattle(enemies,decor,hud,[d])
                                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/enemies/%sattack.png" % d.name),not battleside,False),[enemyp[0] - 60 + 120 * battleside,230 - d.size[1]])
                                                            pygame.display.flip()
                                                        if event.type == pygame.MOUSEMOTION:
                                                            mouseposition = event.pos[:]
                                                            animatebattle(enemies,decor,hud,[d])
                                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/enemies/%sattack.png" % d.name),not battleside,False),[enemyp[0] - 60 + 120 * battleside,230 - d.size[1]])
                                                            pygame.display.flip()
                                            elif d.attacktype == "range":
                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/enemies/%sattack.png" % d.name),not battleside,False),[selfp[0],230 - d.size[1]])
                                                #arrow animation
                                                arrpos = [selfp[0] + 37 - 74 * battleside,130]
                                                while ((not battleside) and arrpos[0] + 30 < enemyp[0]) or (battleside and arrpos[0] > enemyp[0] + 60):#abs(arrpos[0] - enemyp[0]) > 30:
                                                    for event in pygame.event.get():
                                                        if not abs(arrpos[0] - enemyp[0]) > 30:
                                                            break
                                                        if event.type == pygame.USEREVENT + 2 + 1:
                                                            arrpos[0] -= -10 + 20 * battleside
                                                            animatebattle(enemies,decor,hud)
                                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/enemies/%sattack.png" % d.name),not battleside,False),arrpos)
                                                            pygame.display.flip()
                                                        if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1) or event.type == pygame.KEYDOWN:
                                                            hud,team,enemies = battledelay(hud,team,enemies,decor,event)
                                                            animatebattle(enemies,decor,hud)
                                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/enemies/%sattack.png" % d.name),not battleside,False),arrpos)
                                                            pygame.display.flip()
                                                        if event.type == pygame.MOUSEMOTION:
                                                            mouseposition = event.pos[:]
                                                            animatebattle(enemies,decor,hud)
                                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/enemies/%sattack.png" % d.name),not battleside,False),arrpos)
                                                            pygame.display.flip()
                                        if (d.attack + d.effect[1] * (d.effect[0] == "strength")) - (dtarget.defence + dtarget.effect[1] * (dtarget.effect[0] == "resistance")) > 0:
                                            dtarget.health -= (d.attack + d.effect[1] * (d.effect[0] == "strength")) - (dtarget.defence + dtarget.effect[1] * (dtarget.effect[0] == "resistance"))
                                        else:
                                            dtarget.health -= 1
                                        if dtarget.health < 0:
                                            dtarget.health = 0
                                        animatebattle(enemies,decor,hud)
                                        pygame.display.flip()
                                        yp = 0
                                        while yp < 10:
                                            for event in pygame.event.get():
                                                if event.type == pygame.USEREVENT + 2 + 1:
                                                    yp += 1
                                                if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1) or event.type == pygame.KEYDOWN:
                                                    hud,team,enemies = battledelay(hud,team,enemies,decor,event)
                                                    animatebattle(enemies,decor,hud)
                                                    pygame.display.flip()
                                                if event.type == pygame.MOUSEMOTION:
                                                    mouseposition = event.pos[:]
                                                    animatebattle(enemies,decor,hud)
                                                    pygame.display.flip()
                                    if dtarget.health <= 0:
                                        dtarget.health = 0
                                        d.charge = 0
                                        lose = True
                                        for e in team:
                                            if e.health > 0:
                                                lose = False
                                                break
                                        if lose:
                                            #Lose screen
                                            return False
                                        else:
                                            for d in enemies:
                                                if d.target.health == 0:
                                                    for e in team:
                                                        if e.health > 0:
                                                            d.target = e
                                                            break
                                        #character lose animation
                                        animatebattle(enemies,decor,hud)
                                        pygame.display.flip()
                                        yp = 0
                                        while yp < 25:
                                            for event in pygame.event.get():
                                                if event.type == pygame.USEREVENT + 2 + 1:
                                                    yp += 1
                                                if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1) or event.type == pygame.KEYDOWN:
                                                    hud,team,enemies = battledelay(hud,team,enemies,decor,event)
                                                    animatebattle(enemies,decor,hud)
                                                    pygame.display.flip()
                                                if event.type == pygame.MOUSEMOTION:
                                                    mouseposition = event.pos[:]
                                                    animatebattle(enemies,decor,hud)
                                                    pygame.display.flip()
                                        animatebattle(enemies,decor,hud)
                                        pygame.display.flip()
                                else:
                                    #dodge
                                    #animation
                                    if doanimations:
                                        selfp,enemyp = animatebattle(enemies,decor,hud,[d,dtarget])
                                        #screen.blit(pygame.image.load("assets/graphics/characters/%s.png" % dtarget.name),[enemyp[0],130])
                                        if d.attacktype == "melee":
                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/enemies/%sattack.png" % d.name),not battleside,False),[enemyp[0] - 60 + 120 * battleside,230 - d.size[1]])
                                            if dtarget.shield != None:
                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % dtarget.shield.name),not battleside,False),[enemyp[0] + 40 - 80 * battleside - 10 * (not battleside),130])
                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % dtarget.name),not battleside,False),[enemyp[0] + 40 - 80 * battleside,130])
                                            if dtarget.armor != None:
                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % dtarget.armor.name),not battleside,False),[enemyp[0] + 40 - 80 * battleside,130])
                                            if dtarget.weapon != None:
                                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % dtarget.weapon.name),not battleside,False),[enemyp[0] + 40 - 80 * battleside - 10 * (not battleside),130])
                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sarm.png" % dtarget.name),not battleside,False),[enemyp[0] + 40 - 80 * battleside,130])
                                            pygame.display.flip()
                                            yp = 0
                                            while yp < 20:
                                                for event in pygame.event.get():
                                                    if event.type == pygame.USEREVENT + 2 + 1:
                                                        yp += 1
                                                    if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1) or event.type == pygame.KEYDOWN:
                                                        hud,team,enemies = battledelay(hud,team,enemies,decor,event)
                                                        animatebattle(enemies,decor,hud,[d,dtarget])
                                                        screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/enemies/%sattack.png" % d.name),not battleside,False),[enemyp[0] - 60 + 120 * battleside,230 - d.size[1]])
                                                        if dtarget.shield != None:
                                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % dtarget.shield.name),not battleside,False),[enemyp[0] + 40 - 80 * battleside - 10 * (not battleside),130])
                                                        screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % dtarget.name),not battleside,False),[enemyp[0] + 40 - 80 * battleside,130])
                                                        if dtarget.armor != None:
                                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % dtarget.armor.name),not battleside,False),[enemyp[0] + 40 - 80 * battleside,130])
                                                        if dtarget.weapon != None:
                                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % dtarget.weapon.name),not battleside,False),[enemyp[0] + 40 - 80 * battleside - 10 * (not battleside),130])
                                                        screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sarm.png" % dtarget.name),not battleside,False),[enemyp[0] + 40 - 80 * battleside,130])
                                                        pygame.display.flip()
                                                    if event.type == pygame.MOUSEMOTION:
                                                        mouseposition = event.pos[:]
                                                        animatebattle(enemies,decor,hud,[d,dtarget])
                                                        screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/enemies/%sattack.png" % d.name),not battleside,False),[enemyp[0] - 60 + 120 * battleside,230 - d.size[1]])
                                                        if dtarget.shield != None:
                                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % dtarget.shield.name),not battleside,False),[enemyp[0] + 40 - 80 * battleside - 10 * (not battleside),130])
                                                        screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % dtarget.name),not battleside,False),[enemyp[0] + 40 - 80 * battleside,130])
                                                        if dtarget.armor != None:
                                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % dtarget.armor.name),not battleside,False),[enemyp[0] + 40 - 80 * battleside,130])
                                                        if dtarget.weapon != None:
                                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % dtarget.weapon.name),not battleside,False),[enemyp[0] + 40 - 80 * battleside - 10 * (not battleside),130])
                                                        screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sarm.png" % dtarget.name),not battleside,False),[enemyp[0] + 40 - 80 * battleside,130])
                                                        pygame.display.flip()
                                        elif d.attacktype == "range":
                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/enemies/%s.png" % d.name),not battleside,False),[selfp[0],130])
                                            #arrow animation
                                            #wand animation
                                            arrpos = [selfp[0] + 37 - 74 * battleside,130]
                                            while arrpos[0] > -60 and arrpos[0] < 560:
                                                for event in pygame.event.get():
                                                    if event.type == pygame.USEREVENT + 2 + 1:
                                                        arrpos[0] -= -10 + 20 * battleside
                                                        yp = 0
                                                        selfp,enemyp = animatebattle(enemies,decor,hud,[d,dtarget])
                                                        screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/enemies/%s.png" % d.name),not battleside,False),[selfp[0],230 - d.size[1]])
                                                        if dtarget.shield != None:
                                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % dtarget.shield.name),not battleside,False),[enemyp[0] + 40 - 80 * battleside - 10 * (not battleside),130])
                                                        screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % dtarget.name),not battleside,False),[enemyp[0] + 40 - 80 * battleside,130])
                                                        if dtarget.armor != None:
                                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % dtarget.armor.name),not battleside,False),[enemyp[0] + 40 - 80 * battleside,130])
                                                        if dtarget.weapon != None:
                                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % dtarget.weapon.name),not battleside,False),[enemyp[0] + 40 - 80 * battleside - 10 * (not battleside),130])
                                                        screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sarm.png" % dtarget.name),not battleside,False),[enemyp[0] + 40 - 80 * battleside,130])
                                                        screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/enemies/%sattack.png" % d.name),not battleside,False),arrpos)
                                                        pygame.display.flip()
                                                        if arrpos[0] > -60 and arrpos[0] < 560:
                                                            break
                                                    if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1) or event.type == pygame.KEYDOWN:
                                                        hud,team,enemies = battledelay(hud,team,enemies,decor,event)
                                                        selfp,enemyp = animatebattle(enemies,decor,hud,[d,dtarget])
                                                        screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/enemies/%s.png" % d.name),not battleside,False),[selfp[0],130])
                                                        if dtarget.shield != None:
                                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % dtarget.shield.name),not battleside,False),[enemyp[0] + 40 - 80 * battleside - 10 * (not battleside),130])
                                                        screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % dtarget.name),not battleside,False),[enemyp[0] + 40 - 80 * battleside,130])
                                                        if dtarget.armor != None:
                                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % dtarget.armor.name),not battleside,False),[enemyp[0] + 40 - 80 * battleside,130])
                                                        if dtarget.weapon != None:
                                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % dtarget.weapon.name),not battleside,False),[enemyp[0] + 40 - 80 * battleside - 10 * (not battleside),130])
                                                        screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sarm.png" % dtarget.name),not battleside,False),[enemyp[0] + 40 - 80 * battleside,130])
                                                        screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/enemies/%sattack.png" % d.name),not battleside,False),arrpos)
                                                        pygame.display.flip()
                                                    if event.type == pygame.MOUSEMOTION:
                                                        mouseposition = event.pos[:]
                                                        selfp,enemyp = animatebattle(enemies,decor,hud,[d,dtarget])
                                                        screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/enemies/%s.png" % d.name),not battleside,False),[selfp[0],130])
                                                        if dtarget.shield != None:
                                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % dtarget.shield.name),not battleside,False),[enemyp[0] + 40 - 80 * battleside - 10 * (not battleside),130])
                                                        screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % dtarget.name),not battleside,False),[enemyp[0] + 40 - 80 * battleside,130])
                                                        if dtarget.armor != None:
                                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % dtarget.armor.name),not battleside,False),[enemyp[0] + 40 - 80 * battleside,130])
                                                        if dtarget.weapon != None:
                                                            screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % dtarget.weapon.name),not battleside,False),[enemyp[0] + 40 - 80 * battleside - 10 * (not battleside),130])
                                                        screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sarm.png" % dtarget.name),not battleside,False),[enemyp[0] + 40 - 80 * battleside,130])
                                                        screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/enemies/%sattack.png" % d.name),not battleside,False),arrpos)
                                                        pygame.display.flip()
                                    animatebattle(enemies,decor,hud)
                                    pygame.display.flip()
                                    yp = 0
                                    while yp < 10:
                                        for event in pygame.event.get():
                                            if event.type == pygame.USEREVENT + 2 + 1:
                                                yp += 1
                                            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1) or event.type == pygame.KEYDOWN:
                                                hud,team,enemies = battledelay(hud,team,enemies,decor,event)
                                                animatebattle(enemies,decor,hud)
                                                pygame.display.flip()
                                            if event.type == pygame.MOUSEMOTION:
                                                mouseposition = event.pos[:]
                                                animatebattle(enemies,decor,hud)
                                                pygame.display.flip()
                                d.charge = 0
                        if d.effect[0] != None:
                            d.effect[2] -= 1
                            if d.effect[0] == "poison":
                                d.poisoncharge += 1
                                if d.poisoncharge == 100:
                                    d.poisoncharge = 0
                                    d.health -= d.effect[1] #maybe change vallues
                                    if d.health < 0:
                                        d.health = 0
                            if d.effect[2] == 0:
                                d.effect = [None,0,0]
                        if d.health <= 0:
                            #rewards
                            #animation
                            drop = []
                            if random.randint(0,100) < 100:
                                if d.level == 2:
                                    drop = [96]
                                elif d.level == 3:
                                    drop = [random.choice([96,100])]
                                elif d.level == 4:
                                    drop = [random.choice([96,100,104])]
                                elif d.level == 5:
                                    drop = [random.choice([96,96,97,100,100,101,104,104,105,108,108,109])]
                                elif d.level == 6:
                                    drop = [random.choice([96,97,97,100,101,101,104,105,105,108,109,109,112,113,113])]
                                elif d.level == 7:
                                    drop = [random.choice([97,101,105,109,113])]
                                elif d.level == 8:
                                    drop = [random.choice([97,98,101,102,105,106,109,110,113,114])]
                                elif d.level == 9:
                                    drop = [random.choice([98,102,106,110,114])]
                                elif d.level == 10:
                                    drop = [random.choice([98,98,99,102,102,103,106,106,107,110,110,111,114,114,115])]
                                elif d.level == 11:
                                    drop = [random.choice([98,99,99,102,103,103,106,107,107,110,111,111,114,115,115])]
                                elif d.level == 12 or d.level == 13:
                                    drop = [random.choice([99,103,107,111,115])]
                            if doanimations:
                                enemyp = animatebattle(enemies,decor,hud,[d])[0]
                                for f in range(3):
                                    animatebattle(enemies,decor,hud)
                                    screen.blit(pygame.transform.scale(pygame.image.load("assets/graphics/extra/poof%s.png" % f),d.size),enemyp)
                                    pygame.display.flip()
                                    yp = 0
                                    while yp < 40:
                                        for event in pygame.event.get():
                                            if event.type == pygame.USEREVENT + 2 + 1:
                                                yp += 1
                                            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1) or event.type == pygame.KEYDOWN:
                                                hud,team,enemies = battledelay(hud,team,enemies,decor,event)
                                                animatebattle(enemies,decor,hud)
                                                screen.blit(pygame.transform.scale(pygame.image.load("assets/graphics/extra/poof%s.png" % f),d.size),enemyp)
                                                pygame.display.flip()
                                            if event.type == pygame.MOUSEMOTION:
                                                mouseposition = event.pos[:]
                                                animatebattle(enemies,decor,hud)
                                                screen.blit(pygame.transform.scale(pygame.image.load("assets/graphics/extra/poof%s.png" % f),d.size),enemyp)
                                                pygame.display.flip()
                                    #rewards
                                enemyp = animatebattle(enemies,decor,hud,[d])[0]
                                if drop != []:
                                    drpos = random.randint(0,20)
                                    screen.blit(pygame.image.load("assets/graphics/items/%s.png" % items[drop[0]].name),[enemyp[0] + drpos,190])
                                pygame.display.flip()
                                yp = 0
                                while yp < 20:
                                    for event in pygame.event.get():
                                        if event.type == pygame.USEREVENT + 2 + 1:
                                            yp += 1
                                        if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1) or event.type == pygame.KEYDOWN:
                                            hud,team,enemies = battledelay(hud,team,enemies,decor,event)
                                            enemyp = animatebattle(enemies,decor,hud,[d])[0]
                                            screen.blit(pygame.image.load("assets/graphics/items/%s.png" % items[drop[0]].name),[enemyp[0] + drpos,190])
                                            pygame.display.flip()
                                        if event.type == pygame.MOUSEMOTION:
                                            mouseposition = event.pos[:]
                                            enemyp = animatebattle(enemies,decor,hud,[d])[0]
                                            screen.blit(pygame.image.load("assets/graphics/items/%s.png" % items[drop[0]].name),[enemyp[0] + drpos,190])
                                            pygame.display.flip()
                                enemyp = animatebattle(enemies,decor,hud,[d])[0]
                                pygame.display.flip()
                            enemies.remove(d)
                            animatebattle(enemies,decor,hud)
                            pygame.display.flip()
                            if drop != []:
                                if None in inventory[:15 * len(team)]:
                                    inventory[inventory.index(None)] = drop[0]
                            money += random.randint(d.loot[0],d.loot[1])
                            if len(enemies) == 0:
                                return True
                            else:
                                for e in team:
                                    if not e.target in enemies:
                                        e.target = enemies[0]
                    for d in team:
                        if d.carry != None:
                            d,team,enemies = d.carry.update(d,team,enemies)
                    if tick == 0:
                        animatebattle(enemies,decor,hud)
                        pygame.display.flip()
            #elif event.type == pygame.USEREVENT + 3:
             #   pass
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                p = 0
                entvol = 0
                for d in enemies:
                    entvol += d.size[0] / 2
                for d in enemies:#560 - 10 - 120 - 30 * len(enemies) + p #(10 + 120) + 30 * len(team) - p - size
                    if (battleside and mouseposition[0] > 430 - entvol + p and mouseposition[0] < 430 + d.size[0] - entvol + p and mouseposition[1] > 230 - d.size[1] and mouseposition[1] < 230) or (not battleside and mouseposition[0] > 130 + entvol - p - d.size[0] and mouseposition[0] < 130 + entvol - p and mouseposition[1] > 230 - d.size[1] and mouseposition[1] < 230):
                        hud = d
                        break
                    p += d.size[0]
                p = 0
                for d in team:#10 + 120 + 30 * len(team) - 60 + p #10 + 120 + 30 * len(team) - 60 + p
                    if (battleside and mouseposition[0] > 130 + 30 * len(team) - p - 60 and mouseposition[0] < 190 + 30 * len(team) - p - 60 and mouseposition[1] > 130 and mouseposition[1] < 230) or (not battleside and mouseposition[0] > 430 - 30 * len(team) + p and mouseposition[0] < 490 - 30 * len(team) + p and mouseposition[1] > 130 and mouseposition[1] < 230):
                        hud = d
                        break
                    p += 60
                if mouseposition[0] > 410 and mouseposition[0] < 530 and mouseposition[1] > 260 and mouseposition[1] < 286 and hud.good:
                    moveteam(team,enemies,decor,hud)
                elif mouseposition[0] > 410 and mouseposition[0] < 530 and mouseposition[1] > 287 and mouseposition[1] < 313 and hud.good:
                    tard = target(enemies,decor,hud)
                    if tard != None:
                        hud.target = tard
                elif mouseposition[0] > 450 and mouseposition[0] < 490 and mouseposition[1] > 343 and mouseposition[1] < 383 and hud.good:
                    if hud.carry != None:
                        hud,team,enemies = hud.carry.use(hud,team,enemies,decor)
                animatebattle(enemies,decor,hud)
                pygame.display.flip()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    if len(team) > 0 + 3*battleside:
                        hud = team[0 + 3*battleside]
                elif event.key == pygame.K_2:
                    if len(team) > 1 + 1*battleside:
                        hud = team[1 + 1*battleside]
                elif event.key == pygame.K_3:
                    if len(team) > 2 - 1*battleside:
                        hud = team[2 - 1*battleside]
                elif event.key == pygame.K_4:
                    if len(team) > 3 - 3*battleside:
                        hud = team[3 - 3*battleside]
                elif event.key == pygame.K_f:
                    if hud.good:
                        tard = target(enemies,decor,hud)
                        if tard != None:
                            hud.target = tard
                elif event.key == pygame.K_r:
                    if hud.good:
                        moveteam(team,enemies,decor,hud)
                elif event.key == pygame.K_v:
                    if hud.good:
                        if hud.carry != None:
                            hud,team,enemies = hud.carry.use(hud,team,enemies,decor)
                animatebattle(enemies,decor,hud)
                pygame.display.flip()
            if event.type == pygame.MOUSEMOTION:
                mouseposition = event.pos[:]
                animatebattle(enemies,decor,hud)
                pygame.display.flip()
            if event.type == pygame.QUIT:
                read = False
                running = False
                playing = False
                break 
    #pygame.display.flip()
def animatebattle(enemies,decor,hud,exceptions=[]):
    global mouseposition,mousedown
    selfpos = []
    screen.blit(pygame.image.load("assets/graphics/dungeons/%s.png" % decor),[0,0])
    p = 0
    entvol = 0
    if battleside:
        for d in enemies:
            entvol += d.size[0] / 2
        for d in enemies:
            #560 - 10 - 120 - 30 * len(enemies) + p
            if not d in exceptions:
                if mouseposition[0] > 430 - entvol - p and mouseposition[0] < 430 + d.size[0] - entvol - p and mouseposition[1] > 230 - d.size[1] and mouseposition[1] < 230:
                    screen.blit(pygame.transform.scale(pygame.image.load("assets/graphics/extra/characterhighlight.png"),d.size),[430 - entvol - p,230 - d.size[1]])
                screen.blit(pygame.image.load("assets/graphics/enemies/%s.png" % d.name),[430 - entvol - p,230 - d.size[1]])
                pygame.draw.rect(screen,[200,200,200],[430 - entvol - p + 5,231,d.size[0] - 10,10])
                pygame.draw.rect(screen,[0,255,0],[430 - entvol - p + 5,231,(d.size[0] - 10) * (float(d.health) / d.maxhealth),10])
                pygame.draw.arc(screen,[220,220,0],[430 - entvol - p,230 - d.size[1] - 21,20,20],1.570,1.570 + (7.853 - 1.570) * (float(d.charge) / d.delay),10)
                if d.effect[0] != None:
                    screen.blit(pygame.image.load("assets/graphics/extra/%s.png" % d.effect[0]),[430 - entvol - p,230 - d.size[1] - 51])
                    screen.blit(linefont.render("%s" % ("0" * (d.effect[2] < 1000) + str(int(d.effect[2] / 100))),0,[0,0,150]),[460 - entvol - p,230 - d.size[1] - 51 + 11])
                    if d.effect[0] == "frozen":
                        screen.blit(pygame.transform.scale(pygame.image.load("assets/graphics/extra/ice.png"),d.size),[430 - entvol - p,230 - d.size[1]])
            else:
                selfpos.append([430 - entvol - p,230 - d.size[1]])
            p -= d.size[0]
        p = -60
        for d in team:
            if not d in exceptions:
                #10 + 120 + 30 * len(team) - 60 + p
                if mouseposition[0] > 130 + 30 * len(team) + p and mouseposition[0] < 190 + 30 * len(team) + p and mouseposition[1] > 130 and mouseposition[1] < 230:
                    screen.blit(pygame.image.load("assets/graphics/extra/characterhighlight.png"),[130 + 30 * len(team) + p,130])
                if d.health > 0:
                    if d.shield != None:
                        screen.blit(pygame.image.load("assets/graphics/characters/%s.png" % d.shield.name),[130 + 30 * len(team) + p,130])
                    screen.blit(pygame.image.load("assets/graphics/characters/%s.png" % d.name),[130 + 30 * len(team) + p,130])
                    if d.armor != None:
                        screen.blit(pygame.image.load("assets/graphics/characters/%s.png" % d.armor.name),[130 + 30 * len(team) + p,130])
                    if d.weapon != None:
                        screen.blit(pygame.image.load("assets/graphics/characters/%s.png" % d.weapon.name),[130 + 30 * len(team) + p,130])
                    screen.blit(pygame.image.load("assets/graphics/characters/%sarm.png" % d.name),[130 + 30 * len(team) + p,130])
                    pygame.draw.rect(screen,[255,0,0],[130 + 30 * len(team) + p + 5,231,50,10])
                    pygame.draw.rect(screen,[0,255,0],[130 + 30 * len(team) + p + 5,231,50 * (float(d.health) / d.maxhealth),10])
                    pygame.draw.arc(screen,[255,255,0],[130 + 30 * len(team) + p,109,20,20],1.570,1.570 + (7.853 - 1.570) * (float(d.charge) / d.delay),10)
                    if d.effect[0] != None:
                        screen.blit(pygame.image.load("assets/graphics/extra/%s.png" % d.effect[0]),[130 + 30 * len(team) + p,79])
                        screen.blit(linefont.render("%s" % ("0" * (d.effect[2] < 1000) + str(int(d.effect[2] / 100))),0,[0,0,150]),[160 + 30 * len(team) + p,79 + 11])
                else:
                    screen.blit(pygame.image.load("assets/graphics/characters/%ssleep.png" % d.name),[130 + 30 * len(team) + p,130])
            else:
                selfpos.append([130 + 30 * len(team) + p,130])
                #selfpos.append([100 + entvol - p,230 - 100])
            p -= 60
    else:
        for d in enemies:
            entvol += d.size[0] / 2
        for d in enemies:
            #(10 + 120) + 30 * len(team) - p - size
            if not d in exceptions:
                if mouseposition[0] > 130 + entvol - p - d.size[0] and mouseposition[0] < 130 + entvol - p and mouseposition[1] > 230 - d.size[1] and mouseposition[1] < 230:
                    screen.blit(pygame.transform.scale(pygame.image.load("assets/graphics/extra/characterhighlight.png"),d.size),[130 + entvol - p - d.size[0],230 - d.size[1]])
                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/enemies/%s.png" % d.name),True,False),[130 + entvol - p - d.size[0],230 - d.size[1]])
                pygame.draw.rect(screen,[200,200,200],[130 + entvol - p - d.size[0] + 5,231,d.size[0] - 10,10])
                pygame.draw.rect(screen,[0,255,0],[130 + entvol - p - d.size[0] + 5,231,(d.size[0] - 10) * (float(d.health) / d.maxhealth),10])
                pygame.draw.arc(screen,[220,220,0],[130 + entvol - p - d.size[0],230 - d.size[1] - 21,20,20],1.570,1.570 + (7.853 - 1.570) * (float(d.charge) / d.delay),10)
                if d.effect[0] != None:
                    screen.blit(pygame.image.load("assets/graphics/extra/%s.png" % d.effect[0]),[130 + entvol - p - d.size[0],230 - d.size[1] - 51])
                    screen.blit(linefont.render("%s:%s" % (int(d.effect[2] / 6000),int(d.effect[2] / 100)),0,[0,0,150]),[160 + entvol - p - d.size[0],230 - d.size[1] - 51])
                    if d.effect[0] == "frozen":
                        screen.blit(pygame.transform.scale(pygame.image.load("assets/graphics/extra/ice.png"),d.size),[130 + entvol - p - d.size[0],230 - d.size[1]])
            else:
                selfpos.append([130 + entvol - p - d.size[0],230 - d.size[1]])
            p += d.size[0]
        p = 0
        for d in team:
            if not d in exceptions:
                #(560 - 10 - 120) - 30 * len(team) + p
                #430 - 30 * len(team) + p
                if mouseposition[0] > 430 - 30 * len(team) + p and mouseposition[0] < 490 - 30 * len(team) + p and mouseposition[1] > 130 and mouseposition[1] < 230:
                    screen.blit(pygame.image.load("assets/graphics/extra/characterhighlight.png"),[430 - 30 * len(team) + p,130])
                if d.health > 0:
                    if d.shield != None:
                        screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % d.shield.name),True,False),[430 - 30 * len(team) + p - 10,130])
                    screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % d.name),True,False),[430 - 30 * len(team) + p,130])
                    if d.armor != None:
                        screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % d.armor.name),True,False),[430 - 30 * len(team) + p,130])
                    if d.weapon != None:
                        screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%s.png" % d.weapon.name),True,False),[430 - 30 * len(team) + p - 10,130])
                    screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%sarm.png" % d.name),True,False),[430 - 30 * len(team) + p,130])
                    pygame.draw.rect(screen,[255,0,0],[430 - 30 * len(team) + p + 5,231,50,10])
                    pygame.draw.rect(screen,[0,255,0],[430 - 30 * len(team) + p + 5,231,50 * (float(d.health) / d.maxhealth),10])
                    pygame.draw.arc(screen,[255,255,0],[430 - 30 * len(team) + p,109,20,20],1.570,1.570 + (7.853 - 1.570) * (float(d.charge) / d.delay),10)
                    if d.effect[0] != None:
                        screen.blit(pygame.image.load("assets/graphics/extra/%s.png" % d.effect[0]),[430 - 30 * len(team) + p,79])
                        screen.blit(linefont.render("%s:%s" % (int(d.effect[2] / 6000),int(d.effect[2] / 100)),0,[0,0,150]),[460 - 30 * len(team) + p,79])
                else:
                    screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/characters/%ssleep.png" % d.name),True,False),[430 - 30 * len(team) + p,130])
            else:
                selfpos.append([430 - 30 * len(team) + p,130])
                #selfpos.append([430 - 30 * len(team) + p,230 - 100])
            p += 60
    if hud.good == True:
        screen.blit(pygame.image.load("assets/graphics/extra/battlehud1.png"),[0,0])
        screen.blit(linefont.render(hud.name,0,[150,120,0]),[10,255])
        if hud.shield != None:
            screen.blit(pygame.image.load("assets/graphics/characters/%s.png" % hud.shield.name),[15,285])
        screen.blit(pygame.image.load("assets/graphics/characters/%s.png" % hud.name),[15,285])
        if hud.armor != None:
            screen.blit(pygame.image.load("assets/graphics/characters/%s.png" % hud.armor.name),[15,285])
        if hud.weapon != None:
            screen.blit(pygame.image.load("assets/graphics/characters/%s.png" % hud.weapon.name),[15,285])
        screen.blit(pygame.image.load("assets/graphics/characters/%sarm.png" % hud.name),[15,285])
        if hud.weapon != None:
            screen.blit(pygame.image.load("assets/graphics/extra/slot.png"),[90,290])
            screen.blit(hud.weapon.texture,[90,290])
        if hud.armor != None:
            screen.blit(pygame.image.load("assets/graphics/extra/slot.png"),[150,290])
            screen.blit(hud.armor.texture,[150,290])
        if hud.shield != None:
            screen.blit(pygame.image.load("assets/graphics/extra/slot.png"),[210,290])
            screen.blit(hud.shield.texture,[210,290])
        if hud.ring1 != None:
            screen.blit(pygame.image.load("assets/graphics/extra/slot.png"),[120,345])
            screen.blit(hud.ring1.texture,[120,345])
        if hud.ring2 != None:
            screen.blit(pygame.image.load("assets/graphics/extra/slot.png"),[180,345])
            screen.blit(hud.ring2.texture,[180,345])
        screen.blit(linefont.render("%s/%s" % (hud.health,hud.maxhealth),0,[0,0,0]),[300,260])
        screen.blit(linefont.render("%s" % hud.attack + (" + %s" % hud.effect[1]) * (hud.effect[0] == "strength"),0,[0,0,0]),[300,286])
        screen.blit(linefont.render("%s" % hud.defence + (" + %s" % hud.effect[1]) * (hud.effect[0] == "resistance"),0,[0,0,0]),[300,312])
        screen.blit(linefont.render("%s" % hud.speed + (" + %s" % hud.effect[1]) * (hud.effect[0] == "swiftness"),0,[0,0,0]),[300,338])
        screen.blit(linefont.render("%s" % hud.luck + (" + %s" % hud.effect[1]) * (hud.effect[0] == "charm"),0,[0,0,0]),[300,364])
        if hud.carry != None:
            screen.blit(pygame.image.load("assets/graphics/extra/slot.png"),[450,343])
            if hud.carry.itemtype == "spell":
                screen.blit(hud.carry.offtexture,[450,343])
                screen.blit(pygame.transform.chop(hud.carry.texture,[0,0,0,40 - (40 * (float(hud.spellcharge) / hud.carry.delay))]),[450,343 + (40 - (40 * (float(hud.spellcharge) / hud.carry.delay)))])
            else:
                screen.blit(hud.carry.texture,[450,343])
        else:
            if mouseposition[0] > 450 and mouseposition[0] < 490 and mouseposition[1] > 343 and mouseposition[1] < 383:
                screen.blit(pygame.image.load("assets/graphics/extra/carryselect.png"),[450,343])
            #else:
             #   screen.blit(pygame.image.load("assets/graphics/extra/carryselect.png"),[450,343])
        if mouseposition[0] > 410 and mouseposition[0] < 530 and mouseposition[1] > 260 and mouseposition[1] < 286:
            screen.blit(pygame.image.load("assets/graphics/extra/movebuttonon.png"),[410,260])
        elif mouseposition[0] > 410 and mouseposition[0] < 530 and mouseposition[1] > 287 and mouseposition[1] < 313:
            screen.blit(pygame.image.load("assets/graphics/extra/targetbuttonon.png"),[410,287])
        elif mouseposition[0] > 450 and mouseposition[0] < 490 and mouseposition[1] > 343 and mouseposition[1] < 383:
            if hud.carry != None:
                hud.carry.description()
        elif mouseposition[0] > 90 and mouseposition[0] < 130 and mouseposition[1] > 290 and mouseposition[1] < 330:
            if hud.weapon != None:
                hud.weapon.description()
        elif mouseposition[0] > 150 and mouseposition[0] < 190 and mouseposition[1] > 290 and mouseposition[1] < 330:
            if hud.armor != None:
                hud.armor.description()
        elif mouseposition[0] > 210 and mouseposition[0] < 250 and mouseposition[1] > 290 and mouseposition[1] < 330:
            if hud.shield != None:
                hud.shield.description()
        elif mouseposition[0] > 120 and mouseposition[0] < 160 and mouseposition[1] > 350 and mouseposition[1] < 390:
            if hud.ring1 != None:
                hud.ring1.description()
        elif mouseposition[0] > 180 and mouseposition[0] < 220 and mouseposition[1] > 350 and mouseposition[1] < 390:
            if hud.ring2 != None:
                hud.ring2.description()
    else:
        screen.blit(pygame.image.load("assets/graphics/extra/battlehud2.png"),[0,0])
        if hud.name == "fogspector":
            screen.blit(linefont.render("??????",0,[150,120,0]),[10,255])
        else:
            screen.blit(linefont.render(hud.name,0,[150,120,0]),[10,255])
        screen.blit(pygame.transform.scale(pygame.transform.flip(pygame.image.load("assets/graphics/enemies/%s.png" % hud.name),True,False),[60,100]),[15,285])
        screen.blit(linefont.render("%s/%s" % (hud.health,hud.maxhealth),0,[0,0,0]),[300,260])
        screen.blit(linefont.render("%s" % hud.attack + (" + %s" % hud.effect[1]) * (hud.effect[0] == "strength"),0,[0,0,0]),[300,286])
        screen.blit(linefont.render("%s" % hud.defence + (" + %s" % hud.effect[1]) * (hud.effect[0] == "resistance"),0,[0,0,0]),[300,312])
        screen.blit(linefont.render("%s" % hud.speed + (" + %s" % hud.effect[1]) * (hud.effect[0] == "swiftness"),0,[0,0,0]),[300,338])
        screen.blit(linefont.render("%s" % hud.luck + (" + %s" % hud.effect[1]) * (hud.effect[0] == "charm"),0,[0,0,0]),[300,364])
    if not exceptions == []:
        return selfpos
def game(need):
    global team,mouseposition,mousedown
    if not quests[18]:
        quests[18] = True
        teach("game")
    inventoryon = True
    health = 3
    score = 0
    tick = 0
    last = "melon"
    scoreadd = [0,0]
    bounce = []
    falling = []
    arrows = []
    bounceaway = []
    hit = False
    shield = 0
    bow = 0
    speed = 0
    playerpos = 280
    pygame.time.set_timer(pygame.USEREVENT + 1,100)
    animategame(health,score,last,bounce,falling,hit,arrows,bounceaway,need,shield,bow,speed,playerpos)
    pygame.display.flip()
    while inventoryon:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                playing = False
                inventoryon = False
                break
            if event.type == pygame.MOUSEBUTTONUP:
                mousedown = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mousedown = True
                if bow > 0:
                    arrows.append([playerpos - 20,340])
            if event.type == pygame.USEREVENT + 1:
                if mouseposition[0] > playerpos + 5 + 10 * (speed > 0):
                    playerpos += 10 + 10 * (speed > 0)
                elif mouseposition[0] < playerpos - 5 - 10 * (speed > 0):
                    playerpos -= 10 + 10 * (speed > 0)
                for d in bounceaway[:]:
                    d[0] += d[4]
                    d[1] -= d[3]
                    d[3] -= 4
                    if d[0] > 560:
                        bounceaway.remove(d)
                    elif d[0] + 40 < 0:
                        bounceaway.remove(d)
                for d in bounce[:]:
                    d[0] += d[4]
                    d[1] -= d[3]
                    d[3] -= 4
                    if d[0] > 230 and d[0] + 40 < 330 and d[1] > 280:
                        bounce.remove(d)
                        if d[2] == "melon" or d[2] == "grape" or d[2] == "orange" or d[2] == "lemon":
                            score += 10
                            last = d[2]
                        elif d[2] == "mango" or d[2] == "dragon":
                            score += 30
                            last = d[2]
                        elif d[2] == "goldenapple":
                            score += 100
                        else:
                            score -= 30
                            bounceaway.append([d[0],d[1],d[2] + last,29,-20 + 40 * (d[4] > 0)])
                        #scoreaddanimation
                        if score >= need:
                            for d in team:
                                d.health = d.maxhealth
                            screen.blit(pygame.image.load("assets/graphics/game/endscreen1.png"),[0,0])
                            pygame.display.flip()
                            pygame.time.delay(1000)
                            return
                for d in falling[:]:
                    if d[2] == "splat" or d[2] == "break" or d[2] == "ouch":
                        falling.remove(d)
                        continue
                    d[1] += 15
                    if d[0] + 40 > playerpos - 30 - 20 * (shield > 0) and d[0] < playerpos + 30 + 20 * (shield > 0) and d[1] + 40 > 280:
                        hit = True
                        if d[2] == "rock":
                            d[2] = "break"
                            if shield == 0:
                                health -= 1
                                if health == 0:
                                    animategame(health,score,last,bounce,falling,hit,arrows,bounceaway,need,shield,bow,speed,playerpos)
                                    #screen.blit(pygame.image.load("assets/graphics/game/deathscreen.png"),[0,0])
                                    pygame.display.flip()
                                    pygame.time.delay(500)
                                    if score > need * .5:
                                        screen.blit(pygame.image.load("assets/graphics/game/endscreen2.png"),[0,0])
                                    elif score > need * .25:
                                        screen.blit(pygame.image.load("assets/graphics/game/endscreen3.png"),[0,0])
                                    elif score >= 0:
                                        screen.blit(pygame.image.load("assets/graphics/game/endscreen4.png"),[0,0])
                                    else:
                                        screen.blit(pygame.image.load("assets/graphics/game/endscreen5.png"),[0,0])
                                    pygame.display.flip()
                                    pygame.time.delay(1000)
                                    rscore = score
                                    if rscore <= 0:
                                        rscore = 0
                                        return
                                    rlen = range(len(team))
                                    #addhealth1 = team[0].health + team[1].health + team[2].health + team[3].health
                                    #for d in rlen[:]:
                                     #   if team[d].health == team[d].maxhealth:
                                      #      rlen.remove(d)
                                    f = True
                                    while f:
                                        f = False
                                        for d in rlen[:]:
                                            if team[d].maxhealth - team[d].health <= int(rscore / len(rlen)):
                                                rscore -= team[d].maxhealth - team[d].health
                                                team[d].health = team[d].maxhealth
                                                rlen.remove(d)
                                                f = True
                                    for d in rlen[:]:
                                        team[d].health += int(rscore / len(rlen))
                                    for d in range(rscore % len(rlen)):
                                        team[rlen[d]].health += 1
                                    #print addhealth1,team[0].health + team[1].health + team[2].health + team[3].health,score,team[0].health + team[1].health + team[2].health + team[3].health - addhealth1
                                    """while rscore > 0:
                                        for d in range(len(rlen)):
                                            if team[rlen[d]].maxhealth - team[rlen[d]].health > int(rscore / (len(rlen) - d) + .75):
                                                team[rlen[d]].health += int(rscore / (len(rlen) - d) + .75)
                                                rscore -= int(rscore / (len(rlen) - d) + .75)
                                            else:
                                                rscore -= team[rlen[d]].maxhealth - team[rlen[d]].health
                                                team[rlen[d]].health = team[rlen[d]].maxhealth
                                                rlen.remove(rlen[d])
                                                break"""
                                    #for d in range(len(team)):
                                     #   if team[d].maxhealth - team[d].health > int(rscore / (len(team) - d)):
                                      #      team[d].health += int(rscore / (len(team) - d))
                                       #     rscore -= int(rscore / (len(team) - d))
                                        #else:
                                         #   rscore -= team[d].maxhealth - team[d].health
                                          #  team[d].health = team[d].maxhealth
                                    #for d in team:
                                     #   if d.maxhealth - d.health > int(score / len(team))
                                      #      d.health += int(score / len(team))
                                       # else:
                                        #    d.health = d.maxhealth
                                    #for dh in range(score - len(team) * int(score / len(team))):
                                     #   team[dh].health += 1
                                    """t = len(team)
                                    while score > 0:
                                        for d in team:
                                            if d.health < d.maxhealth:
                                                if d.maxhealth - d.health >= int(score / t):
                                                    if int(score / t) == 0:
                                                        d.health += 1
                                                        score -= 1
                                                    else:
                                                        d.health += int(score / t)
                                                        score -= int(score / t)
                                                elif d.maxhealth - d.health <= int(score / t):
                                                    score -= d.maxhealth - d.health
                                                    d.health = d.maxhealth
                                                    t -= 1"""
                                    return
                        elif d[2] == "shield":
                            falling.remove(d)
                            shield = 100
                        elif d[2] == "bow":
                            falling.remove(d)
                            bow = 100
                        elif d[2] == "speed":
                            falling.remove(d)
                            speed = 100
                        elif d[2] == "heartfruit":
                            falling.remove(d)
                            if health < 3:
                                health += 1
                        else:
                            falling.remove(d)
                            bounce.append([d[0],d[1],d[2],14,((280 - (d[0] + 20)) / 10.0)])
                            """if d[0] > 260:
                                bounce[-1].append(-15)
                            else:
                                bounce[-1].append(15)"""
                    elif d[1] + 40 > 380:
                        d[1] = 340
                        if d[2] == "rock" or d[2] == "bow" or d[2] == "shield" or d[2] == "speed":
                            d[2] = "break"
                        elif d[2] == "critter":
                            d[2] = "ouch"
                        else:
                            d[2] = "splat"
                for d in arrows[:]:
                    d[1] -= 15
                    if d[1] + 40 < 0:
                        arrows.remove(d)
                        continue
                    for k in falling[:]:
                        if k[0] + 40 > d[0] and k[0] < d[0] + 40 and k[1] + 40 > d[1] and k[1] < d[1] + 40:
                            arrows.remove(d)
                            if k[2] == "melon" or k[2] == "grape" or k[2] == "orange" or k[2] == "lemon":
                                score += 10
                                falling[falling.index(k)][2] = "splat"
                            elif k[2] == "mango" or k[2] == "dragon":
                                score += 30
                                falling[falling.index(k)][2] = "splat"
                            elif k[2] == "goldenapple":
                                score += 100
                                falling[falling.index(k)][2] = "splat"
                            elif k[2] == "rock":
                                score += 10
                                falling[falling.index(k)][2] = "break"
                            elif k[2] == "critter":
                                score += 10
                                falling[falling.index(k)][2] = "ouch"
                            elif k[2] == "shield":
                                falling.remove(k)
                                shield = 100
                            elif k[2] == "bow":
                                falling.remove(k)
                                bow = 100
                            elif k[2] == "speed":
                                falling.remove(k)
                                speed = 100
                            elif k[2] == "heartfruit":
                                falling.remove(k)
                                if health < 3:
                                    health += 1
                            if score >= need:
                                for d in team:
                                    d.health = d.maxhealth
                                screen.blit(pygame.image.load("assets/graphics/game/endscreen1.png"),[0,0])
                                pygame.display.flip()
                                pygame.time.delay(1000)
                                return
                            break
                if shield > 0:
                    shield -= 1
                if bow > 0:
                    bow -= 1
                if speed > 0:
                    speed -= 1
                tick += 1
                if tick == 6:
                    dy = random.randint(1,612)
                    if dy in range(1,71):
                        ty = "mango"
                    elif dy in range(71,141):
                        ty = "melon"
                    elif dy in range(141,211):
                        ty = "orange"
                    elif dy in range(211,281):
                        ty = "grape"
                    elif dy in range(281,351):
                        ty = "lemon"
                    elif dy in range(351,421):
                        ty = "dragon"
                    elif dy in range(421,541):
                        ty = "rock"
                    elif dy in range(541,553):
                        ty = "shield"
                    elif dy in range(553,565):
                        ty = "bow"
                    elif dy in range(565,589):
                        ty = "critter"
                    elif dy in range(589,595):
                        ty = "heartfruit"
                    elif dy in range(595,601):
                        ty = "goldenapple"
                    elif dy in range(601,613):
                        ty = "speed"
                    falling.append([random.randint(0,520),-40,ty])
                    tick = 0
                animategame(health,score,last,bounce,falling,hit,arrows,bounceaway,need,shield,bow,speed,playerpos)
                pygame.display.flip()
                hit = False
            if event.type == pygame.MOUSEMOTION:
                mouseposition = event.pos[:]
                if mouseposition[0] > 560:
                    mouseposition[0] = 560
                elif mouseposition[1] < 0:
                    mouseposition[1] = 0
                #animategame(health,score,last,bounce,falling,hit,arrows,bounceaway,need,shield,bow,playerpos)
                pygame.display.flip()
def animategame(health,score,last,bounce,falling,hit,arrows,bounceaway,need,shield,bow,speed,playerpos):
    global mouseposition,mousedown
    screen.blit(pygame.image.load("assets/graphics/game/game.png"),[0,0])
    for d in bounce:
        screen.blit(pygame.image.load("assets/graphics/game/%s.png" % d[2]),d[:2])
    for d in bounceaway:
        screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/game/%s.png" % d[2]),d[4] > 0,False),d[:2])
    screen.blit(pygame.image.load("assets/graphics/game/basket.png"),[0,0])
    for d in falling:
        screen.blit(pygame.image.load("assets/graphics/game/%s.png" % d[2]),d[:2])
    for d in arrows:
        screen.blit(pygame.image.load("assets/graphics/game/arrow.png"),d[:2])
    screen.blit(pygame.image.load("assets/graphics/game/%s.png" % last),[330,10])
    screen.blit(linefont.render("%s/%s" % (score,need),0,[0,0,0]),[360,15])
    py = 50
    if shield > 0:
        screen.blit(pygame.image.load("assets/graphics/game/shield.png"),[330,py])
        screen.blit(linefont.render("%s" % (shield),0,[0,0,0]),[360,py + 5])
        py += 40
    if bow > 0:
        screen.blit(pygame.image.load("assets/graphics/game/bow.png"),[330,py])
        screen.blit(linefont.render("%s" % (bow),0,[0,0,0]),[360,py + 5])
        py += 40
    if speed > 0:
        screen.blit(pygame.image.load("assets/graphics/game/speed.png"),[330,py])
        screen.blit(linefont.render("%s" % (speed),0,[0,0,0]),[360,py + 5])
        py += 40
    px = 10
    for d in range(health):
        screen.blit(pygame.image.load("assets/graphics/game/heart.png"),[px,10])
        px += 40
    for d in range(3 - health):
        screen.blit(pygame.image.load("assets/graphics/game/damageheart.png"),[px,10])
        px += 40
    if hit:
        if playerpos > 280:
            screen.blit(pygame.image.load("assets/graphics/game/playerbounceleft.png"),[playerpos - 30,280])
        else:
            screen.blit(pygame.image.load("assets/graphics/game/playerbounceright.png"),[playerpos - 30,280])
    else:
        screen.blit(pygame.image.load("assets/graphics/game/player.png"),[playerpos - 30,280])
    if shield > 0:
        screen.blit(pygame.image.load("assets/graphics/game/playershield.png"),[playerpos - 50,280])
bagmoneypos = [297,265]
costpos = [40,355]
coppercointexture = pygame.image.load("assets/graphics/extra/coinscopper.png")
silvercointexture = pygame.image.load("assets/graphics/extra/coinssilver.png")
goldencointexture = pygame.image.load("assets/graphics/extra/coinsgold.png")
def shop(merchandise):
    global inventory,crafting,result,holding,team,money,coinred,mouseposition,mousedown
    pygame.time.set_timer(pygame.USEREVENT + 2,30)
    coinblibs = []
    tick = 0
    total = 0
    coinred = 0
    inventoryon = True
    selected = None
    select = [None,None]
    buy = True
    panel = "inventory"
    shelf = 0
    viewcoins = money
    animateshop(merchandise,selected,select,buy,panel,shelf,coinblibs,viewcoins)
    pygame.display.flip()
    while inventoryon:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                playing = False
                inventoryon = False
                break
            if event.type == pygame.USEREVENT + 2:
                animatecoin = False
                if len(coinblibs) > 0:
                    animatecoin = True
                if coinred > 0:
                    coinred -= 17
                    animatecoin = True
                for c in coinblibs[:]:
                    coinblibs[coinblibs.index(c)][0] -= c[2]
                    coinblibs[coinblibs.index(c)][1] -= c[3]
                    if c[0] >= bagmoneypos[0] - 21 or c[0] <= costpos[0] - 21:
                        coinblibs.remove(c)
                        if c[0] >= bagmoneypos[0] - 21:
                            if c[4] == "copper":
                                viewcoins += 1
                            if c[4] == "silver":
                                viewcoins += 10
                            if c[4] == "gold":
                                viewcoins += 100
                if total > 0:
                    tick += 1
                    if tick == 3:
                        #bagmoneypos = [292,265]
                        #costpos = [40,355]
                        #bagmoneypos = [271,260]
                        #costpos = [19,350]
                        tick = 0
                        if total >= 100:
                            total -= 100
                            viewcoins -= 100
                            coinblibs.append([bagmoneypos[0] - 21.0,bagmoneypos[1] - 5.0,(bagmoneypos[0] - costpos[0]) / 30.0,(bagmoneypos[1] - costpos[1]) / 30.0,"gold"])
                        elif total >= 10:
                            total -= 10
                            viewcoins -= 10
                            coinblibs.append([bagmoneypos[0] - 21.0,bagmoneypos[1] - 5.0,(bagmoneypos[0] - costpos[0]) / 30.0,(bagmoneypos[1] - costpos[1]) / 30.0,"silver"])
                        else:
                            total -= 1
                            viewcoins -= 1
                            coinblibs.append([bagmoneypos[0] - 21.0,bagmoneypos[1] - 5.0,(bagmoneypos[0] - costpos[0]) / 30.0,(bagmoneypos[1] - costpos[1]) / 30.0,"copper"])
                elif total < 0:
                    tick += 1
                    if tick == 3:
                        tick = 0
                        if total <= -100:
                            total += 100
                            #viewcoins += 100
                            coinblibs.append([costpos[0] - 21.0,costpos[1] - 5.0,(costpos[0] - bagmoneypos[0]) / 30.0,(costpos[1] - bagmoneypos[1]) / 30.0,"gold"])
                        elif total <= -10:
                            total += 10
                            #viewcoins += 10
                            coinblibs.append([costpos[0] - 21.0,costpos[1] - 5.0,(costpos[0] - bagmoneypos[0]) / 30.0,(costpos[1] - bagmoneypos[1]) / 30.0,"silver"])
                        else:
                            total += 1
                            #viewcoins += 1
                            coinblibs.append([costpos[0] - 21.0,costpos[1] - 5.0,(costpos[0] - bagmoneypos[0]) / 30.0,(costpos[1] - bagmoneypos[1]) / 30.0,"copper"])
                if animatecoin:
                    animateshop(merchandise,selected,select,buy,panel,shelf,coinblibs,viewcoins)
                    pygame.display.flip()
            if event.type == pygame.MOUSEBUTTONUP:
                mousedown = False
                animateshop(merchandise,selected,select,buy,panel,shelf,coinblibs,viewcoins)
                pygame.display.flip()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mousedown = True
                if mouseposition[0] > 70 and mouseposition[0] < 140 and mouseposition[1] > 260 and mouseposition[1] < 300:
                    if selected != None:
                        if buy:
                            if None in inventory[:15 * len(team)]:
                                if money >= prices[selected]:
                                    money -= prices[selected]
                                    inventory[inventory.index(None)] = selected
                                    #go to bag animation
                                    total += prices[selected]
                                    animateshop(merchandise,selected,select,buy,panel,shelf,coinblibs,viewcoins)
                                    pygame.display.flip()
                                else:
                                    coinred = 255
                            else:
                                pass
                                #you don't have enough room animation
                        else:
                            if select[0] == "inventory":
                                inventory[select[1]] = None
                                money += int(prices[selected] * .8)
                                animateshop(merchandise,selected,select,buy,panel,shelf,coinblibs,viewcoins)
                                pygame.display.flip()
                            elif select[0] == "team":
                                for d in team:
                                    if d.name == select[1][0]:
                                        break
                                if select[1][1] == 0:
                                    d.health -= d.weapon.health
                                    d.maxhealth -= d.weapon.health
                                    d.attack -= d.weapon.attack
                                    d.defence -= d.weapon.defence
                                    d.speed -= d.weapon.speed
                                    d.luck -= d.weapon.luck
                                    d.weapon = None
                                    d.delay = int(6000 / (d.speed + d.effect[1] * (d.effect[0] == "swiftness")))
                                    money += int(prices[selected] * .8)
                                    animateshop(merchandise,selected,select,buy,panel,shelf,coinblibs,viewcoins)
                                    pygame.display.flip()
                                elif select[1][1] == 1:
                                    d.health -= d.armor.health
                                    d.maxhealth -= d.armor.health
                                    d.attack -= d.armor.attack
                                    d.defence -= d.armor.defence
                                    d.speed -= d.armor.speed
                                    d.luck -= d.armor.luck
                                    d.armor = None
                                    d.delay = int(6000 / (d.speed + d.effect[1] * (d.effect[0] == "swiftness")))
                                    money += int(prices[selected] * .8)
                                    animateshop(merchandise,selected,select,buy,panel,shelf,coinblibs,viewcoins)
                                    pygame.display.flip()
                                elif select[1][1] == 2:
                                    d.health -= d.shield.health
                                    d.maxhealth -= d.shield.health
                                    d.attack -= d.shield.attack
                                    d.defence -= d.shield.defence
                                    d.speed -= d.shield.speed
                                    d.luck -= d.shield.luck
                                    d.shield = None
                                    d.delay = int(6000 / (d.speed + d.effect[1] * (d.effect[0] == "swiftness")))
                                    money += int(prices[selected] * .8)
                                    animateshop(merchandise,selected,select,buy,panel,shelf,coinblibs,viewcoins)
                                    pygame.display.flip()
                                elif select[1][1] == 3:
                                    d.health -= d.ring1.health
                                    d.maxhealth -= d.ring1.health
                                    d.attack -= d.ring1.attack
                                    d.defence -= d.ring1.defence
                                    d.speed -= d.ring1.speed
                                    d.luck -= d.ring1.luck
                                    d.ring1 = None
                                    d.delay = int(6000 / (d.speed + d.effect[1] * (d.effect[0] == "swiftness")))
                                    money += int(prices[selected] * .8)
                                    animateshop(merchandise,selected,select,buy,panel,shelf,coinblibs,viewcoins)
                                    pygame.display.flip()
                                elif select[1][1] == 4:
                                    d.health -= d.ring2.health
                                    d.maxhealth -= d.ring2.health
                                    d.attack -= d.ring2.attack
                                    d.defence -= d.ring2.defence
                                    d.speed -= d.ring2.speed
                                    d.luck -= d.ring2.luck
                                    d.ring2 = None
                                    d.delay = int(6000 / (d.speed + d.effect[1] * (d.effect[0] == "swiftness")))
                                    money += int(prices[selected] * .8)
                                    animateshop(merchandise,selected,select,buy,panel,shelf,coinblibs,viewcoins)
                                    pygame.display.flip()
                                elif select[1][1] == 5:
                                    d.carry = None
                                    money += int(prices[selected] * .8)
                                    animateshop(merchandise,selected,select,buy,panel,shelf,coinblibs,viewcoins)
                                    pygame.display.flip()
                            total -= int(prices[selected] * .8)
                            selected = None
                            #coin spread animation
                elif mouseposition[0] > 277 and mouseposition[0] < 536 and mouseposition[1] > 305 and mouseposition[1] < 389:
                    if (mouseposition[0] - 277) % 44 <= 40 and (mouseposition[1] - 305) % 44 <= 40:
                        if int((mouseposition[0] - 277) / 44) + 6 * int((mouseposition[1] - 305) / 44) < len(merchandise):
                            selected = merchandise[12 * shelf + int((mouseposition[0] - 277) / 44) + 6 * int((mouseposition[1] - 305) / 44)]
                            select = ["store",12 * shelf + int((mouseposition[0] - 277) / 44) + 6 * int((mouseposition[1] - 305) / 44)]
                            buy = True
                            animateshop(merchandise,selected,select,buy,panel,shelf,coinblibs,viewcoins)
                            pygame.display.flip()
                elif mouseposition[0] > 260 and mouseposition[0] < 274 and mouseposition[1] > 300 and mouseposition[1] < 383:
                    if shelf > 0:
                        shelf -= 1
                        animateshop(merchandise,selected,select,buy,panel,shelf,coinblibs,viewcoins)
                        pygame.display.flip()
                elif mouseposition[0] > 539 and mouseposition[0] < 553 and mouseposition[1] > 300 and mouseposition[1] < 383:
                    if (shelf + 1) * 12 < len(merchandise):
                        shelf += 1
                        animateshop(merchandise,selected,select,buy,panel,shelf,coinblibs,viewcoins)
                        pygame.display.flip()
                elif mouseposition[0] > 18 and mouseposition[0] < 18 + 132 * len(team) and mouseposition[1] > 18 and mouseposition[1] < 234 and panel == "inventory":
                    if (mouseposition[0] - 18) % 44 <= 40 and (mouseposition[1] - 18) % 44 <= 40:
                        if inventory[5 * int((mouseposition[0] - 18) / 44) + int((mouseposition[1] - 18) / 44)] != None:
                            selected = inventory[5 * int((mouseposition[0] - 18) / 44) + int((mouseposition[1] - 18) / 44)]
                            select = ["inventory",5 * int((mouseposition[0] - 18) / 44) + int((mouseposition[1] - 18) / 44)]
                            buy = False
                            animateshop(merchandise,selected,select,buy,panel,shelf,coinblibs,viewcoins)
                            pygame.display.flip()
                elif mouseposition[0] > 18 and mouseposition[0] < 546 and mouseposition[1] > 18 and mouseposition[1] < 234 and panel == "team":
                    px = 28
                    py = 3
                    for d in team:
                        if d.weapon != None:
                            if mouseposition[0] > px + 84 and mouseposition[0] < px + 124 and mouseposition[1] > py + 13 and mouseposition[1] < py + 53 and mousedown:
                                selected = d.weapon.itemid
                                select = ["team",[d.name,0]]
                                buy = False
                                animateshop(merchandise,selected,select,buy,panel,shelf,coinblibs,viewcoins)
                                pygame.display.flip()
                                break
                        if d.armor != None:
                            if mouseposition[0] > px + 140 and mouseposition[0] < px + 180 and mouseposition[1] > py + 13 and mouseposition[1] < py + 53 and mousedown:
                                selected = d.armor.itemid
                                select = ["team",[d.name,1]]
                                buy = False
                                animateshop(merchandise,selected,select,buy,panel,shelf,coinblibs,viewcoins)
                                pygame.display.flip()
                                break
                        if d.shield != None:
                            if mouseposition[0] > px + 196 and mouseposition[0] < px + 236 and mouseposition[1] > py + 13 and mouseposition[1] < py + 53 and mousedown:
                                selected = d.shield.itemid
                                select = ["team",[d.name,2]]
                                buy = False
                                animateshop(merchandise,selected,select,buy,panel,shelf,coinblibs,viewcoins)
                                pygame.display.flip()
                                break
                        if d.ring1 != None:
                            if mouseposition[0] > px + 84 and mouseposition[0] < px + 124 and mouseposition[1] > py + 67 and mouseposition[1] < py + 107 and mousedown:
                                selected = d.ring1.itemid
                                select = ["team",[d.name,3]]
                                buy = False
                                animateshop(merchandise,selected,select,buy,panel,shelf,coinblibs,viewcoins)
                                pygame.display.flip()
                                break
                        if d.ring2 != None:
                            if mouseposition[0] > px + 140 and mouseposition[0] < px + 180 and mouseposition[1] > py + 67 and mouseposition[1] < py + 107 and mousedown:
                                selected = d.ring2.itemid
                                select = ["team",[d.name,4]]
                                buy = False
                                animateshop(merchandise,selected,select,buy,panel,shelf,coinblibs,viewcoins)
                                pygame.display.flip()
                                break
                        if d.carry != None:
                            if mouseposition[0] > px + 196 and mouseposition[0] < px + 236 and mouseposition[1] > py + 67 and mouseposition[1] < py + 107 and mousedown:
                                selected = d.carry.itemid
                                select = ["team",[d.name,5]]
                                buy = False
                                animateshop(merchandise,selected,select,buy,panel,shelf,coinblibs,viewcoins)
                                pygame.display.flip()
                                break
                        px += 254
                        if px > 300:
                            py += 120
                            px = 28
                elif mouseposition[0] > 511 and mouseposition[0] < 551 and mouseposition[1] > 252 and mouseposition[1] < 292:
                    inventoryon = False
                    break
                elif mouseposition[0] > 545 and mouseposition[0] < 560 and mouseposition[1] > 72 and mouseposition[1] < 180:
                    if panel == "inventory":
                        panel = "team"
                    else:
                        panel = "inventory"
                    animateshop(merchandise,selected,select,buy,panel,shelf,coinblibs,viewcoins)
                    pygame.display.flip()
            if event.type == pygame.MOUSEMOTION:
                mouseposition = event.pos[:]
                animateshop(merchandise,selected,select,buy,panel,shelf,coinblibs,viewcoins)
                pygame.display.flip()
def animateshop(merchandise,selected,select,buy,panel,shelf,coinblibs,viewcoins):
    global coinred,mouseposition,mousedown
    screen.blit(pygame.image.load("assets/graphics/extra/shopbuy.png"),[0,0])
    if selected != None:
        if buy == True:
            if mouseposition[0] > 70 and mouseposition[0] < 140 and mouseposition[1] > 260 and mouseposition[1] < 300 and money >= prices[selected]:
                screen.blit(pygame.image.load("assets/graphics/extra/buybuttonselect.png"),[70,255])
            else:
                screen.blit(pygame.image.load("assets/graphics/extra/buybutton.png"),[70,255])
            screen.blit(linefont.render("%s" % (prices[selected]),0,[0,0,0]),[40,355])
            if prices[selected] < 100:
                screen.blit(coppercointexture,[19,350])
            elif prices[selected] < 1000:
                screen.blit(silvercointexture,[19,350])
            else:
                screen.blit(goldencointexture,[19,350])
        else:
            if mouseposition[0] > 70 and mouseposition[0] < 140 and mouseposition[1] > 255 and mouseposition[1] < 295:
                screen.blit(pygame.image.load("assets/graphics/extra/sellbuttonselect.png"),[70,255])
            else:
                screen.blit(pygame.image.load("assets/graphics/extra/sellbutton.png"),[70,255])
            screen.blit(linefont.render("%s" % int(prices[selected] * .8),0,[0,0,0]),costpos)
            if int(prices[selected] * .8) < 100:
                screen.blit(pygame.image.load("assets/graphics/extra/coinscopper.png"),[19,350])
            elif int(prices[selected] * .8) < 1000:
                screen.blit(pygame.image.load("assets/graphics/extra/coinssilver.png"),[19,350])
            else:
                screen.blit(pygame.image.load("assets/graphics/extra/coinsgold.png"),[19,350])
        screen.blit(items[selected].texture,[12,255])
        screen.blit(linefont.render("%s" % items[selected].name,0,[0,0,0]),[10,305])
        if "ring" in items[selected].itemtype:
            screen.blit(linefont.render("ring Lv.%s" % (items[selected].level),0,[0,0,0]),[30,325])
        elif items[selected].itemtype == "ingredient":
            screen.blit(linefont.render("ingredient Lv.%s" % (items[selected].level),0,[0,0,0]),[10,325])
        else:
            screen.blit(linefont.render("%s Lv.%s" % (items[selected].itemtype,items[selected].level),0,[0,0,0]),[30,325])
        if items[selected].itemtype == "ingredient" or items[selected].itemtype == "potion" or items[selected].itemtype == "spell":
            pass
        else:
            screen.blit(linefont.render(" + %s" % items[selected].health,0,[0,0,0]),[190,260])
            screen.blit(linefont.render(" + %s" % items[selected].attack,0,[0,0,0]),[190,286])
            screen.blit(linefont.render(" + %s" % items[selected].defence,0,[0,0,0]),[190,312])
            screen.blit(linefont.render(" + %s" % items[selected].speed,0,[0,0,0]),[190,338])
            screen.blit(linefont.render(" + %s" % items[selected].luck,0,[0,0,0]),[190,364])
    if shelf > 0:
        screen.blit(pygame.image.load("assets/graphics/extra/leftstore.png"),[260,301])
    if (shelf + 1) * 12 < len(merchandise):
        screen.blit(pygame.image.load("assets/graphics/extra/rightstore.png"),[539,301])
    px = 277
    py = 305
    for p in merchandise[0 + 12 * shelf:12 + 12 * shelf]:
        if not mousedown:
            if mouseposition[0] > px and mouseposition[0] < px + 40 and mouseposition[1] > py and mouseposition[1] < py + 40:
                pass
                #screen.blit(pygame.image.load("assets/graphics/extra/slotselect.png"),[px,py])
        screen.blit(items[p].texture,[px,py])
        px += 44
        if px > 520:
            px = 277
            py += 44
    if not mousedown:
        #if mouseposition[0] > 281 and mouseposition[0] < 540 and mouseposition[1] > 308 and mouseposition[1] < 391:
         #   if (mouseposition[0] - 281) % 44 <= 40 and (mouseposition[1] - 308) % 44 <= 40:
          #      screen.blit(pygame.image.load("assets/graphics/extra/slotselect.png"),[281 + int((mouseposition[0] - 281) / 44) * 44,308 + int((mouseposition[1] - 308) / 44) * 44])
        if mouseposition[0] > 260 and mouseposition[0] < 274 and mouseposition[1] > 301 and mouseposition[1] < 383 and shelf > 0:            
            if shelf > 0:
                screen.blit(pygame.image.load("assets/graphics/extra/leftstoreselect.png"),[260,301])
        elif mouseposition[0] > 539 and mouseposition[0] < 553 and mouseposition[1] > 301 and mouseposition[1] < 383 and (shelf + 1) * 12 < len(merchandise):
            if (shelf + 1) * 12 < len(merchandise):
                screen.blit(pygame.image.load("assets/graphics/extra/rightstoreselect.png"),[539,301])
        elif mouseposition[0] > 545 and mouseposition[0] < 560 and mouseposition[1] > 72 and mouseposition[1] < 180:
            screen.blit(pygame.image.load("assets/graphics/extra/bigarrow.png"),[545,72])
        if mouseposition[0] > 511 and mouseposition[0] < 551 and mouseposition[1] > 252 and mouseposition[1] < 292:
            screen.blit(pygame.image.load("assets/graphics/extra/map2.png"),[511,252])
        else:
            screen.blit(pygame.image.load("assets/graphics/extra/map1.png"),[511,252])
    else:
        screen.blit(pygame.image.load("assets/graphics/extra/map1.png"),[511,252])
    #bagmoneypos = [271,260]
    #costpos = [19,350]
    if viewcoins < 100:
        screen.blit(pygame.image.load("assets/graphics/extra/coinscopper.png"),[276,260])
    elif viewcoins < 1000:
        screen.blit(pygame.image.load("assets/graphics/extra/coinssilver.png"),[276,260])
    else:
        screen.blit(pygame.image.load("assets/graphics/extra/coinsgold.png"),[276,260])
    screen.blit(linefont.render("%s" % viewcoins,0,[coinred,0,0]),bagmoneypos)
    if select[0] == "shop":
        if select[1] >= 12 * shelf and select[1] < 12 * shelf + 12:
            screen.blit(pygame.image.load("assets/graphics/extra/shopselect.png"),[286 + 44 * int((select[1] - 12 * shelf) % 6) - 3,308 + 44 * int((select[1] - 12 * shelf) / 6) - 3])
    if panel == "inventory":
        #screen.blit(pygame.image.load("assets/graphics/extra/shopbuy.png"),[0,0])
        screen.blit(pygame.image.load("assets/graphics/extra/inventoryslotsside.png"),[0,0])
        px = 16
        py = 13
        for p in range(len(team)):
            screen.blit(pygame.image.load("assets/graphics/extra/inventoryslots.png"),[px,py])
            px += 132
        """if not mousedown:
            #542
            if mouseposition[0] > 18 and mouseposition[0] < 18 + 131 * len(team) and mouseposition[1] > 18 and mouseposition[1] < 234:
                if (mouseposition[0] - 18) % 44 <= 40 and (mouseposition[1] - 18) % 44 <= 40:
                    pass
                    #screen.blit(pygame.image.load("assets/graphics/extra/slotselect.png"),[18 + int((mouseposition[0] - 18) / 44) * 44,18 + int((mouseposition[1] - 18) / 44) * 44])"""
        px = 18
        py = 18
        for p in inventory:
            if p != None:
                screen.blit(items[p].texture,[px,py])
            py += 44
            if py > 220:
                py = 18
                px += 44
        if select[0] == "inventory":
            screen.blit(pygame.image.load("assets/graphics/extra/shopselect.png"),[18 + 44 * int(select[1] / 5) - 3,18 + 44 * int(select[1] % 5) - 3])
    else:
        px = 28
        py = 2
        for d in team:
            screen.blit(pygame.image.load("assets/graphics/extra/shopinventoryhud2.png"),[px,py])
            if d.shield != None:
                screen.blit(pygame.image.load("assets/graphics/characters/%s.png" % d.shield.name),[px + 10,py + 10])
            screen.blit(pygame.image.load("assets/graphics/characters/%s.png" % d.name),[px + 10,py + 10])
            if d.armor != None:
                screen.blit(pygame.image.load("assets/graphics/characters/%s.png" % d.armor.name),[px + 10,py + 10])
            if d.weapon != None:
                screen.blit(pygame.image.load("assets/graphics/characters/%s.png" % d.weapon.name),[px + 10,py + 10])
            screen.blit(pygame.image.load("assets/graphics/characters/%sarm.png" % d.name),[px + 10,py + 10])
            if d.weapon != None:
                screen.blit(pygame.image.load("assets/graphics/extra/slot.png"),[px + 84,py + 13])
                if mouseposition[0] > px + 84 and mouseposition[0] < px + 124 and mouseposition[1] > py + 13 and mouseposition[1] < py + 53 and not mousedown:
                    pass
                    #screen.blit(pygame.image.load("assets/graphics/extra/slotselect.png"),[px + 84,py + 13])
                screen.blit(d.weapon.texture,[px + 84,py + 13])
            elif mouseposition[0] > px + 84 and mouseposition[0] < px + 124 and mouseposition[1] > py + 13 and mouseposition[1] < py + 53 and not mousedown:
                pass
                #screen.blit(pygame.image.load("assets/graphics/extra/weaponselect.png"),[px + 84,py + 13])
            if d.armor != None:
                screen.blit(pygame.image.load("assets/graphics/extra/slot.png"),[px + 140,py + 13])
                if mouseposition[0] > px + 140 and mouseposition[0] < px + 180 and mouseposition[1] > py + 13 and mouseposition[1] < py + 53 and not mousedown:
                    pass
                    #screen.blit(pygame.image.load("assets/graphics/extra/slotselect.png"),[px + 140,py + 13])
                screen.blit(d.armor.texture,[px + 140,py + 13])
            elif mouseposition[0] > px + 140 and mouseposition[0] < px + 180 and mouseposition[1] > py + 13 and mouseposition[1] < py + 53 and not mousedown:
                pass
                #screen.blit(pygame.image.load("assets/graphics/extra/armorselect.png"),[px + 140,py + 13])
            if d.shield != None:
                screen.blit(pygame.image.load("assets/graphics/extra/slot.png"),[px + 196,py + 13])
                if mouseposition[0] > px + 196 and mouseposition[0] < px + 236 and mouseposition[1] > py + 13 and mouseposition[1] < py + 53 and not mousedown:
                    pass
                    #screen.blit(pygame.image.load("assets/graphics/extra/slotselect.png"),[px + 196,py + 13])
                screen.blit(d.shield.texture,[px + 196,py + 13])
            elif mouseposition[0] > px + 196 and mouseposition[0] < px + 236 and mouseposition[1] > py + 13 and mouseposition[1] < py + 53 and not mousedown:
                pass
                #screen.blit(pygame.image.load("assets/graphics/extra/shieldnselect.png"),[px + 196,py + 13])
            if d.ring1 != None:
                screen.blit(pygame.image.load("assets/graphics/extra/slot.png"),[px + 84,py + 67])
                if mouseposition[0] > px + 84 and mouseposition[0] < px + 124 and mouseposition[1] > py + 67 and mouseposition[1] < py + 107 and not mousedown:
                    pass
                    #screen.blit(pygame.image.load("assets/graphics/extra/slotselect.png"),[px + 84,py + 67])
                screen.blit(d.ring1.texture,[px + 84,py + 67])
            elif mouseposition[0] > px + 84 and mouseposition[0] < px + 124 and mouseposition[1] > py + 67 and mouseposition[1] < py + 107 and not mousedown:
                pass
                #screen.blit(pygame.image.load("assets/graphics/extra/ringselect.png"),[px + 84,py + 67])
            if d.ring2 != None:
                screen.blit(pygame.image.load("assets/graphics/extra/slot.png"),[px + 140,py + 67])
                if mouseposition[0] > px + 140 and mouseposition[0] < px + 180 and mouseposition[1] > py + 67 and mouseposition[1] < py + 107 and not mousedown:
                    pass
                    #screen.blit(pygame.image.load("assets/graphics/extra/slotselect.png"),[px + 140,py + 67])
                screen.blit(d.ring2.texture,[px + 140,py + 67])
            elif mouseposition[0] > px + 140 and mouseposition[0] < px + 180 and mouseposition[1] > py + 67 and mouseposition[1] < py + 107 and not mousedown:
                pass
                #screen.blit(pygame.image.load("assets/graphics/extra/ringselect.png"),[px + 140,py + 67])
            if d.carry != None:
                screen.blit(pygame.image.load("assets/graphics/extra/slot.png"),[px + 196,py + 67])
                if mouseposition[0] > px + 196 and mouseposition[0] < px + 236 and mouseposition[1] > py + 67 and mouseposition[1] < py + 107 and not mousedown:
                    pass
                    #screen.blit(pygame.image.load("assets/graphics/extra/slotselect.png"),[px + 196,py + 67])
                screen.blit(d.carry.texture,[px + 196,py + 67])
            elif mouseposition[0] > px + 196 and mouseposition[0] < px + 236 and mouseposition[1] > py + 67 and mouseposition[1] < py + 107 and not mousedown:
                pass
                #screen.blit(pygame.image.load("assets/graphics/extra/carryselect.png"),[px + 196,py + 67])
            if select[0] == "team":
                if select[1][0] == d.name:
                    screen.blit(pygame.image.load("assets/graphics/extra/shopselect.png"),[px + 84 + 56 * int(select[1][1] % 3) - 3,py + 13 + 54 * int(select[1][1] / 3) - 3])
            px += 254
            if px > 300:
                py += 120
                px = 28
    for c in coinblibs[:]:
        screen.blit(pygame.image.load("assets/graphics/extra/coin%s.png" % c[4]),c[0:2])
playerslot = [35,285]
swordslot = [110,290]
armorslot = [swordslot[0] + 55,swordslot[1]]
shieldslot = [swordslot[0] + 55 * 2,swordslot[1]]
ring1slot = [swordslot[0],swordslot[1] + 55]
ring2slot = [swordslot[0] + 55,swordslot[1] + 55]
carryslot = [swordslot[0] + 55 * 2,swordslot[1] + 55]
def inventoryopen():
    global inventory,crafting,result,holding,team,mouseposition,mousedown
    inventoryon = True
    hud = team[0]
    animateinventory(hud,holding,crafting,result)
    pygame.display.flip()
    while inventoryon:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                playing = False
                inventoryon = False
                break
            if event.type == pygame.MOUSEBUTTONUP:
                mousedown = False
                animateinventory(hud,holding,crafting,result)
                pygame.display.flip()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mousedown = True
                if mouseposition[0] > 0 and mouseposition[0] < 25 and mouseposition[1] > 300 and mouseposition[1] < 350:
                    hud = team[team.index(hud) - 1]
                elif mouseposition[0] > 535 and mouseposition[0] < 560 and mouseposition[1] > 300 and mouseposition[1] < 350:
                    hud = team[team.index(hud) - (len(team) - 1)]
                elif mouseposition[0] > 510 and mouseposition[0] < 550 and mouseposition[1] > 350 and mouseposition[1] < 390:
                    inventoryon = False
                    break
                elif mouseposition[0] > 386 and mouseposition[0] < 426 and mouseposition[1] > 259 and mouseposition[1] < 299:
                    if crafting[0] != None:
                        if holding != None:
                            hold = holding
                            holding = crafting[0]
                            crafting[0] = hold
                        else:
                            holding = crafting[0]
                            crafting[0] = None
                    else:
                        if holding != None:
                            crafting[0] = holding
                            holding = None
                elif mouseposition[0] > 436 and mouseposition[0] < 476 and mouseposition[1] > 259 and mouseposition[1] < 299:
                    if crafting[1] != None:
                        if holding != None:
                            hold = holding
                            holding = crafting[1]
                            crafting[1] = hold
                        else:
                            holding = crafting[1]
                            crafting[1] = None
                    else:
                        if holding != None:
                            crafting[1] = holding
                            holding = None
                elif mouseposition[0] > 486 and mouseposition[0] < 526 and mouseposition[1] > 259 and mouseposition[1] < 299:
                    if crafting[2] != None:
                        if holding != None:
                            hold = holding
                            holding = crafting[2]
                            crafting[2] = hold
                        else:
                            holding = crafting[2]
                            crafting[2] = None
                    else:
                        if holding != None:
                            crafting[2] = holding
                            holding = None
                elif mouseposition[0] > 406 and mouseposition[0] < 506 and mouseposition[1] > 340 and mouseposition[1] < 390:
                    if result != None:
                        if mouseposition[0] > 436 and mouseposition[0] < 476 and mouseposition[1] > 345 and mouseposition[1] < 385:
                            if holding == None:
                                holding = result
                                result = None
                    else:
                        if hud.name == "Stella":
                            full = True
                            for d in crafting:
                                if d != None:
                                    if not items[d].itemtype == "ingredient":
                                        full = False
                                else:
                                    full = False
                            if full:
                                if items[crafting[0]].level == items[crafting[1]].level and items[crafting[1]].level == items[crafting[2]].level and items[crafting[1]].level != 6:
                                    if items[crafting[0]].potiontype == items[crafting[1]].potiontype and items[crafting[1]].potiontype == items[crafting[2]].potiontype:
                                        for d in items:
                                            if d.itemtype == "potion" and d.potiontype == items[crafting[0]].potiontype and d.level == items[crafting[0]].level:
                                                result = d.itemid
                                                break
                                        crafting = [None,None,None]
                                        for clip in range(1,15):
                                            screen.blit(pygame.image.load("assets/graphics/extra/animations/crafting/brew/craftingbrew%s.png" % clip),[400,303])
                                            pygame.display.flip()
                                            pygame.time.delay(50)
                            else:
                                full = True
                                for d in crafting:
                                    if d != None:
                                        if not items[d].itemtype == "potion":
                                            full = False
                                    else:
                                        full = False
                                if full:
                                    if items[crafting[0]].level == items[crafting[1]].level and items[crafting[1]].level == items[crafting[2]].level and items[crafting[1]].level != 6:
                                        if items[crafting[0]].potiontype == items[crafting[1]].potiontype and items[crafting[1]].potiontype == items[crafting[2]].potiontype:
                                            for d in items:
                                                if d.itemtype == "potion" and d.potiontype == items[crafting[0]].potiontype and d.level == items[crafting[0]].level + 1:
                                                    result = d.itemid
                                                    break
                                            crafting = [None,None,None]
                                            for clip in range(1,15):
                                                screen.blit(pygame.image.load("assets/graphics/extra/animations/crafting/brew/craftingbrew%s.png" % clip),[400,303])
                                                pygame.display.flip()
                                                pygame.time.delay(50)
                        elif hud.name == "Marvin":
                            full = True
                            for d in crafting:
                                if d != None:
                                    if not items[d].itemtype in ["sword","hammer","armor","shield","bow"]:
                                        full = False
                                else:
                                    full = False
                            if full:
                                if items[crafting[0]].level == items[crafting[1]].level and items[crafting[1]].level == items[crafting[2]].level and items[crafting[1]].level != 6:
                                    if items[crafting[0]].itemtype == items[crafting[1]].itemtype and items[crafting[1]].itemtype == items[crafting[2]].itemtype:
                                        for d in items:
                                            if d.itemtype == items[crafting[0]].itemtype and d.level == items[crafting[0]].level + 1:
                                                result = d.itemid
                                                break
                                    else:
                                        typ = random.choice(["sword","hammer","armor","shield","bow"])
                                        for d in items:
                                            if d.itemtype == typ and d.level == items[crafting[0]].level + 1:
                                                result = d.itemid
                                                break
                                    crafting = [None,None,None]
                                    for clip in range(1,15):
                                        screen.blit(pygame.image.load("assets/graphics/extra/animations/crafting/forge/craftingforge%s.png" % clip),[400,303])
                                        pygame.display.flip()
                                        pygame.time.delay(50)
                        elif hud.name == "Luna":
                            full = True
                            for d in crafting:
                                if d != None:
                                    if not items[d].equipt == "ring":
                                        full = False
                                else:
                                    full = False
                            if full:
                                if items[crafting[0]].level == items[crafting[1]].level and items[crafting[1]].level == items[crafting[2]].level and items[crafting[1]].level != 6:
                                    if items[crafting[0]].itemtype == items[crafting[1]].itemtype and items[crafting[1]].itemtype == items[crafting[2]].itemtype:
                                        for d in items:
                                            if d.equipt == "ring" and d.itemtype == items[crafting[0]].itemtype and d.level == items[crafting[0]].level + 1:
                                                result = d.itemid
                                                break
                                    else:
                                        typ = random.choice(["healthring","attackring","defencering","speedring","luckring"])
                                        for d in items:
                                            if d.equipt == "ring" and d.itemtype == typ and d.level == items[crafting[0]].level + 1:
                                                result = d.itemid
                                                break
                                    crafting = [None,None,None]
                                    for clip in range(1,15):
                                        screen.blit(pygame.image.load("assets/graphics/extra/animations/crafting/magic/craftingmagic%s.png" % clip),[400,303])
                                        pygame.display.flip()
                                        pygame.time.delay(50)
                            else:
                                full = True
                                for d in crafting:
                                    if d != None:
                                        if not items[d].itemtype == "wand":
                                            full = False
                                    else:
                                        full = False
                                if full:
                                    if items[crafting[0]].level == items[crafting[1]].level and items[crafting[1]].level == items[crafting[2]].level and items[crafting[1]].level != 6:
                                        for d in items:
                                            if d.itemtype == "wand" and d.level == items[crafting[0]].level + 1:
                                                result = d.itemid
                                                break
                                        crafting = [None,None,None]
                                        for clip in range(1,15):
                                            screen.blit(pygame.image.load("assets/graphics/extra/animations/crafting/magic/craftingmagic%s.png" % clip),[400,303])
                                            pygame.display.flip()
                                            pygame.time.delay(50)
                elif mouseposition[0] > 18 and mouseposition[0] < 18 + 132 * len(team) and mouseposition[1] > 18 and mouseposition[1] < 234:
                    if (mouseposition[0] - 18) % 44 <= 40 and (mouseposition[1] - 18) % 44 <= 40:
                        if inventory[5 * int((mouseposition[0] - 18) / 44) + int((mouseposition[1] - 18) / 44)] != None:
                            if holding != None:
                                hold = holding
                                holding = inventory[5 * int((mouseposition[0] - 18) / 44) + int((mouseposition[1] - 18) / 44)]
                                inventory[5 * int((mouseposition[0] - 18) / 44) + int((mouseposition[1] - 18) / 44)] = hold
                            else:
                                holding = inventory[5 * int((mouseposition[0] - 18) / 44) + int((mouseposition[1] - 18) / 44)]
                                inventory[5 * int((mouseposition[0] - 18) / 44) + int((mouseposition[1] - 18) / 44)] = None
                        else:
                            if holding != None:
                                inventory[5 * int((mouseposition[0] - 18) / 44) + int((mouseposition[1] - 18) / 44)] = holding
                                holding = None
                elif mouseposition[0] > swordslot[0] and mouseposition[0] < swordslot[0] + 40 and mouseposition[1] > swordslot[1] and mouseposition[1] < swordslot[1] + 40:
                    if hud.weapon != None:
                        if holding != None:
                            if items[holding].equipt == "weapon":
                                hud.health -= hud.weapon.health
                                hud.maxhealth -= hud.weapon.health
                                hud.attack -= hud.weapon.attack
                                hud.defence -= hud.weapon.defence
                                hud.speed -= hud.weapon.speed
                                hud.luck -= hud.weapon.luck
                                hud.health += items[holding].health
                                hud.maxhealth += items[holding].health
                                hud.attack += items[holding].attack
                                hud.defence += items[holding].defence
                                hud.speed += items[holding].speed
                                hud.luck += items[holding].luck
                                hud.delay = int(6000 / (hud.speed + hud.effect[1] * (hud.effect[0] == "swiftness")))
                                hold = holding
                                holding = hud.weapon.itemid
                                hud.weapon = items[hold]
                        else:
                            hud.health -= hud.weapon.health
                            hud.maxhealth -= hud.weapon.health
                            hud.attack -= hud.weapon.attack
                            hud.defence -= hud.weapon.defence
                            hud.speed -= hud.weapon.speed
                            hud.luck -= hud.weapon.luck
                            hud.delay = int(6000 / (hud.speed + hud.effect[1] * (hud.effect[0] == "swiftness")))
                            holding = hud.weapon.itemid
                            hud.weapon = None
                    else:
                        if holding != None:
                            if items[holding].equipt == "weapon":
                                hud.health += items[holding].health
                                hud.maxhealth += items[holding].health
                                hud.attack += items[holding].attack
                                hud.defence += items[holding].defence
                                hud.speed += items[holding].speed
                                hud.luck += items[holding].luck
                                hud.delay = int(6000 / (hud.speed + hud.effect[1] * (hud.effect[0] == "swiftness")))
                                hud.weapon = items[holding]
                                holding = None
                elif mouseposition[0] > armorslot[0] and mouseposition[0] < armorslot[0] + 40 and mouseposition[1] > armorslot[1] and mouseposition[1] < armorslot[1] + 40:
                    if hud.armor != None:
                        if holding != None:
                            if items[holding].equipt == "armor":
                                hud.health -= hud.armor.health
                                hud.maxhealth -= hud.armor.health
                                hud.attack -= hud.armor.attack
                                hud.defence -= hud.armor.defence
                                hud.speed -= hud.armor.speed
                                hud.luck -= hud.armor.luck
                                hud.health += items[holding].health
                                hud.maxhealth += items[holding].health
                                hud.attack += items[holding].attack
                                hud.defence += items[holding].defence
                                hud.speed += items[holding].speed
                                hud.luck += items[holding].luck
                                hud.delay = int(6000 / (hud.speed + hud.effect[1] * (hud.effect[0] == "swiftness")))
                                hold = holding
                                holding = hud.armor.itemid
                                hud.armor = items[hold]
                        else:
                            hud.health -= hud.armor.health
                            hud.maxhealth -= hud.armor.health
                            hud.attack -= hud.armor.attack
                            hud.defence -= hud.armor.defence
                            hud.speed -= hud.armor.speed
                            hud.luck -= hud.armor.luck
                            hud.delay = int(6000 / (hud.speed + hud.effect[1] * (hud.effect[0] == "swiftness")))
                            holding = hud.armor.itemid
                            hud.armor = None
                    else:
                        if holding != None:
                            if items[holding].equipt == "armor":
                                hud.health += items[holding].health
                                hud.maxhealth += items[holding].health
                                hud.attack += items[holding].attack
                                hud.defence += items[holding].defence
                                hud.speed += items[holding].speed
                                hud.luck += items[holding].luck
                                hud.delay = int(6000 / (hud.speed + hud.effect[1] * (hud.effect[0] == "swiftness")))
                                hud.armor = items[holding]
                                holding = None
                elif mouseposition[0] > shieldslot[0] and mouseposition[0] < shieldslot[0] + 40 and mouseposition[1] > shieldslot[1] and mouseposition[1] < shieldslot[1] + 40:
                    if hud.shield != None:
                        if holding != None:
                            if items[holding].equipt == "shield":
                                hud.health -= hud.shield.health
                                hud.maxhealth -= hud.shield.health
                                hud.attack -= hud.shield.attack
                                hud.defence -= hud.shield.defence
                                hud.speed -= hud.shield.speed
                                hud.luck -= hud.shield.luck
                                hud.health += items[holding].health
                                hud.maxhealth += items[holding].health
                                hud.attack += items[holding].attack
                                hud.defence += items[holding].defence
                                hud.speed += items[holding].speed
                                hud.luck += items[holding].luck
                                hud.delay = int(6000 / (hud.speed + hud.effect[1] * (hud.effect[0] == "swiftness")))
                                hold = holding
                                holding = hud.shield.itemid
                                hud.shield = items[hold]
                        else:
                            hud.health -= hud.shield.health
                            hud.maxhealth -= hud.shield.health
                            hud.attack -= hud.shield.attack
                            hud.defence -= hud.shield.defence
                            hud.speed -= hud.shield.speed
                            hud.luck -= hud.shield.luck
                            hud.delay = int(6000 / (hud.speed + hud.effect[1] * (hud.effect[0] == "swiftness")))
                            holding = hud.shield.itemid
                            hud.shield = None
                    else:
                        if holding != None:
                            if items[holding].equipt == "shield":
                                hud.health += items[holding].health
                                hud.maxhealth += items[holding].health
                                hud.attack += items[holding].attack
                                hud.defence += items[holding].defence
                                hud.speed += items[holding].speed
                                hud.luck += items[holding].luck
                                hud.delay = int(6000 / (hud.speed + hud.effect[1] * (hud.effect[0] == "swiftness")))
                                hud.shield = items[holding]
                                holding = None
                elif mouseposition[0] > ring1slot[0] and mouseposition[0] < ring1slot[0] + 40 and mouseposition[1] > ring1slot[1] and mouseposition[1] < ring1slot[1] + 40:
                    if hud.ring1 != None:
                        if holding != None:
                            if items[holding].equipt == "ring":
                                hud.health -= hud.ring1.health
                                hud.maxhealth -= hud.ring1.health
                                hud.attack -= hud.ring1.attack
                                hud.defence -= hud.ring1.defence
                                hud.speed -= hud.ring1.speed
                                hud.luck -= hud.ring1.luck
                                hud.health += items[holding].health
                                hud.maxhealth += items[holding].health
                                hud.attack += items[holding].attack
                                hud.defence += items[holding].defence
                                hud.speed += items[holding].speed
                                hud.luck += items[holding].luck
                                hud.delay = int(6000 / (hud.speed + hud.effect[1] * (hud.effect[0] == "swiftness")))
                                hold = holding
                                holding = hud.ring1.itemid
                                hud.ring1 = items[hold]
                        else:
                            hud.health -= hud.ring1.health
                            hud.maxhealth -= hud.ring1.health
                            hud.attack -= hud.ring1.attack
                            hud.defence -= hud.ring1.defence
                            hud.speed -= hud.ring1.speed
                            hud.luck -= hud.ring1.luck
                            hud.delay = int(6000 / (hud.speed + hud.effect[1] * (hud.effect[0] == "swiftness")))
                            holding = hud.ring1.itemid
                            hud.ring1 = None
                    else:
                        if holding != None:
                            if items[holding].equipt == "ring":
                                hud.health += items[holding].health
                                hud.maxhealth += items[holding].health
                                hud.attack += items[holding].attack
                                hud.defence += items[holding].defence
                                hud.speed += items[holding].speed
                                hud.luck += items[holding].luck
                                hud.delay = int(6000 / (hud.speed + hud.effect[1] * (hud.effect[0] == "swiftness")))
                                hud.ring1 = items[holding]
                                holding = None
                elif mouseposition[0] > ring2slot[0] and mouseposition[0] < ring2slot[0] + 40 and mouseposition[1] > ring2slot[1] and mouseposition[1] < ring2slot[1] + 40:
                    if hud.ring2 != None:
                        if holding != None:
                            if items[holding].equipt == "ring":
                                hud.health -= hud.ring2.health
                                hud.maxhealth -= hud.ring2.health
                                hud.attack -= hud.ring2.attack
                                hud.defence -= hud.ring2.defence
                                hud.speed -= hud.ring2.speed
                                hud.luck -= hud.ring2.luck
                                hud.health += items[holding].health
                                hud.maxhealth += items[holding].health
                                hud.attack += items[holding].attack
                                hud.defence += items[holding].defence
                                hud.speed += items[holding].speed
                                hud.luck += items[holding].luck
                                hud.delay = int(6000 / (hud.speed + hud.effect[1] * (hud.effect[0] == "swiftness")))
                                hold = holding
                                holding = hud.ring2.itemid
                                hud.ring2 = items[hold]
                        else:
                            hud.health -= hud.ring2.health
                            hud.maxhealth -= hud.ring2.health
                            hud.attack -= hud.ring2.attack
                            hud.defence -= hud.ring2.defence
                            hud.speed -= hud.ring2.speed
                            hud.luck -= hud.ring2.luck
                            hud.delay = int(6000 / (hud.speed + hud.effect[1] * (hud.effect[0] == "swiftness")))
                            holding = hud.ring2.itemid
                            hud.ring2 = None
                    else:
                        if holding != None:
                            if items[holding].equipt == "ring":
                                hud.health += items[holding].health
                                hud.maxhealth += items[holding].health
                                hud.attack += items[holding].attack
                                hud.defence += items[holding].defence
                                hud.speed += items[holding].speed
                                hud.luck += items[holding].luck
                                hud.delay = int(6000 / (hud.speed + hud.effect[1] * (hud.effect[0] == "swiftness")))
                                hud.ring2 = items[holding]
                                holding = None
                elif mouseposition[0] > carryslot[0] and mouseposition[0] < carryslot[0] + 40 and mouseposition[1] > carryslot[1] and mouseposition[1] < carryslot[1] + 40:
                    if hud.carry != None:
                        if holding != None:
                            if items[holding].itemtype == "potion" or items[holding].itemtype == "spell":
                                hold = holding
                                holding = hud.carry.itemid
                                hud.carry = items[hold]
                        else:
                            holding = hud.carry.itemid
                            hud.carry = None
                    else:
                        if holding != None:
                            if items[holding].itemtype == "potion" or items[holding].itemtype == "spell":
                                hud.carry = items[holding]
                                holding = None
                animateinventory(hud,holding,crafting,result)
                pygame.display.flip()
            if event.type == pygame.MOUSEMOTION:
                mouseposition = event.pos[:]
                animateinventory(hud,holding,crafting,result)
                pygame.display.flip()
def animateinventory(hud,holding,crafting,result):
    global mouseposition,mousedown
    if hud.name == "Stella" or hud.name == "Marvin" or hud.name == "Luna":
        screen.blit(pygame.image.load("assets/graphics/extra/inventoryhud2.png"),[0,0])
    else:
        screen.blit(pygame.image.load("assets/graphics/extra/inventoryhud1.png"),[0,0])
    px = 16
    for p in range(len(team)):
        screen.blit(pygame.image.load("assets/graphics/extra/inventoryslots.png"),[px,13])
        px += 132
    if not mousedown:
        if mouseposition[0] > 0 and mouseposition[0] < 25 and mouseposition[1] > 275 and mouseposition[1] < 375:
            screen.blit(pygame.image.load("assets/graphics/extra/leftselect.png"),[0,275])
        elif mouseposition[0] > 535 and mouseposition[0] < 560 and mouseposition[1] > 275 and mouseposition[1] < 375:
            screen.blit(pygame.image.load("assets/graphics/extra/rightselect.png"),[535,275])
        """elif mouseposition[0] > 18 and mouseposition[0] < 18 + 132 * len(team) and mouseposition[1] > 18 and mouseposition[1] < 234:
            if (mouseposition[0] - 18) % 44 <= 40 and (mouseposition[1] - 18) % 44 <= 40:
                pass
                screen.blit(pygame.image.load("assets/graphics/extra/slotselect.png"),[18 + int((mouseposition[0] - 18) / 44) * 44,18 + int((mouseposition[1] - 18) / 44) * 44])
        elif mouseposition[0] > swordslot[0] and mouseposition[0] < swordslot[0] + 40 and mouseposition[1] > swordslot[1] and mouseposition[1] < swordslot[1] + 40:
            if hud.weapon != None:
                screen.blit(pygame.image.load("assets/graphics/extra/slotselect.png"),swordslot)
            else:
                screen.blit(pygame.image.load("assets/graphics/extra/weaponselect.png"),swordslot)
        elif mouseposition[0] > armorslot[0] and mouseposition[0] < armorslot[0] + 40 and mouseposition[1] > armorslot[1] and mouseposition[1] < armorslot[1] + 40:
            if hud.armor != None:
                screen.blit(pygame.image.load("assets/graphics/extra/slotselect.png"),armorslot)
            else:
                screen.blit(pygame.image.load("assets/graphics/extra/armorselect.png"),armorslot)
        elif mouseposition[0] > shieldslot[0] and mouseposition[0] < shieldslot[0] + 40 and mouseposition[1] > shieldslot[1] and mouseposition[1] < shieldslot[1] + 40:
            if hud.shield != None:
                screen.blit(pygame.image.load("assets/graphics/extra/slotselect.png"),shieldslot)
            else:
                screen.blit(pygame.image.load("assets/graphics/extra/shieldselect.png"),shieldslot)
        elif mouseposition[0] > ring1slot[0] and mouseposition[0] < ring1slot[0] + 40 and mouseposition[1] > ring1slot[1] and mouseposition[1] < ring1slot[1] + 40:
            if hud.ring1 != None:
                screen.blit(pygame.image.load("assets/graphics/extra/slotselect.png"),ring1slot)
            else:
                screen.blit(pygame.image.load("assets/graphics/extra/ringselect.png"),ring1slot)
        elif mouseposition[0] > ring2slot[0] and mouseposition[0] < ring2slot[0] + 40 and mouseposition[1] > ring2slot[1] and mouseposition[1] < ring2slot[1] + 40:
            if hud.ring2 != None:
                screen.blit(pygame.image.load("assets/graphics/extra/slotselect.png"),ring2slot)
            else:
                screen.blit(pygame.image.load("assets/graphics/extra/ringselect.png"),ring2slot)
        elif mouseposition[0] > carryslot[0] and mouseposition[0] < carryslot[0] + 40 and mouseposition[1] > carryslot[1] and mouseposition[1] < carryslot[1] + 40:
            if hud.carry != None:
                screen.blit(pygame.image.load("assets/graphics/extra/slotselect.png"),carryslot)
            else:
                screen.blit(pygame.image.load("assets/graphics/extra/carryselect.png"),carryslot)
        elif hud.name == "Stella" or hud.name == "Marvin" or hud.name == "Luna":
            px = 386
            for d in crafting:
                if mouseposition[0] > px and mouseposition[0] < px + 40 and mouseposition[1] > 259 and mouseposition[1] < 299:
                    screen.blit(pygame.image.load("assets/graphics/extra/slotselect.png"),[px,259])
                px += 50
        elif hud.name == "Stella" or hud.name == "Marvin" or hud.name == "Luna":
            if mouseposition[0] > 436 and mouseposition[0] < 476 and mouseposition[1] > 345 and mouseposition[1] < 385:
                if result != None:
                    screen.blit(pygame.image.load("assets/graphics/extra/slotselect.png"),[436,345])"""
    px = 18
    py = 18
    for p in inventory:
        if p != None:
            screen.blit(items[p].texture,[px,py])
        py += 44
        if py > 220:
            py = 18
            px += 44
    screen.blit(linefont.render(hud.name,0,[180,120,0]),[35,255])
    if hud.shield != None:
        screen.blit(pygame.image.load("assets/graphics/characters/%s.png" % hud.shield.name),playerslot)
    screen.blit(pygame.image.load("assets/graphics/characters/%s.png" % hud.name),playerslot)
    if hud.armor != None:
        screen.blit(pygame.image.load("assets/graphics/characters/%s.png" % hud.armor.name),playerslot)
    if hud.weapon != None:
        screen.blit(pygame.image.load("assets/graphics/characters/%s.png" % hud.weapon.name),playerslot)
    screen.blit(pygame.image.load("assets/graphics/characters/%sarm.png" % hud.name),playerslot)
    if hud.weapon != None:
        screen.blit(pygame.image.load("assets/graphics/extra/slot.png"),swordslot)
        screen.blit(hud.weapon.texture,swordslot)
    if hud.armor != None:
        screen.blit(pygame.image.load("assets/graphics/extra/slot.png"),armorslot)
        screen.blit(hud.armor.texture,armorslot)
    if hud.shield != None:
        screen.blit(pygame.image.load("assets/graphics/extra/slot.png"),shieldslot)
        screen.blit(hud.shield.texture,shieldslot)
    if hud.ring1 != None:
        screen.blit(pygame.image.load("assets/graphics/extra/slot.png"),ring1slot)
        screen.blit(hud.ring1.texture,ring1slot)
    if hud.ring2 != None:
        screen.blit(pygame.image.load("assets/graphics/extra/slot.png"),ring2slot)
        screen.blit(hud.ring2.texture,ring2slot)
    if hud.carry != None:
        screen.blit(pygame.image.load("assets/graphics/extra/slot.png"),carryslot) 
        screen.blit(hud.carry.texture,carryslot)
    if hud.name == "Stella" or hud.name == "Marvin" or hud.name == "Luna":
        px = 386
        for d in crafting:
            if d != None:
                screen.blit(items[d].texture,[px,259])
            px += 50
        if result != None:
            screen.blit(items[result].texture,[436,345])
        else:
            craftable = False
            if hud.name == "Stella":
                full = True
                for d in crafting:
                    if d != None:
                        if not items[d].itemtype == "ingredient":
                            full = False
                    else:
                        full = False
                if full:
                    if items[crafting[0]].level == items[crafting[1]].level and items[crafting[1]].level == items[crafting[2]].level and items[crafting[1]].level != 6:
                        if items[crafting[0]].potiontype == items[crafting[1]].potiontype and items[crafting[1]].potiontype == items[crafting[2]].potiontype:
                            craftable = True
                else:
                    full = True
                    for d in crafting:
                        if d != None:
                            if not items[d].itemtype == "potion":
                                full = False
                        else:
                            full = False
                    if full:
                        if items[crafting[0]].level == items[crafting[1]].level and items[crafting[1]].level == items[crafting[2]].level and items[crafting[1]].level != 6:
                            if items[crafting[0]].potiontype == items[crafting[1]].potiontype and items[crafting[1]].potiontype == items[crafting[2]].potiontype:
                                craftable = True
            elif hud.name == "Marvin":
                full = True
                for d in crafting:
                    if d != None:
                        if not items[d].itemtype in ["sword","hammer","armor","shield","bow"]:
                            full = False
                    else:
                        full = False
                if full:
                    if items[crafting[0]].level == items[crafting[1]].level and items[crafting[1]].level == items[crafting[2]].level and items[crafting[1]].level != 6:
                        craftable = True
            elif hud.name == "Luna":
                full = True
                for d in crafting:
                    if d != None:
                        if not items[d].equipt == "ring":
                            full = False
                    else:
                        full = False
                if full:
                    if items[crafting[0]].level == items[crafting[1]].level and items[crafting[1]].level == items[crafting[2]].level and items[crafting[1]].level != 6:
                        craftable = True
                else:
                    for d in crafting:
                        if d != None:
                            if not items[d].itemtype == "wand":
                                full = False
                        else:
                            full = False
                    if full:
                        if items[crafting[0]].level == items[crafting[1]].level and items[crafting[1]].level == items[crafting[2]].level and items[crafting[1]].level != 6:
                            craftable = True
            if craftable:
                if mouseposition[0] > 406 and mouseposition[0] < 506 and mouseposition[1] > 340 and mouseposition[1] < 390:
                    screen.blit(pygame.image.load("assets/graphics/extra/craftbutton1.png"),[0,0])
                else:
                    screen.blit(pygame.image.load("assets/graphics/extra/craftbutton2.png"),[0,0])
            else:
                screen.blit(pygame.image.load("assets/graphics/extra/craftbutton1.png"),[0,0])
    else:
        if money < 100:
            screen.blit(pygame.image.load("assets/graphics/extra/coinscopper.png"),[276 + 106,260])
        elif money < 1000:
            screen.blit(pygame.image.load("assets/graphics/extra/coinssilver.png"),[276 + 106,260])
        else:
            screen.blit(pygame.image.load("assets/graphics/extra/coinsgold.png"),[276 + 106,260])
        screen.blit(linefont.render("%s" % money,0,[0,0,0]),[297 + 106,265])
    screen.blit(linefont.render("%s" % hud.maxhealth,0,[0,0,0]),[315,260])
    screen.blit(linefont.render("%s" % hud.attack,0,[0,0,0]),[315,286])
    screen.blit(linefont.render("%s" % hud.defence,0,[0,0,0]),[315,312])
    screen.blit(linefont.render("%s" % hud.speed,0,[0,0,0]),[315,338])
    screen.blit(linefont.render("%s" % hud.luck,0,[0,0,0]),[315,364])
    
    #screen.blit(linefont.render("%s" % hud.maxhealth,0,[0,0,0]),[315,255])
    #screen.blit(linefont.render("%s" % hud.attack,0,[0,0,0]),[315,281])
    #screen.blit(linefont.render("%s" % hud.defence,0,[0,0,0]),[315,307])
    #screen.blit(linefont.render("%s" % hud.speed,0,[0,0,0]),[315,333])
    #screen.blit(linefont.render("%s" % hud.luck,0,[0,0,0]),[315,359])
    if mouseposition[0] > swordslot[0] and mouseposition[0] < swordslot[0] + 40 and mouseposition[1] > swordslot[1] and mouseposition[1] < swordslot[1] + 40:
        if hud.weapon != None:
            hud.weapon.description()
    elif mouseposition[0] > armorslot[0] and mouseposition[0] < armorslot[0] + 40 and mouseposition[1] > armorslot[1] and mouseposition[1] < armorslot[1] + 40:
        if hud.armor != None:
            hud.armor.description()
    elif mouseposition[0] > shieldslot[0] and mouseposition[0] < shieldslot[0] + 40 and mouseposition[1] > shieldslot[1] and mouseposition[1] < shieldslot[1] + 40:
        if hud.shield != None:
            hud.shield.description()
    elif mouseposition[0] > ring1slot[0] and mouseposition[0] < ring1slot[0] + 40 and mouseposition[1] > ring1slot[1] and mouseposition[1] < ring1slot[1] + 40:
        if hud.ring1 != None:
            hud.ring1.description()
    elif mouseposition[0] > ring2slot[0] and mouseposition[0] < ring2slot[0] + 40 and mouseposition[1] > ring2slot[1] and mouseposition[1] < ring2slot[1] + 40:
        if hud.ring2 != None:
            hud.ring2.description()
    elif mouseposition[0] > carryslot[0] and mouseposition[0] < carryslot[0] + 40 and mouseposition[1] > carryslot[1] and mouseposition[1] < carryslot[1] + 40:
        if hud.carry != None:
            hud.carry.description()
    elif mouseposition[0] > 18 and mouseposition[0] < 18 + 132 * len(team) and mouseposition[1] > 18 and mouseposition[1] < 234:
        if (mouseposition[0] - 18) % 44 <= 40 and (mouseposition[1] - 18) % 44 <= 40:
            if inventory[5 * int((mouseposition[0] - 18) / 44) + int((mouseposition[1] - 18) / 44)] != None:
                items[inventory[5 * int((mouseposition[0] - 18) / 44) + int((mouseposition[1] - 18) / 44)]].description()
    if hud.name == "Stella" or hud.name == "Marvin" or hud.name == "Luna":
        px = 386
        for d in crafting:
            if d != None:
                if mouseposition[0] > px and mouseposition[0] < px + 40 and mouseposition[1] > 275 and mouseposition[1] < 320:
                    items[d].description()
            px += 50
    if mouseposition[0] > 510 and mouseposition[0] < 550 and mouseposition[1] > 350 and mouseposition[1] < 390:
        screen.blit(pygame.image.load("assets/graphics/extra/map2.png"),[510,350])
    else:
        screen.blit(pygame.image.load("assets/graphics/extra/map1.png"),[510,350])
    if holding != None:
        screen.blit(items[holding].texture,[mouseposition[0] - 20,mouseposition[1] - 20])
def options():
    global mouseposition,mousedown,battlespeed,doanimations,battleside,doclips
    screenup = True
    screen.blit(pygame.image.load("assets/graphics/extra/options.png"),[0,0])
    if mouseposition[0] > 29 and mouseposition[0] < 530 and mouseposition[1] > 29 and mouseposition[1] < 80:
        if battlespeed == 1:
            screen.blit(pygame.image.load("assets/graphics/extra/optionsbutton11glow.png"),[29,29])
        if battlespeed == 2:
            screen.blit(pygame.image.load("assets/graphics/extra/optionsbutton12glow.png"),[29,29])
        if battlespeed == 3:
            screen.blit(pygame.image.load("assets/graphics/extra/optionsbutton13glow.png"),[29,29])
        if battlespeed == 4:
            screen.blit(pygame.image.load("assets/graphics/extra/optionsbutton14glow.png"),[29,29])
    else:
        if battlespeed == 1:
            screen.blit(pygame.image.load("assets/graphics/extra/optionsbutton11.png"),[29,29])
        if battlespeed == 2:
            screen.blit(pygame.image.load("assets/graphics/extra/optionsbutton12.png"),[29,29])
        if battlespeed == 3:
            screen.blit(pygame.image.load("assets/graphics/extra/optionsbutton13.png"),[29,29])
        if battlespeed == 4:
            screen.blit(pygame.image.load("assets/graphics/extra/optionsbutton14.png"),[29,29])
    if mouseposition[0] > 29 and mouseposition[0] < 530 and mouseposition[1] > 101 and mouseposition[1] < 152:
        if doanimations:
            screen.blit(pygame.image.load("assets/graphics/extra/optionsbutton21glow.png"),[29,101])
        else:
            screen.blit(pygame.image.load("assets/graphics/extra/optionsbutton22glow.png"),[29,101])
    else:
        if doanimations:
            screen.blit(pygame.image.load("assets/graphics/extra/optionsbutton21.png"),[29,101])
        else:
            screen.blit(pygame.image.load("assets/graphics/extra/optionsbutton22.png"),[29,101])
    if mouseposition[0] > 29 and mouseposition[0] < 530 and mouseposition[1] > 173 and mouseposition[1] < 224:
        if battleside:
            screen.blit(pygame.image.load("assets/graphics/extra/optionsbutton31glow.png"),[29,173])
        else:
            screen.blit(pygame.image.load("assets/graphics/extra/optionsbutton32glow.png"),[29,173])
    else:
        if battleside:
            screen.blit(pygame.image.load("assets/graphics/extra/optionsbutton31.png"),[29,173])
        else:
            screen.blit(pygame.image.load("assets/graphics/extra/optionsbutton32.png"),[29,173])
    if mouseposition[0] > 29 and mouseposition[0] < 530 and mouseposition[1] > 245 and mouseposition[1] < 296:
        if doclips:
            screen.blit(pygame.image.load("assets/graphics/extra/optionsbutton41glow.png"),[29,245])
        else:
            screen.blit(pygame.image.load("assets/graphics/extra/optionsbutton42glow.png"),[29,245])
    else:
        if doclips:
            screen.blit(pygame.image.load("assets/graphics/extra/optionsbutton41.png"),[29,245])
        else:
            screen.blit(pygame.image.load("assets/graphics/extra/optionsbutton42.png"),[29,245])
    if mouseposition[0] > 510 and mouseposition[0] < 550 and mouseposition[1] > 350 and mouseposition[1] < 390:
        screen.blit(pygame.image.load("assets/graphics/extra/gear2.png"),[510,350])
    else:
        screen.blit(pygame.image.load("assets/graphics/extra/gear1.png"),[510,350])
    pygame.display.flip()
    while screenup:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                playing = False
                visit = False
                screenup = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if mouseposition[0] > 29 and mouseposition[0] < 530 and mouseposition[1] > 29 and mouseposition[1] < 80:
                    battlespeed += 1
                    if battlespeed > 4:
                        battlespeed = 1
                elif mouseposition[0] > 29 and mouseposition[0] < 530 and mouseposition[1] > 101 and mouseposition[1] < 152:
                    doanimations = not doanimations
                elif mouseposition[0] > 29 and mouseposition[0] < 530 and mouseposition[1] > 173 and mouseposition[1] < 224:
                    battleside = not battleside
                elif mouseposition[0] > 29 and mouseposition[0] < 530 and mouseposition[1] > 245 and mouseposition[1] < 296:
                    doclips = not doclips
                elif mouseposition[0] > 510 and mouseposition[0] < 550 and mouseposition[1] > 350 and mouseposition[1] < 390:
                    screenup = False
                screen.blit(pygame.image.load("assets/graphics/extra/options.png"),[0,0])
                if mouseposition[0] > 29 and mouseposition[0] < 530 and mouseposition[1] > 29 and mouseposition[1] < 80:
                    if battlespeed == 1:
                        screen.blit(pygame.image.load("assets/graphics/extra/optionsbutton11glow.png"),[29,29])
                    if battlespeed == 2:
                        screen.blit(pygame.image.load("assets/graphics/extra/optionsbutton12glow.png"),[29,29])
                    if battlespeed == 3:
                        screen.blit(pygame.image.load("assets/graphics/extra/optionsbutton13glow.png"),[29,29])
                    if battlespeed == 4:
                        screen.blit(pygame.image.load("assets/graphics/extra/optionsbutton14glow.png"),[29,29])
                else:
                    if battlespeed == 1:
                        screen.blit(pygame.image.load("assets/graphics/extra/optionsbutton11.png"),[29,29])
                    if battlespeed == 2:
                        screen.blit(pygame.image.load("assets/graphics/extra/optionsbutton12.png"),[29,29])
                    if battlespeed == 3:
                        screen.blit(pygame.image.load("assets/graphics/extra/optionsbutton13.png"),[29,29])
                    if battlespeed == 4:
                        screen.blit(pygame.image.load("assets/graphics/extra/optionsbutton14.png"),[29,29])
                if mouseposition[0] > 29 and mouseposition[0] < 530 and mouseposition[1] > 101 and mouseposition[1] < 152:
                    if doanimations:
                        screen.blit(pygame.image.load("assets/graphics/extra/optionsbutton21glow.png"),[29,101])
                    else:
                        screen.blit(pygame.image.load("assets/graphics/extra/optionsbutton22glow.png"),[29,101])
                else:
                    if doanimations:
                        screen.blit(pygame.image.load("assets/graphics/extra/optionsbutton21.png"),[29,101])
                    else:
                        screen.blit(pygame.image.load("assets/graphics/extra/optionsbutton22.png"),[29,101])
                if mouseposition[0] > 29 and mouseposition[0] < 530 and mouseposition[1] > 173 and mouseposition[1] < 224:
                    if battleside:
                        screen.blit(pygame.image.load("assets/graphics/extra/optionsbutton31glow.png"),[29,173])
                    else:
                        screen.blit(pygame.image.load("assets/graphics/extra/optionsbutton32glow.png"),[29,173])
                else:
                    if battleside:
                        screen.blit(pygame.image.load("assets/graphics/extra/optionsbutton31.png"),[29,173])
                    else:
                        screen.blit(pygame.image.load("assets/graphics/extra/optionsbutton32.png"),[29,173])
                if mouseposition[0] > 29 and mouseposition[0] < 530 and mouseposition[1] > 245 and mouseposition[1] < 296:
                    if doclips:
                        screen.blit(pygame.image.load("assets/graphics/extra/optionsbutton41glow.png"),[29,245])
                    else:
                        screen.blit(pygame.image.load("assets/graphics/extra/optionsbutton42glow.png"),[29,245])
                else:
                    if doclips:
                        screen.blit(pygame.image.load("assets/graphics/extra/optionsbutton41.png"),[29,245])
                    else:
                        screen.blit(pygame.image.load("assets/graphics/extra/optionsbutton42.png"),[29,245])
                if mouseposition[0] > 510 and mouseposition[0] < 550 and mouseposition[1] > 350 and mouseposition[1] < 390:
                    screen.blit(pygame.image.load("assets/graphics/extra/gear2.png"),[510,350])
                else:
                    screen.blit(pygame.image.load("assets/graphics/extra/gear1.png"),[510,350])
                pygame.display.flip()
            if event.type == pygame.MOUSEMOTION:
                mouseposition = event.pos[:]
                screen.blit(pygame.image.load("assets/graphics/extra/options.png"),[0,0])
                if mouseposition[0] > 29 and mouseposition[0] < 530 and mouseposition[1] > 29 and mouseposition[1] < 80:
                    if battlespeed == 1:
                        screen.blit(pygame.image.load("assets/graphics/extra/optionsbutton11glow.png"),[29,29])
                    if battlespeed == 2:
                        screen.blit(pygame.image.load("assets/graphics/extra/optionsbutton12glow.png"),[29,29])
                    if battlespeed == 3:
                        screen.blit(pygame.image.load("assets/graphics/extra/optionsbutton13glow.png"),[29,29])
                    if battlespeed == 4:
                        screen.blit(pygame.image.load("assets/graphics/extra/optionsbutton14glow.png"),[29,29])
                else:
                    if battlespeed == 1:
                        screen.blit(pygame.image.load("assets/graphics/extra/optionsbutton11.png"),[29,29])
                    if battlespeed == 2:
                        screen.blit(pygame.image.load("assets/graphics/extra/optionsbutton12.png"),[29,29])
                    if battlespeed == 3:
                        screen.blit(pygame.image.load("assets/graphics/extra/optionsbutton13.png"),[29,29])
                    if battlespeed == 4:
                        screen.blit(pygame.image.load("assets/graphics/extra/optionsbutton14.png"),[29,29])
                if mouseposition[0] > 29 and mouseposition[0] < 530 and mouseposition[1] > 101 and mouseposition[1] < 152:
                    if doanimations:
                        screen.blit(pygame.image.load("assets/graphics/extra/optionsbutton21glow.png"),[29,101])
                    else:
                        screen.blit(pygame.image.load("assets/graphics/extra/optionsbutton22glow.png"),[29,101])
                else:
                    if doanimations:
                        screen.blit(pygame.image.load("assets/graphics/extra/optionsbutton21.png"),[29,101])
                    else:
                        screen.blit(pygame.image.load("assets/graphics/extra/optionsbutton22.png"),[29,101])
                if mouseposition[0] > 29 and mouseposition[0] < 530 and mouseposition[1] > 173 and mouseposition[1] < 224:
                    if battleside:
                        screen.blit(pygame.image.load("assets/graphics/extra/optionsbutton31glow.png"),[29,173])
                    else:
                        screen.blit(pygame.image.load("assets/graphics/extra/optionsbutton32glow.png"),[29,173])
                else:
                    if battleside:
                        screen.blit(pygame.image.load("assets/graphics/extra/optionsbutton31.png"),[29,173])
                    else:
                        screen.blit(pygame.image.load("assets/graphics/extra/optionsbutton32.png"),[29,173])
                if mouseposition[0] > 29 and mouseposition[0] < 530 and mouseposition[1] > 245 and mouseposition[1] < 296:
                    if doclips:
                        screen.blit(pygame.image.load("assets/graphics/extra/optionsbutton41glow.png"),[29,245])
                    else:
                        screen.blit(pygame.image.load("assets/graphics/extra/optionsbutton42glow.png"),[29,245])
                else:
                    if doclips:
                        screen.blit(pygame.image.load("assets/graphics/extra/optionsbutton41.png"),[29,245])
                    else:
                        screen.blit(pygame.image.load("assets/graphics/extra/optionsbutton42.png"),[29,245])
                if mouseposition[0] > 510 and mouseposition[0] < 550 and mouseposition[1] > 350 and mouseposition[1] < 390:
                    screen.blit(pygame.image.load("assets/graphics/extra/gear2.png"),[510,350])
                else:
                    screen.blit(pygame.image.load("assets/graphics/extra/gear1.png"),[510,350])
                pygame.display.flip()
def playclip(name):
    global mousedown
    if doclips:
        pygame.time.set_timer(pygame.USEREVENT + 2,100)
        frame = 0
        screenup = True
        while screenup:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    playing = False
                    visit = False
                    screenup = False
                    break
                if event.type == pygame.USEREVENT + 2:
                    frame += 1
                    try:
                        screen.blit(pygame.image.load("assets/graphics/extra/animations/clips/%s/frame%s.png" % (name,frame)),[0,0])
                        pygame.display.flip()
                    except:
                        screenup = False
                        break
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    screenup = False
                    break
                if event.type == pygame.MOUSEMOTION:
                    mouseposition = event.pos[:]
    mousedown = False
def save():
    with open("assets/saves/save.pkl","wb") as setsave:
        teamsave = []
        for d in team:
            te = [d.name,None,None,None,None,None,None]
            if d.weapon != None:
                te[1] = d.weapon.itemid
            if d.armor != None:
                te[2] = d.armor.itemid
            if d.shield != None:
                te[3] = d.shield.itemid
            if d.ring1 != None:
                te[4] = d.ring1.itemid
            if d.ring2 != None:
                te[5] = d.ring2.itemid
            if d.carry != None:
                te[6] = d.carry.itemid
            teamsave.append(te)
        pickle.dump([inventory,crafting,result,holding,money,teamsave,progress,position,quests,battlespeed,battleside,doanimations,doclips,tutorial,scroll],setsave,-1)
        setsave.close()
try:
    with open("assets/saves/save.pkl","rb") as load:
        inventory,crafting,result,holding,money,teamload,progress,position,quests,battlespeed,battleside,doanimations,doclips,tutorial,scroll = pickle.load(load)
        team = []
        for t in teamload:
            team.append(character(t[0],t[1],t[2],t[3],t[4],t[5],t[6]))
        positionuse = positions[position][:]
except:
    inventory = []
    for i in range(60):
        inventory.append(None)
    crafting = [None,None,None]
    result = None
    holding = None
    money = 50
    team = [character("Jason",None,None,None,None,None,None)]
    progress = 0
    position = 0
    positionuse = positions[position][:]
    quests = []
    for q in range(1000):
        quests.append(False)
    battlespeed = 2
    battleside = True
    doanimations = True
    doclips = True
    tutorial = 1
    scroll = 10234 - 400
direction = 1
mouseposition = [0,0]
running = True
menubutton1 = [142,297]
menubutton2 = [510,350]
menubutton3 = [-80,-320]
pausebutton1 = [120,50]
pausebutton2 = [120,130]
pausebutton3 = [120,210]
pausebutton4 = [120,290]
buttonsize1 = [276,79]
buttonsize2 = [40,40]
buttonsize3 = [0,0]
buttonsize4 = [320,60]
mousedown = False
running = True
playing = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            playing = False
            break
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if mouseposition[0] > menubutton1[0] and mouseposition[0] < menubutton1[0] + buttonsize1[0] and mouseposition[1] > menubutton1[1] and mouseposition[1] < menubutton1[1] + buttonsize1[1]:
                playing = True
                if tutorial == 0:
                    animatemap()
                    pygame.display.flip()
                elif tutorial == 1:
                    playclip("beginning")
                    screen.blit(pygame.image.load("assets/graphics/city/panellatown.png"),[0,0])
                    for d in cities[0].people:
                        if quests[d.value] == False:
                            if mouseposition[0] > d.position[0] and mouseposition[0] < d.position[0] + d.size[0] and mouseposition[1] > d.position[1] and mouseposition[1] < d.position[1] + d.size[1]:
                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/city/%sglow.png" % d.name),d.facing,False),d.position)
                            else:
                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/city/%s.png" % d.name),d.facing,False),d.position)
                    pygame.display.flip()
                    readbox(["Jason! the dark wizard mavorov", "has stolen are sacred crystal"],"oldfox")
                    readbox(["If he can harness its power","he will become unstoppable"],"oldfox")
                    readbox(["You must travel to his castle","in the north to reclaim it"],"oldfox")
                    screen.blit(pygame.image.load("assets/graphics/city/panellatown.png"),[0,0])
                    for d in cities[0].people:
                        if quests[d.value] == False:
                            if mouseposition[0] > d.position[0] and mouseposition[0] < d.position[0] + d.size[0] and mouseposition[1] > d.position[1] and mouseposition[1] < d.position[1] + d.size[1]:
                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/city/%sglow.png" % d.name),d.facing,False),d.position)
                            else:
                                screen.blit(pygame.transform.flip(pygame.image.load("assets/graphics/city/%s.png" % d.name),d.facing,False),d.position)
                    pygame.display.flip()
                    pygame.time.delay(500)
                    readbox(["The first thing to do is buy","a sword at the shop"],"oldfox")
                    cities[0].visit()
            elif mouseposition[0] > menubutton2[0] and mouseposition[0] < menubutton2[0] + buttonsize2[0] and mouseposition[1] > menubutton2[1] and mouseposition[1] < menubutton2[1] + buttonsize2[1]:
                options()
            elif mouseposition[0] > menubutton3[0] and mouseposition[0] < menubutton3[0] + buttonsize3[0] and mouseposition[1] > menubutton3[1] and mouseposition[1] < menubutton3[1] + buttonsize3[1]:
                running = False
                save()
        elif event.type == pygame.MOUSEMOTION:
            mouseposition = event.pos[:]
        if not playing:
            screen.blit(pygame.image.load("assets/graphics/extra/menu.png"),[0,0])
            if mouseposition[0] > menubutton1[0] and mouseposition[0] < menubutton1[0] + buttonsize1[0] and mouseposition[1] > menubutton1[1] and mouseposition[1] < menubutton1[1] + buttonsize1[1]:
                screen.blit(pygame.image.load("assets/graphics/extra/menubutton1.png"),[0,0])
            #else:
                #screen.blit(pygame.image.load("assets/graphics/extra/menubutton1.png"),[0,0])
            if mouseposition[0] > menubutton2[0] and mouseposition[0] < menubutton2[0] + buttonsize1[0] and mouseposition[1] > menubutton2[1] and mouseposition[1] < menubutton2[1] + buttonsize1[1]:
                screen.blit(pygame.image.load("assets/graphics/extra/gear2.png"),menubutton2)
            else:
                screen.blit(pygame.image.load("assets/graphics/extra/gear1.png"),menubutton2)
            #if mouseposition[0] > menubutton3[0] and mouseposition[0] < menubutton3[0] + buttonsize[0] and mouseposition[1] > menubutton3[1] and mouseposition[1] < menubutton3[1] + buttonsize[1]:
                #screen.blit(pygame.image.load("assets/graphics/extra/menubutton3glow.png"),menubutton3)
            #else:
                #screen.blit(pygame.image.load("assets/graphics/extra/menubutton3.png"),menubutton3)
            #if mouseposition[0] > 510 and mouseposition[0] < 550 and mouseposition[1] > 350 and mouseposition[1] < 390:
                #screen.blit(pygame.image.load("assets/graphics/extra/gear2.png"),[510,310])
            #else:
                #screen.blit(pygame.image.load("assets/graphics/extra/gear1.png"),[510,310])
            pygame.display.flip()
        else:
            animatemap()
            pygame.display.flip()
    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                playing = False
                break
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                found = False
                broken = False
                for d in dungeons:
                    if broken:
                        break
                    if mouseposition[0] > d.position[0] and mouseposition[0] < d.position[0] + 30 + 40 * (d.size - 1) and mouseposition[1] > d.position[1] - scroll and mouseposition[1] < d.position[1] + 30 + 40 * (d.size - 1) - scroll:
                        if d.value <= progress + 1:
                            if position != d.value:
                                for i in range(abs(d.value - position)):
                                    positionuse[0] = float(positionuse[0])
                                    positionuse[1] = float(positionuse[1])
                                    if d.value > position:
                                        direction = 1
                                    else:
                                        direction = -1
                                    for i in range(10):
                                        positionuse[0] += (positions[position + 1 * (d.value > position) + -1 * (d.value < position)][0] - positions[position][0]) / 10.0
                                        positionuse[1] += (positions[position + 1 * (d.value > position) + -1 * (d.value < position)][1] - positions[position][1]) / 10.0
                                        for event in pygame.event.get():
                                            if event.type == pygame.QUIT:
                                                running = False
                                                playing = False
                                                menu = False
                                                break
                                            elif event.type == pygame.MOUSEMOTION:
                                                if mousedown:
                                                    scroll += mouseposition[1] - event.pos[1]
                                                    if scroll > 10234 - 400:
                                                        scroll = 10234 - 400
                                                    elif scroll < 0:
                                                        scroll = 0
                                                mouseposition = event.pos[:]
                                            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                                                mousedown = True
                                                for d in dungeons:
                                                    if mouseposition[0] > d.position[0] and mouseposition[0] < d.position[0] + 30 + 40 * (d.size - 1) and mouseposition[1] > d.position[1] - scroll and mouseposition[1] < d.position[1] + 30 + 40 * (d.size - 1) - scroll:
                                                        if d.value <= progress + 1:
                                                            if position != d.value:
                                                                position = d.value
                                                                positionuse = positions[position][:]
                                                                broken = True
                                                                break
                                            elif event.type == pygame.MOUSEBUTTONUP:
                                                mousedown = False
                                        if position == d.value:
                                            break
                                        animatemap()
                                        pygame.display.flip()
                                        pygame.time.delay(20)
                                    position += 1 * (d.value > position) + -1 * (d.value < position)
                                    positionuse = positions[position][:]
                                positionuse = positions[position][:]
                            else:
                                if d.name in clippoints:
                                    playclip(d.name)
                                if d.play():
                                    if progress < d.value:
                                        progress += 1
                                        #animation
                                else:
                                    if d.size == 1:
                                        for i in range(1,4):
                                            animatemap()
                                            screen.blit(pygame.image.load("assets/graphics/extra/loseskull%s.png" % i),[d.position[0] - 30,d.position[1] - 30 - scroll])
                                            pygame.display.flip()
                                            pygame.time.delay(100)
                                    elif d.size == 2:
                                        for i in range(1,4):
                                            animatemap()
                                            screen.blit(pygame.image.load("assets/graphics/extra/bigloseskull%s.png" % i),[d.position[0] - 25,d.position[1] - 25 - scroll])
                                            pygame.display.flip()
                                            pygame.time.delay(100)
                                for dd in team:
                                    dd.health = dd.maxhealth
                                    dd.effect = [None,0,0]
                                    dd.spellcharge = 0
                                save()
                            animatemap()
                            pygame.display.flip()
                            found = True
                if not found:
                    broken = False
                    for d in cities:
                        if broken:
                            break
                        if mouseposition[0] > d.position[0] and mouseposition[0] < d.position[0] + d.size[0] and mouseposition[1] > d.position[1] - scroll and mouseposition[1] < d.position[1] + d.size[1] - scroll:
                            if d.value <= progress + 1:
                                if position != d.value:
                                    for i in range(abs(d.value - position)):
                                        positionuse[0] = float(positionuse[0])
                                        positionuse[1] = float(positionuse[1])
                                        if d.value > position:
                                            direction = 1
                                        else:
                                            direction = -1
                                        for i in range(10):
                                            positionuse[0] += (positions[position + 1 * (d.value > position) + -1 * (d.value < position)][0] - positions[position][0]) / 10.0
                                            positionuse[1] += (positions[position + 1 * (d.value > position) + -1 * (d.value < position)][1] - positions[position][1]) / 10.0
                                            for event in pygame.event.get():
                                                if event.type == pygame.QUIT:
                                                    running = False
                                                    playing = False
                                                    menu = False
                                                    break
                                                elif event.type == pygame.MOUSEMOTION:
                                                    if mousedown:
                                                        scroll += mouseposition[1] - event.pos[1]
                                                        if scroll > 10234 - 400:
                                                            scroll = 10234 - 400
                                                        elif scroll < 0:
                                                            scroll = 0
                                                    mouseposition = event.pos[:]
                                                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                                                    mousedown = True
                                                    for d in cities:
                                                        if mouseposition[0] > d.position[0] and mouseposition[0] < d.position[0] + d.size[0] and mouseposition[1] > d.position[1] - scroll and mouseposition[1] < d.position[1] + d.size[1] - scroll:
                                                            if d.value <= progress + 1:
                                                                if position != d.value:
                                                                    position = d.value
                                                                    positionuse = positions[position][:]
                                                                    broken = False
                                                                    break
                                                elif event.type == pygame.MOUSEBUTTONUP:
                                                    mousedown = False
                                            if position == d.value:
                                                break
                                            animatemap()
                                            pygame.display.flip()
                                            pygame.time.delay(20)
                                        position += 1 * (d.value > position) + -1 * (d.value < position)
                                        positionuse = positions[position][:]
                                    positionuse = positions[position][:]
                                else:
                                    if d.name == "panellatown" and progress == 103:
                                        panellawin.visit()
                                    else:
                                        d.visit()
                                    save()
                                animatemap()
                                pygame.display.flip()
                                found = True
                                break
                if mouseposition[0] > 510 and mouseposition[0] < 550 and mouseposition[1] > 350 and mouseposition[1] < 390 and not found:
                    inventoryopen()
                    animatemap()
                    pygame.display.flip()
                    save()
                if mouseposition[0] > 510 and mouseposition[0] < 550 and mouseposition[1] > 310 and mouseposition[1] < 350:
                    menu = True
                    pygame.event.clear()
                    screen.blit(pygame.image.load("assets/graphics/extra/pausemenu.png"),[0,0])
                    if mouseposition[0] > pausebutton1[0] and mouseposition[0] < pausebutton1[0] + buttonsize4[0] and mouseposition[1] > pausebutton1[1] and mouseposition[1] < pausebutton1[1] + buttonsize4[1]:
                        screen.blit(pygame.image.load("assets/graphics/extra/pausebutton1glow.png"),pausebutton1)
                    #else:
                     #   screen.blit(pygame.image.load("assets/graphics/extra/pausebutton1.png"),pausebutton1)
                    if mouseposition[0] > pausebutton2[0] and mouseposition[0] < pausebutton2[0] + buttonsize4[0] and mouseposition[1] > pausebutton2[1] and mouseposition[1] < pausebutton2[1] + buttonsize4[1]:
                        screen.blit(pygame.image.load("assets/graphics/extra/pausebutton2glow.png"),pausebutton2)
                    #else:
                     #   screen.blit(pygame.image.load("assets/graphics/extra/pausebutton2.png"),pausebutton2)
                    if mouseposition[0] > pausebutton3[0] and mouseposition[0] < pausebutton3[0] + buttonsize4[0] and mouseposition[1] > pausebutton3[1] and mouseposition[1] < pausebutton3[1] + buttonsize4[1]:
                        screen.blit(pygame.image.load("assets/graphics/extra/pausebutton3glow.png"),pausebutton3)
                    #else:
                     #   screen.blit(pygame.image.load("assets/graphics/extra/pausebutton3.png"),pausebutton3)
                    if mouseposition[0] > pausebutton4[0] and mouseposition[0] < pausebutton4[0] + buttonsize4[0] and mouseposition[1] > pausebutton4[1] and mouseposition[1] < pausebutton4[1] + buttonsize4[1]:
                        screen.blit(pygame.image.load("assets/graphics/extra/pausebutton4glow.png"),pausebutton4)
                    #else:
                     #   screen.blit(pygame.image.load("assets/graphics/extra/pausebutton4.png"),pausebutton4)
                    pygame.display.flip()
                    while menu:
                        for event in pygame.event.get():
                            if event.type < 27:
                                if event.type == pygame.QUIT:
                                    running = False
                                    playing = False
                                    menu = False
                                    break
                                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                                    if mouseposition[0] > pausebutton1[0] and mouseposition[0] < pausebutton1[0] + buttonsize4[0] and mouseposition[1] > pausebutton1[1] and mouseposition[1] < pausebutton1[1] + buttonsize4[1]:
                                        menu = False
                                        animatemap()
                                        pygame.display.flip()
                                    elif mouseposition[0] > pausebutton2[0] and mouseposition[0] < pausebutton2[0] + buttonsize4[0] and mouseposition[1] > pausebutton2[1] and mouseposition[1] < pausebutton2[1] + buttonsize4[1]:
                                        options()
                                        animatemap()
                                        pygame.display.flip()
                                    elif mouseposition[0] > pausebutton3[0] and mouseposition[0] < pausebutton3[0] + buttonsize4[0] and mouseposition[1] > pausebutton3[1] and mouseposition[1] < pausebutton3[1] + buttonsize4[1]:
                                        save()
                                    elif mouseposition[0] > pausebutton4[0] and mouseposition[0] < pausebutton4[0] + buttonsize4[0] and mouseposition[1] > pausebutton4[1] and mouseposition[1] < pausebutton4[1] + buttonsize4[1]:
                                        save()
                                        running = False
                                        playing = False
                                        menu = False
                                        break
                                    if menu:
                                        screen.blit(pygame.image.load("assets/graphics/extra/pausemenu.png"),[0,0])
                                        if mouseposition[0] > pausebutton1[0] and mouseposition[0] < pausebutton1[0] + buttonsize4[0] and mouseposition[1] > pausebutton1[1] and mouseposition[1] < pausebutton1[1] + buttonsize4[1]:
                                            screen.blit(pygame.image.load("assets/graphics/extra/pausebutton1glow.png"),pausebutton1)
                                        #else:
                                         #   screen.blit(pygame.image.load("assets/graphics/extra/pausebutton1.png"),pausebutton1)
                                        if mouseposition[0] > pausebutton2[0] and mouseposition[0] < pausebutton2[0] + buttonsize4[0] and mouseposition[1] > pausebutton2[1] and mouseposition[1] < pausebutton2[1] + buttonsize4[1]:
                                            screen.blit(pygame.image.load("assets/graphics/extra/pausebutton2glow.png"),pausebutton2)
                                        #else:
                                         #   screen.blit(pygame.image.load("assets/graphics/extra/pausebutton2.png"),pausebutton2)
                                        if mouseposition[0] > pausebutton3[0] and mouseposition[0] < pausebutton3[0] + buttonsize4[0] and mouseposition[1] > pausebutton3[1] and mouseposition[1] < pausebutton3[1] + buttonsize4[1]:
                                            screen.blit(pygame.image.load("assets/graphics/extra/pausebutton3glow.png"),pausebutton3)
                                        #else:
                                         #   screen.blit(pygame.image.load("assets/graphics/extra/pausebutton3.png"),pausebutton3)
                                        if mouseposition[0] > pausebutton4[0] and mouseposition[0] < pausebutton4[0] + buttonsize4[0] and mouseposition[1] > pausebutton4[1] and mouseposition[1] < pausebutton4[1] + buttonsize4[1]:
                                            screen.blit(pygame.image.load("assets/graphics/extra/pausebutton4glow.png"),pausebutton4)
                                        #else:
                                         #   screen.blit(pygame.image.load("assets/graphics/extra/pausebutton4.png"),pausebutton4)
                                        pygame.display.flip()
                                if event.type == pygame.MOUSEMOTION:
                                    mouseposition = event.pos[:]
                                    if menu:
                                        screen.blit(pygame.image.load("assets/graphics/extra/pausemenu.png"),[0,0])
                                        if mouseposition[0] > pausebutton1[0] and mouseposition[0] < pausebutton1[0] + buttonsize4[0] and mouseposition[1] > pausebutton1[1] and mouseposition[1] < pausebutton1[1] + buttonsize4[1]:
                                            screen.blit(pygame.image.load("assets/graphics/extra/pausebutton1glow.png"),pausebutton1)
                                        #else:
                                         #   screen.blit(pygame.image.load("assets/graphics/extra/pausebutton1.png"),pausebutton1)
                                        if mouseposition[0] > pausebutton2[0] and mouseposition[0] < pausebutton2[0] + buttonsize4[0] and mouseposition[1] > pausebutton2[1] and mouseposition[1] < pausebutton2[1] + buttonsize4[1]:
                                            screen.blit(pygame.image.load("assets/graphics/extra/pausebutton2glow.png"),pausebutton2)
                                        #else:
                                         #   screen.blit(pygame.image.load("assets/graphics/extra/pausebutton2.png"),pausebutton2)
                                        if mouseposition[0] > pausebutton3[0] and mouseposition[0] < pausebutton3[0] + buttonsize4[0] and mouseposition[1] > pausebutton3[1] and mouseposition[1] < pausebutton3[1] + buttonsize4[1]:
                                            screen.blit(pygame.image.load("assets/graphics/extra/pausebutton3glow.png"),pausebutton3)
                                        #else:
                                         #   screen.blit(pygame.image.load("assets/graphics/extra/pausebutton3.png"),pausebutton3)
                                        if mouseposition[0] > pausebutton4[0] and mouseposition[0] < pausebutton4[0] + buttonsize4[0] and mouseposition[1] > pausebutton4[1] and mouseposition[1] < pausebutton4[1] + buttonsize4[1]:
                                            screen.blit(pygame.image.load("assets/graphics/extra/pausebutton4glow.png"),pausebutton4)
                                        #else:
                                         #   screen.blit(pygame.image.load("assets/graphics/extra/pausebutton4.png"),pausebutton4)
                                        pygame.display.flip()
                            if not menu:
                                break
                            #animatemap()
                if not found:
                    mousedown = True
            elif event.type == pygame.MOUSEBUTTONUP:
                mousedown = False
            elif event.type == pygame.MOUSEMOTION:
                if mousedown:
                    scroll += mouseposition[1] - event.pos[1]
                    if scroll > 10234 - 400:
                        scroll = 10234 - 400
                    elif scroll < 0:
                        scroll = 0
                mouseposition = event.pos[:]
                animatemap()
                pygame.display.flip()
pygame.quit()
