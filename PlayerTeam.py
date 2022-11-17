import team

class PlayerTeam(team):

    __nb_warriors : int
    __nb_hunters : int
    __nb_wizards :int
    __damage : float
    __luck : float
    __flee : float

    def __init__(self) -> None:
        super.__init__(self)
        

    def get_team_damage(self) -> float:
        tt_dmg = 0
        for memb in self.members:
            tt_dmg += memb.damage
        return tt_dmg

    def get_team_luck(self) -> float:
        tt_luck = 0
        for memb in self.members:
            tt_luck += memb.luck
        return tt_luck

    def get_team_flee(self) -> float:
        tt_flee = 0
        for memb in self.members:
            tt_flee += memb.flee
        return tt_flee

    def get_nb_warrior(self) -> int:
        return self.__nb_warriors

    def get_nb_hunter(self) -> int:
        return self.__nb_hunters

    def get_nb_wizards(self) -> int:
        return self.__nb_wizards

    def __repr__(self) -> str:
        return "AllyTeam(__nb_warriors='{}', __nb_hunters='{}', __nb_wizards='{}', __damage='{}', __luck='{}', __flee='{}'".format(self.__nb_warriors, self.__nb_hunters, self.__nb_wizards, self.__damage, self.__luck, self.__flee)
