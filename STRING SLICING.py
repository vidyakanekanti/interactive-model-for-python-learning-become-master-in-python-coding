import sys
import time
from io import StringIO

print("Welcome to Python Tutor - String Slicing Challenges")

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
    """Executes a specific string slicing task and tracks user attempts."""
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

# 13 String Slicing Challenges
def task_1():
    return execute_task("Extract the first 5 characters of a string.",
                        "Use slicing syntax: `string[:5]` to get the first 5 characters.",
                        "s = 'HelloWorld'\nprint(s[:5])", 1)

def task_2():
    return execute_task("Extract the last 4 characters of a string.",
                        "Use negative indexing: `string[-4:]` to get last 4 characters.",
                        "s = 'PythonProgramming'\nprint(s[-4:])", 2)

def task_3():
    return execute_task("Extract every second character from a string.",
                        "Use step in slicing: `string[::2]` to skip alternate characters.",
                        "s = 'abcdefgh'\nprint(s[::2])", 3)

def task_4():
    return execute_task("Reverse a string using slicing.",
                        "Use `[::-1]` to reverse a string.",
                        "s = 'Python'\nprint(s[::-1])", 4)

def task_5():
    return execute_task("Extract a substring from index 3 to 8.",
                        "Use `string[3:9]` to extract characters from index 3 to 8.",
                        "s = 'Programming'\nprint(s[3:9])", 5)

def task_6():
    return execute_task("Extract all characters except the first and last.",
                        "Use `string[1:-1]` to exclude the first and last characters.",
                        "s = 'Python'\nprint(s[1:-1])", 6)

def task_7():
    return execute_task("Extract only the vowels from a string.",
                        "Use slicing along with a loop or comprehension.",
                        "s = 'education'\nvowels = ''.join([ch for ch in s if ch in 'aeiouAEIOU'])\nprint(vowels)", 7)

def task_8():
    return execute_task("Extract characters from index 2 to 10 with a step of 2.",
                        "Use `string[2:11:2]` to get characters skipping every second one.",
                        "s = 'abcdefghijkl'\nprint(s[2:11:2])", 8)

def task_9():
    return execute_task("Extract all characters except the last three.",
                        "Use `string[:-3]` to remove the last three characters.",
                        "s = 'Programming'\nprint(s[:-3])", 9)

def task_10():
    return execute_task("Extract the middle three characters of a string with an odd length.",
                        "Find the middle index and extract three characters.",
                        "s = 'abcdefg'\nmid = len(s) // 2\nprint(s[mid-1:mid+2])", 10)

def task_11():
    return execute_task("Extract all uppercase letters from a string.",
                        "Use list comprehension with condition checking for `isupper()`.",
                        "s = 'HelloWORLD123'\nuppercase = ''.join([ch for ch in s if ch.isupper()])\nprint(uppercase)", 11)

def task_12():
    return execute_task("Extract all numeric digits from a string.",
                        "Use list comprehension with `isdigit()` to filter numbers.",
                        "s = 'AB12CD34'\nnumbers = ''.join([ch for ch in s if ch.isdigit()])\nprint(numbers)", 12)

def task_13():
    return execute_task("Extract all words from a sentence in reverse order.",
                        "Use `split()` and slicing to reverse word order.",
                        "s = 'Python is fun'\nwords = s.split()\nprint(' '.join(words[::-1]))", 13)

# Task list
tasks = [task_1, task_2, task_3, task_4, task_5, task_6, task_7, task_8, task_9, task_10, task_11, task_12, task_13]

def main():
    print("\n🚀 Welcome to Python Tutor - String Slicing Challenges")
    
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
