total_cost = 1000000
portion_down_payment = 0.25
down_payment = total_cost * portion_down_payment
r = 0.04
semi_annual_raise = 0.07
total_months = 36
epsilon = 100

annual_salary = float(input("Enter your starting salary:"))


def savings_three_years(portion_saved):
    current_savings, salary = 0.0, annual_salary
    portion_saved /= 10000.0
    for i in range(1, total_months + 1):
        current_savings += current_savings * r / 12
        current_savings += salary * portion_saved / 12
        if i % 6 == 0:
            salary += salary * semi_annual_raise
    return current_savings


low, high, bi_steps = 0, 10000, 0
while low <= high:
    guess = (low + high) // 2
    savings = savings_three_years(guess)
    bi_steps += 1
    if savings < down_payment:
        low = guess + 1
    elif savings > down_payment + epsilon:
        high = guess - 1
    else:
        print("Best savings rate:", guess / 10000.0)
        print("Steps in bisection search:", bi_steps)
        break

if low > high:
    print("It is not possible to pay the down payment in three years.")
