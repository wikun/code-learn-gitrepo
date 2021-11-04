age = 12
if age <= 4:
    print('cost is $0')
elif age <= 18:
    print('cost is $25')
else:
    print('cost is $40')

age = 12
if age <= 4:
    print('cost is $0')
elif age <= 18:
    print('cost is $25')
elif age <= 65:
    print('cost is $40')
else:
    print('cost is $20')

# ignore else
age = 12
if age <= 4:
    print('cost is $0')
elif age <= 18:
    print('cost is $25')
elif age <= 65:
    print('cost is $40')
elif age > 65:
    print('cost is $20')