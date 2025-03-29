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

# 13 NEW Questions on range()
def task_1():
    return execute_task("Print numbers from 5 to 50 with a step of 5 using range().",
                        "Use range(start, stop, step) to print multiples of 5.",
                        "for i in range(5, 51, 5):\n    print(i, end=' ')", 1)

def task_2():
    return execute_task("Print the sum of even numbers from 1 to N using range().",
                        "Use range() with a step of 2 to select even numbers.",
                        "n = int(input('Enter N: '))\nprint(sum(range(2, n+1, 2)))", 2)

def task_3():
    return execute_task("Print numbers from N to 1 in steps of 3.",
                        "Use a negative step in range() for decrementing values.",
                        "n = int(input('Enter N: '))\nfor i in range(n, 0, -3):\n    print(i, end=' ')", 3)

def task_4():
    return execute_task("Print all prime numbers from 1 to N using range().",
                        "Use range() with a loop to check prime numbers.",
                        "n = int(input('Enter N: '))\ndef is_prime(num):\n    return num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1))\nfor i in range(1, n+1):\n    if is_prime(i):\n        print(i, end=' ')", 4)

def task_5():
    return execute_task("Print the factorial of N using range().",
                        "Use range() with a loop to multiply factorial values.",
                        "n = int(input('Enter N: '))\nfact = 1\nfor i in range(1, n+1):\n    fact *= i\nprint(fact)", 5)

def task_6():
    return execute_task("Find the sum of squares of first N numbers using range().",
                        "Use list comprehension with range().",
                        "n = int(input('Enter N: '))\nprint(sum(i**2 for i in range(1, n+1)))", 6)

def task_7():
    return execute_task("Generate and print a list of first N cube numbers using range().",
                        "Use list comprehension with range().",
                        "n = int(input('Enter N: '))\ncubes = [i**3 for i in range(1, n+1)]\nprint(cubes)", 7)

def task_8():
    return execute_task("Find the largest multiple of 7 in the range 1 to N.",
                        "Use range() to find the largest number divisible by 7.",
                        "n = int(input('Enter N: '))\nprint(max(i for i in range(1, n+1) if i % 7 == 0))", 8)

def task_9():
    return execute_task("Print the first N numbers in a geometric sequence with ratio 2.",
                        "Use range() and a loop to generate geometric sequences.",
                        "n = int(input('Enter N: '))\na = 1\nfor i in range(n):\n    print(a, end=' ')\n    a *= 2", 9)

def task_10():
    return execute_task("Print all numbers between N and M that are divisible by both 3 and 4.",
                        "Use range() and a loop with conditions.",
                        "n, m = map(int, input('Enter N and M: ').split())\nfor i in range(n, m+1):\n    if i % 3 == 0 and i % 4 == 0:\n        print(i, end=' ')", 10)

def task_11():
    return execute_task("Print a number triangle using range().",
                        "Use nested loops with range() to print a triangle pattern.",
                        "n = int(input('Enter N: '))\nfor i in range(1, n+1):\n    print(' '.join(str(j) for j in range(1, i+1)))", 11)

def task_12():
    return execute_task("Print a pyramid pattern using range().",
                        "Use nested loops with range() to generate a pyramid.",
                        "n = int(input('Enter number of rows: '))\nfor i in range(1, n+1):\n    print(' '*(n-i) + '*'*(2*i-1))", 12)

def task_13():
    return execute_task("Print all numbers in the range of 1 to 100 but skip numbers that are divisible by both 5 and 7.",
                        "Use range() and continue statement to skip specific numbers.",
                        "for i in range(1, 101):\n    if i % 5 == 0 and i % 7 == 0:\n        continue\n    print(i, end=' ')", 13)

tasks = [task_1, task_2, task_3, task_4, task_5, task_6, task_7, task_8, task_9, task_10, task_11, task_12, task_13]

def main():
    print("Welcome to Python Tutor - Advanced Questions on `range()` Function")
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

if __name__ == "__main__":
    main()
