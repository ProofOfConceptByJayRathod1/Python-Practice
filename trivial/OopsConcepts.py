import statistics


class Computer:
    classVariable=1
    def featureImpl(self):
        print("feature computer implementation")
    def __init__(self, cpu, ram,rom, instanceVariable):
        self.cpu=cpu
        self.ram=ram
        self.rom=rom
        self.instanceVariable=instanceVariable
    def __int__(self):
        print("in computer init")

        print("inside paramtererized constructor init") # this is a default constructor if only self parameeter is passed otherwise it becomes a paramerterized constructor
    def configuration(self):
        print(self.cpu,self.ram,self.rom,self.instanceVariable,self.classVariable),

class Compiter:
    def __int__(self):
        print("in compiter init-----")
    def featureImpl(self):
        print("feature compiter implementation")
object1 = Computer("nvidia", "4GB", "1TB","instaneVariable") # just like in java the default constructor is invoked as soon as the object is initialized
object2 = Computer("intel", "16GB", "10TB","instaneVariable")    # init called again, we are actuailly passing 4 objects here, they are self, cpu, ram, rom
Computer.configuration(object1)
object1.classVariable=2
Computer.configuration(object1)
Computer.classVariable=4
Computer.configuration(object1)
Computer.configuration(object2)
compiterObject1=Compiter()
compiterObject2 =Compiter()
print(id(compiterObject1))
print(id(compiterObject2))


class AnotherClass(Computer,Compiter):# this is inheritance

    cv=5

    def __init__(self,a,b,c,ai,bi,ci):
        self.a=a
        self.b=b
        self.c=c
        self.inner=self.InnerClass(ai,bi,ci)
    def __int__(self):
        # in the below init as there is multiple inheritance, as there will be two parent class init methods
        # in this scenario MRO is followed Method resolution order so as we have written compiter before it will take init of compiter not computer
        # the same logic applies when there are same method names in the two inherited parent class
        super().__init__()  # here we aere trying to call the init method of parent class (this will not get printed as only the init method of child class will be called)

    class InnerClass:
        def __init__(self, ai, bi, ci):
            self.ai = ai
            self.bi = bi
            self.ci = ci

    def average(self):
        list=[self.a,self.b,self.c]
        return statistics.mean(list),self.a,self.b,self.c,self.inner.ai,self.inner.bi,self.inner.ci

    @classmethod # we have to use class decorator beacause we are using class variable
    def getClassVariable(cls):
        return cls.cv

    @staticmethod
    def getStaticMethodThatHasNothingToDoWithClassVariable():
        print("inside the static variable get method that does not use class variabl")

    def featureImpl(self):
        super().featureImpl()

a=AnotherClass(2,4,6,"holy","inner","class")
# inner=AnotherClass.InnerClass()
# print(inner)

b=AnotherClass(1,3,5,"holy1","inner1","class1")

print(a.average())
print(b.average())
a.featureImpl()



#duck typing in python

class Class1:
    def method1(self):
        print(1)
        print(2)
class Class2:
    def method1(self):
        print(3)
        print(4)
class Class3:
    def method2(self,argumentForWhichMethod):
        argumentForWhichMethod.method1()

objClass1=Class2() #call method1 from class1 and if we chage it to class 2 we get 3 and 4

objClass3=Class3()

objClass3.method2(objClass1)


# overloading


class AddMulDivSubOverLoading:

    def methodOverLoading(self,v1=None,v2=None,v3=None):
        s=0
        if v1!=None and v2!=None and v3!=None:
            s=v3+v2+v1
        elif v1!=None and v2!=None:
            s=v1+v2
        else:
            s=v1
        #     so there is no concept of method overloading in pythin but we can create method like this with if conditions so that we can pass 2 or 3 arguments
        return s
    def __init__(self, a1, b1):
        self.a1=a1
        self.b1=b1

    def __add__(self, other):
        a= self.a1 + other.a1
        b = self.b1 + other.b1
        objectAMDS= AddMulDivSubOverLoading(a,b)

        return objectAMDS

    def __mul__(self, other):
        a= self.a1 * other.a1
        b = self.b1 * other.b1
        objectAMDS= AddMulDivSubOverLoading(a,b)

        return objectAMDS

    def __sub__(self, other):

        a= self.a1 - other.a1
        b = self.b1 - other.b1
        objectAMDS= AddMulDivSubOverLoading(a,b)

        return objectAMDS

    def __str__(self):
        return '{} {}'.format(self.a1,self.b1)
o1=AddMulDivSubOverLoading(1,3)
o2=AddMulDivSubOverLoading(2,6)

anotherthree=o1*o2 #this is overloading as int internally call __add__ div etc methods but using + we have overlaoded __add__ and other methods

print(anotherthree.a1, anotherthree.b1)
print("O1 is: ",o1)# as we are overloading __str__ method

print(o1.methodOverLoading(1,2))
# in python for any arithmatic operation method is called so we can overload that method like the above
# method overloading concept doesnt exist in python


# method overriding

class Or1:
    def or1(self):
        print("in method or1 ")
class Or2(Or1):
    def or1(self):
        print("in method or1 of Or2 class ")


or2obj=Or2()
or2obj.or1()# so or1 of Or1 was overridden by or1 of Or2
