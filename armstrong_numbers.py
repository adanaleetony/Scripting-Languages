def armstrong_numbers(n):
    for i in range(10**(n-1),10**n):
        sum = 0
        number = i
        while number > 0:
            total = 1
            digit = number % 10
            for k in range(n):
                total *= digit 
            sum += total    
            number = number//10
        if sum==i:
            print(i,end=" ")
armstrong_numbers(4)