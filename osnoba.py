import pygame as pg
import setimg as se

# Инициализация pg
pg.init()



class Game:
    def __init__(self):

        # Создание окна
        self.screen = pg.display.set_mode(se.SIZE)


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
        while asd > 0:
            pg.draw.line(self.screen, [0,0,0],[dsa,0],[dsa,se.SIZE[1]])
            pg.display.flip()
            asd = asd - 1
            dsa = dsa + se.SIRINA_POLOSKI
        

if __name__ == "__main__":
    Game()