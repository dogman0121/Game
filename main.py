import pygame
import sys
from player import Player
from chest import Chest
from chest_interface import Interface


class Window:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((600,600))
        pygame.display.set_caption("О май гад!")
        player = Player()
        chest = Chest()
        interface = Interface()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        player.mright = True
                    if event.key == pygame.K_a:
                        player.mleft = True
                    if event.key == pygame.K_w:
                        player.mup = True
                    if event.key == pygame.K_s:
                        player.mdown = True
                    if event.key == pygame.K_SPACE:
                        interface.opened = bool(interface.opened ^ True)
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_d:
                        player.mright = False
                    if event.key == pygame.K_a:
                        player.mleft = False
                    if event.key == pygame.K_w:
                        player.mup = False
                    if event.key == pygame.K_s:
                        player.mdown = False
            player.update()
            self.display.fill((0,0,0))
            self.display.blit(player.screen, (player.x,player.y))
            self.display.blit(chest.screen, (300, 300))
            if interface.opened:
                self.display.blit(interface.screen, (150,100))
            pygame.display.flip()

Window()


