# python-assignment-part1-
(base) nikitapatwari@Nikitas-MacBook-Air untitled folder % /usr/local
/bin/python3 "/Users/ni
kitapatwari/Desktop/unt
itled folder/part2_orde
r_system.py"

TASK 1 — Explore the Menu
--------------------------------------------------
===== Starters =====
Paneer Tikka       ₹180.00   [Available]
Chicken Wings      ₹220.00   [Unavailable]
Veg Soup           ₹120.00   [Available]

===== Mains =====
Butter Chicken     ₹320.00   [Available]
Dal Tadka          ₹180.00   [Available]
Veg Biryani        ₹250.00   [Available]
Garlic Naan        ₹ 40.00   [Available]

===== Desserts =====
Gulab Jamun        ₹ 90.00   [Available]
Rasgulla           ₹ 80.00   [Available]
Ice Cream          ₹110.00   [Unavailable]

Total number of items on menu : 10
Total number of available items : 8
Most expensive item : Butter Chicken (₹320.00)
Items priced under ₹150:
- Veg Soup: ₹120.00
- Garlic Naan: ₹40.00
- Gulab Jamun: ₹90.00
- Rasgulla: ₹80.00
- Ice Cream: ₹110.00

TASK 2 — Cart Operations
--------------------------------------------------
Step 1: Add Paneer Tikka x2
Added "Paneer Tikka" x2 to cart.

Current Cart:
- Paneer Tikka | Qty: 2 | Price: ₹180.00 | Total: ₹360.00

Step 2: Add Gulab Jamun x1
Added "Gulab Jamun" x1 to cart.

Current Cart:
- Paneer Tikka | Qty: 2 | Price: ₹180.00 | Total: ₹360.00
- Gulab Jamun | Qty: 1 | Price: ₹90.00 | Total: ₹90.00

Step 3: Add Paneer Tikka x1
"Paneer Tikka" already in cart. Quantity updated to 3.

Current Cart:
- Paneer Tikka | Qty: 3 | Price: ₹180.00 | Total: ₹540.00
- Gulab Jamun | Qty: 1 | Price: ₹90.00 | Total: ₹90.00

Step 4: Add Mystery Burger
Cannot add "Mystery Burger" - item does not exist in menu.

Current Cart:
- Paneer Tikka | Qty: 3 | Price: ₹180.00 | Total: ₹540.00
- Gulab Jamun | Qty: 1 | Price: ₹90.00 | Total: ₹90.00

Step 5: Add Chicken Wings
Cannot add "Chicken Wings" - item is unavailable.

Current Cart:
- Paneer Tikka | Qty: 3 | Price: ₹180.00 | Total: ₹540.00
- Gulab Jamun | Qty: 1 | Price: ₹90.00 | Total: ₹90.00

Step 6: Remove Gulab Jamun
"Gulab Jamun" removed from cart.

Current Cart:
- Paneer Tikka | Qty: 3 | Price: ₹180.00 | Total: ₹540.00

========== Order Summary ==========
Paneer Tikka       x3    ₹540.00
------------------------------------
Subtotal:             ₹540.00
GST (5%):             ₹27.00
Total Payable:        ₹567.00
====================================

TASK 3 — Inventory Tracker with Deep Copy
--------------------------------------------------
Before manual change:
Inventory stock of Paneer Tikka: 10
Backup stock of Paneer Tikka   : 10

After manual change:
Inventory stock of Paneer Tikka: 99
Backup stock of Paneer Tikka   : 10

Inventory restored.
Inventory stock of Paneer Tikka: 10
Backup stock of Paneer Tikka   : 10

Order fulfilment:
Paneer Tikka: deducted 3, remaining stock = 7

Reorder Alerts:

Final inventory:
Paneer Tikka       Stock: 7
Chicken Wings      Stock: 8
Veg Soup           Stock: 15
Butter Chicken     Stock: 12
Dal Tadka          Stock: 20
Veg Biryani        Stock: 6
Garlic Naan        Stock: 30
Gulab Jamun        Stock: 5
Rasgulla           Stock: 4
Ice Cream          Stock: 7

Inventory backup:
Paneer Tikka       Stock: 10
Chicken Wings      Stock: 8
Veg Soup           Stock: 15
Butter Chicken     Stock: 12
Dal Tadka          Stock: 20
Veg Biryani        Stock: 6
Garlic Naan        Stock: 30
Gulab Jamun        Stock: 5
Rasgulla           Stock: 4
Ice Cream          Stock: 7

TASK 4 — Daily Sales Log Analysis
--------------------------------------------------
Revenue per day:
2025-01-01: ₹790.00
2025-01-02: ₹560.00
2025-01-03: ₹960.00
2025-01-04: ₹570.00

Best-selling day: 2025-01-03 (₹960.00)
Most ordered item: Garlic Naan (5 orders)

Updated Revenue per day:
2025-01-01: ₹790.00
2025-01-02: ₹560.00
2025-01-03: ₹960.00
2025-01-04: ₹570.00
2025-01-05: ₹750.00

Updated best-selling day: 2025-01-03 (₹960.00)

All orders:
1. [2025-01-01] Order #1 — ₹220.00 — Items: Paneer Tikka, Garlic Naan
2. [2025-01-01] Order #2 — ₹210.00 — Items: Gulab Jamun, Veg Soup
3. [2025-01-01] Order #3 — ₹360.00 — Items: Butter Chicken, Garlic Naan
4. [2025-01-02] Order #4 — ₹220.00 — Items: Dal Tadka, Garlic Naan
5. [2025-01-02] Order #5 — ₹340.00 — Items: Veg Biryani, Gulab Jamun
6. [2025-01-03] Order #6 — ₹260.00 — Items: Paneer Tikka, Rasgulla
7. [2025-01-03] Order #7 — ₹570.00 — Items: Butter Chicken, Veg Biryani
8. [2025-01-03] Order #8 — ₹130.00 — Items: Garlic Naan, Gulab Jamun
9. [2025-01-04] Order #9 — ₹300.00 — Items: Dal Tadka, Garlic Naan, Rasgulla
10. [2025-01-04] Order #10 — ₹270.00 — Items: Paneer Tikka, Gulab Jamun
11. [2025-01-05] Order #11 — ₹490.00 — Items: Butter Chicken, Gulab Jamun, Garlic Naan
12. [2025-01-05] Order #12 — ₹260.00 — Items: Paneer Tikka, Rasgulla
(base) nikitapatwari@Nikitas-MacBook-Air untitled folder % /usr/local/bin/python3 "/Users/nikitapatwari/Desktop/untitled folder/
part1_grade_tracker.py"

TASK 1 — Data Parsing & Profile Cleaning
--------------------------------------------------
================================
Student : Ayesha Sharma
Roll No : 101
Marks   : [88, 72, 95, 60, 78]
✓ Valid name
================================
================================
Student : Rohit Verma
Roll No : 102
Marks   : [55, 68, 49, 72, 61]
✓ Valid name
================================
================================
Student : Priya Nair
Roll No : 103
Marks   : [91, 85, 88, 94, 79]
✓ Valid name
================================
================================
Student : Karan Mehta
Roll No : 104
Marks   : [40, 55, 38, 62, 50]
✓ Valid name
================================
================================
Student : Sneha Pillai
Roll No : 105
Marks   : [75, 80, 70, 68, 85]
✓ Valid name
================================

Roll number 103 name formats:
ALL CAPS  : PRIYA NAIR
lowercase : priya nair

TASK 2 — Marks Analysis Using Loops & Conditionals
--------------------------------------------------

Student Name: Ayesha Sharma

Subject-wise Grades:
Math       : 88 -> A
Physics    : 72 -> B
CS         : 95 -> A+
English    : 60 -> C
Chemistry  : 78 -> B

Summary:
Total marks            : 393
Average marks          : 78.6
Highest scoring subject: CS (95)
Lowest scoring subject : English (60)

Add new subjects (type 'done' to stop)
Enter subject name: biology
Enter marks for biology (0-100): 86
biology added successfully.

Enter subject name: done

Updated Result:
New subjects added : 1
Updated average    : 79.83

TASK 3 — Class Performance Summary
--------------------------------------------------
Name               | Average | Status
----------------------------------------
Ayesha Sharma      | 78.60   | Pass
Rohit Verma        | 61.00   | Pass
Priya Nair         | 87.40   | Pass
Karan Mehta        | 49.00   | Fail
Sneha Pillai       | 75.60   | Pass

Class Summary:
Passed students : 4
Failed students : 1
Class topper    : Priya Nair (87.4)
Class average   : 70.32

TASK 4 — String Manipulation Utility
--------------------------------------------------
1. Stripped essay:
python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.

2. Title Case:
Python Is A Versatile Language. It Supports Object Oriented, Functional, And Procedural Programming. Python Is Widely Used In Data Science And Machine Learning.

3. Count of 'python':
2

4. Replaced essay:
Python 🐍 is a versatile language. it supports object oriented, functional, and procedural programming. Python 🐍 is widely used in data science and machine learning.

5. List of sentences:
['python is a versatile language', 'it supports object oriented, functional, and procedural programming', 'python is widely used in data science and machine learning.']

6. Numbered sentences:
1. python is a versatile language.
2. it supports object oriented, functional, and procedural programming.
3. python is widely used in data science and machine learning.
(base) nikitapatwari@Nikitas-MacBook-Air untitled folder % 
