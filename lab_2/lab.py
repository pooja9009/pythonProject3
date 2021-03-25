'''check whether 5 is in first 5 natural number or not. hint:list=>[1,2,3,4,5]
list=[1,2,3,4,5]
if 5 in list:
    print('yes')
else:
    print('no')'''

#WAP which accepts marks of four subjects and display total marks, percentage and grade.
eng=float(input('enter a marks of of english: '))
nep=float(input('enter a marks of nepali: '))
math=float(input('enter a marks of math: '))
sci=float(input('enter a marks of science: '))
total=(eng+nep+math+sci)/400
total_per=total*100
if total_per > 70:
    print('distinction')
elif total_per > 60:
    print('first division')
elif total_per > 50:
    print('second division')
else:
    print('you are fail')
