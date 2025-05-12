from marker import Marker
obj1=Marker('b')
obj2=Marker('r')
l=[]
l.append(obj1)
l.append(obj2)
obj1.color='aharaf'
print(l[0].color)

# l=[1,2,3]
# filter(lambda  n:n%2==0,l)
# # from myexperiance.files import simplefileoperation
# # simplefileoperation.myread('/data.txt','all')
# # # class Class1:
# # #
# # #     def __init__(self,o1,o2,o3,o4):
# # #         self.walls=[o1,o2,o3,o4]
# # #     def enterromm(self,objinsr):
# # #         self.insr=objinsr
# # #     def exsit(self):
# # #         self.insr=None
# # #
# # # #objeclass1 use objeclass
# # # class Class2:
# # #     pass
# # #
# # # # from marker import Marker,colors
# # # # from Instructor import Instructor
# # # # from room import Room
# # # # #object marker
# # # # blackpen=Marker(colors[0])
# # # # objins=Instructor(1,'aya')
# # # #
# # # # objins.writeonboard(blackpen)
# # # # roomobj=Room(1,20,objins)
# # # # roomobj2=Room(1,20,None)
# # # #
# # # # # #struct ???charc.
# # # # # #oop paradigm char&actions
# # # # # #class ,object(instance)
# # # # # class Car:
# # # # #     def __init__(self,color):
# # # # #
# # # # #         self.color=color
# # # # # car1=Car('black')
# # # # # class Human:
# # # # #     #class var
# # # # #     count=0
# # # # #     #constructor ,magical func,special
# # # # #     #autocalling when obj created
# # # # #     def __init__(self,id,name,car1):
# # # # #         #instance var
# # # # #         self.id=id
# # # # #         self.name=name
# # # # #         self.car=car1
# # # # #         # Human.count += 1
# # # # #         Human.incrementcount()
# # # # #         # self.incrementcount()
# # # # #         # print('hi from human const',self)
# # # # #     #instance method
# # # # #     def display (self):
# # # # #         print(f'''Name:{self.name}
# # # # #         ID:{self.id}''')
# # # # #     #class method
# # # # #     @classmethod #pass class name
# # # # #     def getcount(cls):
# # # # #         print(cls,cls.count)
# # # # #     @classmethod
# # # # #     def incrementcount(cls):
# # # # #         cls.count+=1
# # # # #     @staticmethod#arg--->ref object,class,as it
# # # # #     def measuretemp(temp):
# # # # #         if(temp>37):
# # # # #             return 'hot'
# # # # #         elif(temp<37):
# # # # #             return 'cold'
# # # # #         else:
# # # # #             return 'normal'
# # # # #
# # # # # print(Human.measuretemp(37))
# # # # # sama=Human(1,'sama')#call const.
# # # # # print(sama.measuretemp(37))
# # # # # #     #static method
# # # # # # Human.getcount()
# # # # # #
# # # # # # Human.incrementcount()
# # # # # #
# # # # # # sama=Human(1,'sama')#call const.
# # # # # # # sama.incrementcount(10)
# # # # # # # obj2=Human(2,'mark')
# # # # # # # obj3=Human(3,'mai')
# # # # # # # sama.display()
# # # # # # # obj2.display()
# # # # # # # obj2.count=10
# # # # # # # print('c---')
# # # # # # # obj2.count+=1 #remove address--->4
# # # # # # # print(Human.count)
# # # # # # # print(sama.count)
# # # # # # print(obj2.count)
# # # # # # print(obj3.count)
# # # # # #
# # # # # # # # [[1],[2,4],[3,6,9]]
# # # # # # # tablenum=3
# # # # # # # print([
# # # # # # #     [
# # # # # # #         (number * n) for n in range(1,number+1)
# # # # # #     ] for number in range(1,tablenum+1)
# # # # # #
# # # # # # ])
# # # # # #
# # # # # # # l=[]
# # # # # # # for n in range(1,6):
# # # # # # #     if(n %2==0):
# # # # # # #         l.append(n)
# # # # # # # print(l)
# # # # # # # print([
# # # # # # #     num for num in range(1,6)
# # # # # # #     if num%2==0
# # # # # # # ])