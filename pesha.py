import pygame as pg
import setimg as se
import sprait as sp
import random as ra

class Pesha:
    def __init__(self, hazbahie_hot, dlitelhoct_hot):
        self.hazbahie_hot = hazbahie_hot
        self.dlitelhoct_hot = dlitelhoct_hot
        self.spisok_hota=[]
        self.kartinka_mani = pg.image.load('long_tile_pressed.png')
        self.kartinka_mini = pg.image.load('short_tile_pressed.png')
        self.kartinka_mani_nas = pg.image.load('long_tile.png')
        self.kartinka_mini_nas = pg.image.load('short_tile.png')
        self.breme = 0
        self.breme_nota = 0
        self.mani=[self.kartinka_mini, self.kartinka_mani]
        self.mani_nas=[self.kartinka_mini_nas, self.kartinka_mani_nas]
        self.ciclo = 0
        self.kallis = len(self.hazbahie_hot)
        

    def socd(self):
        asd=ra.randint(0,se.POLOSKI-1)
        if self.breme-self.breme_nota >1000 and self.kallis>self.ciclo :
            a = self.dlitelhoct_hot[self.ciclo]
            self.hota = sp.Hota(asd*se.SIRINA_POLOSKI, 0, self.hazbahie_hot[self.ciclo], a, self.mani[a-1], self.mani_nas[a-1])
            self.ciclo = self.ciclo + 1
            self.spisok_hota.append(self.hota)
            self.breme_nota=pg.time.get_ticks()    
        
    
    def ris(self, okno):
        for a in self.spisok_hota:
            a.ris(okno)
    
    def dbug(self):
        for a in self.spisok_hota:
            a.dbig()
        self.breme=pg.time.get_ticks()