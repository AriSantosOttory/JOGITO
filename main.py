import pygame

from game import Game

g = Game() #facilitar toda essa bagaça!

while g.running:
    g.curr_menu.display_menu()
    g.game_loop()

pygame.quit()
