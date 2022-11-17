# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 10:02:57 2022

@author: pierr


Member
SebastienMorais commented

La classe Team est abstraite. Elle a pour attribut protégé _members et les méthodes :

__init__(self, members)
__len__(self)
__getitem__(self)

Optionnel : vous pouvez implémenter la méthode magique __iter__(self) qui vous retournera une instance de TeamIterator (développement optionnel #8) :

__iter__(self) -> TeamIterator
"""
from abc import ABC


class team(ABC): # hériter de ABC(Abstract base class)

    _members = []
    def __init__(self, members):
        self.members = members
        
    def __len__(self,members):
        lenght = len(members)
        return lenght
        
    def __getitem__(self,index):
        return self.members[index]
        
    


          