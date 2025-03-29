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

# Chapter: input(), print(), and Expressions
def task_1():
    return execute_task("Take a user's name as input and print a greeting message.",
                        "The input() function takes user input as a string, and print() displays it.",
                        "name = input('Enter your name: ')\nprint('Hello,', name + '!')", 1)

def task_2():
    return execute_task("Take two numbers as input and print their sum.",
                        "Use input() to take input and convert it to integers before performing addition.",
                        "a = int(input('Enter first number: '))\nb = int(input('Enter second number: '))\nprint('Sum:', a + b)", 2)

def task_3():
    return execute_task("Print a sentence using multiple arguments in print().",
                        "Use print() with multiple arguments separated by commas.",
                        "print('Python is', 'awesome!', 'Let\'s learn it together.')", 3)

def task_4():
    return execute_task("Print a formatted string using f-strings.",
                        "Use f-strings to insert variables into a string.",
                        "name = 'Alice'\nage = 25\nprint(f'My name is {name} and I am {age} years old.')", 4)

def task_5():
    return execute_task("Print a string with special characters like newline and tab.",
                        "Use escape sequences like \\n (new line) and \\t (tab).",
                        "print('Hello\\nWorld!\\tPython is fun!')", 5)

def task_6():
    return execute_task("Print a string multiple times using the * operator.",
                        "Use the * operator to repeat a string multiple times.",
                        "print('Python! ' * 3)", 6)

def task_7():
    return execute_task("Take a user's age as input and print a message with type checking.",
                        "Use type() to check the variable type and convert input using int().",
                        "age = input('Enter your age: ')\nprint('Before conversion:', type(age))\nage = int(age)\nprint('After conversion:', type(age))", 7)

def task_8():
    return execute_task("Evaluate a mathematical expression using eval().",
                        "The eval() function evaluates an expression given as a string.",
                        "expr = input('Enter a mathematical expression: ')\nprint('Result:', eval(expr))", 8)

def task_9():
    return execute_task("Use sep and end parameters in print() to format output.",
                        "The sep parameter defines a separator, and end specifies the ending character.",
                        "print('Python', 'is', 'awesome', sep='-', end='!')", 9)

def task_10():
    return execute_task("Print a float value rounded to 2 decimal places.",
                        "Use the round() function to limit decimal places.",
                        "num = 3.1415926535\nprint('Rounded:', round(num, 2))", 10)

def task_11():
    return execute_task("Take multiple inputs in one line and print them.",
                        "Use input().split() to take multiple inputs at once.",
                        "a, b, c = input('Enter three values: ').split()\nprint('You entered:', a, b, c)", 11)

def task_12():
    return execute_task("Take user input and print whether it's a number or a string.",
                        "Use isdigit() to check if a string contains only numbers.",
                        "user_input = input('Enter something: ')\nif user_input.isdigit():\n    print('You entered a number.')\nelse:\n    print('You entered a string.')", 12)

def task_13():
    return execute_task("Print a statement using concatenation and string conversion.",
                        "Use str() to convert non-string values before concatenation.",
                        "name = 'John'\nage = 30\nprint('Name: ' + name + ', Age: ' + str(age))", 13)

tasks = [task_1, task_2, task_3, task_4, task_5, task_6, task_7, task_8, task_9, task_10, task_11, task_12, task_13]

def print_report():
    print("\n=== Performance Report ===")
    for i in range(1, len(tasks) + 1):
        attempts = task_attempts.get(i, 0)
        time_taken = task_times.get(i, 0)
        print(f"Task {i}: {attempts} attempt(s), {time_taken} sec")
    print("=========================")

def main():
    print("Welcome to Python Tutor - input(), print(), and Expressions")
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
