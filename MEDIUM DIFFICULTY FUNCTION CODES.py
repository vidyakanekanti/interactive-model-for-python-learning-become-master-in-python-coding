import sys
import time
from io import StringIO

print("Welcome to Python Tutor - Medium Difficulty Function Challenges")

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
    
    lines = []
    print("\n⌨️ Enter your code (type 'done' to finish, 'exit' to quit):")
    while True:
        line = input(">>> ").strip()
        if line.lower() in ["done", "exit"]:
            break
        lines.append(line)
    
    return "\n".join(lines)

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
    """Executes a specific function challenge and tracks user attempts."""
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

# 13 Medium-Difficulty Function Challenges
def task_1():
    return execute_task("Write a function to check if a number is prime.",
                        "A prime number is only divisible by 1 and itself.",
                        "def is_prime(n):\n    if n < 2: return False\n    for i in range(2, int(n**0.5) + 1):\n        if n % i == 0:\n            return False\n    return True\nprint(is_prime(11))", 1)

def task_2():
    return execute_task("Write a function to reverse a string.",
                        "Use slicing or loops to reverse a string.",
                        "def reverse_string(s):\n    return s[::-1]\nprint(reverse_string('hello'))", 2)

def task_3():
    return execute_task("Write a function to find the factorial of a number.",
                        "Factorial of n is n*(n-1)*(n-2)...*1.",
                        "def factorial(n):\n    return 1 if n == 0 else n * factorial(n-1)\nprint(factorial(5))", 3)

def task_4():
    return execute_task("Write a function to check if a string is a palindrome.",
                        "A palindrome reads the same forward and backward.",
                        "def is_palindrome(s):\n    return s == s[::-1]\nprint(is_palindrome('racecar'))", 4)

def task_5():
    return execute_task("Write a function to find the GCD of two numbers.",
                        "Use recursion or loops to compute GCD.",
                        "def gcd(a, b):\n    return a if b == 0 else gcd(b, a % b)\nprint(gcd(48, 18))", 5)

def task_6():
    return execute_task("Write a function to compute Fibonacci numbers.",
                        "Use recursion or loops to generate Fibonacci.",
                        "def fibonacci(n):\n    if n <= 1: return n\n    return fibonacci(n-1) + fibonacci(n-2)\nprint(fibonacci(6))", 6)

def task_7():
    return execute_task("Write a function to count vowels in a string.",
                        "Use a loop or list comprehension.",
                        "def count_vowels(s):\n    return sum(1 for c in s if c in 'aeiouAEIOU')\nprint(count_vowels('hello world'))", 7)

def task_8():
    return execute_task("Write a function to find the largest element in a list.",
                        "Use loops or Python's max function.",
                        "def largest(lst):\n    return max(lst)\nprint(largest([1, 5, 3, 9, 2]))", 8)

def task_9():
    return execute_task("Write a function to find the sum of digits of a number.",
                        "Convert to string or use mod/division.",
                        "def sum_digits(n):\n    return sum(int(d) for d in str(n))\nprint(sum_digits(1234))", 9)

def task_10():
    return execute_task("Write a function to check if a number is an Armstrong number.",
                        "An Armstrong number is equal to the sum of its digits raised to power of digits.",
                        "def is_armstrong(n):\n    return n == sum(int(d)**len(str(n)) for d in str(n))\nprint(is_armstrong(153))", 10)

def task_11():
    return execute_task("Write a function to count words in a string.",
                        "Use split() method.",
                        "def count_words(s):\n    return len(s.split())\nprint(count_words('hello world this is python'))", 11)

def task_12():
    return execute_task("Write a function to find the intersection of two lists.",
                        "Use list comprehension or set operations.",
                        "def intersection(lst1, lst2):\n    return list(set(lst1) & set(lst2))\nprint(intersection([1,2,3],[2,3,4]))", 12)

def task_13():
    return execute_task("Write a function to convert Celsius to Fahrenheit.",
                        "Use the formula (C * 9/5) + 32.",
                        "def celsius_to_fahrenheit(c):\n    return (c * 9/5) + 32\nprint(celsius_to_fahrenheit(0))", 13)

# Task list
tasks = [task_1, task_2, task_3, task_4, task_5, task_6, task_7, task_8, task_9, task_10, task_11, task_12, task_13]

def main():
    print("\n🚀 Welcome to Python Tutor - Medium Difficulty Function Challenges")
    while True:
        task_num = input("\n🎯 Enter problem number (or 'exit' to quit): ").strip()
        if task_num.lower() == "exit":
            break
        if task_num.isdigit() and 1 <= int(task_num) <= len(tasks):
            tasks[int(task_num) - 1]()
if __name__ == "__main__":
    main()
