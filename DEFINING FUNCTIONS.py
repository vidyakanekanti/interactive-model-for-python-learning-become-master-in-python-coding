import sys
import time
from io import StringIO

print("Welcome to Python Tutor - Basics of Functions & Function Calls for BTech Placements")

# Tracking attempts and time
task_attempts = {}
task_times = {}

def get_user_code(prompt, explanation, example_code):
    """Prompts user for input, explains the concept, and captures their code."""
    print("\n" + "=" * 50)
    print(f"💡 Task: {prompt}")
    print("-" * 50)
    print("📖 Explanation:")
    print(explanation)
    print("📝 Example Code:")
    print(example_code)
    print("=" * 50)
    
    # User code input
    lines = []
    print("\n⌨️ Enter your code (type 'done' to finish, 'exit' to quit):")
    while True:
        line = input(">>> ").strip()
        if line.lower() in ["done", "exit"]:
            break
        lines.append(line)
    
    code = "\n".join(lines)
    return code

def run_code(code):
    """Executes the user's code and returns the output or error message."""
    old_stdout = sys.stdout
    redirected_output = StringIO()
    sys.stdout = redirected_output
    try:
        exec(code, globals())
        output = redirected_output.getvalue().strip()
    except Exception as e:
        output = f"❌ Error: {str(e)}"
    finally:
        sys.stdout = old_stdout
    return output

def execute_task(challenge, explanation, example, task_num):
    """Executes a specific function problem and tracks user attempts."""
    attempts = 0
    start_time = time.time()
    
    while True:
        attempts += 1
        user_code = get_user_code(challenge, explanation, example)
        output = run_code(user_code)
        
        if "Error" in output:
            print(f"\n⚠️ Feedback: {output}. Try again!")
        else:
            print(f"\n✅ Feedback: Well done! 🎉 Output:\n{output}")
            break
    
    end_time = time.time()
    task_attempts[task_num] = attempts
    task_times[task_num] = round(end_time - start_time, 2)
    
    return input("\n🔄 Redo this task? (yes/no): ").strip().lower() == "yes"

# 10 Function-Based Challenges
def task_1():
    return execute_task("Define and call a simple function.",
                        "Use the `def` keyword to define a function and call it using `function_name()`.",
                        "def greet():\n    print('Hello, world!')\ngreet()", 1)

def task_2():
    return execute_task("Pass arguments to a function.",
                        "Functions can take parameters, which allow you to pass values.",
                        "def greet(name):\n    print(f'Hello, {name}!')\ngreet('Alice')", 2)

def task_3():
    return execute_task("Use a function with a return statement.",
                        "The `return` statement lets a function send a value back to the caller.",
                        "def add(a, b):\n    return a + b\nprint(add(3, 5))", 3)

def task_4():
    return execute_task("Use default parameters in a function.",
                        "Default arguments allow you to call a function with fewer parameters.",
                        "def greet(name='Guest'):\n    print(f'Hello, {name}!')\ngreet()\ngreet('Alice')", 4)

def task_5():
    return execute_task("Use keyword arguments while calling a function.",
                        "Keyword arguments let you specify parameters by name.",
                        "def introduce(name, age):\n    print(f'{name} is {age} years old.')\nintroduce(age=25, name='Bob')", 5)

def task_6():
    return execute_task("Use variable-length arguments (*args).",
                        "`*args` allows a function to accept any number of positional arguments.",
                        "def add_numbers(*args):\n    return sum(args)\nprint(add_numbers(1, 2, 3, 4))", 6)

def task_7():
    return execute_task("Use variable-length keyword arguments (**kwargs).",
                        "`**kwargs` allows a function to accept any number of keyword arguments.",
                        "def show_info(**kwargs):\n    for key, value in kwargs.items():\n        print(f'{key}: {value}')\nshow_info(name='Alice', age=30, city='New York')", 7)

def task_8():
    return execute_task("Use a function inside another function (nested functions).",
                        "A function can be defined inside another function for local usage.",
                        "def outer():\n    def inner():\n        print('Inner function!')\n    inner()\nouter()", 8)

def task_9():
    return execute_task("Use a function as an argument (higher-order function).",
                        "Functions can accept other functions as arguments.",
                        "def apply(func, x):\n    return func(x)\ndef square(n):\n    return n * n\nprint(apply(square, 5))", 9)

def task_10():
    return execute_task("Use lambda functions in Python.",
                        "A lambda function is a small anonymous function.",
                        "square = lambda x: x * x\nprint(square(6))", 10)

# Task list
tasks = [task_1, task_2, task_3, task_4, task_5, task_6, task_7, task_8, task_9, task_10]

def main():
    print("\n🚀 Welcome to Python Tutor - Basics of Functions & Function Calls for BTech Placements")
    
    while True:
        task_num = input("\n🎯 Enter problem number (or 'exit' to quit): ").strip()
        
        if task_num.lower() == "exit":
            print("\n📊 Session Summary:")
            for key, attempts in task_attempts.items():
                print(f"Problem {key}: {attempts} attempts, Time: {task_times.get(key, 0)} sec")
            print("👋 Thank you for practicing with Python Tutor! 🚀")
            break

        if task_num.isdigit():
            task_num = int(task_num)
            if 1 <= task_num <= len(tasks):
                redo = True
                while redo:
                    redo = tasks[task_num - 1]()
            else:
                print(f"❌ Invalid problem number. Choose between 1 and {len(tasks)}.")
        else:
            print("❌ Invalid input. Enter a valid problem number.")

if __name__ == "__main__":
    main()
