# from dataclasses import dataclass
#
#
# class Thing:
#     def __int__(self, name, weight, price):
#         self.name = name
#         self.weight = weight
#         self.price = price
#
# t = Thing('book', 1, 2.5)
# print(t)
# def __repr__(self):
#     return f'name = {self.name}, weight = {self.weight}, price{self.price}'
# @dataclass
#
# class ThingDate:
#     name: str
#     weight: int
#     price: float
# t = Thing('book', 1, 2.5)
# print(t)
# # td = ThingDate('magazine', 1, 3.5)
# # print(td)
# # from dataclasses import make_dataclass


# class Car:
#      def __init__(self, model, max_speed, price):
#          self.model = model
#          self.max_speed = max_speed
#          self.price = price
#
#      def get_max_speed(self):
#          return self.max_speed
#  CarDate = make_dataclass("Carclass", [("model", srt),
#                                        "max_speed",
#                                        ("price", float, field(default=0))],
#                           namespace={'get_max_speed': lambda self: self.max_speed})
#  c = CarData("BMW", 256, 4096)
#  print(c)
#  print(c.get_max_speed())







 #from dataclasses import dataclass

#
# @dataclass
# class Goods:
#     current_vid = 0
#
#     vid: int = field(init=False)
#     price: Any = None
#     weight: Any = None
#
#     def __post_init__(self):
#         print("Goods: posts_init")
#         Goods.current_vid += 1
#         self.vid = Goods.current_vid
#
# b = Book =(1000, 100, "Python OOП", "Балакирев С.М")
# print(b)
from dataclasses import dataclass


# gi = GoodIfrit(80, "Hazrul", 3)
# gi.change_goodness(4)
# print(gi)
# gi1 = gi + 15
# print(gi1)
# print(gi(31))

# @dataclass
# class VectorData:
#     x: int
#     y: int = field(comare=False)
#     z: int = field(default=12)
#     cals_lee: InitVar[bool] = True
#     length: float = feild(init=False, compare=False)
#     pi: float = field(init=False)
#
#     def __pst_inint__(self):
#         self.leght = (self.x** 2 + self.y **2 + self.z **2) **0.5
#         self.pi = 3.14
#
# vd = VectorData(1, 2)
# vd2 = VectorData(1, 3)
# print(vd, vd2)
# print(vd == vd2)


#  from dataclasses import dataclass, field, InitVar
#  from typing import Any
#
#  @dataclass
#  class Goods:
#  curent_vid = 0
#
#      vid: field(init=False)
#      price: Any
#      weight: Any
#      def __post_init__(self):
#          print('Good: postInit')
#          Goods.current_vid += 1
#          self.vid = Goods.current_vid
#
#
# @dataclass class Book(Goods):
#      title: str
#      author: str
#      price: float
# g = Goods("1515", "1245 p", 21)
# print(g)
# g2 = Goods("1515", 14, 21)
# print(g2)
# b = Book(2, 5, 'ng', 'ofrjn')
# print(b)
#
# weight: int

# from dataclasses import dataclass
# class AirCastle(object):
#     def __init__(self, height, ac, color):
#         self.height = height
#         self.clounds = clounds
#         self.color = color
# @dataclass
# class AirDate:
#     hight = int
#     clounds = int
#     color: str
#
#     def change_height(self, other):
#         c = self.clounds + value
#         if c < 0
#             c = 0
#         self.clounds = c
#
#     def __add__(self,other):
#         if not isinstance(other,
#                           int)
#             raise TypeError('error')
#         self.clounds += other
#         self.hight += other // 5
#         return AirDate(self.hight, self.clounds, self.color)
#
#     def opacity(self, degree):
#         self.degree = self.hight // degree * self.clounds
#         print(f'Прозрачный облаков:{self.degree}')
#
#     def __str__(self):
#         return f'The AirCastle at an altitude of {self.change_height()} meters is {self.color} with {self.clounds} clouds '
#     def __eq__(self, other):
#         if not isinstance(ohter, AirData):
#             raise TypeError
#         return self.clounds <= other.clounds
#
# # castle = AirDate(1, 3, 'blue')
# # print(castle)
# # castle.change_height(5)
# # castle.change_height(+10)
# # print(castle)
# # castle = castle + 100
# # print(castle)
# # castle.opacity(150)
# print(castle)
# print(castle == castle1)
# print(castle < castle1)

class dataclasses import dataclass

@dataclass
class Goodifrit:
    hight: int
    name: str
    happy: int
    def change_goodness(self, mood):
        x = self.happy + mood
        if x < 3:
            x = 0
        self.happy = x

    def __add__(self, other):
        if not isinstance(other, int):
            raise TypeError('ar')
        return(Goodifrit(self.hight + other, self.name, self.happy))

    def argument(self, paran):
        return f"{paran + self.happy // self.hight}"

    def __str__(self):
        return f"Good Ifrit {self.name}, height {self.height}, goodness {self.happy}"

    def __eq__(self, other):
        if not isinstance(other.GoodIfrit):
            raise TypeError
        if self.happy > other.happy:
            if self.hight > other.height
                if self.name > other.name:
                    return True 
                return False


    def __gt__(self, other):
        if not isinstance(other, Goodifrit):
            raise  TypeError
        return(self.happy, self.hight, self.name) > (other.happy, other.hight, other.name)


y = Goodifrit(20, 'Вася', 10)
y.change_goodness(-50)
print(y)
print(y + 69)
print(y.argument(1000)
dl = GoodIfrit(20, 'Вася', 20 )
print(dt >= y)