table_number = int(input("Enter number to write table"))
end_number = int(input("Enter number till where to write table"))


def table_mul(table_number:int,end_number:int):
    for i in range(end_number):
        print(f"{i+1} * {table_number} = { (i + 1) * table_number}")
        if i == end_number:
            break

table_mul(table_number,end_number)