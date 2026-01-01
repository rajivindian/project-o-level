import sys
import datetime

# This defines your goals
goals = ["Data Analytics", "Digital Marketing", "Visual Design", "Python Automation"]

print("--- SYSTEM DIAGNOSTIC ---")
print(f"Python Version: {sys.version.split()[0]}")
print(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d')}")
print("-" * 20)
print("MY LEARNING GOALS:")

# This loop prints your goals one by one
for goal in goals:
    print(f"[ ] {goal}")

print("-" * 20)
print("System ready. Let's begin.")