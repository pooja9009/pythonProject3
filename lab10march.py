#if temp is greater than 30, its a hot day otherwise if its less than 10; its a cold day:
#otherwise, its neither hot nor cold.
temperature = int(input('enter the current temperature:'))
if temperature >30:
    print(f'its a hot day')
elif temperature > 10:
    print(f'its a cold day')
else:
    print(f'its neither hot nor cold')


#if name is less than 3 characters long name must be at least 3 characters otherwise
# if its more than 50 characters name must be maximum of 50 characters otherwise - name looks good

name=input('enter a name: ')

if len(name)<3:
    print('name must be at least 3 characters')
elif len(name)>50:
    print('name must be less than 50 characters')
else:
    print('name looks good')


#task... weight converter:
#input the weight of a person in either kg or lbs. if the person provides his/her weight
# in kg then convert it intolbs else convert it to kg

weight = int(input('enter a weight: '))
unit=input('(L)bs or (K)g : ')
if unit.upper()=="L":
    converted_lbs = weight * 0.45
    print(f'the person is{converted_lbs} kilos')
elif unit.upper() == "K":
    converted_kg = weight/0.45
    print (f'the person weight is{converted_kg}pounds')
else:
    print(f'please enter a appropriate character as K for kg and L for lbs!!')













