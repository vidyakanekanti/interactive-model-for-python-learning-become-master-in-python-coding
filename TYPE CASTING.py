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

# Chapter: Type Casting & input()
def task_1():
    return execute_task("Use input() to take a string input from the user and print it.",
                        "The input() function reads user input as a string.",
                        "name = input('Enter your name: ')\nprint('Hello,', name)", 1)

def task_2():
    return execute_task("Take an integer input using input() and print its double.",
                        "Use int() to convert the input from string to an integer.",
                        "num = int(input('Enter a number: '))\nprint('Double:', num * 2)", 2)

def task_3():
    return execute_task("Take a floating-point input and print its square.",
                        "Use float() to convert input into a floating-point number.",
                        "num = float(input('Enter a number: '))\nprint('Square:', num ** 2)", 3)

def task_4():
    return execute_task("Take a Boolean input (1 for True, 0 for False) and print its negation.",
                        "Use bool() to convert integer input into Boolean.",
                        "val = bool(int(input('Enter 1 for True, 0 for False: ')))\nprint('Negation:', not val)", 4)

def task_5():
    return execute_task("Convert an integer input to a string and concatenate it with another string.",
                        "Use str() to convert an integer to a string.",
                        "age = int(input('Enter your age: '))\nprint('You are ' + str(age) + ' years old.')", 5)

def task_6():
    return execute_task("Take two inputs, one integer and one float, and add them together.",
                        "Use int() and float() to convert inputs before performing arithmetic operations.",
                        "num1 = int(input('Enter an integer: '))\nnum2 = float(input('Enter a float: '))\nprint('Sum:', num1 + num2)", 6)

def task_7():
    return execute_task("Convert a float input to an integer and print both values.",
                        "Use int() to convert a float into an integer, removing the decimal part.",
                        "num = float(input('Enter a float number: '))\nprint('Original:', num, 'Integer:', int(num))", 7)

def task_8():
    return execute_task("Convert an integer to binary, octal, and hexadecimal formats.",
                        "Use bin(), oct(), and hex() to convert an integer to different number systems.",
                        "num = int(input('Enter an integer: '))\nprint('Binary:', bin(num))\nprint('Octal:', oct(num))\nprint('Hexadecimal:', hex(num))", 8)

def task_9():
    return execute_task("Take a string input representing a number and convert it to an integer and float.",
                        "Use int() and float() to convert a string number into integer and float types.",
                        "num_str = input('Enter a number as string: ')\nprint('Integer:', int(num_str))\nprint('Float:', float(num_str))", 9)

def task_10():
    return execute_task("Use eval() to take a mathematical expression as input and evaluate it.",
                        "The eval() function executes a string as a Python expression.",
                        "expression = input('Enter a math expression: ')\nprint('Result:', eval(expression))", 10)

def task_11():
    return execute_task("Take multiple inputs in a single line and convert them into integers.",
                        "Use map() with int() to convert multiple inputs into integers.",
                        "a, b, c = map(int, input('Enter three numbers: ').split())\nprint('Sum:', a + b + c)", 11)

def task_12():
    return execute_task("Take user input, check if it can be converted to an integer, and handle errors.",
                        "Use try-except to handle invalid integer conversions.",
                        "try:\n    num = int(input('Enter an integer: '))\n    print('Valid number:', num)\nexcept ValueError:\n    print('Invalid input! Please enter a valid integer.')", 12)

def task_13():
    return execute_task("Take a list of space-separated numbers, convert to integers, and print the maximum.",
                        "Use list comprehension to convert input values into a list of integers.",
                        "nums = [int(x) for x in input('Enter numbers: ').split()]\nprint('Max number:', max(nums))", 13)

tasks = [task_1, task_2, task_3, task_4, task_5, task_6, task_7, task_8, task_9, task_10, task_11, task_12, task_13]

def print_report():
    print("\n=== Performance Report ===")
    for i in range(1, len(tasks) + 1):
        attempts = task_attempts.get(i, 0)
        time_taken = task_times.get(i, 0)
        print(f"Task {i}: {attempts} attempt(s), {time_taken} sec")
    print("=========================")

def main():
    print("Welcome to Python Tutor - Type Casting & input()")
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
