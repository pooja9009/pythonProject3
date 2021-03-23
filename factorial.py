'''n!=n*(n-1)*n.......n
num=int(input('enter the number: '))
product=1
for i in range(1, num+1):
    product=product*i
print(product,'is the factorial of the given number')


#defining the function sum
def sum():
    print('inside the function')
    num1=int(input('enter the first number: '))
    num2=int(input('enter a second number: '))
    answer=num1+num2
    print(f'the sum of {num1} and {num2} is {answer}')

 # calling of the function
sum()

def sub():
    print('inside the function')
    num1 = int(input('enter the first number: '))
    num2 = int(input('enter a second number: '))
    subtraction = num1 - num2
    print(f'the sub of {num1} and {num2} is {subtraction}')

 # calling of the function
sub()

def mul():
    print('inside the function')
    num1 = int(input('enter the first number: '))
    num2 = int(input('enter a second number: '))
    multiplication = num1 * num2
    print(f'the mul of {num1} and {num2} is {multiplication}')

#calling of the function
mul()

#march22
 #defination of the function

def sum(a,b):
    c=a+b
    print(f'the sum of {a} and {b} is {c}')

#callinf of the function
a=int(input('enter a number: '))
b=int(input('enter 2nd number: '))
sum(a,b)

#return statement returns the value from outside
def sum(a,b):
    c=a+b
    #print(f'the sum of {a} and {b} is {c}')
    return c
#callinf of the function
a=int(input('enter a number: '))
b=int(input('enter 2nd number: '))
print(sum(a,b))

#function with parameter and no return type
def sum(a,b):
    c=a+b
    print(c)

#calling in function
a=int(input('enter a number: '))
b=int(input('enter a 2nd number: '))
sum(a,b)

#function with no parameter and with return type
def sum():
    c=a+b
    return c
#calling
a=int(input('enter 1st number: '))
b=int(input('enter 2nd number: '))
print(sum())

#funtion with parameter and return type
def sum(a,b):
    c=a+b
    return c
#calling
a=int(input('enter 1st number: '))
b=int(input('enter 2nd number: '))
print(sum(a,b))'''








