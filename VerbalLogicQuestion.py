# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 21:05:15 2022

@author: Elif
"""
from logic import *
kisiler = ["Ayse", "Onur", "Tülin", "Mehmet","Efe"]
yayinlar = ["Makale", "Deneme", "Şiir"]

symbols = []
for kisi in kisiler:
    for yayin in yayinlar:
        symbols.append(Symbol(f"{kisi}{yayin}"))
        
knowledge = And()

for kisi in kisiler:
    knowledge.add(Or(
        Symbol(f"{kisi}Makale"),
        Symbol(f"{kisi}Deneme"),
        Symbol(f"{kisi}Şiir")
        )
        )
def check_knowledge(knowledge):
    for symbol in symbols:
        if model_check(knowledge, symbol):
            print(f"{symbol}: YES", "green")
        elif not model_check(knowledge, Not(symbol)):
            print(f"{symbol}: MAYBE")

for kisi in kisiler:
    for kisi1 in kisiler:
        for kisi2 in kisiler:
            if kisi1 != kisi2:
                knowledge.add(
                    Implication(
                        Symbol(f"{kisi1}{yayin}"), Not(Symbol(f"{kisi2}{yayin}"))
                    )
                )
                    
for kisi in kisiler:
    for yayin1 in yayinlar:
        for yayin2 in yayinlar:
            if yayin1 != yayin2:
                knowledge.add(
                    Implication(
                        Symbol(f"{kisi}{yayin1}"), Not(Symbol(f"{kisi}{yayin2}")))
                    )
                
               
knowledge.add(
    Not(Symbol("OnurDeneme"))
)
knowledge.add(
   Symbol("AyseMakale")
 )
knowledge.add(
    Symbol("EfeDeneme")
    )
knowledge.add(  
   Not(Symbol("OnurSiir")))
knowledge.add(
    Symbol("OnurMakale")
    )
   
                 
print(check_knowledge(knowledge))