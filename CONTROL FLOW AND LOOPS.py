import sys
import time
from io import StringIO

print("Note: This tutorial helps you learn Python step by step. No additional installation is required for basic Python.")

# Tracking attempts and time
task_attempts = {}
task_times = {}

def get_user_code(prompt, example_code):
    print(prompt)
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

def execute_task(challenge, example, task_num):
    attempts = 0
    start_time = time.time()
    while True:
        attempts += 1
        user_code = get_user_code(challenge, example)
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
    return execute_task("Use an if-else statement to check if a number is positive, negative, or zero.", "num = int(input('Enter a number: '))\nif num > 0:\n    print('Positive')\nelif num < 0:\n    print('Negative')\nelse:\n    print('Zero')", 1)

def task_2():
    return execute_task("Use a for loop to iterate through a list of numbers and print them.", "numbers = [10, 20, 30, 40]\nfor num in numbers:\n    print(num)", 2)

def task_3():
    return execute_task("Use a while loop to print numbers from 1 to 5.", "i = 1\nwhile i <= 5:\n    print(i)\n    i += 1", 3)

def task_4():
    return execute_task("Use a nested loop to print a pattern of stars.", "for i in range(1, 6):\n    for j in range(i):\n        print('*', end='')\n    print()", 4)

def task_5():
    return execute_task("Write a function that checks if a number is prime.", "def is_prime(n):\n    if n <= 1:\n        return False\n    for i in range(2, int(n**0.5) + 1):\n        if n % i == 0:\n            return False\n    return True\nprint(is_prime(7))", 5)

def task_6():
    return execute_task("Use list comprehension to filter even numbers from a list.", "numbers = [1, 2, 3, 4, 5, 6]\neven_numbers = [num for num in numbers if num % 2 == 0]\nprint(even_numbers)", 6)

def task_7():
    return execute_task("Use break to stop a loop when a condition is met.", "for i in range(1, 10):\n    if i == 5:\n        break\n    print(i)", 7)

def task_8():
    return execute_task("Use continue to skip an iteration in a loop.", "for i in range(1, 6):\n    if i == 3:\n        continue\n    print(i)", 8)

def task_9():
    return execute_task("Use pass inside a loop as a placeholder.", "for i in range(5):\n    if i == 2:\n        pass # Placeholder\n    else:\n        print(i)", 9)

def task_10():
    return execute_task("Use the enumerate function in a loop.", "words = ['apple', 'banana', 'cherry']\nfor index, word in enumerate(words):\n    print(index, word)", 10)

def task_11():
    return execute_task("Use the zip function to iterate over two lists.", "list1 = ['a', 'b', 'c']\nlist2 = [1, 2, 3]\nfor a, b in zip(list1, list2):\n    print(a, b)", 11)

def task_12():
    return execute_task("Write a function that finds the factorial of a number using recursion.", "def factorial(n):\n    return 1 if n == 0 else n * factorial(n-1)\nprint(factorial(5))", 12)

def task_13():
    return execute_task("Implement a Fibonacci sequence generator.", "def fibonacci(n):\n    a, b = 0, 1\n    for _ in range(n):\n        print(a, end=' ')\n        a, b = b, a + b\nprint(fibonacci(10))", 13)

def task_14():
    return execute_task("Find the sum of all even numbers up to a given number.", "n = int(input('Enter a number: '))\nprint(sum([i for i in range(n+1) if i % 2 == 0]))", 14)

def task_15():
    return execute_task("Reverse a given string using a loop.", "s = input('Enter a string: ')\nreversed_s = ''\nfor char in s:\n    reversed_s = char + reversed_s\nprint(reversed_s)", 15)

tasks = [task_1, task_2, task_3, task_4, task_5, task_6, task_7, task_8, task_9, task_10, task_11, task_12, task_13, task_14, task_15]

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
