class demo1:
    def __init__(self,a=10,b=5):
        self.a = a
        self.b = b

class demo2:
    def __init__(self,a,b):
        self._a = a
        self.__b = b

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self,value):
        self.__b = value

    @property
    def output(self):
        print("a=%d,b=%d" %(self._a,self.b))

    def __call__(self):
        return self.output

class demo3(object):
    '''
    staticmethos clsmethod
    '''
    c = 8
    def __init__(self,a=10,b=5):
        self._a = a
        self.__b = b

    def add(self):
        return self._a + self.__b

    @staticmethod
    def static():
        print("half c and _a is ",demo3.c/2)

    @classmethod
    def clsmethod(cls,num):
        return cls(num,demo3.c)

# demo = demo1()
# demo.a = 5
# demo.b = 10
# print(demo.a,demo.b)
# demo = demo2(5,6)
# # demo.output
# # demo._a = 6
# # # demo._demo__b = 7
# # demo.b = 7
# # # demo.output
# # demo()

demo = demo3()
demo3.static()
print(demo3.clsmethod(4))
new_ins = demo3.__init__(demo)
#print(new_ins.add())
print(new_ins)