import pygame
pygame.init()
pygame.mixer.init()
chan = pygame.mixer.Channel(1)
fileo = open("assets/audio/monsters/albatross.wav","r")
sound = pygame.mixer.Sound(fileo)
chan.queue(sound)
while chan.get_busy():
  pass
fileo.close()
