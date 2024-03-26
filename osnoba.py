import pygame as pg
import setimg as se
import sprait as sp
import random as ra
import pesha as pa

pg.init()



class Game:
    def __init__(self):
        self.pesha=pa.Pesha(1, 2)
        self.screen = pg.display.set_mode(se.SIZE)
        self.casi=pg.time.Clock()
        


        self.run()

    def run(self):
        while True:
            self.event()
            self.update()
            self.ris()
            self.casi.tick(60)
            
            

    def event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
        

    def update(self):
        self.pesha.socd()
        self.pesha.dbug()

    def ris(self):
        self.screen.fill([255,255,255])
        asd = se.POLOSKI
        dsa = se.SIRINA_POLOSKI
        self.pesha.ris(self.screen)
        while asd > 0:
            pg.draw.line(self.screen, [0,0,0],[dsa,0],[dsa,se.SIZE[1]])
            asd = asd - 1
            dsa = dsa + se.SIRINA_POLOSKI
        pg.display.flip()    
        

if __name__ == "__main__":
    Game()