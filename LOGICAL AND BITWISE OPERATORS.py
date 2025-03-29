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

# Chapter: Logical & Bitwise Operators
def task_1():
    return execute_task("Use logical AND (and) operator to check if two conditions are true.",
                        "Logical AND (and) returns True only if both conditions are True.",
                        "a, b = 10, 20\nprint(a > 5 and b < 30)", 1)

def task_2():
    return execute_task("Use logical OR (or) operator to check if at least one condition is true.",
                        "Logical OR (or) returns True if at least one condition is True.",
                        "a, b = 10, 5\nprint(a > 15 or b < 10)", 2)

def task_3():
    return execute_task("Use logical NOT (not) operator to invert a Boolean expression.",
                        "Logical NOT (not) negates the boolean value of an expression.",
                        "x = True\nprint(not x)", 3)

def task_4():
    return execute_task("Check if a number is within a range using logical AND.",
                        "Use relational and logical operators together to check a range.",
                        "num = 15\nprint(num >= 10 and num <= 20)", 4)

def task_5():
    return execute_task("Check if a number is out of a range using logical OR.",
                        "Use logical OR (or) to check if a number is outside a given range.",
                        "num = 25\nprint(num < 10 or num > 20)", 5)

def task_6():
    return execute_task("Use a combination of logical AND, OR, and NOT operators in a complex condition.",
                        "Combine multiple logical operators in a single statement.",
                        "a, b, c = 10, 20, 30\nprint(a < b and not (c < a or b > c))", 6)

def task_7():
    return execute_task("Perform bitwise AND (&) operation on two numbers.",
                        "Bitwise AND compares each bit and returns 1 if both bits are 1.",
                        "a, b = 5, 3\nprint(a & b)", 7)

def task_8():
    return execute_task("Perform bitwise OR (|) operation on two numbers.",
                        "Bitwise OR compares each bit and returns 1 if either bit is 1.",
                        "a, b = 5, 3\nprint(a | b)", 8)

def task_9():
    return execute_task("Perform bitwise XOR (^) operation on two numbers.",
                        "Bitwise XOR compares each bit and returns 1 if bits are different.",
                        "a, b = 5, 3\nprint(a ^ b)", 9)

def task_10():
    return execute_task("Perform bitwise NOT (~) operation on a number.",
                        "Bitwise NOT (~) inverts all bits of a number.",
                        "num = 5\nprint(~num)", 10)

def task_11():
    return execute_task("Perform left shift (<<) operation on a number.",
                        "Left shift (<<) shifts bits to the left, multiplying the number by 2 for each shift.",
                        "num = 5\nprint(num << 1)", 11)

def task_12():
    return execute_task("Perform right shift (>>) operation on a number.",
                        "Right shift (>>) shifts bits to the right, dividing the number by 2 for each shift.",
                        "num = 20\nprint(num >> 1)", 12)

def task_13():
    return execute_task("Combine logical and bitwise operators in a single expression.",
                        "Use a mix of logical and bitwise operators to check conditions.",
                        "a, b = 6, 3\nprint((a > b and (a & b) == 2) or (a | b) > 5)", 13)

tasks = [task_1, task_2, task_3, task_4, task_5, task_6, task_7, task_8, task_9, task_10, task_11, task_12, task_13]

def print_report():
    print("\n=== Performance Report ===")
    for i in range(1, len(tasks) + 1):
        attempts = task_attempts.get(i, 0)
        time_taken = task_times.get(i, 0)
        print(f"Task {i}: {attempts} attempt(s), {time_taken} sec")
    print("=========================")

def main():
    print("Welcome to Python Tutor - Logical & Bitwise Operators")
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
