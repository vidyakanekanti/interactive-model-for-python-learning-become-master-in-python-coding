import sys
import time
from io import StringIO

print("\n\U0001F680 Welcome to Python Tutor - Mastering map() Function Challenges!")

# Tracking attempts and time
task_attempts = {}
task_times = {}

def get_user_code(prompt, explanation, example_code):
    """Prompts user for input, explains the concept, and captures their code."""
    print("\n" + "=" * 50)
    print(f"\U0001F4A1 Task: {prompt}")
    print("-" * 50)
    print("\U0001F4D6 Explanation:")
    print(explanation)
    print("\U0001F4DD Example Code:")
    print(example_code)
    print("=" * 50)
    
    # User code input
    lines = []
    print("\n\U00002328 Enter your code (type 'done' to finish, 'exit' to quit):")
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
    
    return input("\n\U0001F504 Redo this task? (yes/no): ").strip().lower() == "yes"

# 🏆 map() Function Challenges
def task_1():
    return execute_task("Use map() to double each number in a list.",
                        "map() applies a function to each element in an iterable. Here, we double each number.",
                        "numbers = [1, 2, 3, 4]\ndoubled = list(map(lambda x: x * 2, numbers))\nprint(doubled)", 1)

def task_2():
    return execute_task("Use map() to convert a list of strings to integers.",
                        "map() can be used to convert data types efficiently.",
                        "strings = ['10', '20', '30']\nintegers = list(map(int, strings))\nprint(integers)", 2)

def task_3():
    return execute_task("Use map() to find the square of each element in a list.",
                        "The lambda function squares each element.",
                        "numbers = [2, 4, 6, 8]\nsquared = list(map(lambda x: x**2, numbers))\nprint(squared)", 3)

def task_4():
    return execute_task("Use map() to add 5 to each element in a list.",
                        "We use lambda to add a constant value to each element.",
                        "numbers = [10, 15, 20] \nnew_numbers = list(map(lambda x: x + 5, numbers))\nprint(new_numbers)", 4)

def task_5():
    return execute_task("Use map() with two lists to add corresponding elements.",
                        "map() can take multiple iterables.",
                        "a = [1, 2, 3]\nb = [4, 5, 6]\nsum_list = list(map(lambda x, y: x + y, a, b))\nprint(sum_list)", 5)

def task_6():
    return execute_task("Use map() to capitalize each word in a list.",
                        "We apply str.upper to each element.",
                        "words = ['hello', 'world']\ncapitalized = list(map(str.upper, words))\nprint(capitalized)", 6)

def task_7():
    return execute_task("Use map() to extract the length of each word in a list.",
                        "We use len() function within map().",
                        "words = ['apple', 'banana', 'cherry']\nlengths = list(map(len, words))\nprint(lengths)", 7)

def task_8():
    return execute_task("Use map() to check if numbers are even or odd.",
                        "We return 'Even' or 'Odd' based on condition.",
                        "numbers = [10, 15, 22, 33]\neven_odd = list(map(lambda x: 'Even' if x % 2 == 0 else 'Odd', numbers))\nprint(even_odd)", 8)

def task_9():
    return execute_task("Use map() to calculate the factorial of each number.",
                        "Using math.factorial to compute factorial.",
                        "import math\nnumbers = [3, 4, 5]\nfactorials = list(map(math.factorial, numbers))\nprint(factorials)", 9)

def task_10():
    return execute_task("Use map() to convert temperatures from Celsius to Fahrenheit.",
                        "Formula: F = (C * 9/5) + 32",
                        "celsius = [0, 100, 37]\nfahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))\nprint(fahrenheit)", 10)

def task_11():
    return execute_task("Use map() to replace vowels in words with '*'",
                        "Using a lambda function to replace vowels.",
                        "words = ['apple', 'banana']\nreplace_vowels = list(map(lambda w: ''.join('*' if c in 'aeiou' else c for c in w), words))\nprint(replace_vowels)", 11)

def task_12():
    return execute_task("Use map() to reverse each string in a list.",
                        "We apply slicing to reverse strings.",
                        "words = ['hello', 'world']\nreversed_words = list(map(lambda w: w[::-1], words))\nprint(reversed_words)", 12)

def task_13():
    return execute_task("Use map() to check if numbers are prime.",
                        "Using a helper function to check for prime numbers.",
                        "def is_prime(n): return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))\nnumbers = [2, 4, 7, 9]\nprimes = list(map(is_prime, numbers))\nprint(primes)", 13)

tasks = [task_1, task_2, task_3, task_4, task_5, task_6, task_7, task_8, task_9, task_10, task_11, task_12, task_13]
