#if temp is greater than 30, its a hot day otherwise if its less than 10; its a cold day:
#otherwise, its neither hot nor cold.


temperature = int(input('enter the current temperature:'))
if temperature >30:
    print(f'its a hot day')
elif temperature > 10:
    print(f'its a cold day')
else:
    print(f'its neither hot nor cold')