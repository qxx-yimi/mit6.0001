def calculate_months_for_down_payment(annual_salary, portion_saved, total_cost):
    global current_savings
    months = 0
    while current_savings < total_cost * portion_down_payment:
        current_savings += current_savings * r / 12
        current_savings += annual_salary * portion_saved / 12
        months += 1
    return months


def main():
    annual_salary = float(input("Enter your annual salary: "))
    portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
    total_cost = float(input("Enter the cost of your dream home: "))
    months = calculate_months_for_down_payment(annual_salary, portion_saved, total_cost)
    print("Number of months: ", months)


if __name__ == '__main__':
    portion_down_payment = 0.25
    current_savings = 0.0
    r = 0.04
    main()
