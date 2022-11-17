from random import random

class Zombie :
    def __init__(self) -> None:      
        damage = random.randrange(1, 2, 0.1)
        loot = random.randrange(0.5, 1, 0.1)