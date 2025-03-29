import sys
import time
from io import StringIO

print("Welcome to Python Tutor - List Functions Challenges for BTech Placements")

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
    """Executes a specific list function problem and tracks user attempts."""
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

# 13 List Function-Based Programming Challenges
def task_1():
    return execute_task("Use `.append()` to add elements to a list.",
                        "The `.append()` method adds an element to the end of the list.",
                        "lst = [1, 2, 3]\nlst.append(4)\nprint(lst)", 1)

def task_2():
    return execute_task("Use `.extend()` to merge two lists.",
                        "The `.extend()` method adds elements from another iterable.",
                        "lst1 = [1, 2, 3]\nlst2 = [4, 5, 6]\nlst1.extend(lst2)\nprint(lst1)", 2)

def task_3():
    return execute_task("Use `.insert()` to add an element at a specific index.",
                        "The `.insert(index, element)` method adds an element at a given position.",
                        "lst = [1, 2, 4]\nlst.insert(2, 3)\nprint(lst)", 3)

def task_4():
    return execute_task("Use `.remove()` to delete a specific element from a list.",
                        "The `.remove(value)` method deletes the first occurrence of the value.",
                        "lst = [1, 2, 3, 2]\nlst.remove(2)\nprint(lst)", 4)

def task_5():
    return execute_task("Use `.pop()` to remove an element by index.",
                        "The `.pop(index)` method removes an element at the given index.",
                        "lst = [1, 2, 3, 4]\nlst.pop(2)\nprint(lst)", 5)

def task_6():
    return execute_task("Use `.index()` to find the first occurrence of an element.",
                        "The `.index(value)` method returns the index of the first match.",
                        "lst = [10, 20, 30, 20]\nprint(lst.index(20))", 6)

def task_7():
    return execute_task("Use `.count()` to find the frequency of an element.",
                        "The `.count(value)` method returns the number of times an element appears.",
                        "lst = [1, 2, 2, 3, 4, 2]\nprint(lst.count(2))", 7)

def task_8():
    return execute_task("Use `.sort()` to sort a list in ascending order.",
                        "The `.sort()` method sorts the list in place.",
                        "lst = [3, 1, 4, 1, 5, 9]\nlst.sort()\nprint(lst)", 8)

def task_9():
    return execute_task("Use `.reverse()` to reverse a list.",
                        "The `.reverse()` method modifies the list in place.",
                        "lst = [1, 2, 3, 4]\nlst.reverse()\nprint(lst)", 9)

def task_10():
    return execute_task("Use `.copy()` to create a shallow copy of a list.",
                        "The `.copy()` method returns a new list with the same elements.",
                        "lst = [1, 2, 3]\ncopied_lst = lst.copy()\nprint(copied_lst)", 10)

def task_11():
    return execute_task("Use `.clear()` to empty a list.",
                        "The `.clear()` method removes all elements from the list.",
                        "lst = [1, 2, 3]\nlst.clear()\nprint(lst)", 11)

def task_12():
    return execute_task("Use `del` to remove elements by index or delete the entire list.",
                        "The `del` keyword deletes elements at an index or removes the whole list.",
                        "lst = [1, 2, 3, 4]\ndel lst[2]\nprint(lst)", 12)

def task_13():
    return execute_task("Use `sorted()` to return a new sorted list without modifying the original.",
                        "The `sorted(iterable)` function returns a new sorted list.",
                        "lst = [4, 2, 9, 1]\nprint(sorted(lst))\nprint(lst)", 13)

# Task list
tasks = [task_1, task_2, task_3, task_4, task_5, task_6, task_7, task_8, task_9, task_10, task_11, task_12, task_13]

def main():
    print("\n🚀 Welcome to Python Tutor - List Functions Challenges for BTech Placements")
    
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
