# def decimal_to_base(n, base):
#     digits = "0123456789ABCDEF"  
#     if n == 0:
#         return "0"
#     result = ""
#     num = n
#     while num > 0:
#         remainder = num % base
#         result = digits[remainder] + result
#         num //= base
#     return result
# number=int(input("Enter a decimal number"))
# base=int(input("Enter the base"))
# print(decimal_to_base(number,base))

digits = "0123456789ABCDEF"  
n=int(input('Enter a number:'))
base=int(input('Enter the base:'))
result=''
while(n>0):

    remainder=n%base
    result = digits[remainder] + result
    n=n//base
else:
    result=0
print(result)
