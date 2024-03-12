import pygame as pg
import setimg as se
import sprait as sp

pg.init()



class Game:
    def __init__(self):
        self.kartinka = pg.image.load('long_tile_pressed.png')
        self.screen = pg.display.set_mode(se.SIZE)
        self.hota = sp.Hota(50, 50, "c4", 2, self.kartinka)


        self.run()

    def run(self):
        while True:
            self.event()
            self.update()
            self.ris()

    def event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()

    def update(self):
        ...

    def ris(self):
        self.screen.fill([255,255,255])
        asd = se.POLOSKI
        dsa = se.SIRINA_POLOSKI
        self.hota.ris(self.screen)
        while asd > 0:
            pg.draw.line(self.screen, [0,0,0],[dsa,0],[dsa,se.SIZE[1]])
            asd = asd - 1
            dsa = dsa + se.SIRINA_POLOSKI
        pg.display.flip()    
        

if __name__ == "__main__":
    Game()