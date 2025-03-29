import sys
import time
from io import StringIO

print("\n🚀 Welcome to Python Tutor - map() with Integer Input Challenges")

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

# 🏆 map() with Integer Input Challenges
def task_1():
    return execute_task("Use map() to read space-separated integers and store them in a list.",
                        "map() is useful to convert multiple inputs into integers.",
                        "numbers = list(map(int, input().split()))\nprint(numbers)", 1)

def task_2():
    return execute_task("Use map() to read three integers and find their sum.",
                        "You can unpack map() results directly.",
                        "a, b, c = map(int, input().split())\nprint(a + b + c)", 2)

def task_3():
    return execute_task("Read N integers and find their average using map().",
                        "Use sum() and len() functions.",
                        "numbers = list(map(int, input().split()))\nprint(sum(numbers) / len(numbers))", 3)

def task_4():
    return execute_task("Convert space-separated integers into a list of squares using map().",
                        "Apply a lambda function inside map().",
                        "numbers = list(map(lambda x: x**2, map(int, input().split())))\nprint(numbers)", 4)

def task_5():
    return execute_task("Use map() to multiply all input numbers by 2.",
                        "You can chain map() with a lambda function.",
                        "numbers = list(map(lambda x: x * 2, map(int, input().split())))\nprint(numbers)", 5)

def task_6():
    return execute_task("Filter even numbers using map() and list comprehension.",
                        "Use modulo operation inside list comprehension.",
                        "numbers = list(map(int, input().split()))\nevens = [x for x in numbers if x % 2 == 0]\nprint(evens)", 6)

def task_7():
    return execute_task("Convert integer inputs to their absolute values.",
                        "Use abs() function inside map().",
                        "numbers = list(map(abs, map(int, input().split())))\nprint(numbers)", 7)

def task_8():
    return execute_task("Find the maximum of three numbers using map().",
                        "Use max() function with unpacked inputs.",
                        "a, b, c = map(int, input().split())\nprint(max(a, b, c))", 8)

def task_9():
    return execute_task("Read a list of numbers and compute their product.",
                        "Use reduce() from functools.",
                        "from functools import reduce\nnumbers = list(map(int, input().split()))\nprint(reduce(lambda x, y: x * y, numbers))", 9)

def task_10():
    return execute_task("Find all odd numbers from input using map() and filter().",
                        "Use filter() alongside map().",
                        "numbers = list(map(int, input().split()))\nodds = list(filter(lambda x: x % 2 != 0, numbers))\nprint(odds)", 10)

def task_11():
    return execute_task("Use map() to compute factorials of a list of numbers.",
                        "Use the math module for factorial calculations.",
                        "import math\nnumbers = list(map(int, input().split()))\nfactorials = list(map(math.factorial, numbers))\nprint(factorials)", 11)

def task_12():
    return execute_task("Convert temperatures from Celsius to Fahrenheit using map().",
                        "Use the conversion formula: F = C * 9/5 + 32.",
                        "celsius = list(map(int, input().split()))\nfahrenheit = list(map(lambda x: x * 9/5 + 32, celsius))\nprint(fahrenheit)", 12)

def task_13():
    return execute_task("Convert binary string inputs into decimal numbers using map().",
                        "Use int() with base 2.",
                        "binaries = input().split()\ndecimals = list(map(lambda x: int(x, 2), binaries))\nprint(decimals)", 13)

tasks = [task_1, task_2, task_3, task_4, task_5, task_6, task_7, task_8, task_9, task_10, task_11, task_12, task_13]

def main():
    while True:
        task_num = input("\n🎯 Enter problem number (or 'exit' to quit): ").strip()
        if task_num.lower() == "exit":
            print("\n📊 Session Summary:")
            for key, attempts in task_attempts.items():
                print(f"Problem {key}: {attempts} attempts, Time: {task_times.get(key, 0)} sec")
            print("👋 Thank you for practicing with Python Tutor! 🚀")
            break
        if task_num.isdigit() and 1 <= int(task_num) <= len(tasks):
            redo = True
            while redo:
                redo = tasks[int(task_num) - 1]()
        else:
            print(f"❌ Invalid problem number. Choose between 1 and {len(tasks)}.")

if __name__ == "__main__":
    main()
