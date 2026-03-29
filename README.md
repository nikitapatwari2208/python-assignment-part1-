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
(base) nikitapatwari@Nikitas-MacBook-Air untitled folder % 
