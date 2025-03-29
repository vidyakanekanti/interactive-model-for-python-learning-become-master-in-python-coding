import sys
import time
from io import StringIO

print("Welcome to Python Tutor - String Challenges for BTech Placements")

# Tracking attempts and time
task_attempts = {}
task_times = {}

def get_user_code(prompt, explanation, example_code):
    """Prompts user for input, explains the concept, and captures their code."""
    print("\n" + "=" * 60)
    print(f"💡 Problem: {prompt}")
    print("-" * 60)
    print("📖 Explanation:")
    print(explanation)
    print("📝 Example Code:")
    print(example_code)
    print("=" * 60)
    
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
    """Executes a specific string problem and tracks user attempts."""
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
    
    return input("\n🔄 Redo this problem? (yes/no): ").strip().lower() == "yes"

# 13 String Challenges for Placements
def task_1():
    return execute_task("Reverse a given string without using built-in functions.",
                        "Use a loop or recursion to reverse the string manually.",
                        "s = 'hello'\n# Expected Output: 'olleh'", 1)

def task_2():
    return execute_task("Check if a given string is a palindrome.",
                        "A palindrome reads the same forwards and backwards.",
                        "s = 'madam'\n# Expected Output: True", 2)

def task_3():
    return execute_task("Find the first non-repeating character in a string.",
                        "Use a dictionary to track character frequencies.",
                        "s = 'swiss'\n# Expected Output: 'w'", 3)

def task_4():
    return execute_task("Count the frequency of each character in a string.",
                        "Use a dictionary to store character counts.",
                        "s = 'banana'\n# Expected Output: {'b':1, 'a':3, 'n':2}", 4)

def task_5():
    return execute_task("Check if two strings are anagrams.",
                        "Anagrams contain the same characters in a different order.",
                        "s1 = 'listen', s2 = 'silent'\n# Expected Output: True", 5)

def task_6():
    return execute_task("Find all substrings of a given string.",
                        "Use nested loops to generate all possible substrings.",
                        "s = 'abc'\n# Expected Output: ['a', 'ab', 'abc', 'b', 'bc', 'c']", 6)

def task_7():
    return execute_task("Convert a sentence to title case.",
                        "Title case means the first letter of each word is capitalized.",
                        "s = 'hello world'\n# Expected Output: 'Hello World'", 7)

def task_8():
    return execute_task("Find the longest word in a sentence.",
                        "Use `split()` to break the string into words and find the longest.",
                        "s = 'The quick brown fox'\n# Expected Output: 'quick'", 8)

def task_9():
    return execute_task("Check if a string contains only digits.",
                        "Use `isdigit()` or a loop to verify all characters.",
                        "s = '12345'\n# Expected Output: True", 9)

def task_10():
    return execute_task("Remove duplicate characters from a string.",
                        "Use a set to store unique characters.",
                        "s = 'programming'\n# Expected Output: 'progamin'", 10)

def task_11():
    return execute_task("Compress a string using character counts.",
                        "Use a loop to count consecutive characters.",
                        "s = 'aaabbc'\n# Expected Output: 'a3b2c1'", 11)

def task_12():
    return execute_task("Find the most frequent character in a string.",
                        "Use a dictionary to count occurrences.",
                        "s = 'mississippi'\n# Expected Output: 'i'", 12)

def task_13():
    return execute_task("Replace all spaces in a string with '%20' (URL Encoding).",
                        "Use `replace()` or a loop to substitute spaces.",
                        "s = 'Mr John Smith'\n# Expected Output: 'Mr%20John%20Smith'", 13)

# Task list
tasks = [task_1, task_2, task_3, task_4, task_5, task_6, task_7, task_8, task_9, task_10, task_11, task_12, task_13]

def main():
    print("\n🚀 Welcome to Python Tutor - High-Quality String Problems for BTech Placements")
    
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
