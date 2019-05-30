#Lab 04 - While Loops Problem 4 - Salary and Retirement
#Heather Gates

year = 2
salary = float(input("Please enter the first year salary: "))
retirement_acct = salary * 0.05
print("Total retirement funds after one year is: $", format(retirement_acct, ".2f"))
while year <= 10:
    new_salary = (salary * 0.02) + salary
    retirement = new_salary * 0.05
    retirement_acct = retirement_acct + retirement
    salary = new_salary
    print("Salary year", year, "is $", format(new_salary, ".2f"))
    print("Retirement saved in year", year, "is $", format(retirement, ".2f"))
    print("Total retirement funds saved is: $", format(retirement_acct, ".2f"))
    year = year + 1
