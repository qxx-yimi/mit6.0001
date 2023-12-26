portion_down_payment = 0.25
current_savings = 0.0
r = 0.04
annual_salary = float(input("Enter your starting annual salary:"))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal:"))
total_cost = float(input("Enter the cost of your dream home:"))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal:"))

months = 0
while current_savings < total_cost * portion_down_payment:
    current_savings += current_savings * r / 12
    current_savings += annual_salary * portion_saved / 12
    months += 1
    if months % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise

print("Number of months:", months)
