num=int(input('enter a number: '))
for i in range(1,11):
    mul=num*i
    print(mul)

def table():
    num=int(input('enter a number: '))
    for i in range(1,11):
        mul=num*i
        print(f'{num} * {i} = {mul}')
#calling the function
table()

def outr_function():
    b=20
    def inner_func():
        c=30
a=10

def outer_function():
    a=20
    def inner_function():
        a=30
        print('inner: ',a)
    inner_function()
    print('a: ',a)

a=10
outer_function()
print('a:',a)

def outer_function():
    global a
    a=20
    def inner_function():
        global a
        a=30
        print('inner: ',a)
    inner_function()
    print('a: ',a)
a=10
outer_function()
print('a:',a)



