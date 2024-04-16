import pygame as pg
import setimg as se

class Mene:
    def __init__(self, game):
        self.kart_mene = pg.image.load('menu.png')
        self.kart_mene = pg.transform.scale(self.kart_mene, se.SIZE)
        self.game = game
        

    def ris(self):
        self.game.screen.blit(self.kart_mene, [0, 0])

        pg.display.flip()  

    def event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()

    def update(self):
        pass
