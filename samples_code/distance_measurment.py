# -*- coding: utf-8 -*-
import sys
import math
from SimpleCV import *

cam = Camera(0,{"width":1280,"height":720})

tmp = Image("pepsi_logo3.png").grayscale()
object_width = 66
object_height= 116


"""
m = []
f = 10
for i in range(0,f):
    img = cam.getImage().grayscale()

    match = img.findKeypointMatch(tmp, quality=400.0, minDist=0.6, minMatch=0.20)

    if match:
        match.draw(color = (128,40,40), width=4, autocolor=False)
        center = match.coordinates()
        m.append(center)
        if len(m)== 1:
            x1 = m.pop(0)
            x1 = x1.tolist()
            x1 = x1.pop()
            x_1 = x1.pop(0)
            y_1 = x1.pop(0)
            x_1 = int(float(x_1))
            y_1 = int(float(y_1))
            m.append(x_1)
            m.append(y_1)

"""
"""
    Legenda:
    x --> točka ujemanja na okvirju (1280,720). Točka je lahko tudi y,
    vendar morate potem računati na podlagi višine slike in pikslov.
    W --> širina okvirja (frame)na kameri (1280 pixlov).
    H --> velikost okvrija (frame) na kameri (720 pixlov).

    IW --> realna širina v okolju. Širina slike v milimetrih. Širina se
    povečuje, če je razdalja objekta daljša.
    IH --> realna višina v okolju. Širina slike je v milimetrih. Višina
    se na povečevanje razdalje objekta povečuje.
    Pmm --> razmerje med širino okvirja(pixel) in širino slike(mm)
    Wr --> razmerje realne širine in realne razdalje. To je konstatno
    fiksno razmerje 0.92
    OW --> širina objekta, ki ga zmerimo v milimetrih.
    OH --> višina objekta, ki ga zmerimo v milimetrih.
    r --> razdalja med objektom in kamero.
    D --> razdalja, ko je 1pix/mm
"""
"""    
x = x_1
y = y_1
print x
print y
W = img.width
IW = 1280
Pmm = W/IW
D = 1391
r = []
OW = 66
"""

img = cam.live().grayscale()

while True:
    match = img.findKeypointMatch(tmp, quality=400.0, minDist=0.6, minMatch=0.20)

    if match:
        match.draw(color = (128,40,40), width=4, autocolor=False)
        center = match.coordinates()
        match.show()
