import pygame as pg
import setimg as se
import pygame.freetype as pf
import pesha as pa

class Mene:
    def __init__(self, game):
        self.kart_mene = pg.image.load('menu.png')
        self.kart_mene = pg.transform.scale(self.kart_mene, se.SIZE)
        self.game = game
        self.srift=pf.Font('teddy-bear.ttf',40)
        self.pes1 = [255, 87, 51]
        self.pes2 = [51, 255, 189]
        self.pes3 = [51, 255, 189]
        self.nomer = 1

        

    def ris(self):
        
        self.game.screen.blit(self.kart_mene, [0, 0])
        self.srift.render_to(self.game.screen, [20, 30], 'лес ёлка роды', self.pes1)
        self.srift.render_to(self.game.screen, [20, 80], 'белая берёзка под моим окном', self.pes2)
        self.srift.render_to(self.game.screen, [20, 130], 'вечер', self.pes3)

        pg.display.flip()  

    def event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN:
                if event.key  == pg.K_DOWN:
                    if self.nomer == 1:
                        self.nomer=2
                        self.pes1 = [51, 255, 189]
                        self.pes2 = [255, 87, 51]

                    elif self.nomer == 2:
                        self.nomer=3
                        self.pes2 = [51, 255, 189]
                        self.pes3 = [255, 87, 51]
                    elif self.nomer == 3:
                        self.nomer=1
                        self.pes3 = [51, 255, 189]
                        self.pes1 = [255, 87, 51]
                if event.key  == pg.K_UP:
                    if self.nomer == 1:
                        self.nomer=3
                        self.pes1 = [51, 255, 189]
                        self.pes3 = [255, 87, 51]
                    elif self.nomer == 2:
                        self.nomer=1
                        self.pes2 = [51, 255, 189]
                        self.pes1 = [255, 87, 51]
                    elif self.nomer == 3:
                        self.nomer=2
                        self.pes3 = [51, 255, 189]
                        self.pes2 = [255, 87, 51]

                if event.key == pg.K_RETURN:
                    self.game.igra=1
                    self.game.pesha.spisok_hota = []
                    if self.nomer == 1:
                        self.game.pesha=pa.Pesha(se.CHRISTMAS_TREE_NOTES, se.CHRISTMAS_TREE_DURATION)
                    if self.nomer == 2:
                        self.game.pesha=pa.Pesha(se.BIRCH_NOTES, se.BIRCH_DURATION)
                    if self.nomer == 3:
                        self.game.pesha=pa.Pesha(se.MORNING_NOTES, se.MORNING_DURATION)





    def update(self):
        pass
