import sys
import time
from io import StringIO

print("Welcome to Python Tutor - String Functions Challenges")

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
    """Executes a specific string function task and tracks user attempts."""
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

# 13 String Functions Challenges
def task_1():
    return execute_task("Convert a string to uppercase using a string function.",
                        "Use `upper()` to convert all characters to uppercase.",
                        "s = 'hello world'\nprint(s.upper())", 1)

def task_2():
    return execute_task("Convert a string to lowercase using a string function.",
                        "Use `lower()` to convert all characters to lowercase.",
                        "s = 'HELLO WORLD'\nprint(s.lower())", 2)

def task_3():
    return execute_task("Capitalize the first letter of a string.",
                        "Use `capitalize()` to make only the first letter uppercase.",
                        "s = 'python is fun'\nprint(s.capitalize())", 3)

def task_4():
    return execute_task("Swap uppercase and lowercase letters in a string.",
                        "Use `swapcase()` to flip letter cases.",
                        "s = 'HeLLo WoRLd'\nprint(s.swapcase())", 4)

def task_5():
    return execute_task("Title-case a string (capitalize each word's first letter).",
                        "Use `title()` to capitalize the first letter of each word.",
                        "s = 'python programming language'\nprint(s.title())", 5)

def task_6():
    return execute_task("Find the position of the word 'Python' in a sentence.",
                        "Use `find('word')` to get the index of the first occurrence.",
                        "s = 'I love Python programming!'\nprint(s.find('Python'))", 6)

def task_7():
    return execute_task("Replace all occurrences of 'Python' with 'Java' in a string.",
                        "Use `replace('old', 'new')` to modify text.",
                        "s = 'Python is great! Python is fun!'\nprint(s.replace('Python', 'Java'))", 7)

def task_8():
    return execute_task("Check if a string starts with 'Hello'.",
                        "Use `startswith('word')` to check if a string begins with a substring.",
                        "s = 'Hello, how are you?'\nprint(s.startswith('Hello'))", 8)

def task_9():
    return execute_task("Check if a string ends with 'world!'.",
                        "Use `endswith('word')` to check if a string ends with a substring.",
                        "s = 'Hello world!'\nprint(s.endswith('world!'))", 9)

def task_10():
    return execute_task("Count the number of times 'o' appears in a string.",
                        "Use `count('character')` to count occurrences.",
                        "s = 'hello world!'\nprint(s.count('o'))", 10)

def task_11():
    return execute_task("Remove leading and trailing spaces from a string.",
                        "Use `strip()` to remove spaces from both ends.",
                        "s = '   Python   '\nprint(s.strip())", 11)

def task_12():
    return execute_task("Split a string into a list of words.",
                        "Use `split('delimiter')` to break a string into parts.",
                        "s = 'Python is fun'\nprint(s.split())", 12)

def task_13():
    return execute_task("Join a list of words into a single string with spaces.",
                        "Use `join()` to combine words into a single string.",
                        "words = ['Python', 'is', 'awesome']\nprint(' '.join(words))", 13)

# Task list
tasks = [task_1, task_2, task_3, task_4, task_5, task_6, task_7, task_8, task_9, task_10, task_11, task_12, task_13]

def main():
    print("\n🚀 Welcome to Python Tutor - String Functions Challenges")
    
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
