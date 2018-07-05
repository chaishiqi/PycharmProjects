'''
mataclass
'''

def fn(self,name="hello"):
    print("hi,%s"% name)
'''
三个参数：类的名称，父类，调用的方法
'''
Hello = type('hello',(object,),dict(sayhello=fn))

hello = Hello()
hello.sayhello()

class MetaClass(type):
    def __new__(cls, name, base, attrs):
        attrs['say_'+name] = lambda self,value,saying=name:print(saying+','+value+'!')
        return type.__new__(cls,name,base,attrs)

class China(object,metaclass=MetaClass):
    pass

china = China()
china.say_China('nihao')

class Field(object):
    def __init__(self,name,value):
        self.name = name
        self.type = type

    def __str__(self):
        print("%s,%s" %(self.__class__.__name__,self.name))

class StringField(Field):
    def __init__(self,name):
        super(StringField,self).__init__(name,'varchar(100)')

class IntegerField(Field):
    def __init__(self,name):
        super(IntegerField,self).__init__(name,'bigint(5)')

inte = IntegerField('age')
inte.__str__()