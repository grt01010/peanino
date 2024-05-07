import pygame as pg
import setimg as se
import sprait as sp
import random as ra
import pesha as pa
import pygame.freetype as pf
import mene as me


pg.init()
pg.mixer.init(channels=10)



class Game:
    def __init__(self):
        self.pesha = pa.Pesha(se.BIRCH_NOTES, se.BIRCH_DURATION)
        self.screen = pg.display.set_mode(se.SIZE)
        self.casi = pg.time.Clock()
        self.kones = pf.Font(None, 11)
        self.mene = me.Mene(self)
        self.igra = 0
        


        self.run()

    def run(self):
        while True:
            if self.igra==0:
                self.mene.event()
                self.mene.update() 
                self.mene.ris()
            else:
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
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    self.igra = 0
                    pg.mixer.stop()
                    


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
        if  self.pesha.kallis==self.pesha.ciclo and self.pesha.spisok_hota[-1].kBadrat.y>600 :
            nena=self.pesha.nasok()
            if nena == 0:
                self.kones.render_to(self.screen, [se.SIZE[0]/2, se.SIZE[1]/2], 'вы победили')
            if nena > 0:
                self.kones.render_to(self.screen, [se.SIZE[0]/2, se.SIZE[1]/2], 'вы проиграли')

        pg.display.flip()   

        
if __name__ == "__main__":
    Game()