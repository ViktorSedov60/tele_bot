from datetime import datetime as dt
# from time import sleep


class Player:
    __LVL, __HEALTH = 1, 100
    __slots__ = ['__lvl', '__health', '__born']

    def __init__(self):
        self.__lvl = Player.__LVL
        self.__health = Player.__HEALTH
        self.__born = dt.now()
    @property
    def lvl(self):
        return self.__lvl, f'{dt.now() - self.__born}' #вычисляем время жизни персонажа


    # def get__lvl(self):  заменили на  @property
    #     return self.__lvl

    @lvl.setter
    def lvl(self, numeric):
        self.__lvl += Player.__typeTest(numeric)
        if self.__lvl >= 100: self.__lvl = 100

    @classmethod
    def set_cls_field(cls, lvl=1, health=100):
        cls.__LVL = lvl
        cls.__HEALTH = health

    # def set__lvl(self, numeric): заменили на @lvl.setter
    #     self.__lvl += numeric

    @staticmethod
    def __typeTest(value):
        if isinstance(value, int):
            return value
        else:
            raise  TypeError('Must be int')