# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 09:26:06 2022

@author: pierr
"""

"""La classe Warrior a les attributs suivants :

dégat : valeur aléatoire entre 3 et 5
chance : valeur de 5
fuite : valeur de 3
prix : valeur de 10
type d'unité : "warrior"

Note : la fonction choice du module random peut vous aider, e.g. random.choice(range(10)), random.choice(["ceci", "est", "un", "test"])
"""
import random
class Warrior:
    
    damage = random.randrange(3,5)
    luck = 5
    flee = 3
    price = 10
    type = "warrior"
    
    


