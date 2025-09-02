
# n=25
# base=2
# remainder=[]
# while(n>0):
#     remainder.append(n%base)
#     n=n//base
# print(remainder[::-1])  # o/p [1, 1, 0, 0, 1]

# n=int(input('Enter a number:'))
# base=int(input('Enter the base:'))
# remainder=[]
# while(n>0):
#     remainder.append(n%base)
#     n=n//base
    
# print(remainder[::-1])

n=int(input('Enter a number:'))
base=int(input('Enter the base:'))
remainder=[]
while(n>0):
    remainder.append(n%base)
    n=n//base
else:
    remainder.append(0)
print(remainder[::-1])

 