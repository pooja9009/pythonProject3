#for-else loop
for i in range(4):
    print(i)
else:
    print('program is over')

#continue statement
for i in range(4):
    if i==2:
        continue
    print(i)
fruits = ['apple', 'banana', 'cherry']
for x in fruits:
    if x == 'banana':
        continue
    print(x)

#break statement
for i in range(4):
    if i==2:
        break
    print(i)
for val in 'string':
    if val=='i':
        break
    print (val)
print('end')

fruits = ['apple', 'banana', 'cherry']
for x in fruits:
    print(x)
    if x=='banana':
        break

#while-loop
i=0 #initialization
while i<=10: #condition
    print(i)
    i=i+1 #stepping
print('program is over')

i=10 #initialization
while i>=1: #condition
    print(i)
    i=i-1 #stepping
print('program is over')

#wap to print all the odd and even number with appropriate msg from 1-50.
i=0
while i<=50:
    i=i+1
    if i%2==0:
        print(i,'it is even number')
    else:
        print(i,'it is odd number')

#WAP to find the sum of elements of list using for loop and while loop.
   #for loop:
lst=[10,  31, 37, 40, 56, 63, 70]
sum = 0
for i in lst:
    sum = sum+i
print(sum)