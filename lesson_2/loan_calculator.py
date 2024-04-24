def prompt(msg):
    print(f'=> {msg}')

while True:
    monthly_payment = 0

    print("-------------------------------------")
    prompt("Welcome to the loan calculator")
    print("-------------------------------------")

    prompt("Input the loan amount: ")
    loan_amount = float(input())

    prompt("Enter in the APR (Ex: 5 for 5%): ")
    monthly_interest = (float(input()) / 100) / 12

    prompt("Enter in duration of loan in years: ")
    loan_duration_in_months = float(input()) * 12

    try:
        monthly_payment = loan_amount * (monthly_interest / (1 - (1 + monthly_interest) ** (-loan_duration_in_months)))
    except ZeroDivisionError:
        monthly_payment = loan_amount / loan_duration_in_months

    print(f'The monthly payment is ${"%.2f" % monthly_payment}')

    prompt("Would you like to do another calculation? ")
    answer = input().lower()


    while True:
        if answer.startswith('n') or answer.startswith('y'):
            break

        prompt("Please enter 'y' or 'n'.")
        answer = input().lower()

    if answer[0] == 'n':
        break
