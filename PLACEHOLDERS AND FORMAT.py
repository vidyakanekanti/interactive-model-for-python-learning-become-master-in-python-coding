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

# Chapter: format() and Placeholder {}
def task_1():
    return execute_task("Use format() to print your name and age.",
                        "Use placeholders {} to insert values into a string.",
                        "name = 'Alice'\nage = 25\nprint('My name is {} and I am {} years old.'.format(name, age))", 1)

def task_2():
    return execute_task("Format a floating number to two decimal places.",
                        "Use {:.2f} inside format() to limit decimals.",
                        "pi = 3.141592\nprint('Pi to two decimal places: {:.2f}'.format(pi))", 2)

def task_3():
    return execute_task("Rearrange placeholders using index numbers.",
                        "Placeholders can be reordered using numbers inside {}.",
                        "print('{1} {0} {2}'.format('world', 'Hello', '!'))", 3)

def task_4():
    return execute_task("Use named placeholders inside format().",
                        "Provide keyword arguments inside format().",
                        "print('My name is {name} and I am {age} years old.'.format(name='Bob', age=30))", 4)

def task_5():
    return execute_task("Align text to left, right, and center.",
                        "Use {:<}, {:>} and {:^} inside format().",
                        "print('|{:<10}|{:^10}|{:>10}|'.format('Left', 'Center', 'Right'))", 5)

def task_6():
    return execute_task("Format numbers with commas as thousand separators.",
                        "Use {:,} inside format().",
                        "num = 1234567\nprint('Formatted number: {:,}'.format(num))", 6)

def task_7():
    return execute_task("Convert a number to binary, octal, and hexadecimal.",
                        "Use {:b}, {:o}, {:x} inside format().",
                        "num = 255\nprint('Binary: {:b}, Octal: {:o}, Hex: {:x}'.format(num, num, num))", 7)

def task_8():
    return execute_task("Use format() with a dictionary.",
                        "Use **dict_name to unpack dictionary values inside format().",
                        "person = {'name': 'Charlie', 'age': 28}\nprint('My name is {name} and I am {age} years old.'.format(**person))", 8)

def task_9():
    return execute_task("Use format() to format a date.",
                        "Use placeholders to insert day, month, and year.",
                        "day, month, year = 15, 'March', 2025\nprint('Today is {} {} {}.'.format(day, month, year))", 9)

def task_10():
    return execute_task("Format a percentage with two decimal places.",
                        "Use {:.2%} to format percentages.",
                        "value = 0.8567\nprint('Percentage: {:.2%}'.format(value))", 10)

def task_11():
    return execute_task("Use format() inside f-strings.",
                        "Combine format() with f-strings.",
                        "name = 'David'\nage = 40\nprint(f'My name is {name} and I am {age} years old.')", 11)

def task_12():
    return execute_task("Fill placeholders with a dynamic width.",
                        "Use {:width} inside format().",
                        "width = 15\nprint('{:>{}}'.format('Aligned', width))", 12)

def task_13():
    return execute_task("Pad numbers with leading zeros.",
                        "Use {:0width} inside format().",
                        "num = 7\nprint('Padded number: {:03}'.format(num))", 13)

tasks = [task_1, task_2, task_3, task_4, task_5, task_6, task_7, task_8, task_9, task_10, task_11, task_12, task_13]

def print_report():
    print("\n=== Performance Report ===")
    for i in range(1, len(tasks) + 1):
        attempts = task_attempts.get(i, 0)
        time_taken = task_times.get(i, 0)
        print(f"Task {i}: {attempts} attempt(s), {time_taken} sec")
    print("=========================")

def main():
    print("Welcome to Python Tutor - format() and Placeholder {}")
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
