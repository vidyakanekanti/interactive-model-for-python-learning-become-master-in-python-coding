import sys
import time
from io import StringIO

print("Note: This tutorial helps you learn Python step by step. No additional installation is required for basic Python.")

# Tracking attempts and time
task_attempts = {}
task_times = {}

def get_user_code(prompt, explanation, example_code):
    print(prompt)
    print("Explanation:")
    print(explanation)
    print(f"Example:")
    print(example_code)
    lines = []
    print("Enter your code (type 'done' on a new line to finish, or 'exit' to quit):")
    while True:
        line = input(">>> ").strip()
        if line.lower() in ["done", "exit"]:
            break
        lines.append(line)
    code = "\n".join(lines)
    return code

def run_code(code):
    old_stdout = sys.stdout
    redirected_output = StringIO()
    sys.stdout = redirected_output
    try:
        exec(code, globals())
        output = redirected_output.getvalue().strip()
    except Exception as e:
        output = f"Error: {str(e)}"
    finally:
        sys.stdout = old_stdout
    return output

def execute_task(challenge, explanation, example, task_num):
    attempts = 0
    start_time = time.time()
    while True:
        attempts += 1
        user_code = get_user_code(challenge, explanation, example)
        output = run_code(user_code)
        if "Error" in output:
            print(f"Feedback: {output}. Try again!")
        else:
            print(f"Feedback: Well done! Output: {output}")
            break
    end_time = time.time()
    task_attempts[task_num] = attempts
    task_times[task_num] = round(end_time - start_time, 2)
    return input("Redo this task? (yes/no): ").strip().lower() == "yes"

# Chapter: if-else with Logical Operators
def task_1():
    return execute_task("Check if a number is between 10 and 50 (inclusive).",
                        "Use `and` to ensure both conditions are met.",
                        "num = int(input('Enter a number: '))\nif 10 <= num <= 50:\n    print('Within Range')\nelse:\n    print('Out of Range')", 1)

def task_2():
    return execute_task("Check if a number is even and greater than 20.",
                        "Use `and` to check both conditions.",
                        "num = int(input('Enter a number: '))\nif num % 2 == 0 and num > 20:\n    print('Valid Number')\nelse:\n    print('Invalid Number')", 2)

def task_3():
    return execute_task("Check if a person is eligible for a senior citizen discount (age 60 or above) or a student discount (age below 18).",
                        "Use `or` to allow either condition.",
                        "age = int(input('Enter your age: '))\nif age >= 60 or age < 18:\n    print('Eligible for Discount')\nelse:\n    print('Not Eligible')", 3)

def task_4():
    return execute_task("Check if a number is neither negative nor zero.",
                        "Use `not` to negate a condition.",
                        "num = int(input('Enter a number: '))\nif not (num <= 0):\n    print('Positive Number')\nelse:\n    print('Negative or Zero')", 4)

def task_5():
    return execute_task("Check if a person is eligible to work (age between 18 and 60).",
                        "Use `and` to check the valid range.",
                        "age = int(input('Enter age: '))\nif 18 <= age <= 60:\n    print('Eligible to Work')\nelse:\n    print('Not Eligible')", 5)

def task_6():
    return execute_task("Check if a year is a leap year using `and` and `or`.",
                        "A leap year must be divisible by 4 and not by 100, unless it is also divisible by 400.",
                        "year = int(input('Enter a year: '))\nif (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):\n    print('Leap Year')\nelse:\n    print('Not a Leap Year')", 6)

def task_7():
    return execute_task("Check if a password is strong (8+ characters and contains a digit).",
                        "Use `and` to check multiple conditions.",
                        "password = input('Enter password: ')\nif len(password) >= 8 and any(char.isdigit() for char in password):\n    print('Strong Password')\nelse:\n    print('Weak Password')", 7)

def task_8():
    return execute_task("Check if a number is either a multiple of 3 or 7.",
                        "Use `or` to allow multiple conditions.",
                        "num = int(input('Enter a number: '))\nif num % 3 == 0 or num % 7 == 0:\n    print('Multiple of 3 or 7')\nelse:\n    print('Not a Multiple')", 8)

def task_9():
    return execute_task("Check if a triangle is valid based on three given sides.",
                        "A triangle is valid if the sum of any two sides is greater than the third.",
                        "a, b, c = map(int, input('Enter three sides: ').split())\nif a + b > c and a + c > b and b + c > a:\n    print('Valid Triangle')\nelse:\n    print('Invalid Triangle')", 9)

def task_10():
    return execute_task("Check if a person is an adult (18+ years) and has a driving license.",
                        "Use `and` to verify both conditions.",
                        "age = int(input('Enter age: '))\nlicense_status = input('Do you have a driving license? (yes/no): ').lower()\nif age >= 18 and license_status == 'yes':\n    print('Eligible to Drive')\nelse:\n    print('Not Eligible')", 10)

def task_11():
    return execute_task("Check if a user has entered a valid email (must contain `@` and `.`).",
                        "Use `and` to verify multiple conditions.",
                        "email = input('Enter email: ')\nif '@' in email and '.' in email:\n    print('Valid Email')\nelse:\n    print('Invalid Email')", 11)

def task_12():
    return execute_task("Determine if a number is within a range (1-100) and is even.",
                        "Use `and` to combine conditions.",
                        "num = int(input('Enter a number: '))\nif 1 <= num <= 100 and num % 2 == 0:\n    print('Valid')\nelse:\n    print('Invalid')", 12)

def task_13():
    return execute_task("Check if a word is a palindrome (same forwards and backwards).",
                        "Use `not` to check if reversing the word changes it.",
                        "word = input('Enter a word: ')\nif word == word[::-1]:\n    print('Palindrome')\nelse:\n    print('Not a Palindrome')", 13)

tasks = [task_1, task_2, task_3, task_4, task_5, task_6, task_7, task_8, task_9, task_10, task_11, task_12, task_13]

def main():
    print("Welcome to Python Tutor - if-else with Logical Operators")
    while True:
        task_num = input("Enter task number (or 'exit' to quit): ").strip()
        if task_num.lower() == "exit":
            break
        if task_num.isdigit():
            task_num = int(task_num)
            if 1 <= task_num <= len(tasks):
                redo = True
                while redo:
                    redo = tasks[task_num - 1]()
            else:
                print(f"Invalid task number. Choose between 1 and {len(tasks)}.")
        else:
            print("Invalid input. Enter a valid task number.")

if __name__ == "__main__":
    main()
