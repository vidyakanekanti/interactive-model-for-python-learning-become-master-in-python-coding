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

# Chapter: if-else, elif, and nested conditions
def task_1():
    return execute_task("Check if a number is positive, negative, or zero.",
                        "Use if-elif-else to categorize a number.",
                        "num = int(input('Enter a number: '))\nif num > 0:\n    print('Positive')\nelif num < 0:\n    print('Negative')\nelse:\n    print('Zero')", 1)

def task_2():
    return execute_task("Check if a person is eligible to vote (age 18 or above).",
                        "Use an if-else condition to verify age.",
                        "age = int(input('Enter your age: '))\nif age >= 18:\n    print('Eligible to vote')\nelse:\n    print('Not eligible')", 2)

def task_3():
    return execute_task("Find the largest of three numbers.",
                        "Use if-elif-else to compare three numbers.",
                        "a, b, c = 10, 20, 30\nif a >= b and a >= c:\n    print(a)\nelif b >= a and b >= c:\n    print(b)\nelse:\n    print(c)", 3)

def task_4():
    return execute_task("Check if a year is a leap year.",
                        "A year is leap if it is divisible by 4 but not by 100 unless also divisible by 400.",
                        "year = int(input('Enter a year: '))\nif (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):\n    print('Leap Year')\nelse:\n    print('Not a Leap Year')", 4)

def task_5():
    return execute_task("Check if a character is a vowel or consonant.",
                        "Use if-elif-else to classify alphabet characters.",
                        "char = input('Enter a character: ').lower()\nif char in 'aeiou':\n    print('Vowel')\nelse:\n    print('Consonant')", 5)

def task_6():
    return execute_task("Check if a number is even or odd.",
                        "Use the modulus operator to determine even or odd.",
                        "num = int(input('Enter a number: '))\nif num % 2 == 0:\n    print('Even')\nelse:\n    print('Odd')", 6)

def task_7():
    return execute_task("Determine the grade of a student based on marks.",
                        "Use if-elif-else to categorize marks into grades.",
                        "marks = int(input('Enter marks: '))\nif marks >= 90:\n    print('Grade: A')\nelif marks >= 75:\n    print('Grade: B')\nelif marks >= 50:\n    print('Grade: C')\nelse:\n    print('Grade: F')", 7)

def task_8():
    return execute_task("Check if a number is a multiple of both 3 and 5.",
                        "Use an if condition with logical operators.",
                        "num = int(input('Enter a number: '))\nif num % 3 == 0 and num % 5 == 0:\n    print('Multiple of both 3 and 5')\nelse:\n    print('Not a multiple of both')", 8)

def task_9():
    return execute_task("Check if a password is strong (at least 8 characters).",
                        "Use if-else to verify the length of a string.",
                        "password = input('Enter a password: ')\nif len(password) >= 8:\n    print('Strong Password')\nelse:\n    print('Weak Password')", 9)

def task_10():
    return execute_task("Check if a number is within a given range (10-50).",
                        "Use an if statement with the range condition.",
                        "num = int(input('Enter a number: '))\nif 10 <= num <= 50:\n    print('Within Range')\nelse:\n    print('Out of Range')", 10)

def task_11():
    return execute_task("Check if a triangle is valid given three sides.",
                        "A triangle is valid if the sum of any two sides is greater than the third side.",
                        "a, b, c = map(int, input('Enter three sides: ').split())\nif a + b > c and a + c > b and b + c > a:\n    print('Valid Triangle')\nelse:\n    print('Invalid Triangle')", 11)

def task_12():
    return execute_task("Check if a number is prime.",
                        "A prime number has only two divisors: 1 and itself.",
                        "num = int(input('Enter a number: '))\nif num > 1:\n    for i in range(2, int(num ** 0.5) + 1):\n        if num % i == 0:\n            print('Not Prime')\n            break\n    else:\n        print('Prime')\nelse:\n    print('Not Prime')", 12)

def task_13():
    return execute_task("Classify a number as small, medium, or large.",
                        "Use nested if-else conditions to categorize numbers.",
                        "num = int(input('Enter a number: '))\nif num < 10:\n    print('Small')\nelif num < 50:\n    print('Medium')\nelse:\n    print('Large')", 13)

tasks = [task_1, task_2, task_3, task_4, task_5, task_6, task_7, task_8, task_9, task_10, task_11, task_12, task_13]

def main():
    print("Welcome to Python Tutor - if-else, elif, and Nested Conditions")
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
