'''
类装饰器
'''


def deco(declass):
    class Declass():
        def __init__(self, age, color):
            self.wrap = declass(age)
            self.color = color

        def show(self):
            print('age=', self.wrap.age)
            print('color=', self.color)

    return Declass


@deco
class Dec1():
    def __init__(self, age):
        self.age = age

    def show(self):
        print('age=', self.age)


import pdb
pdb.set_trace()
d = Dec1('15', 'red')
d.show()
