import math


def is_prime(num:int):
    num = abs(num)
    if num == 0 or num == 1: 
        return False
    elif num == 2:
        return True
    
    elif num % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(num) + 1),2):
        if num % i == 0:
            return False
        
    return True


def even_odd(num:int):
    if num % 2 == 0:
        return "EVEN"

    return "ODD"


def negative_positive(num:int):
    if num > 0 :
        return "POSITIVE"
    
    elif num < 0:
        return "NEGATIVE"
    
    return "ZERO"


def main(num:int):
    prime = 'PRIME' if is_prime(num) else 'NON PRIME'
    is_even = even_odd(num)
    negative_positive_number = negative_positive(num)
    return (negative_positive_number,is_even,prime)


numbers = int(input("Enter a number"))
main(numbers)
        

