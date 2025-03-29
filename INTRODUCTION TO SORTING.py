import sys
import time
from io import StringIO

print("\n🚀 Welcome to Python Tutor - Sorting Algorithm Challenges for BTech Placements")

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

# 10 Important Sorting Algorithm Challenges
def task_1():
    return execute_task("Implement Bubble Sort.",
                        "Bubble Sort compares adjacent elements and swaps them if they are in the wrong order. The largest element bubbles to the end in each pass.",
                        "def bubble_sort(arr):\n  n = len(arr)\n  for i in range(n):\n    for j in range(n-i-1):\n      if arr[j] > arr[j+1]:\n        arr[j], arr[j+1] = arr[j+1], arr[j]\n  return arr\nprint(bubble_sort([64, 34, 25, 12, 22, 11, 90]))", 1)

def task_2():
    return execute_task("Implement Selection Sort.",
                        "Selection Sort repeatedly selects the smallest element and swaps it to its correct position.",
                        "def selection_sort(arr):\n  for i in range(len(arr)):\n    min_idx = i\n    for j in range(i+1, len(arr)):\n      if arr[j] < arr[min_idx]:\n        min_idx = j\n    arr[i], arr[min_idx] = arr[min_idx], arr[i]\n  return arr\nprint(selection_sort([64, 25, 12, 22, 11]))", 2)

def task_3():
    return execute_task("Implement Insertion Sort.",
                        "Insertion Sort builds the sorted array one item at a time, shifting elements to insert new elements in the correct position.",
                        "def insertion_sort(arr):\n  for i in range(1, len(arr)):\n    key = arr[i]\n    j = i-1\n    while j >= 0 and key < arr[j]:\n      arr[j + 1] = arr[j]\n      j -= 1\n    arr[j + 1] = key\n  return arr\nprint(insertion_sort([12, 11, 13, 5, 6]))", 3)

def task_4():
    return execute_task("Implement Merge Sort.",
                        "Merge Sort divides the array into halves, sorts them recursively, and merges them back in sorted order.",
                        "def merge_sort(arr):\n  if len(arr) > 1:\n    mid = len(arr) // 2\n    L, R = arr[:mid], arr[mid:]\n    merge_sort(L)\n    merge_sort(R)\n    i = j = k = 0\n    while i < len(L) and j < len(R):\n      if L[i] < R[j]:\n        arr[k] = L[i]\n        i += 1\n      else:\n        arr[k] = R[j]\n        j += 1\n      k += 1\n    while i < len(L):\n      arr[k] = L[i]\n      i += 1\n      k += 1\n    while j < len(R):\n      arr[k] = R[j]\n      j += 1\n      k += 1\n  return arr\nprint(merge_sort([38, 27, 43, 3, 9, 82, 10]))", 4)

def task_5():
    return execute_task("Implement Quick Sort.",
                        "Quick Sort selects a pivot, partitions elements, and sorts them recursively.",
                        "def quick_sort(arr):\n  if len(arr) <= 1:\n    return arr\n  pivot = arr[len(arr) // 2]\n  left = [x for x in arr if x < pivot]\n  middle = [x for x in arr if x == pivot]\n  right = [x for x in arr if x > pivot]\n  return quick_sort(left) + middle + quick_sort(right)\nprint(quick_sort([10, 7, 8, 9, 1, 5]))", 5)

def task_6():
    return execute_task("Implement Heap Sort.",
                        "Heap Sort first builds a heap and then extracts elements in sorted order.",
                        "import heapq\ndef heap_sort(arr):\n  heapq.heapify(arr)\n  return [heapq.heappop(arr) for _ in range(len(arr))]\nprint(heap_sort([3, 2, 1, 5, 4, 8, 7]))", 6)

def task_7():
    return execute_task("Implement Counting Sort.",
                        "Counting Sort works for small positive integers by counting occurrences and placing elements in sorted order.",
                        "def counting_sort(arr):\n  max_val = max(arr)\n  count = [0] * (max_val + 1)\n  for num in arr:\n    count[num] += 1\n  sorted_arr = []\n  for i, val in enumerate(count):\n    sorted_arr.extend([i] * val)\n  return sorted_arr\nprint(counting_sort([4, 2, 2, 8, 3, 3, 1]))", 7)

tasks = [task_1, task_2, task_3, task_4, task_5, task_6, task_7]

def main():
    while True:
        task_num = input("\n🎯 Enter sorting problem number (or 'exit' to quit): ").strip()
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
