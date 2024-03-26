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
        self.breme = 0
        self.breme_nota = 0
        self.mani=[self.kartinka_mini, self.kartinka_mani]
        
        

    def socd(self):
        asd=ra.randint(0,se.POLOSKI-1)
        if self.breme-self.breme_nota >1000:
            self.hota = sp.Hota(asd*se.SIRINA_POLOSKI, 0, "c4", 1, self.mani[ra.randint(0, 1)])
            self.spisok_hota.append(self.hota)
            self.breme_nota=pg.time.get_ticks()
        
    
    def ris(self, okno):
        for a in self.spisok_hota:
            a.ris(okno)
    
    def dbug(self):
        for a in self.spisok_hota:
            a.dbig()
        self.breme=pg.time.get_ticks()