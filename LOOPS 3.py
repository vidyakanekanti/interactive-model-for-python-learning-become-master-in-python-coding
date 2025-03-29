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

# Chapter 2: Control Flow & Loops
def task_1():
    return execute_task("Find the largest of three numbers using if-elif-else.",
                        "Compare three numbers using conditional statements.",
                        "a, b, c = 10, 20, 30\nif a >= b and a >= c:\n    print(a)\nelif b >= a and b >= c:\n    print(b)\nelse:\n    print(c)", 1)

def task_2():
    return execute_task("Check if a number is a perfect square.",
                        "A perfect square is a number whose square root is an integer.",
                        "import math\nnum = int(input('Enter a number: '))\nif math.isqrt(num) ** 2 == num:\n    print('Perfect Square')\nelse:\n    print('Not a Perfect Square')", 2)

def task_3():
    return execute_task("Print numbers from 1 to N without using a loop.",
                        "Use recursion to print numbers instead of a loop.",
                        "def print_numbers(n):\n    if n > 0:\n        print_numbers(n - 1)\n        print(n)\nn = int(input('Enter N: '))\nprint_numbers(n)", 3)

def task_4():
    return execute_task("Print all Armstrong numbers within a range.",
                        "An Armstrong number is equal to the sum of its digits raised to the power of the number of digits.",
                        "for num in range(100, 1000):\n    order = len(str(num))\n    sum_digits = sum(int(digit) ** order for digit in str(num))\n    if num == sum_digits:\n        print(num)", 4)

def task_5():
    return execute_task("Find the LCM of two numbers using loops.",
                        "LCM is the smallest number divisible by both numbers.",
                        "a, b = 12, 18\ngreater = max(a, b)\nwhile True:\n    if greater % a == 0 and greater % b == 0:\n        print(greater)\n        break\n    greater += 1", 5)

def task_6():
    return execute_task("Generate a Fibonacci sequence using recursion.",
                        "The Fibonacci sequence follows F(n) = F(n-1) + F(n-2).",
                        "def fibonacci(n):\n    if n <= 1:\n        return n\n    return fibonacci(n-1) + fibonacci(n-2)\nn = int(input('Enter n: '))\nfor i in range(n):\n    print(fibonacci(i), end=' ')", 6)

def task_7():
    return execute_task("Reverse a given string without using built-in functions.",
                        "Use a loop to reverse the string manually.",
                        "s = input('Enter a string: ')\nrev_s = ''\nfor char in s:\n    rev_s = char + rev_s\nprint(rev_s)", 7)

def task_8():
    return execute_task("Find the sum of digits of a number recursively.",
                        "Extract digits using modulus and recursion.",
                        "def sum_digits(n):\n    if n == 0:\n        return 0\n    return n % 10 + sum_digits(n // 10)\nn = int(input('Enter a number: '))\nprint(sum_digits(n))", 8)

def task_9():
    return execute_task("Find whether a number is prime or not using a function.",
                        "A prime number is only divisible by 1 and itself.",
                        "def is_prime(n):\n    if n < 2:\n        return False\n    for i in range(2, int(n ** 0.5) + 1):\n        if n % i == 0:\n            return False\n    return True\nn = int(input('Enter a number: '))\nprint(is_prime(n))", 9)

def task_10():
    return execute_task("Print a pyramid pattern using nested loops.",
                        "Use a nested loop structure to print a pyramid of stars.",
                        "rows = 5\nfor i in range(1, rows + 1):\n    print(' ' * (rows - i) + '*' * (2 * i - 1))", 10)

tasks = [task_1, task_2, task_3, task_4, task_5, task_6, task_7, task_8, task_9, task_10]

def print_report():
    print("\n=== Performance Report ===")
    for i in range(1, len(tasks) + 1):
        attempts = task_attempts.get(i, 0)
        time_taken = task_times.get(i, 0)
        print(f"Task {i}: {attempts} attempt(s), {time_taken} sec")
    print("=========================")

def main():
    print("Welcome to Python Tutor - Chapter 2: Control Flow & Loops")
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
    print_report()

if __name__ == "__main__":
    main()
