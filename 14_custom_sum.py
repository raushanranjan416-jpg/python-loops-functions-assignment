def my_sum(numbers:list):
    sum = 0
    for i in range(len(numbers)):

        if not (type(numbers[i]) == int or type(numbers[i]) == float ):
            continue
        
        sum += numbers[i]

    
    return sum

print(my_sum([5,4,2,10,13,17,21,-4]))
