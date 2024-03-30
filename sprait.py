import pygame as pg

class Hota:
    def __init__(self, x, y, HacBaHie, dlina, kart, kart_nas):
        self.HacBaHie =HacBaHie
        self.dlina = dlina
        self.kart = kart 
        self.kBadrat = pg.Rect([x, y], kart.get_size())
        self.kart_nas = kart_nas
        self.zByk = pg.mixer.Sound('Sounds/a-0.ogg')

    def ris(self, okno):
        okno.blit(self.kart, self.kBadrat)

    def dbig(self):
        self.kBadrat.y = self.kBadrat.y + 5

    def klik(self):
        self.kart = self.kart_nas
        self.zByk.play()