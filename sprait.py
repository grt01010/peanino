import pygame as pg

class Hota:
    def __init__(self, x, y, HacBaHie, dlina, kart):
        self.HacBaHie =HacBaHie
        self.dlina = dlina
        self.kart = kart 
        self.kBadrat = pg.Rect([x, y], kart.get_size())

    def ris(self, okno):
        okno.blit(self.kart, self.kBadrat)

    def dbig(self):
        self.kBadrat.y = self.kBadrat.y + 2