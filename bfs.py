# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 18:38:55 2022

@author: aynur
"""

grafik={'A':['B','C'],
        'B':['D','E'],
        'C':['F','G'],
        'D':['I','İ','J'],
        'E':['K','L'],
        'F':['M','N'],
        'G':[],
        'I':[],
        'İ':[],
        'J':[],
        'K':[],
        'L':[],
        'M':[],
        'N':[],
        
        }
ziyaret=[]
yıgın=[]
def bfs(ziyaret, grafik, dügüm):
    ziyaret.append(dügüm)
    yıgın.append(dügüm)
    while yıgın:
        s=yıgın.pop(0)
        print(s)
        
        for komsu in grafik[s]:
            if komsu not in ziyaret:
                yıgın.append(komsu)
                
bfs(ziyaret, grafik, 'A')