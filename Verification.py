#

# class A:
#     def a(self):
#         print('A')
#
# class B:
#     def a(self):
#         print('B')
#
# class C(B):
#     def a(self):
#        print('C')
#
# class D(C, A):
#     def a(self):
#         super().a()
#         # print(self.__class__.__mro__)
#
#
# print(D.__mro__)



class Verification:

    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.__LenPassword()

    def __LenPassword(self):
        if len(self.password) < 8:
            raise ValueError ('слабый пароль')

    def save(self):
        with open('users', 'a') as r:
            r.write(f'{self.login, self.password}'+'\n')

