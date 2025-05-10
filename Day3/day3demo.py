import re
emreg=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
s='as asd@gmail.com sdsd asd@hotmail.com'
print(re.match(emreg,s))
print(re.fullmatch(emreg,s))
print(re.findall(emreg,s))
# import os
# os.chmod()
# os.chdir()
# # if(os.name=='nt'):
# #     print(os.system('dir'))
# else:
#     print(os.getlogin())
#     print(os.system('ls -lr /'))
# from  math import pi as mathpi
# print(mathpi)
# pi='pythob pi'
# print(pi)
# # import math
# # print(math.pi)
# # print(math.factorial(5))
# # # #open path,mode
# try:
#     with  open('data.txt','r+') as file:
#         if file.readable():
#             print(file.read(5))
#             # file.seek(0)
#             file.write('\nanwer')
#             # file.save()
#             print(file.read())
#
#             # print(
#             # file.readlines())
#             # print(file.readline())
#             # print(file.readline())
#             # print(file.readline())
#             # print('===',file.read(),'===')
#             # content=file.read(2)
#             # print(file.read())#
#             # print(content,type(content))
# except FileNotFoundError:
#     print('file not found')
# # #simple files only
# # file=open('data.txt','a')
# # if(file.writable()):
#     print(file,type(file))
#     data="""1,abdal
#     2,ebram"""
#     file.write(data)
#     # names=['abds\n','oraby\n','amira\n','remonda','ebram']
#     # file.writelines(names)
#     # file.write(r"1,abdall\\n")
#     # file.write('2,amira')
#     # file.write('sdsd/d')
# #close
# file.close()
#
#
# # open file ,path(extenation),mode
# # mode(r,a,w,r+,rb,rb+)
# # r--->readonly,file exsitst
# # w--->writeonly,file exs--->clear,not xsist--->creat
# #
# #
# # unstructured,semistru(xml,json,text)
# # l=[1,2,3,4]
# #
# # for num in l:
# #     # print(num,end=',')
# #     if(num==2):
# #         break
# #
# # else:
# #     print('loop in all list  items number not fount')
# # # import sys
# # try:
# #     #if connect
# #     print('hi from try block')
# #     # 1/0
# #     int('a')
# # except ZeroDivisionError:
# #     print('cannt divid by zero')
# # except ValueError:
# #     print('cast error')
# # except:
# #     print(sys.exc_info()[1])
#
# # except:
# #     print('error')
# #     print(sys.exc_info()[1])
# # #excption handaling
# # n1=eval(input('enter num'))
# # n2=eval(input('enter num'))
# #
# # if(n2!=0):n1/n2
# # # # #scope
# # # name='global'
# # # def outer():
# # #     # name='local in outer fun'
# # #     def inner():
# # #         name='innrer'
# # #         # global name
# # #         #access local var & change val
# # #         #first local var
# # #         # nonlocal name
# # #         print(name)#?
# # #         # name='inner name'
# # #         def medhat():
# # #
# # #     inner()
# # #     print(name)
# # # outer()
# # # print(name)
# # # # #global 0 indentions,if,for,while
# # # # varglobal='global'
# # # # print(varglobal)
# # # # if(True):
# # # #     print(varglobal)
# # # #     varglobal='change by if'
# # # # print(varglobal)
# # # # def fun():
# # # #     varlocal='local'#calling ,end calling
# # # #     #accsess global read only
# # # #     #change
# # # #     global  varglobal
# # # #     #declare local var
# # # #     # varglobal = 'changed by fun'
# # # #     print(varlocal,varglobal)
# # # #
# # # # fun()
# # # # print(varglobal)
# # # #
# # # #
# # # # #lamda function anomyes ,single line
# # # # #
# # # # # y=lambda input:out
# # # # # # y()
# # # # # mysum=lambda  x,y: x+y
# # # # # print(mysum(1,2))
# # # # #
# # # # # def fun(x):
# # # # #     print(x)
# # # # #
# # # # # # y=1+2
# # # # #
# # # # # fun(lambda x,z:x+z)
# # # # #recusion function
# # # # # #call it self & and stop on condition
# # # # # def myfatorial(num):
# # # # #     if(num>1):
# # # # #        return num*myfatorial(num-1)
# # # # #     else:
# # # # #         return 1
# # # # # print(myfatorial)
# # # # # myfatorial(5)
# # # # #
# # # #
# # # #
# # # #
# # # # # def mysum(n1,n2):
# # # # #     n1=input('enter num')
# # # # #     return n1+n2
# # # # # mysum(1,3)
# # # # # n1=input('enter number')
# # # # # n2=input('enter number')
# # # # # mysum(n1,n2)
# # # # #
# # # # # mysum(input('enter number'))
# # # # # def calarea():
# # # # #     shape=input('enter ')