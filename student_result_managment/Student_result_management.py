# Mini Project 1: Student Result Management System
# Beginner Level Python Project

print("=== Student Result Management System ===")

while True:
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))

    if marks >= 75:
        result = "Distinction"
    elif marks >= 60:
        result = "First Class"
    elif marks >= 40:
        result = "Pass"
    else:
        result = "Fail"

    print("\n--- Result ---")
    print("Name   :", name)
    print("Marks  :", marks)
    print("Result :", result)
