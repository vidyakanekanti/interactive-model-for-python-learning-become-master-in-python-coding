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

# Chapter: Arithmetic, Relational & Bitwise Operators
def task_1():
    return execute_task("Perform basic arithmetic operations: addition, subtraction, multiplication, and division.",
                        "Use +, -, *, and / operators to perform arithmetic operations.",
                        "a, b = 10, 3\nprint(a + b, a - b, a * b, a / b)", 1)

def task_2():
    return execute_task("Find the remainder of a division operation.",
                        "Use the modulus operator (%) to find the remainder.",
                        "a, b = 10, 3\nprint(a % b)", 2)

def task_3():
    return execute_task("Use the floor division operator to divide two numbers.",
                        "The // operator performs division and rounds down the result.",
                        "a, b = 10, 3\nprint(a // b)", 3)

def task_4():
    return execute_task("Raise a number to a power using the exponentiation operator.",
                        "Use ** to raise a number to a power.",
                        "a, b = 2, 3\nprint(a ** b)", 4)

def task_5():
    return execute_task("Compare two numbers using relational operators (==, !=, >, <, >=, <=).",
                        "Relational operators compare values and return True or False.",
                        "a, b = 10, 20\nprint(a == b, a != b, a > b, a < b, a >= b, a <= b)", 5)

def task_6():
    return execute_task("Check if a number is even or odd using relational and modulus operators.",
                        "Use % 2 to determine if a number is even or odd.",
                        "num = 7\nprint('Even' if num % 2 == 0 else 'Odd')", 6)

def task_7():
    return execute_task("Check if a number is within a range using relational operators.",
                        "Use < and > to check if a number lies within a given range.",
                        "num = 15\nprint(10 <= num <= 20)", 7)

def task_8():
    return execute_task("Perform bitwise AND, OR, and XOR operations.",
                        "Use &, |, and ^ for bitwise operations.",
                        "a, b = 5, 3\nprint(a & b, a | b, a ^ b)", 8)

def task_9():
    return execute_task("Perform left shift and right shift operations on a number.",
                        "Use << to shift bits left and >> to shift bits right.",
                        "num = 5\nprint(num << 1, num >> 1)", 9)

def task_10():
    return execute_task("Find if a number is positive, negative, or zero using relational operators.",
                        "Use if-elif-else conditions with >, <, and == operators.",
                        "num = -10\nif num > 0:\n    print('Positive')\nelif num < 0:\n    print('Negative')\nelse:\n    print('Zero')", 10)

def task_11():
    return execute_task("Use bitwise NOT operator to invert bits of a number.",
                        "Use ~ to flip all bits of a number (bitwise NOT).",
                        "num = 5\nprint(~num)", 11)

def task_12():
    return execute_task("Use relational operators to compare strings.",
                        "Strings can be compared lexicographically using relational operators.",
                        "str1, str2 = 'apple', 'banana'\nprint(str1 < str2)", 12)

def task_13():
    return execute_task("Use a combination of arithmetic, relational, and bitwise operators in a single expression.",
                        "Combine different operators in a meaningful way.",
                        "a, b = 6, 3\nprint((a + b) > 5 and (a & b) == 2)", 13)

tasks = [task_1, task_2, task_3, task_4, task_5, task_6, task_7, task_8, task_9, task_10, task_11, task_12, task_13]

def print_report():
    print("\n=== Performance Report ===")
    for i in range(1, len(tasks) + 1):
        attempts = task_attempts.get(i, 0)
        time_taken = task_times.get(i, 0)
        print(f"Task {i}: {attempts} attempt(s), {time_taken} sec")
    print("=========================")

def main():
    print("Welcome to Python Tutor - Arithmetic, Relational & Bitwise Operators")
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
