import sys
import time
from io import StringIO

print("Welcome to Python Tutor - Advanced Questions on Nested `for` Loop Patterns")

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
    """Executes a specific task and tracks user attempts."""
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

# 13 Advanced Pattern Printing Tasks
def task_1():
    return execute_task("Print a diamond pattern using `*`.",
                        "Use nested loops to print spaces and `*` symmetrically.",
                        "n = int(input('Enter N: '))\nfor i in range(1, n+1, 2):\n    print(' ' * ((n-i)//2) + '*' * i)\nfor i in range(n-2, 0, -2):\n    print(' ' * ((n-i)//2) + '*' * i)", 1)

def task_2():
    return execute_task("Print an hourglass pattern using `*`.",
                        "Start with the largest row and decrease to the smallest.",
                        "n = int(input('Enter N: '))\nfor i in range(n, 0, -2):\n    print(' ' * ((n-i)//2) + '*' * i)\nfor i in range(3, n+1, 2):\n    print(' ' * ((n-i)//2) + '*' * i)", 2)

def task_3():
    return execute_task("Print a hollow square pattern with `*`.",
                        "Use conditions inside the nested loop to print borders only.",
                        "n = int(input('Enter N: '))\nfor i in range(n):\n    for j in range(n):\n        if i == 0 or i == n-1 or j == 0 or j == n-1:\n            print('*', end=' ')\n        else:\n            print(' ', end=' ')\n    print()", 3)

def task_4():
    return execute_task("Print a pyramid pattern with numbers.",
                        "Use a loop to center-align numbers in increasing order.",
                        "n = int(input('Enter N: '))\nfor i in range(1, n+1):\n    print(' ' * (n - i), end='')\n    for j in range(1, i+1):\n        print(j, end=' ')\n    print()", 4)

def task_5():
    return execute_task("Print Pascal’s Triangle using a for loop.",
                        "Use binomial coefficients and factorials for each row.",
                        "import math\nn = int(input('Enter N: '))\nfor i in range(n):\n    print(' ' * (n - i), end='')\n    for j in range(i+1):\n        print(math.comb(i, j), end=' ')\n    print()", 5)

def task_6():
    return execute_task("Print a checkerboard pattern of `#` and `.`.",
                        "Use conditional checks inside the nested loop.",
                        "n = int(input('Enter size: '))\nfor i in range(n):\n    for j in range(n):\n        if (i + j) % 2 == 0:\n            print('#', end=' ')\n        else:\n            print('.', end=' ')\n    print()", 6)

def task_7():
    return execute_task("Print a mirrored right-angled triangle with numbers.",
                        "Use loops and string formatting to align numbers.",
                        "n = int(input('Enter N: '))\nfor i in range(1, n+1):\n    print(' ' * (n - i), end='')\n    for j in range(i, 0, -1):\n        print(j, end=' ')\n    print()", 7)

def task_8():
    return execute_task("Print a butterfly pattern using `*`.",
                        "Divide the pattern into two mirrored sections.",
                        "n = int(input('Enter N: '))\nfor i in range(1, n+1):\n    print('*' * i + ' ' * (2 * (n - i)) + '*' * i)\nfor i in range(n-1, 0, -1):\n    print('*' * i + ' ' * (2 * (n - i)) + '*' * i)", 8)

def task_9():
    return execute_task("Print a hollow diamond pattern.",
                        "Use conditions inside the nested loop for borders.",
                        "n = int(input('Enter N: '))\nfor i in range(1, n+1, 2):\n    print(' ' * ((n-i)//2) + '*' + ' ' * (i-2) + ('*' if i>1 else ''))\nfor i in range(n-2, 0, -2):\n    print(' ' * ((n-i)//2) + '*' + ' ' * (i-2) + ('*' if i>1 else ''))", 9)

# Task list
tasks = [task_1, task_2, task_3, task_4, task_5, task_6, task_7, task_8, task_9]

def main():
    print("\n🚀 Welcome to Python Tutor - Advanced Questions on Nested `for` Loop")
    
    while True:
        task_num = input("\n🎯 Enter task number (or 'exit' to quit): ").strip()
        
        if task_num.lower() == "exit":
            print("\n📊 Session Summary:")
            for key, attempts in task_attempts.items():
                print(f"Task {key}: {attempts} attempts, Time: {task_times.get(key, 0)} sec")
            print("👋 Thank you for learning with Python Tutor! 🚀")
            break

        if task_num.isdigit():
            task_num = int(task_num)
            if 1 <= task_num <= len(tasks):
                redo = True
                while redo:
                    redo = tasks[task_num - 1]()
            else:
                print(f"❌ Invalid task number. Choose between 1 and {len(tasks)}.")
        else:
            print("❌ Invalid input. Enter a valid task number.")

if __name__ == "__main__":
    main()
