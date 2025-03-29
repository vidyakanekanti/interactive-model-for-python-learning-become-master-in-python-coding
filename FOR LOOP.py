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

# 13 NEW Questions on for loop
def task_1():
    return execute_task("Print numbers from 1 to 20 using a for loop.",
                        "Use a simple for loop with range().",
                        "for i in range(1, 21):\n    print(i, end=' ')", 1)

def task_2():
    return execute_task("Print all even numbers from 1 to N using a for loop.",
                        "Use range() with step 2 to get even numbers.",
                        "n = int(input('Enter N: '))\nfor i in range(2, n+1, 2):\n    print(i, end=' ')", 2)

def task_3():
    return execute_task("Print the sum of the first N natural numbers.",
                        "Use a for loop to accumulate the sum.",
                        "n = int(input('Enter N: '))\nsum_n = sum(range(1, n+1))\nprint(sum_n)", 3)

def task_4():
    return execute_task("Print the factorial of a given number using a for loop.",
                        "Multiply numbers sequentially in a for loop.",
                        "n = int(input('Enter N: '))\nfact = 1\nfor i in range(1, n+1):\n    fact *= i\nprint(fact)", 4)

def task_5():
    return execute_task("Print Fibonacci sequence up to N terms using a for loop.",
                        "Use a for loop to generate Fibonacci sequence.",
                        "n = int(input('Enter N: '))\na, b = 0, 1\nfor _ in range(n):\n    print(a, end=' ')\n    a, b = b, a + b", 5)

def task_6():
    return execute_task("Reverse a given string using a for loop.",
                        "Loop through the string in reverse order.",
                        "s = input('Enter a string: ')\nrev_s = ''\nfor char in s:\n    rev_s = char + rev_s\nprint(rev_s)", 6)

def task_7():
    return execute_task("Count the occurrences of a character in a string using a for loop.",
                        "Use a for loop to count occurrences.",
                        "s = input('Enter a string: ')\nchar = input('Enter character to count: ')\ncount = 0\nfor c in s:\n    if c == char:\n        count += 1\nprint(count)", 7)

def task_8():
    return execute_task("Print a multiplication table for a given number using a for loop.",
                        "Loop through numbers to generate multiplication results.",
                        "n = int(input('Enter a number: '))\nfor i in range(1, 11):\n    print(f'{n} x {i} = {n*i}')", 8)

def task_9():
    return execute_task("Check if a number is a palindrome using a for loop.",
                        "Reverse the number and compare it to the original.",
                        "n = input('Enter a number: ')\nif n == n[::-1]:\n    print('Palindrome')\nelse:\n    print('Not a Palindrome')", 9)

def task_10():
    return execute_task("Print all numbers from 1 to 100 that are divisible by both 3 and 5 using a for loop.",
                        "Use a for loop with conditions to check divisibility.",
                        "for i in range(1, 101):\n    if i % 3 == 0 and i % 5 == 0:\n        print(i, end=' ')", 10)

def task_11():
    return execute_task("Print a number triangle using a for loop.",
                        "Use a nested loop to print a number pattern.",
                        "n = int(input('Enter N: '))\nfor i in range(1, n+1):\n    print(' '.join(str(j) for j in range(1, i+1)))", 11)

def task_12():
    return execute_task("Find the largest number in a list using a for loop.",
                        "Iterate through the list to find the largest number.",
                        "nums = list(map(int, input('Enter numbers: ').split()))\nmax_num = nums[0]\nfor num in nums:\n    if num > max_num:\n        max_num = num\nprint(max_num)", 12)

def task_13():
    return execute_task("Find the sum of digits of a number using a for loop.",
                        "Extract digits using modulus and accumulate sum.",
                        "n = input('Enter a number: ')\nsum_digits = 0\nfor digit in n:\n    sum_digits += int(digit)\nprint(sum_digits)", 13)

tasks = [task_1, task_2, task_3, task_4, task_5, task_6, task_7, task_8, task_9, task_10, task_11, task_12, task_13]

def main():
    print("Welcome to Python Tutor - Advanced Questions on `for` Loop")
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
