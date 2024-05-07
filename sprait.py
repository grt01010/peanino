import pygame as pg

class Hota:
    def __init__(self, x, y, HacBaHie, dlina, kart, kart_nas,):
        self.HacBaHie =HacBaHie
        self.dlina = dlina
        self.kart = kart 
        self.kBadrat = pg.Rect([x, y], kart.get_size())
        self.kart_nas = kart_nas
        self.zByk = pg.mixer.Sound(F'Sounds/{self.HacBaHie}.ogg')
        self.has=0

    def ris(self, okno):
        okno.blit(self.kart, self.kBadrat)

    def dbig(self):
        self.kBadrat.y = self.kBadrat.y + 5

    def klik(self):
        self.kart = self.kart_nas
        a = pg.mixer.find_channel()
        if a == None:
            pg.mixer.stop()
        else:
            a.queue(self.zByk)
        self.zByk.play()
        self.has=1