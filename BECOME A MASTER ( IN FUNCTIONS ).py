Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import sys
import time
from io import StringIO

print("\n🚀 Welcome to Python Tutor - Hard Functions Challenges for BTech Placements")

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
    """Executes a function problem and tracks user attempts."""
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

# 13 Advanced Function Programming Challenges
def task_1():
    return execute_task("Implement a function to check if a number is prime.",
                        "A prime number is only divisible by 1 and itself. Iterate from 2 to sqrt(n) to check divisibility efficiently.",
                        "def is_prime(n):\n  if n < 2:\n    return False\n  for i in range(2, int(n**0.5) + 1):\n    if n % i == 0:\n      return False\n  return True\nprint(is_prime(29))", 1)

def task_2():
    return execute_task("Write a function to generate the nth Fibonacci number using recursion.",
                        "The Fibonacci sequence is defined as F(n) = F(n-1) + F(n-2). Use recursion with a base case for 0 and 1.",
                        "def fibonacci(n):\n  if n <= 1:\n    return n\n  return fibonacci(n-1) + fibonacci(n-2)\nprint(fibonacci(10))", 2)

def task_3():
    return execute_task("Implement a function to reverse a string using recursion.",
                        "Base case: an empty string or a single character remains unchanged. Otherwise, reverse recursively.",
                        "def reverse_string(s):\n  if len(s) <= 1:\n    return s\n  return s[-1] + reverse_string(s[:-1])\nprint(reverse_string('hello'))", 3)

def task_4():
    return execute_task("Write a function to find all permutations of a string.",
                        "Use recursion to swap characters at each position and generate different arrangements.",
                        "from itertools import permutations\nprint([''.join(p) for p in permutations('ABC')])", 4)

def task_5():
    return execute_task("Implement a function to check if a given string is a palindrome.",
                        "A palindrome reads the same forward and backward. Compare characters from both ends.",
                        "def is_palindrome(s):\n  return s == s[::-1]\nprint(is_palindrome('racecar'))", 5)

def task_6():
    return execute_task("Write a function to compute factorial of a number using recursion.",
                        "Base case: factorial(1) = 1. Recursive case: factorial(n) = n * factorial(n-1).",
                        "def factorial(n):\n  return 1 if n == 1 else n * factorial(n-1)\nprint(factorial(5))", 6)

def task_7():
    return execute_task("Find the greatest common divisor (GCD) of two numbers using recursion.",
                        "Use the Euclidean algorithm: GCD(a, b) = GCD(b, a % b) until b is 0.",
                        "def gcd(a, b):\n  return a if b == 0 else gcd(b, a % b)\nprint(gcd(48, 18))", 7)

def task_8():
    return execute_task("Implement a function to find the longest common prefix among a list of strings.",
                        "Iterate through characters of each word, stopping at the first mismatch.",
                        "def longest_common_prefix(words):\n  prefix = ''\n  for i in zip(*words):\n    if len(set(i)) == 1:\n      prefix += i[0]\n    else:\n      break\n  return prefix\nprint(longest_common_prefix(['flower', 'flow', 'flight']))", 8)

def task_9():
    return execute_task("Implement a function to compute exponentiation (x^y) using recursion.",
                        "Base case: x^0 = 1. Recursive case: x^y = x * x^(y-1).",
                        "def power(x, y):\n  return 1 if y == 0 else x * power(x, y-1)\nprint(power(2, 10))", 9)

def task_10():
    return execute_task("Implement a function to solve the Tower of Hanoi problem.",
                        "Recursively move disks between rods using an auxiliary rod.",
...                         "def tower_of_hanoi(n, source, auxiliary, target):\n  if n > 0:\n    tower_of_hanoi(n-1, source, target, auxiliary)\n    print(f'Move disk {n} from {source} to {target}')\n    tower_of_hanoi(n-1, auxiliary, source, target)\ntower_of_hanoi(3, 'A', 'B', 'C')", 10)
... 
... def task_11():
...     return execute_task("Implement a function to find all subsets of a given set.",
...                         "Use recursion to include/exclude each element in subsets.",
...                         "def subsets(nums):\n  if not nums:\n    return [[]]\n  first, rest = nums[0], subsets(nums[1:])\n  return rest + [[first] + sub for sub in rest]\nprint(subsets([1, 2, 3]))", 11)
... 
... def task_12():
...     return execute_task("Implement a function to compute Pascal’s Triangle up to n rows.",
...                         "Each row is computed using combinations: row[i] = row[i-1] * (n-i+1) // i.",
...                         "def pascal_triangle(n):\n  row = [1]\n  for _ in range(n):\n    print(row)\n    row = [1] + [row[i] + row[i+1] for i in range(len(row)-1)] + [1]\npascal_triangle(5)", 12)
... 
... def task_13():
...     return execute_task("Write a function to generate all valid parentheses combinations of n pairs.",
...                         "Use backtracking to ensure correct placement of parentheses.",
...                         "def generate_parentheses(n, s='', left=0, right=0):\n  if len(s) == 2 * n:\n    print(s)\n  if left < n:\n    generate_parentheses(n, s+'(', left+1, right)\n  if right < left:\n    generate_parentheses(n, s+')', left, right+1)\ngenerate_parentheses(3)", 13)
... 
... tasks = [task_1, task_2, task_3, task_4, task_5, task_6, task_7, task_8, task_9, task_10, task_11, task_12, task_13]
... 
... if __name__ == "__main__":
...     main()
