import sys
import time
from io import StringIO

print("\n🚀 Welcome to Python Tutor - Bubble Sort Challenges for BTech Placements")

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

# 🏆 Bubble Sort Challenges
def task_1():
    return execute_task("Implement a standard Bubble Sort algorithm.",
                        "Bubble Sort compares adjacent elements and swaps them if they are in the wrong order. The largest element bubbles to the end in each pass.",
                        "def bubble_sort(arr):\n  n = len(arr)\n  for i in range(n):\n    for j in range(n-i-1):\n      if arr[j] > arr[j+1]:\n        arr[j], arr[j+1] = arr[j+1], arr[j]\n  return arr\nprint(bubble_sort([64, 34, 25, 12, 22, 11, 90]))", 1)

def task_2():
    return execute_task("Modify Bubble Sort to stop if the array is already sorted.",
                        "This optimization adds a 'swapped' flag. If no swaps occur in a pass, the sorting stops early.",
                        "def optimized_bubble_sort(arr):\n  n = len(arr)\n  for i in range(n):\n    swapped = False\n    for j in range(n-i-1):\n      if arr[j] > arr[j+1]:\n        arr[j], arr[j+1] = arr[j+1], arr[j]\n        swapped = True\n    if not swapped:\n      break\n  return arr\nprint(optimized_bubble_sort([1, 2, 3, 4, 5, 6]))", 2)

def task_3():
    return execute_task("Implement Bubble Sort in descending order.",
                        "Modify the comparison condition to sort elements in descending order.",
                        "def bubble_sort_desc(arr):\n  n = len(arr)\n  for i in range(n):\n    for j in range(n-i-1):\n      if arr[j] < arr[j+1]:\n        arr[j], arr[j+1] = arr[j+1], arr[j]\n  return arr\nprint(bubble_sort_desc([12, 45, 23, 51, 19, 8]))", 3)

def task_4():
    return execute_task("Count the number of swaps in Bubble Sort.",
                        "Modify the Bubble Sort algorithm to count and return the total number of swaps performed.",
                        "def bubble_sort_count_swaps(arr):\n  n = len(arr)\n  swap_count = 0\n  for i in range(n):\n    for j in range(n-i-1):\n      if arr[j] > arr[j+1]:\n        arr[j], arr[j+1] = arr[j+1], arr[j]\n        swap_count += 1\n  return arr, swap_count\nprint(bubble_sort_count_swaps([3, 2, 1, 5, 4]))", 4)

def task_5():
    return execute_task("Use Bubble Sort to sort a list of strings alphabetically.",
                        "Bubble Sort can be applied to strings by comparing them lexicographically.",
                        "def bubble_sort_strings(arr):\n  n = len(arr)\n  for i in range(n):\n    for j in range(n-i-1):\n      if arr[j] > arr[j+1]:\n        arr[j], arr[j+1] = arr[j+1], arr[j]\n  return arr\nprint(bubble_sort_strings(['banana', 'apple', 'cherry', 'date']))", 5)

tasks = [task_1, task_2, task_3, task_4, task_5]

def main():
    while True:
        task_num = input("\n🎯 Enter Bubble Sort problem number (or 'exit' to quit): ").strip()
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
