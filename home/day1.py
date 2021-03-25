'''1.Write a program that takes three numbers and prints their sum. Every number is given on a
separate line.
num1=int(input('enter a number: '))
num2=int(input('enter a number: '))
num3=int(input('enter a number: '))
sum=num1+num2+num3
print('the sum is',sum)
2.Write a program that reads the length of the base and the height of a right-angled triangle and prints
  the area. Every number is given on a separate line.
len=int(input('enter a length: '))
hei=int(input('enter a height: '))
area=( len * hei ) / 2
print('the area of right angle traingle is: ',area)
3.N students take K apples and distribute them among each other evenly. The remaining (the  undivisible)
  part  remains  in  the  basket.  How  many  apples  will  each  single  student get? How many apples
  will remain in the basket? The program reads the numbers N and K. It should print the two answers for the
  questions above.
stu=int(input("Enter the number of the student:"))
app=int(input("Enter the number of the apple:"))
div=(app/stu)
remain=(app%stu)
print("Each studemt got ",div)
print("The remainning apple ",remain)

4.Given the integer N -the number of minutes that is passed since midnight -how many hours and minutes are
  displayed on the 24h digital clock?The program should print two numbers: the numberof hours (between 0
  and 23) and the number of minutes (between 0 and 59).For example, if N = 150, then 150 minutes have
  passed since midnight -i.e. now is 2:30 am. So,the program should print 2 30.
N=int(input('enter a number of minutes: '))
hrs=N//60
min=N%60
print(f"The time is {hrs} {min}")

5.A school decided to replace the desks in three classrooms. Each desk sits two students. Given the number
  of students in each class, print the smallest possible number of desks that can be purchased.The  program
  should  read  three  integers:  the  number  of  students  in  each  of  the  three classes, a, b and c
  respectively.In the first test there are three groups. The first group has 20 students and thus needs 10
  desks. The second group has 21 students, so they can get by with no fewer than 11 desks. 11 desks are also
  enough for the third group of 22 students. So, we need 32 desks in total.
class1=int(input('enter the number of student: '))
class2=int(input('enter the number of student: '))
class3=int(input('enter the number of student: '))
d1=class1 / 2
d2=class2 / 2
d3=class3 / 2
sum = d1+d2+d3
print('the total num of desk needed are: ',sum)

6.Solve each of the following problems using Python Scripts. Make sure you use appropriate variable names
 and comments. When there is a final answer have Python print it to the screen.A person’s body mass index
  (BMI) is defined as:BMI=mass in kg / (height in m)2.
mass=int(input('enter a weight of a person (kg): '))
hei=int(input('enter a height of a person (meter): '))
BMI= mass / (hei *2)
print('the body mass index is: ',BMI)

7.You live 4 miles from university. The bus drives at 25mph but spends 2 minutes at each of the 10 stops
  on the way. How long will the bus journey take? Alternatively, you could run to university. You jog the
  first mile at 7mph; then run the next two at15mph; before jogging the last at 7mph again. Will this be
  quicker or slower than the bus?
time= (1 /25) * 4*60
t_stop= 20
time_taken=time +t_stop
print('total time taken by journey: ',time_taken,"mins")
f1=60/7
f2=(2*60)/15
total_time=f1+f2
print("total_time")
if    time_taken <total_time:
    print("You are slower than bus")

else:
    print("You are faster than bus")

8.Write a Python program which accepts the radius of a circle from the user and compute the area. (area of
 circle = PI * r2).
rad=int(input('enter a radius of circle: '))
pi=3.14
area= pi* rad ** 2
print(f'the area of circle is: ',area)
9.Write a python program to find sum of the first n positive integers. sum = (n*(n+1))/2
num = int(input("Input a number: "))
sum_num = (num * (num + 1)) / 2
print(sum_num)
10. Write a Python program to convert seconds to day, hour, minutes and seconds.
time = float(input("Input time in seconds: "))
day = time // (24 * 3600)
time = time % (24 * 3600)
hour = time // 3600
time %= 3600
minutes = time // 60
time %= 60
seconds = time
print("d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds))'''


