numbers = [5,4,2,10,13,17,21,-4]

def max_min(numbers:list):
    min = 0
    max = 0
    if len(numbers) > 0:
        min = numbers[0]
        max = numbers[0]
    
    for i in numbers:
        if min < i:
            min = i
        elif max > i:
            max = i

    return (max,min)

max,min = max_min(numbers)

print(f"Max value: {max}, Min Value: {min}")