import math

def prime_number_finder(start: int, end : int):

    for i in range(start,end):
        isPrime = is_prime(i)
        if isPrime:
            print(i)



def is_prime(num:int):
    if num == 0 or num == 1 or num < 0: 
        return False
    elif num == 2:
        return True
    
    elif num %2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(num) + 1),2):
        if num % i == 0:
            return False
        
    return True


start_number = int(input("Enter Start Number"))
end_number = int(input("Enter End Number"))

if end_number < start_number:
    print("End number should greater then start number.")

prime_number_finder(start_number,end_number)
        

