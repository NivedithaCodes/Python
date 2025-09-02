# binary = input("Enter a binary number: ")
# decimal = 0
# power = 0  
# for digit in binary[::-1]:
#     decimal += int(digit) * (2 ** power)
#     power += 1
# print("Decimal:",decimal)

binary = input("Enter a binary number: ")

if '.' in binary:
    int_part, frac_part = binary.split('.')
else:
    int_part, frac_part=binary,''

decimal = 0
power = 0  

for digit in int_part[::-1]:
    decimal += int(digit) * (2 ** power)
    power += 1

power=-1

for digit in frac_part:
    decimal += int(digit) * (2 ** power)
    power -= 1



print("Decimal:",decimal)

 