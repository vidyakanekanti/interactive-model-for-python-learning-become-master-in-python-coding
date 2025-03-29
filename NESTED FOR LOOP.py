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

# 13 NEW Questions on Nested for Loop
def task_1():
    return execute_task("Print a square pattern of '*' using a nested for loop.",
                        "Use two for loops, one for rows and another for columns.",
                        "n = int(input('Enter N: '))\nfor i in range(n):\n    for j in range(n):\n        print('*', end=' ')\n    print()", 1)

def task_2():
    return execute_task("Print a right-angled triangle pattern of '*' using a nested for loop.",
                        "Increase the number of '*' in each row using range().",
                        "n = int(input('Enter N: '))\nfor i in range(1, n+1):\n    for j in range(i):\n        print('*', end=' ')\n    print()", 2)

def task_3():
    return execute_task("Print a mirrored right-angled triangle pattern using a nested for loop.",
                        "Use spaces before printing '*'.",
                        "n = int(input('Enter N: '))\nfor i in range(1, n+1):\n    print(' ' * (n - i) + '*' * i)", 3)

def task_4():
    return execute_task("Print a pyramid pattern of '*' using a nested for loop.",
                        "Use a nested loop to align '*' in a pyramid shape.",
                        "n = int(input('Enter N: '))\nfor i in range(1, n+1):\n    print(' ' * (n - i) + '*' * (2 * i - 1))", 4)

def task_5():
    return execute_task("Print an inverted pyramid pattern using a nested for loop.",
                        "Decrease the number of '*' in each row.",
                        "n = int(input('Enter N: '))\nfor i in range(n, 0, -1):\n    print(' ' * (n - i) + '*' * (2 * i - 1))", 5)

def task_6():
    return execute_task("Print a Floyd’s triangle using a nested for loop.",
                        "Print numbers sequentially in a triangle pattern.",
                        "n = int(input('Enter N: '))\nk = 1\nfor i in range(1, n+1):\n    for j in range(i):\n        print(k, end=' ')\n        k += 1\n    print()", 6)

def task_7():
    return execute_task("Print Pascal's Triangle up to N rows using a nested for loop.",
                        "Use factorial and binomial coefficients to print Pascal's Triangle.",
                        "import math\nn = int(input('Enter N: '))\nfor i in range(n):\n    print(' ' * (n - i), end=' ')\n    for j in range(i + 1):\n        print(math.comb(i, j), end=' ')\n    print()", 7)

def task_8():
    return execute_task("Print a checkerboard pattern using a nested for loop.",
                        "Use a nested loop to print alternating '#' and ' '.",
                        "n = int(input('Enter size: '))\nfor i in range(n):\n    for j in range(n):\n        if (i + j) % 2 == 0:\n            print('#', end=' ')\n        else:\n            print(' ', end=' ')\n    print()", 8)

def task_9():
    return execute_task("Print the multiplication table up to N using a nested for loop.",
                        "Use a nested loop to generate tables for numbers 1 to N.",
                        "n = int(input('Enter N: '))\nfor i in range(1, n+1):\n    for j in range(1, 11):\n        print(f'{i} x {j} = {i*j}', end=' | ')\n    print()", 9)

def task_10():
    return execute_task("Print all prime numbers up to N using a nested for loop.",
                        "Check for divisibility using another loop inside the first loop.",
                        "n = int(input('Enter N: '))\nfor i in range(2, n+1):\n    for j in range(2, int(i ** 0.5) + 1):\n        if i % j == 0:\n            break\n    else:\n        print(i, end=' ')", 10)

def task_11():
    return execute_task("Find the transpose of a given matrix using a nested for loop.",
                        "Swap rows and columns using a nested loop.",
                        "matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]\nrows, cols = len(matrix), len(matrix[0])\ntranspose = [[matrix[j][i] for j in range(rows)] for i in range(cols)]\nfor row in transpose:\n    print(row)", 11)

def task_12():
    return execute_task("Sort a list of numbers using Bubble Sort with a nested for loop.",
                        "Repeatedly swap adjacent elements if they are in the wrong order.",
                        "nums = list(map(int, input('Enter numbers: ').split()))\nn = len(nums)\nfor i in range(n):\n    for j in range(n - i - 1):\n        if nums[j] > nums[j + 1]:\n            nums[j], nums[j + 1] = nums[j + 1], nums[j]\nprint(nums)", 12)

def task_13():
    return execute_task("Count the frequency of elements in a list using a nested for loop.",
                        "Use a nested loop to count occurrences manually.",
                        "nums = list(map(int, input('Enter numbers: ').split()))\nfor i in nums:\n    count = 0\n    for j in nums:\n        if i == j:\n            count += 1\n    print(f'{i}: {count}')", 13)

tasks = [task_1, task_2, task_3, task_4, task_5, task_6, task_7, task_8, task_9, task_10, task_11, task_12, task_13]

def main():
    print("Welcome to Python Tutor - Advanced Questions on Nested `for` Loop")
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
