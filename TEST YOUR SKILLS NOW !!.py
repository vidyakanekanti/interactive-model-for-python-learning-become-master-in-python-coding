import sys
import time
from io import StringIO

def get_user_code(question):
    """Prompts user for input and captures their code."""
    print("\n" + "=" * 50)
    print(f"💡 Question: {question}")
    print("=" * 50)
    
    lines = []
    print("\n⌨️ Enter your code (type 'done' to finish):")
    while True:
        line = input(">>> ").strip()
        if line.lower() == "done":
            break
        lines.append(line)
    
    return "\n".join(lines)

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

questions = [
    "1️⃣ Write a Python function to check if a number is prime.",
    "2️⃣ Implement a function that reverses a string without using built-in functions.",
    "3️⃣ Use a lambda function to filter out even numbers from a list.",
    "4️⃣ Implement Bubble Sort to sort a list in ascending order.",
    "5️⃣ Write a program to count the frequency of words in a given sentence.",
    "6️⃣ Create a function that finds the factorial of a number using recursion.",
    "7️⃣ Given a list of numbers, find the second largest number without using built-in functions.",
    "8️⃣ Implement a function that removes duplicates from a list without using set().",
    "9️⃣ Use the map() function to square all elements in a list.",
    "🔟 Implement a function that checks if a given string is a palindrome.",
    "1️⃣1️⃣ Write a function that merges two sorted lists into a single sorted list.",
    "1️⃣2️⃣ Implement a basic try-except block to handle division by zero errors.",
    "1️⃣3️⃣ Write a Python script to read a text file and count the number of lines.",
]

user_codes = []

# Collect user inputs for all questions
for question in questions:
    user_codes.append(get_user_code(question))

print("\n🎯 You have attempted all questions. Now running your solutions...\n")
time.sleep(2)

# Execute and display outputs for all user-submitted codes
for i, code in enumerate(user_codes):
    print("\n" + "=" * 50)
    print(f"🚀 Output for Question {i+1}:")
    print("=" * 50)
    print(run_code(code))
    print("=" * 50)
    time.sleep(1)

print("\n🎉 Test completed! Review your outputs and improve where needed. 🚀")
