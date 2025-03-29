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

# Chapter: Famous Placement Questions - while Loop
def task_1():
    return execute_task("Print numbers from 1 to N using a while loop.",
                        "Use a while loop to incrementally print numbers from 1 to N.",
                        "n = int(input('Enter N: '))\ni = 1\nwhile i <= n:\n    print(i)\n    i += 1", 1)

def task_2():
    return execute_task("Print even numbers up to N using a while loop.",
                        "Use a while loop to print only even numbers.",
                        "n = int(input('Enter N: '))\ni = 2\nwhile i <= n:\n    print(i)\n    i += 2", 2)

def task_3():
    return execute_task("Find the sum of digits of a number using a while loop.",
                        "Extract each digit using modulus and add it to a sum variable.",
                        "num = int(input('Enter a number: '))\nsum_digits = 0\nwhile num > 0:\n    sum_digits += num % 10\n    num //= 10\nprint(sum_digits)", 3)

def task_4():
    return execute_task("Reverse a given number using a while loop.",
                        "Extract digits one by one and construct the reversed number.",
                        "num = int(input('Enter a number: '))\nrev_num = 0\nwhile num > 0:\n    rev_num = rev_num * 10 + num % 10\n    num //= 10\nprint(rev_num)", 4)

def task_5():
    return execute_task("Find whether a number is prime using a while loop.",
                        "Check divisibility from 2 up to sqrt(n) using a while loop.",
                        "num = int(input('Enter a number: '))\ni = 2\nis_prime = True\nwhile i * i <= num:\n    if num % i == 0:\n        is_prime = False\n        break\n    i += 1\nprint('Prime' if is_prime and num > 1 else 'Not Prime')", 5)

def task_6():
    return execute_task("Find the factorial of a number using a while loop.",
                        "Multiply numbers in descending order from n to 1.",
                        "num = int(input('Enter a number: '))\nfact = 1\nwhile num > 1:\n    fact *= num\n    num -= 1\nprint(fact)", 6)

def task_7():
    return execute_task("Check if a number is a palindrome using a while loop.",
                        "Reverse the number and compare it to the original.",
                        "num = int(input('Enter a number: '))\ntemp, rev = num, 0\nwhile temp > 0:\n    rev = rev * 10 + temp % 10\n    temp //= 10\nprint('Palindrome' if num == rev else 'Not Palindrome')", 7)

def task_8():
    return execute_task("Find the sum of first N natural numbers using a while loop.",
                        "Keep adding numbers from 1 to N using a while loop.",
                        "n = int(input('Enter N: '))\nsum_n = 0\ni = 1\nwhile i <= n:\n    sum_n += i\n    i += 1\nprint(sum_n)", 8)

def task_9():
    return execute_task("Print Fibonacci series up to N terms using a while loop.",
                        "Use a while loop to calculate Fibonacci numbers iteratively.",
                        "n = int(input('Enter N: '))\na, b = 0, 1\ni = 0\nwhile i < n:\n    print(a, end=' ')\n    a, b = b, a + b\n    i += 1", 9)

def task_10():
    return execute_task("Find the GCD of two numbers using the Euclidean method with a while loop.",
                        "Use repeated division to find the GCD.",
                        "a, b = map(int, input('Enter two numbers: ').split())\nwhile b:\n    a, b = b, a % b\nprint(a)", 10)

def task_11():
    return execute_task("Count the number of digits in a given number using a while loop.",
                        "Use a while loop to count digits by continuously dividing by 10.",
                        "num = int(input('Enter a number: '))\ncount = 0\nwhile num > 0:\n    count += 1\n    num //= 10\nprint(count)", 11)

def task_12():
    return execute_task("Find the sum of all even numbers between 1 and N using a while loop.",
                        "Incrementally add even numbers while iterating.",
                        "n = int(input('Enter N: '))\ni, sum_even = 2, 0\nwhile i <= n:\n    sum_even += i\n    i += 2\nprint(sum_even)", 12)

def task_13():
    return execute_task("Check if a number is an Armstrong number using a while loop.",
                        "Calculate the sum of digits raised to the power of the number of digits.",
                        "num = int(input('Enter a number: '))\ntemp, order = num, len(str(num))\nsum_digits = 0\nwhile temp > 0:\n    sum_digits += (temp % 10) ** order\n    temp //= 10\nprint('Armstrong' if sum_digits == num else 'Not Armstrong')", 13)

tasks = [task_1, task_2, task_3, task_4, task_5, task_6, task_7, task_8, task_9, task_10, task_11, task_12, task_13]

def main():
    print("Welcome to Python Tutor - Famous Placement Questions on `while` Loop")
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
