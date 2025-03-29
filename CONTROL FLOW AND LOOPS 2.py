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
    return execute_task("Check if a number is even or odd using an if-else statement.",
                        "An even number is divisible by 2, while an odd number is not. The modulo operator (%) helps determine this.",
                        "num = int(input('Enter a number: '))\nif num % 2 == 0:\n    print('Even')\nelse:\n    print('Odd')", 1)

def task_2():
    return execute_task("Print all prime numbers within a given range using a for loop.",
                        "A prime number is only divisible by 1 and itself. We iterate through numbers and check divisibility using a loop.",
                        "start, end = 10, 50\nfor num in range(start, end+1):\n    if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):\n        print(num)", 2)

def task_3():
    return execute_task("Use a while loop to find the sum of digits of a number.",
                        "Extract digits using modulus (%), sum them, and reduce the number using floor division (//).", 
                        "num = int(input('Enter a number: '))\nsum_digits = 0\nwhile num > 0:\n    sum_digits += num % 10\n    num //= 10\nprint(sum_digits)", 3)

def task_4():
    return execute_task("Print a right-angled triangle pattern using nested loops.",
                        "Each row prints increasing '*' characters, using nested loops.",
                        "for i in range(1, 6):\n    print('*' * i)", 4)

def task_5():
    return execute_task("Check if a string is a palindrome using a loop.",
                        "A palindrome reads the same forwards and backwards. We check by reversing the string.",
                        "s = input('Enter a string: ')\nif s == s[::-1]:\n    print('Palindrome')\nelse:\n    print('Not a palindrome')", 5)

def task_6():
    return execute_task("Find the GCD of two numbers using a while loop.",
                        "The greatest common divisor (GCD) is found using the Euclidean algorithm.",
                        "a, b = 56, 98\nwhile b:\n    a, b = b, a % b\nprint(a)", 6)

def task_7():
    return execute_task("Find the factorial of a number using a loop.",
                        "Factorial is calculated as n! = n × (n-1) × ... × 1.",
                        "num = int(input('Enter a number: '))\nfact = 1\nfor i in range(1, num + 1):\n    fact *= i\nprint(fact)", 7)

def task_8():
    return execute_task("Reverse a number using a while loop.",
                        "Extract digits using %, and build the reversed number by shifting digits.",
                        "num = int(input('Enter a number: '))\nrev = 0\nwhile num > 0:\n    rev = rev * 10 + num % 10\n    num //= 10\nprint(rev)", 8)

def task_9():
    return execute_task("Print Fibonacci series up to n terms.",
                        "The Fibonacci series follows: F(n) = F(n-1) + F(n-2).", 
                        "n = int(input('Enter n: '))\na, b = 0, 1\nfor _ in range(n):\n    print(a, end=' ')\n    a, b = b, a + b", 9)

def task_10():
    return execute_task("Find the sum of even and odd numbers in a list.",
                        "Filter even and odd numbers using modulo (%), then sum them separately.",
                        "numbers = [1, 2, 3, 4, 5, 6]\neven_sum = sum(num for num in numbers if num % 2 == 0)\nodd_sum = sum(num for num in numbers if num % 2 != 0)\nprint(even_sum, odd_sum)", 10)

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
