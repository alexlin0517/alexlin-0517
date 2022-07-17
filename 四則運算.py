# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 22:47:15 2021

@author: hello
"""

a=float(input('num1='))
print('1=+')
print('2=-')
print('3=*')
print('4=/')
print('5=√(n2=0)')
print('6=**')
x=int(input('symble='))
b=float(input('num2='))
if (x<=0):
    print('error')
elif (x<1.01):
    print(a+b)
elif (x<2.01):
    print(a-b)
elif (x<3.01):
    print(a*b)
elif (x<4.01):
    print(a/b)
elif (x<5.01):
    print(a**0.5)
elif (x<6.01):
    print(a**b)
else:
    print('error')
    #end
    #alexlin0517