number = int(input("Enter number"))

def even_odd(number:int):

    even_count = 0
    odd_count = 0

    for i in range(number):
        if i % 2 == 0:
            even_count +=1
        else:
            odd_count +=1
    
    return (even_count,odd_count)

even_count,odd_count = even_odd(number)

print(f"Even count: {even_count}, Odd Count: {odd_count}")