class demo(object):
    def __init__(self,a,b):
        self.__a = a
        self.__b = b

    def myprint(self):
        print('a={},b={}'.format(self.__a,self.__b))

# demo1 = demo(10,20)
# print(dir(demo1))
# demo1.myprint()

'''
多重继承
'''
class A:
    def foo(self):
        print('A class')

class B:
    def foo(self):
        print('B class')

class C(B,A):
    pass

c = C()
c.foo()