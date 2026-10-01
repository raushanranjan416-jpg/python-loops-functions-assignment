numbers = [5,4,2,10,13,17,21,-4]

def sum_average(numbers:list):
    sum = 0
    for i in numbers:
        sum +=i

    print(f"Sum : {sum}, Average: {sum/len(numbers)}")

sum_average(numbers)
