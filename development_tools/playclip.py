import random,pygame,pickle
pygame.init()
linefont = pygame.font.Font(None,30)
screen = pygame.display.set_mode([560,400])
doclips = True
running = True
def playclip(name):
    global running
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
                if event.type == pygame.MOUSEBUTTONDOWN:
                    screenup = False
                    break
                if event.type == pygame.MOUSEMOTION:
                    mouseposition = event.pos[:]
for d in range(100):
    if not running:
        break
    playclip("mazorovdefeat")
    #pygame.time.delay(1000)
pygame.quit()
