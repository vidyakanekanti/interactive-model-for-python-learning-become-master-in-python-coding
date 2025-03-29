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
    print("Example:")
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

# Chapter: Print format() with String and Bool
def task_1():
    return execute_task("Use format() to print a greeting message.",
                        "format() allows inserting variables into strings.",
                        "name = 'Alice'\nprint('Hello, {}!'.format(name))", 1)

def task_2():
    return execute_task("Format a string with multiple placeholders.",
                        "Use multiple {} placeholders and format() arguments.",
                        "print('My name is {} and I am {} years old.'.format('Bob', 25))", 2)

def task_3():
    return execute_task("Use named placeholders in format().",
                        "Named placeholders make formatting more readable.",
                        "print('Name: {name}, Age: {age}'.format(name='Charlie', age=30))", 3)

def task_4():
    return execute_task("Format boolean values in a sentence.",
                        "Boolean values can be formatted like strings.",
                        "is_python_fun = True\nprint('Is Python fun? {}'.format(is_python_fun))", 4)

def task_5():
    return execute_task("Align text using format().",
                        "Use < for left align, > for right align, and ^ for center align.",
                        "print('{:<10} {:^10} {:>10}'.format('Left', 'Center', 'Right'))", 5)

def task_6():
    return execute_task("Display a percentage using format().",
                        "Use {:.2%} to format numbers as percentages.",
                        "score = 0.85\nprint('Success rate: {:.2%}'.format(score))", 6)

def task_7():
    return execute_task("Format numbers with leading zeros.",
                        "Use {:03d} to add leading zeros to numbers.",
                        "print('Order number: {:03d}'.format(7))", 7)

def task_8():
    return execute_task("Combine text, numbers, and booleans in format().",
                        "Mix different data types in a formatted string.",
                        "name = 'David'\nage = 28\nverified = True\nprint('{} is {} years old. Verified: {}'.format(name, age, verified))", 8)

def task_9():
    return execute_task("Format a boolean as 'Yes' or 'No'.",
                        "Use conditional expressions inside format().",
                        "is_member = False\nprint('Membership: {}'.format('Yes' if is_member else 'No'))", 9)

def task_10():
    return execute_task("Print a formatted table using format().",
                        "Use format() to structure tabular data.",
                        "print('{:<10} {:>10}'.format('Item', 'Price'))\nprint('{:<10} {:>10.2f}'.format('Apple', 1.5))", 10)

def task_11():
    return execute_task("Use format() to print a binary number.",
                        "Format integers as binary using {:b}.",
                        "num = 10\nprint('Binary of {} is {:b}'.format(num, num))", 11)

def task_12():
    return execute_task("Use format() for hexadecimal conversion.",
                        "Format integers as hexadecimal using {:x}.",
                        "num = 255\nprint('Hex of {} is {:x}'.format(num, num))", 12)

def task_13():
    return execute_task("Format floating-point numbers with precision.",
                        "Use {:.2f} to display numbers with 2 decimal places.",
                        "pi = 3.14159\nprint('Pi rounded: {:.2f}'.format(pi))", 13)

tasks = [task_1, task_2, task_3, task_4, task_5, task_6, task_7, task_8, task_9, task_10, task_11, task_12, task_13]

def print_report():
    print("\n=== Performance Report ===")
    for i in range(1, len(tasks) + 1):
        attempts = task_attempts.get(i, 0)
        time_taken = task_times.get(i, 0)
        print(f"Task {i}: {attempts} attempt(s), {time_taken} sec")
    print("=========================")

def main():
    print("Welcome to Python Tutor - Print format() with Strings & Booleans")
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
