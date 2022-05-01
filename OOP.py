# from tkinter import TK

"""Объект - это единица информации в памяти
экземпляр - конкретный объект какого то  класса
класс - инструкция по созданию объектов определенного типа
метод - функция в классе для воздействия на объект
поля или свойства - переменные в классе
атроибуты - все имена в классе: переменных и методов"""

class Purse: # пример программы кошелька с инкапсуляцией - это __, усли _ то можно изменить
    pass

    def __init__(self, valuta, name = 'Unknown'):
        if valuta not in ('USD', 'EUR'):
            raise ValueError
        self.__money = 0.00
        self.valuta = valuta
        self.name = name
    def top_up_balance(self, skoko):
        self.__money = self.__money + skoko
        return skoko

    def top_down_balance(self, skoko):
        if self.__money - skoko < 0:
            print('Мало денег на счете')
            raise ValueError('Мало денег на счете')
        self.__money = self.__money - skoko
        return skoko

    def info(self):
        print(self.__money)

    def __del__(self):
        print('Кошелек удален')
        return self.__money

x = Purse('USD')
y = Purse('EUR', 'Xren')
x.top_up_balance(100)
y.top_up_balance(100)
x.top_up_balance(y.top_down_balance(70))


x.info()
y.info()

# x.top_down_balance(200)