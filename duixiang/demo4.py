'''
不修改代码修改类方法
'''

class Base(object):
    def setUp(self):
        print("method by base")

class A(Base):
    def setUp(self):
        print("method by a")

class B(Base):
    def setUp(self):
        print("method by b")

class ChangeMethod(object):
    def setMethod(self,ins):
        self.ins = ins()

    def setUp(self):
        self.ins.setUp()

m1 = ChangeMethod()
m1.setMethod(Base)
m1.setUp()
m1.setMethod(A)
m1.setUp()
m1.setMethod(B)