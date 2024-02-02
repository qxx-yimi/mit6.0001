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



def savings_36(start_salary, portion, inv_rate, semi_raise):
    # This should calculate and return the 36 month savings.
    # Make sure to count the months from 0 to 35, not 1 to 36.
    # Apply the semi-annual raise whenever the month is
    # positive and divisible by 6.
    # Do NOT MUTATE (update) the start_salary variable.
    # Create a new fresh variable named salary,
    # set its initial value to start_salary, and mutate that instead.

def bisearch_one_step(saving, down_pay, left, right, portion, steps):
    # This should return the next values of left, right, portion, steps.
    # Do NOT check the loop-stopping condition here.
    # We will do that in the next function.
    # Just use the bisection search logic, regardless of the stopping condition.
    # Use INTEGER DIVISION for the new portion (with // 2 instead of / 2).
    # Do NOT mutate (update) left, right, portion, steps.
    # Create new, fresh variables new_left, new_right, new_portion, new_steps
    # and return those instead.
    # This function is very useful, because you can see the "next step results"
    # without inserting a bunch of print statements everywhere.
    # Because it only advances the search by 1 STEP ONLY.

def bisearch(salary, inv_rate, semi_raise, down_pay, left, right, portion, steps):
    # Use the saving_36 function to calculate the savings for the current portion.
    # If absolute value of (saving - down_pay) is less than 100,
    # you can stop, and return portion and steps.
    # Otherwise, call bisearch_one_step with the savings.
    # This will give you new_left, new_right, new_portion, new_steps.
    # Then call bisearch with these new values. (loop)
    # salary, inv_rate, semi_raise, down_pay stay unchanged.

def optimal_saving_rate(salary, inv_rate, semi_raise, down_pay):
    # Calculate maximum possible 36-month savings with portion = 10000.
    # If this value is less than down_pay, then it's not possible to
    # pay the down payment in 3 years.
    # Otherwise, call bisearch with starting values of
    # left, right, portion = 0, 10000, 5000
    # That will return portion and steps.
    # Then print best savings rate as: portion / 10000,
    # and the number of steps in bisection search.

if __name__ == "__main__":
    # Here define the global constants of semi_raise, inv_rate, down_pay.
    # Then ask user for starting salary.
    # Then call optimal_saving_rate with that salary, and the above 3 constants.


