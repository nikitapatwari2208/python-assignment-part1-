# Student Grade Tracker
# Assignment Solution

# =========================
# Task 1 — Data Parsing & Profile Cleaning
# =========================

raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

print("\nTASK 1 — Data Parsing & Profile Cleaning")
print("-" * 50)

cleaned_students = []

for student in raw_students:
    cleaned_name = student["name"].strip().title()
    cleaned_roll = int(student["roll"])
    cleaned_marks = [int(mark) for mark in student["marks_str"].split(", ")]

    cleaned_student = {
        "name": cleaned_name,
        "roll": cleaned_roll,
        "marks": cleaned_marks
    }
    cleaned_students.append(cleaned_student)

    # Validate name
    is_valid = all(word.isalpha() for word in cleaned_name.split())
    validity = "✓ Valid name" if is_valid else "✗ Invalid name"

    # Print profile card
    print("=" * 32)
    print(f"Student : {cleaned_name}")
    print(f"Roll No : {cleaned_roll}")
    print(f"Marks   : {cleaned_marks}")
    print(validity)
    print("=" * 32)

# Print ALL CAPS and lowercase for roll number 103
for student in cleaned_students:
    if student["roll"] == 103:
        print("\nRoll number 103 name formats:")
        print("ALL CAPS  :", student["name"].upper())
        print("lowercase :", student["name"].lower())


# =========================
# Task 2 — Marks Analysis Using Loops & Conditionals
# =========================

print("\nTASK 2 — Marks Analysis Using Loops & Conditionals")
print("-" * 50)

student_name = "Ayesha Sharma"
subjects = ["Math", "Physics", "CS", "English", "Chemistry"]
marks = [88, 72, 95, 60, 78]

print(f"\nStudent Name: {student_name}")
print("\nSubject-wise Grades:")

for i in range(len(subjects)):
    subject = subjects[i]
    score = marks[i]

    if 90 <= score <= 100:
        grade = "A+"
    elif 80 <= score <= 89:
        grade = "A"
    elif 70 <= score <= 79:
        grade = "B"
    elif 60 <= score <= 69:
        grade = "C"
    else:
        grade = "F"

    print(f"{subject:<10} : {score} -> {grade}")

total_marks = sum(marks)
average_marks = round(total_marks / len(marks), 2)

highest_marks = max(marks)
lowest_marks = min(marks)

highest_subject = subjects[marks.index(highest_marks)]
lowest_subject = subjects[marks.index(lowest_marks)]

print("\nSummary:")
print(f"Total marks            : {total_marks}")
print(f"Average marks          : {average_marks}")
print(f"Highest scoring subject: {highest_subject} ({highest_marks})")
print(f"Lowest scoring subject : {lowest_subject} ({lowest_marks})")

# While loop for marks entry
print("\nAdd new subjects (type 'done' to stop)")

new_subjects_added = 0

while True:
    new_subject = input("Enter subject name: ").strip()

    if new_subject.lower() == "done":
        break

    new_marks_input = input(f"Enter marks for {new_subject} (0-100): ").strip()

    try:
        new_marks = float(new_marks_input)

        if 0 <= new_marks <= 100:
            subjects.append(new_subject)
            marks.append(new_marks)
            new_subjects_added += 1
            print(f"{new_subject} added successfully.\n")
        else:
            print("Warning: Marks must be between 0 and 100. Entry not added.\n")

    except ValueError:
        print("Warning: Invalid input. Please enter a numeric value.\n")

updated_average = round(sum(marks) / len(marks), 2)

print("\nUpdated Result:")
print(f"New subjects added : {new_subjects_added}")
print(f"Updated average    : {updated_average}")


# =========================
# Task 3 — Class Performance Summary
# =========================

print("\nTASK 3 — Class Performance Summary")
print("-" * 50)

class_data = [
    ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
    ("Rohit Verma",    [55, 68, 49, 72, 61]),
    ("Priya Nair",     [91, 85, 88, 94, 79]),
    ("Karan Mehta",    [40, 55, 38, 62, 50]),
    ("Sneha Pillai",   [75, 80, 70, 68, 85]),
]

student_averages = []
pass_count = 0
fail_count = 0

print(f"{'Name':<18} | {'Average':<7} | Status")
print("-" * 40)

for name, scores in class_data:
    avg = round(sum(scores) / len(scores), 2)
    status = "Pass" if avg >= 60 else "Fail"

    if status == "Pass":
        pass_count += 1
    else:
        fail_count += 1

    student_averages.append((name, avg))
    print(f"{name:<18} | {avg:<7.2f} | {status}")

topper = max(student_averages, key=lambda x: x[1])
class_average = round(sum(avg for _, avg in student_averages) / len(student_averages), 2)

print("\nClass Summary:")
print(f"Passed students : {pass_count}")
print(f"Failed students : {fail_count}")
print(f"Class topper    : {topper[0]} ({topper[1]})")
print(f"Class average   : {class_average}")


# =========================
# Task 4 — String Manipulation Utility
# =========================

print("\nTASK 4 — String Manipulation Utility")
print("-" * 50)

essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

# Step 1
clean_essay = essay.strip()
print("1. Stripped essay:")
print(clean_essay)

# Step 2
title_essay = clean_essay.title()
print("\n2. Title Case:")
print(title_essay)

# Step 3
python_count = clean_essay.count("python")
print("\n3. Count of 'python':")
print(python_count)

# Step 4
replaced_essay = clean_essay.replace("python", "Python 🐍")
print("\n4. Replaced essay:")
print(replaced_essay)

# Step 5
sentences = clean_essay.split(". ")
print("\n5. List of sentences:")
print(sentences)

# Step 6
print("\n6. Numbered sentences:")
for index, sentence in enumerate(sentences, start=1):
    sentence = sentence.strip()
    if not sentence.endswith("."):
        sentence += "."
    print(f"{index}. {sentence}")
    