def savings_three_years(portion_saved):
    current_savings, salary = 0.0, annual_salary
    portion_saved /= 10000.0
    for i in range(1, total_months + 1):
        current_savings += current_savings * r / 12
        current_savings += salary * portion_saved / 12
        if i % 6 == 0:
            salary += salary * semi_annual_raise
    return current_savings


def bisearch(low, high, guess, bi_steps):
    savings = savings_three_years(guess)
    bi_steps += 1
    if abs(savings - down_payment) < epsilon:
        return guess / 10000.0, bi_steps
    else:
        if savings < down_payment:
            low = guess + 1
        else:
            high = guess - 1
        return bisearch(low, high, (low+high)//2, bi_steps)


def main():
    if savings_three_years(10000) < down_payment:
        print("It is not possible to pay the down payment in three years.")
    else:
        low, high, guess, bi_steps = 0, 10000, 5000, 0
        best_rate, bi_steps = bisearch(low, high, guess, bi_steps)
        print("Best savings rate:", best_rate)
        print("Steps in bisection search:", bi_steps)


if __name__ == '__main__':
    total_cost = 1000000
    portion_down_payment = 0.25
    down_payment = total_cost * portion_down_payment
    r = 0.04
    semi_annual_raise = 0.07
    total_months = 36
    epsilon = 100

    annual_salary = float(input("Enter your starting salary: "))
    main()

