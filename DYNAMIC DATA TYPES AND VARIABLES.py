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

# Chapter: Dynamic Data Types & Variables
def task_1():
    return execute_task("Declare a variable and print its type.",
                        "Use the type() function to check the data type of a variable.",
                        "x = 10\nprint(type(x))", 1)

def task_2():
    return execute_task("Assign different data types to the same variable and print their types.",
                        "Python allows dynamic typing, meaning a variable can hold different data types at different times.",
                        "x = 10\nprint(type(x))\nx = 'Hello'\nprint(type(x))", 2)

def task_3():
    return execute_task("Swap two variables without using a third variable.",
                        "Python allows swapping variables directly using tuple unpacking.",
                        "a, b = 5, 10\na, b = b, a\nprint(a, b)", 3)

def task_4():
    return execute_task("Convert an integer to a float and a string.",
                        "Use float() to convert an int to a float and str() to convert it to a string.",
                        "num = 10\nprint(float(num))\nprint(str(num))", 4)

def task_5():
    return execute_task("Check the type of user input.",
                        "Use input() to get user input and type() to check its type.",
                        "user_input = input('Enter something: ')\nprint(type(user_input))", 5)

def task_6():
    return execute_task("Change a variable from string to integer and perform an operation.",
                        "Use int() to convert a string to an integer before performing arithmetic operations.",
                        "num_str = '5'\nnum = int(num_str)\nprint(num + 10)", 6)

def task_7():
    return execute_task("Check if a variable is of a specific type using isinstance().",
                        "The isinstance() function checks if a variable is of a particular type.",
                        "x = 3.14\nprint(isinstance(x, float))", 7)

def task_8():
    return execute_task("Demonstrate mutable vs immutable types.",
                        "Lists (mutable) can be changed, whereas strings (immutable) cannot.",
                        "s = 'hello'\ntry:\n    s[0] = 'H'\nexcept TypeError:\n    print('Strings are immutable')\n\nlst = [1, 2, 3]\nlst[0] = 10\nprint(lst)", 8)

def task_9():
    return execute_task("Use type hints for variables in Python.",
                        "Python supports type hints to indicate expected variable types.",
                        "x: int = 10\ny: str = 'Python'\nprint(x, y)", 9)

def task_10():
    return execute_task("Use dynamic typing to store different data types in a list.",
                        "Python lists can store multiple data types due to dynamic typing.",
                        "my_list = [10, 'Hello', 3.14, True]\nfor item in my_list:\n    print(type(item))", 10)

def task_11():
    return execute_task("Check if a variable exists before using it.",
                        "Use the 'in' keyword with locals() or globals() to check if a variable exists.",
                        "var_name = 'x'\nif var_name in globals():\n    print('Variable exists')\nelse:\n    print('Variable does not exist')", 11)

def task_12():
    return execute_task("Use eval() to dynamically assign a variable value.",
                        "The eval() function evaluates a string expression as Python code.",
                        "var_name = 'x'\nvalue = '10'\nglobals()[var_name] = eval(value)\nprint(x)", 12)

def task_13():
    return execute_task("Convert different data types to boolean values and print results.",
                        "Use bool() to see which values evaluate to True or False.",
                        "print(bool(0))\nprint(bool(1))\nprint(bool(''))\nprint(bool('Python'))", 13)

tasks = [task_1, task_2, task_3, task_4, task_5, task_6, task_7, task_8, task_9, task_10, task_11, task_12, task_13]

def print_report():
    print("\n=== Performance Report ===")
    for i in range(1, len(tasks) + 1):
        attempts = task_attempts.get(i, 0)
        time_taken = task_times.get(i, 0)
        print(f"Task {i}: {attempts} attempt(s), {time_taken} sec")
    print("=========================")

def main():
    print("Welcome to Python Tutor - Dynamic Data Types & Variables")
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
