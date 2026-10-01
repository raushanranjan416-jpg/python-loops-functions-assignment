def gross_salary(basic_salary:int, bonus_per:int = 0):
    return basic_salary + (basic_salary * bonus_per / 100)


def tax_amount(gross_salary:int,  tax_per:int = 0):
    return (gross_salary * tax_per / 100)

def final_salary(gross_salary: int, tax_amount:int = 0):
    return gross_salary - tax_amount

def employee(name:str, basic_salary:int, bonus_per:int = 0, tax_per: int = 0):
    gross_sal = gross_salary(basic_salary,bonus_per)
    tax_amt = tax_amount(gross_sal, tax_per)
    final_sal = final_salary(gross_sal,tax_amt)
    print(f"{name} has Gross Salary: Rs {gross_sal}, Tax amount: Rs {tax_amt}, Final Salary: Rs {final_sal}")

employee("Rahul", 60000, 10,5)

