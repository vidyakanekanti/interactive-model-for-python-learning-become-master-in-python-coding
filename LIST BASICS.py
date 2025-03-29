import sys
import time
from io import StringIO

print("Welcome to Python Tutor - List Programming Challenges for BTech Placements")

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
    """Executes a specific list problem and tracks user attempts."""
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

# 13 List-Based Programming Challenges
def task_1():
    return execute_task("Find the maximum element in a list.",
                        "Use a loop or the built-in `max()` function to determine the maximum value.",
                        "lst = [10, 20, 4, 45, 99]\nprint(max(lst))", 1)

def task_2():
    return execute_task("Find the second largest element in a list.",
                        "Sort the list and find the second largest element using indexing.",
                        "lst = [10, 20, 4, 45, 99]\nprint(sorted(set(lst))[-2])", 2)

def task_3():
    return execute_task("Reverse a list without using built-in functions.",
                        "Use a loop to swap elements or implement a recursive function.",
                        "lst = [1, 2, 3, 4, 5]\nprint(lst[::-1])", 3)

def task_4():
    return execute_task("Remove duplicates from a list while maintaining order.",
                        "Use a set to track seen values while iterating over the list.",
                        "lst = [1, 2, 2, 3, 4, 4, 5]\nseen = set()\nres = [x for x in lst if not (x in seen or seen.add(x))]\nprint(res)", 4)

def task_5():
    return execute_task("Merge two sorted lists into one sorted list.",
                        "Use a two-pointer technique or `heapq.merge()`.",
                        "lst1 = [1, 3, 5]\nlst2 = [2, 4, 6]\nprint(sorted(lst1 + lst2))", 5)

def task_6():
    return execute_task("Rotate a list by `k` positions to the right.",
                        "Use slicing to move elements efficiently.",
                        "lst = [1, 2, 3, 4, 5]\nk = 2\nprint(lst[-k:] + lst[:-k])", 6)

def task_7():
    return execute_task("Find all pairs in a list that sum up to a target value.",
                        "Use a dictionary to store complements while iterating.",
                        "lst = [1, 2, 3, 4, 5, 6]\ntarget = 7\npairs = [(x, y) for x in lst for y in lst if x + y == target]\nprint(pairs)", 7)

def task_8():
    return execute_task("Find the intersection of two lists.",
                        "Use set operations to find common elements.",
                        "lst1 = [1, 2, 3, 4]\nlst2 = [3, 4, 5, 6]\nprint(list(set(lst1) & set(lst2)))", 8)

def task_9():
    return execute_task("Find the union of two lists without duplicates.",
                        "Use set operations or `itertools.chain()`.",
                        "lst1 = [1, 2, 3]\nlst2 = [3, 4, 5]\nprint(list(set(lst1) | set(lst2)))", 9)

def task_10():
    return execute_task("Find the missing number in a list of consecutive numbers.",
                        "Use the sum formula `n(n+1)/2` to find the missing element.",
                        "lst = [1, 2, 3, 5]\nn = len(lst) + 1\nprint(n*(n+1)//2 - sum(lst))", 10)

def task_11():
    return execute_task("Check if a list is a palindrome.",
                        "Compare the list with its reverse.",
                        "lst = [1, 2, 3, 2, 1]\nprint(lst == lst[::-1])", 11)

def task_12():
    return execute_task("Flatten a nested list.",
                        "Use recursion or `itertools.chain()`.",
                        "lst = [[1, 2, [3]], [4, 5]]\ndef flatten(lst):\n  for x in lst:\n    if isinstance(x, list):\n      yield from flatten(x)\n    else:\n      yield x\nprint(list(flatten(lst)))", 12)

def task_13():
    return execute_task("Find the longest increasing subsequence in a list.",
                        "Use dynamic programming or binary search.",
                        "lst = [10, 22, 9, 33, 21, 50, 41, 60]\ndef LIS(arr):\n  from bisect import bisect_left\n  sub = []\n  for x in arr:\n    idx = bisect_left(sub, x)\n    if idx == len(sub):\n      sub.append(x)\n    else:\n      sub[idx] = x\n  return len(sub)\nprint(LIS(lst))", 13)

# Task list
tasks = [task_1, task_2, task_3, task_4, task_5, task_6, task_7, task_8, task_9, task_10, task_11, task_12, task_13]

def main():
    print("\n🚀 Welcome to Python Tutor - List Programming Challenges for BTech Placements")
    
    while True:
        task_num = input("\n🎯 Enter problem number (or 'exit' to quit): ").strip()
        
        if task_num.lower() == "exit":
            print("\n📊 Session Summary:")
            for key, attempts in task_attempts.items():
                print(f"Problem {key}: {attempts} attempts, Time: {task_times.get(key, 0)} sec")
            print("👋 Thank you for practicing with Python Tutor! 🚀")
            break

        if task_num.isdigit():
            task_num = int(task_num)
            if 1 <= task_num <= len(tasks):
                redo = True
                while redo:
                    redo = tasks[task_num - 1]()
            else:
                print(f"❌ Invalid problem number. Choose between 1 and {len(tasks)}.")
        else:
            print("❌ Invalid input. Enter a valid problem number.")

if __name__ == "__main__":
    main()
