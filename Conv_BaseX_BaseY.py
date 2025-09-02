def convert_base(number, from_base, to_base):
    # Convert from 'from_base' to decimal
    decimal = int(number, from_base)

    # Convert from decimal to 'to_base'
    digits = "0123456789ABCDEF"
    if decimal == 0:
        return "0"
    
    result = ""
    while decimal > 0:
        remainder = decimal % to_base
        result = digits[remainder] + result
        decimal //= to_base
    
    return result


print(convert_base("1011", 2, 10))
print(convert_base("1011",2,16))