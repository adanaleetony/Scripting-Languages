def binary_to_decimal(num):
    binary = str(num)
    decimal = 0
    for i in range(len(binary)):
        decimal += int(binary[i]) * (2**(len(binary)-i-1))
    return(decimal)