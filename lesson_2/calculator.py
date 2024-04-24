def prompt(message):
    print(f'=> {message}')

def calculate_solution(choice, num1, num2):
    match choice:
        case "1":
            return int(num1) + int(num2)
        case "2":
            return int(num1) - int(num2)
        case "3":
            return int(num1) * int(num2)
        case "4":
            return int(num1) / int(num2)

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False

prompt("Welcome to Calculator!")

prompt("What's the first number? ")
first_number = input()

while invalid_number(first_number):
    prompt("Hmm...that doesn't look like a valid number. Try again.")
    first_number = input()


prompt("What's the second number? ")
second_number = input()

while invalid_number(second_number):
    prompt("Hmm...that doesn't look like a valid number. Try again.")
    second_number = input()

prompt('''What operation would you like to perform?
Enter '1' for add, '2' for subtract, '3' for multiply, '4' for divide. ''')
operation_choice = input()

while operation_choice not in ['1', '2', '3', '4']:
    prompt("Invalid. Please enter 1, 2, 3, or 4")
    operation_choice = input()

answer = calculate_solution(operation_choice, first_number, second_number)

print(f'The result is: {answer}.')
