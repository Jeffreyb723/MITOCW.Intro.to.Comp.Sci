annual_salary = float(input("Enter your  annual salary: "))
portion_saved = float(input("Enter the percent of your slalary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

portion_down_payment = .25
current_savings = float(0)
monthly_salary = annual_salary/12
r = .04
monthly_r = r/12

down_payment = total_cost * portion_down_payment
months = 0

while current_savings < down_payment:
    current_savings *= (1 + monthly_r)
    current_savings += monthly_salary * portion_saved
    months += 1
    
print("Number of months:", months)