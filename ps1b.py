"""
1. Have the user input a semi-annual salary raise semi_annual_raise (as a decimal percentage) 
2. After the 6 th month, increase your salary by that percentage. Do the same after the 12th
   month, the 18 month, and so on.
"""
annual_salary = float(input("Enter your  annual salary: "))
portion_saved = float(input("Enter the percent of your slalary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

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
    if months % 6 == 0:
        monthly_salary *= (1 + semi_annual_raise)
    
print("Number of months:", months)