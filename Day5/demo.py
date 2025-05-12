def fun():
    for n in range(5):
        yield n

gen=iter(fun())
print(next(gen))
print(next(gen))


# l=[1,2,3]
# l[0]
# # sleep()
# itierabl=iter(l)
# print(next(itierabl))
# print(next(itierabl))
# print(next(itierabl))
# print(next(itierabl))
# # # abstract class containe sign.funtiub
# # #inher must implement fun
# # from abc import ABC,abstractmethod
# # class Human(ABC):
# #     def test(self):
# #         print('test')
# #     @abstractmethod
# #     def walk(self):
# #         pass
# #
# # class Employee(Human):
# #     def walk(self):
# #         print('emp w')
# #     # def __str__(self):
# #     #     return f'{self}'
# #     def __len__(self):
# #         return self.salar/1000
# #
# #     def __call__(self, *args, **kwargs):
# # e=Employee()
# # e.test()
# # print(len(e))
# # print(e)#__str__
# #
# #
# #
# # # from multipledispatch import dispatch
# # # @dispatch(int,int)
# # # def fun(x,y):
# # #     pass
# # # @dispatch(float,float)
# # # def fun(x,y):
# # #     pass
# # #
# # # def fun(x:int,y:int):
# # #     pass
# # #
# # # # def fun(x:int,y:int):
# # # #     print(x,y)
# # # #
# # # # def fun(x:str,y:str):
# # # #     print(x,y)
# # # # fun(1,2)
# # # # fun('aya','ali')
# # # # # def fun(*values,type):
# # # # #     sum=0
# # # # #     if(type=='int'):
# # # # #
# # # # #     for n in values:
# # # # #         sum+=n
# # # # #     print(sum)
# # # # # fun(1,2,'int')
# # # # # fun('aya','ali','str')
# # # # # fun(1,2,3,'int')
# # # # # def fun(x,y,z=None):
# # # # #     if(z is None):
# # # # #         print(x,y)
# # # # #     else:
# # # # #         print(x,y,z)
# # # # # fun(1,2)
# # # # # fun(1,2,4)
# # # # # def fun(x,y):
# # # # #     print(x,y)
# # # # # print(fun)
# # # # # def fun(x,y,z):
# # # # #     print(x,y,z)
# # # # # print(fun)
# # # # # fun(1,2)
# # # # # fun(1,2,3)
# # # # # class Class1:
# # # # #     def __init__(self):
# # # # #         self.x=10
# # # # #         self.y=30
# # # # #         print('iam class1 const')
# # # # #     def gety(self):
# # # # #         return self.y
# # # # #     def test(self):
# # # # #         print('clas1 test method ')
# # # # #
# # # # # class Class2:
# # # # #     def __init__(self):
# # # # #         self.x = 20
# # # # #         print('iam class2 const')
# # # # #
# # # # #
# # # # #
# # # # # class Class3(Class2,Class1):
# # # # #     def __init__(self):
# # # # #         super().__init__()
# # # # #
# # # # #     # def __init__(self)
# # # # #     #     self.x = 10
# # # # #
# # # # # c3=Class3()
# # # # # c3.test()
# # # # # # print(c3.y)
# # # # # # #num not chang.
# # # # # # #salary 8000 to 15000
# # # class Human:
# # #     count=0
# # #     def __init__(self,nnum,name,gender,bdate,address):
# # #
# # #         self.__nnum=nnum
# # #         self._name=name
# # #         self.gender=gender
# # #         self.bdate=bdate
# # #         self.address=address
# # #     #setter getter
# # #     def getnnum(self):
# # #         return  self.__nnum
# # #     # def setnum(self,newval):
# # #     #     self.__nnum=newval
# # #
# # #     def eat(self):
# # #         print('human eated')
# # #     def speek(self):
# # #         print(f'iam {self._name}')
# # #     def sleep(self):
# # #         print('human sleep.')
# # #
# # # class Employee (Human):
# # #     count=0
# # #     def __init__(self,nnum,name,gender,bdate,address,salary):
# # #         super().__init__(nnum, name, gender, bdate, address)
# # #         # super(Employee,self).__init__(nnum.nnum, name, gender, bdate, address)
# # #         # self.__salary=salary
# # #         self.Salary=salary
# # #     def speek(self):
# # #         super().speek()
# # #         print(f'iam employee my name{self._name},salary:{self.__salary}')
# # #     #property geeter private
# # #     @property
# # #     def Salary(self):
# # #         return self.__salary
# # #     #setter
# # #     @Salary.setter
# # #     def Salary(self,newval):
# # #         if(newval >=5000 and newval<=15000):
# # #             self.__salary=newval
# # #         else:
# # #             print('invalid salary')
# # #
# # # e=Employee(1,'aya','F',None,None,10000)
# # # h=Human(1,'aya','F',None,None)
# # # e.speek()
# # # h.speek()
# # # # # # class Eng(Employee):
# # # # # #     pass
# # # # # #
# # # # # # eng1=Eng(1,'ssds','M',None,None,5000)
# # # # # # eng1.
# # # # # # #
# # # # # # # h=Human(2,'mark','M',None,None)
# # # # # # #
# # # # # # # e=Employee(1,'aya','F',None,None,8000)
# # # # # # #
# # # # # # # # e.Salary=0
# # # # # # # # print(e.Salary
# # # # # # # #       )
# # # # # # # e.salary=4000
# # # # # # # print(h.getnnum())
# # # # # # # print(e.getnnum())
