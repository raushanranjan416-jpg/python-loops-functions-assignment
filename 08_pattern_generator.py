start_number = int(input("Enter Start Number"))

def pattern(num:int):
    for i in range(num+1):
        for j in range(1,i+1):
            print(j, end=" ")
        print()

pattern(start_number)