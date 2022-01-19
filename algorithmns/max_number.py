#Find maximum number from 3 numbers entered on keyboard

a = int(input('Please enter First Number: '))
b = int(input('Please enter Second Number: '))
c = int(input('Please enter Third Number: '))

if (a >= (b and c)):
    print(f'Maximum number is ', a)
elif (b >= (a and c)):
    print(f'Maximum number is ', b)
elif (c >= (a and b)):
    print(f'Maximum number is ', c)
else:
    print(f'"ERROR!!!')



