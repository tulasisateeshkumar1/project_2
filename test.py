from numpy import *

"""
x=int(input('enter value of x:'))
y=int(input('enter value of y:'))

z=x+y
print(z)

def greet():
    print('hello')
    print('Welcome')


greet()



def count(lst):
    even=0
    odd=0
    for i in lst:
        if(i%2==0):
            even+=1
        else:
            odd+=1
    return even,odd

lst=[2,5,7,8,9,30,23,4]

even,odd =count(lst)

print("even : {} and odd : {}".format(even,odd)) """

def fib(n):
    a,b = 0,1
    if n == 1:
        print(a)
    else:
        #print(a)
        #print(b)
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        print(c)


fib(10)

