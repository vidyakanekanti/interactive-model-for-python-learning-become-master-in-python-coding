import sys
import time
from io import StringIO

print("Welcome to Python Tutor - High-Quality List Challenges for High CTC Placements")

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

# 13 High-Quality List Programming Challenges
def task_1():
    return execute_task("Find the second largest element in a list.",
                        "Sort the list and return the second largest distinct number.",
                        "lst = [10, 20, 4, 45, 99, 99]\nlst = list(set(lst))\nlst.sort()\nprint(lst[-2])", 1)

def task_2():
    return execute_task("Find the missing number in a given list of consecutive numbers.",
                        "Use sum formula or XOR approach to find the missing number.",
                        "lst = [1, 2, 3, 5]\nn = len(lst) + 1\nprint(n*(n+1)//2 - sum(lst))", 2)

def task_3():
    return execute_task("Move all zeros to the end of the list without changing order.",
                        "Use two-pointer technique to move zeros efficiently.",
                        "lst = [0, 1, 0, 3, 12]\nlst.sort(key=lambda x: x == 0)\nprint(lst)", 3)

def task_4():
    return execute_task("Find the intersection of two lists without using set operations.",
                        "Use loops or dictionaries to track occurrences.",
                        "lst1 = [1, 2, 3, 4, 5]\nlst2 = [4, 5, 6, 7]\nprint([x for x in lst1 if x in lst2])", 4)

def task_5():
    return execute_task("Rotate a list to the right by K places.",
                        "Use slicing to rotate the list.",
                        "lst = [1, 2, 3, 4, 5]\nk = 2\nprint(lst[-k:] + lst[:-k])", 5)

def task_6():
    return execute_task("Find the longest consecutive sequence of numbers in a list.",
                        "Sort and iterate through the list while tracking streaks.",
                        "lst = [100, 4, 200, 1, 3, 2]\nlst = set(lst)\nlongest = 0\nfor n in lst:\n  if n-1 not in lst:\n    count = 1\n    while n+count in lst:\n      count += 1\n    longest = max(longest, count)\nprint(longest)", 6)

def task_7():
    return execute_task("Find pairs in a list whose sum equals a given target.",
                        "Use a set or dictionary to track complements.",
                        "lst = [1, 2, 3, 4, 5]\ntarget = 6\npairs = [(x, target-x) for x in lst if (target-x) in lst and x < target-x]\nprint(pairs)", 7)

def task_8():
    return execute_task("Find the majority element in a list (appears more than n/2 times).",
                        "Use a dictionary to count occurrences and find the element.",
                        "from collections import Counter\nlst = [3, 3, 4, 2, 4, 4, 2, 4, 4]\ncounts = Counter(lst)\nprint(max(counts, key=counts.get))", 8)

def task_9():
    return execute_task("Check if a list contains a cycle (linked-list style problem).",
                        "Use Floyd's cycle detection algorithm (Tortoise and Hare method).",
                        "def has_cycle(lst):\n  slow = fast = 0\n  while fast < len(lst)-1 and fast+1 < len(lst)-1:\n    slow += 1\n    fast += 2\n    if lst[slow] == lst[fast]:\n      return True\n  return False\nprint(has_cycle([1, 2, 3, 4, 2]))", 9)

def task_10():
    return execute_task("Find the first non-repeating element in a list.",
                        "Use a dictionary to count occurrences and find the first unique element.",
                        "from collections import Counter\nlst = [1, 2, 3, 1, 2, 4]\ncounts = Counter(lst)\nprint(next(x for x in lst if counts[x] == 1))", 10)

def task_11():
    return execute_task("Implement a custom `map()` function to apply a function to a list.",
                        "Use list comprehension or the `map()` function.",
                        "def square(x): return x*x\nlst = [1, 2, 3, 4]\nprint(list(map(square, lst)))", 11)

def task_12():
    return execute_task("Merge overlapping intervals in a list of pairs.",
                        "Sort intervals and merge overlapping ones.",
                        "intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]\nintervals.sort()\nmerged = [intervals[0]]\nfor start, end in intervals[1:]:\n  if start <= merged[-1][1]:\n    merged[-1][1] = max(end, merged[-1][1])\n  else:\n    merged.append([start, end])\nprint(merged)", 12)

def task_13():
    return execute_task("Find the kth smallest element in a list.",
                        "Use sorting or a heap-based approach for efficiency.",
                        "import heapq\nlst = [7, 10, 4, 3, 20, 15]\nk = 3\nprint(heapq.nsmallest(k, lst)[-1])", 13)

# Task list
tasks = [task_1, task_2, task_3, task_4, task_5, task_6, task_7, task_8, task_9, task_10, task_11, task_12, task_13]

if __name__ == "__main__":
    main()
