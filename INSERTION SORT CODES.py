import sys
import time
from io import StringIO

print("\n🚀 Welcome to Python Tutor - Insertion Sort Challenges for BTech Placements")

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

# 🏆 Insertion Sort Challenges
def task_1():
    return execute_task("Implement a standard Insertion Sort algorithm.",
                        "Insertion Sort works by taking one element at a time and inserting it in its correct position. It runs in O(n^2) time complexity.",
                        "def insertion_sort(arr):\n  for i in range(1, len(arr)):\n    key = arr[i]\n    j = i - 1\n    while j >= 0 and arr[j] > key:\n      arr[j + 1] = arr[j]\n      j -= 1\n    arr[j + 1] = key\n  return arr\nprint(insertion_sort([64, 25, 12, 22, 11]))", 1)

def task_2():
    return execute_task("Modify Insertion Sort to sort in descending order.",
                        "Instead of moving smaller elements to the left, move larger elements.",
                        "def insertion_sort_desc(arr):\n  for i in range(1, len(arr)):\n    key = arr[i]\n    j = i - 1\n    while j >= 0 and arr[j] < key:\n      arr[j + 1] = arr[j]\n      j -= 1\n    arr[j + 1] = key\n  return arr\nprint(insertion_sort_desc([12, 45, 23, 51, 19, 8]))", 2)

def task_3():
    return execute_task("Find the number of shifts in an Insertion Sort process.",
                        "Count how many times elements are shifted during sorting.",
                        "def insertion_sort_shifts(arr):\n  shifts = 0\n  for i in range(1, len(arr)):\n    key = arr[i]\n    j = i - 1\n    while j >= 0 and arr[j] > key:\n      arr[j + 1] = arr[j]\n      j -= 1\n      shifts += 1\n    arr[j + 1] = key\n  return shifts\nprint(insertion_sort_shifts([3, 2, 1, 5, 4]))", 3)

def task_4():
    return execute_task("Use Insertion Sort to sort a list of strings alphabetically.",
                        "Insertion Sort can be applied to strings by comparing them lexicographically.",
                        "def insertion_sort_strings(arr):\n  for i in range(1, len(arr)):\n    key = arr[i]\n    j = i - 1\n    while j >= 0 and arr[j] > key:\n      arr[j + 1] = arr[j]\n      j -= 1\n    arr[j + 1] = key\n  return arr\nprint(insertion_sort_strings(['banana', 'apple', 'cherry', 'date']))", 4)

def task_5():
    return execute_task("Sort a linked list using Insertion Sort.",
                        "Insertion Sort can be applied to linked lists by inserting nodes in sorted order.",
                        "class ListNode:\n  def __init__(self, val=0, next=None):\n    self.val = val\n    self.next = next\n\ndef insertion_sort_linked_list(head):\n  if not head or not head.next:\n    return head\n  sorted_head = ListNode(0)\n  curr = head\n  while curr:\n    prev, temp = sorted_head, sorted_head.next\n    while temp and temp.val < curr.val:\n      prev, temp = temp, temp.next\n    node = ListNode(curr.val)\n    prev.next, node.next = node, temp\n    curr = curr.next\n  return sorted_head.next\n\ndef print_list(head):\n  while head:\n    print(head.val, end=' -> ')\n    head = head.next\n  print('None')\n\n# Example usage:\nn1 = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))\nprint_list(insertion_sort_linked_list(n1))", 5)

tasks = [task_1, task_2, task_3, task_4, task_5]

def main():
    while True:
        task_num = input("\n🎯 Enter Insertion Sort problem number (or 'exit' to quit): ").strip()
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
