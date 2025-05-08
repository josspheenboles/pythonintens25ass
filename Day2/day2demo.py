# #function
word='{}'
print(word.format('pytho'))
msg='Name:{name},track:{track},branch:{branch},{name}'

print(msg.format(name='aya',track='py',branch='ass'))
print(msg.format(track='php',branch='smart',name='alaa'))
# def fun(*arg):
#     if(len(arg)==3):
#         range(arg[0],arg[1],arg[2])
#     elif (len(arg)==2):
#         range(arg[0], arg[1], 1)
#     elif (len(arg)==1):
#         range(0, arg[0], 1)
#     print(arg,type(arg))
# fun(1,10,1)
# print(min(1,2,3,100,-100))
# fun(1,2,3,4,5,6)
# fun(1)#packing (1,)
# fun([1,2])#packing ([1,2],)
# #black box ,arg,return value
#
# # min(1,2,3,3,6,7,8)
# #fun(key=value)
# # def sayhello(name):
# #     return ('hello',name)
# # # calling
# # sayhello('aya')
# # sayhello('alaa')
# #rang,min
# def mymin(*arg):
#     print(arg)
# t=(1,2,3)
# mymin(1,2,3,4,'ss')#(1,2,3,4,'ss')
# mymin(t)#packing ((1,2,3),)
# # #range,
# # #defaulr arg value--->non defaule,defa
# # def myrange(end,start=0,step=1):
# #     print(end,start,step)
# # myrange(10)
# # myrange(10,1)
# # myrange(10,1,2)
#
# # # #non prem.
# # #set collection of values,unique,sorted
# # s={1,5,4,8,3,'aya'}
# # # print(s[0])
# # print(s,type(s))
# # # #list collection of values  as pair of ky &value diff data types
# # # d={'id':1,
# # #    'name':'mai mostafa',
# # #    'track':{'id':20,'name':'python'},
# # #    'curses':['admin1','bash'],
# # #     'id':1000,
# # #    }
# # # d2={'id':10,'branch':'smart'}
# # # d2['id']
# # # d['id']
# # # print(d+d2)#on fly
# # # print(d*2)
# # # d.update(d2)
# # # print(4+5)
# # # for key,value in d.items():
# #
# # # d['grades']=(70,100)
# # # d['id']=10
# # # d.update({'branch':'smart','id':100})
# # # print(d)
# # # for x in d.values():
# # #     print(x)#?
# # # print(type(d),d)
# # # x,y=10,20
# # # x,y=y,x
# # # # name='aya ali'
# # # for index,value in enumerate(name):#[(),(),,,,()]
# # #     # print('char',item[1],'index',item[0])
# # #     print('char',value,'index',index)
# # # *x,*t,z=(2,3,4,444,'df',[])#unpacking
# # # print(x,t,z)
# # # # x=2,3,4,4,5,'sdsd'
# # # # print(type(x))
# # # # # x=1
# # # # x=1.1
# # # # x='dd'
# # # # x=(4,5)#add,add3
# # # # x='ddd'
# # # # #tuple collection of values diff data types,immutable list
# # # t2=(1,1.1,True,'ssds',[3,4],{},(4,4))
# # # t=t2
# # # t=copy(t2)
# # # t[4].append(4)
# # # print(t)
# # # print(t2)
# # # # t=t2+(0,)
# # # # t2='dfdf'
# # #
# # # # t[0]='sdsd'
# # # # print(t)
# # # # print(t2)
# # # # # t[4].append('python track')
# # # # t1=(5,6)
# # # # print(t1+t2)
# # # # print(t1*3)
# # # # # print(t[::-1])
# # # # for item in t:
# # # #     print(item,type(item))
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # # #list collection of values diff data types
# # # # admincours=['admin1','apache','docker','bash']
# # # # l.copy(admincours)
# # # # l[0]='plplpa'
# # # #
# # # # print(admincours)
# # # # print(l)
# # # # devlleop=['python','django','db']
# # # # print(admincours+devlleop)
# # # # print(admincours*3)
# # # # # admincours.extend(devlleop)
# # # # devlleop.extend(admincours)
# # # # print(admincours)
# # # # print(devlleop)
# # # # # l=[1,1.1,True,'aya',[3,4],(),{},1]
# # # # # l.append('python intens')
# # # # # l.insert(1,'dff')
# # # # # l.pop(0)
# # # # # l.remove(True)
# # # # print(l.count(True))
# # # # # print(l.sort())
# # # # print(l)
# # # # print(l[0],len(l))
# # # # print(l[::-1])
# # # # print(l[1:5])
# # # # l[0]='ahmed'
# # # # print(l)
# # # # for item in l:
# # # #     print(item,type(item))
# # # # # while cond:
# # # # #     body
# # # # answer='y'
# # # # while(answer.lower()=='y'):
# # # #     number=eval(input('ente number'))
# # # #     if(isinstance(number,int)):
# # # #         print(number)
# # # #     answer=input('enter y to cont. any key exsit to exsit')
# # #
# # # # for number in range(1,10):
# # # #     pass
# # # # for number in range(1,10):
# # # #     if(number==3):
# # # #         break
# # # #     print(number)
# # # # range(start=0,end,step=1)
# # # # range(0,5)#start,end
# # # # range(0,5,1)#start,end,step
# # # # range(5)
# # # # print(range(1,10,1))
# # # # # for number in range(0,10,2):
# # # # #     # if(number%2==0):
# # # # #         print(number,end=' ')
# # # # # name='aya ali'
# # # # #
# # # # # for char in enumerate(name):#[(index,items),(),,,,()]
# # # # #     print(char)
# # # #
# # # # # num=eval(input('enter number'))
# # # # # if isinstance(num,int):
# # # # #     print(num+1)
# # # # #     print(num+1)
# # # # # elif isinstance(num,float):
# # # # #     print(num + 1)
# # # # # else:
# # # # #     print('num invalid')