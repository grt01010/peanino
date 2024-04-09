import pygame as pg
import setimg as se
import sprait as sp
import random as ra
import pesha as pa
import pygame.freetype as pf


pg.init()



class Game:
    def __init__(self):
        self.pesha = pa.Pesha(se.BIRCH_NOTES, se.BIRCH_DURATION)
        self.screen = pg.display.set_mode(se.SIZE)
        self.casi = pg.time.Clock()
        self.kones = pf.Font(None, 11)
        


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
            if event.type == pg.MOUSEBUTTONDOWN:
                for asd in self.pesha.spisok_hota:
                    if asd.kBadrat.collidepoint(event.pos) and asd.has==0:
                        asd.klik()
        

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
        if  self.pesha.kallis==self.pesha.ciclo:
            self.kones.render_to(self.screen, [se.SIZE[0]/2, se.SIZE[1]/2], 'конец игры')

        pg.display.flip()   

        

if __name__ == "__main__":
    Game()