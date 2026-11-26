# Electrical-bill
Progressive Electricity Billing System
Student Information
- Name: P.Sowmya
- Roll Number: N26V01A0316
- Branch: CSE
- Section:section-4
- Case Study Title: Progressive Electricity Billing System
1. Problem Statement
Develop a Python program to calculate household electricity bills using multiple
progressive consumption slabs, fixed charges, surcharges, and rebates. The
program must accept electricity consumption for several months, calculate
each month's bill, compare the bills, and identify unusual increases.
2. Objectives
1. Calculate electricity charges using progressive slabs.
2. Add the monthly fixed charge.
3. Apply a rebate when consumption is within the specified limit.
4. Calculate the applicable surcharge.
5. Display an itemized bill for each month.
6. Compare bills across multiple months.
7. Flag a bill increase greater than the defined threshold.
3. Assumptions and Sample Tariff
The following rates are illustrative values selected for this academic case
study. They are not represented as the official tariff of any electricity
distribution company. Change the constants at the top of
electricity_billing.py if your faculty provides different rates.
Consumption slab	Rate per unit
First 100 units	Rs. 1.50
Next 100 units (101-200)	Rs. 2.50
Next 100 units (201-300)	Rs. 4.00
Above 300 units	Rs. 6.00


Other assumptions:
- Fixed charge: Rs. 50 per month.
- Rebate: 10% of the energy charge if monthly usage is 100 units or less.
- Surcharge: 5% of the energy charge after rebate plus the fixed charge.
- An unusual increase is a bill increase of more than 30% compared with the
  immediately preceding month.
- Consumption is entered as a non-negative whole number of units.
- The comparison uses total bill amounts, not only energy charges.
- The first month has no previous month for comparison.
4. Algorithm
1. Start the program.
2. Read the number of months to compare.
3. For each month:
   - Read the month name and units consumed.
   - Validate that units are a non-negative integer.
   - Calculate the charge in each slab progressively.
   - Add the slab charges to obtain the energy charge.
   - If consumption is 100 units or less, calculate the 10% rebate.
   - Add the fixed charge to the energy charge after rebate.
   - Calculate the 5% surcharge.
   - Calculate the total bill.
   - Display the itemized bill and store the monthly record.
4. Compare each month's total bill with the previous month's bill.
5. Calculate the percentage change.
6. If the increase is greater than 30%, mark it as an unusual increase.
7. Display the monthly comparison and conclusion.
8. Stop.
5. Flowchart
          +----------------+
          |     START      |
          +----------------+
                  |
                  v
       +----------------------+
       | Read number of months|
       +----------------------+
                  |
                  v
       +----------------------+
       | Read month and units |
       +----------------------+
                  |
                  v
       +----------------------+
       | Calculate slab-wise  |
       | energy charge        |
       +----------------------+
                  |
                  v
       +----------------------+
       | Usage <= 100 units?  |
       +----------------------+
            /          \
          Yes           No
           |             |
           v             |
   +----------------+    |
   | Calculate 10%  |    |
   | rebate         |    |
   +----------------+    |
           |             |
           +------v------+
                  |
                  v
       +----------------------+
       | Add fixed charge and |
       | calculate surcharge |
       +----------------------+
                  |
                  v
       +----------------------+
       | Calculate total bill |
       | and display it       |
       +----------------------+
                  |
                  v
       +----------------------+
       | More months to enter?|
       +----------------------+
            /          \
          Yes           No
           |             |
           +---> Read    v
                next  +----------------------+
                month | Compare monthly bills|
                      +----------------------+
                                |
                                v
                      +----------------------+
                      | Increase greater than |
                      | 30 percent?           |
                      +----------------------+
                           /          \
                         Yes           No
                          |             |
                          v             v
                    +----------+  +-------------+
                    | Flag as  |  | No unusual  |
                    | unusual  |  | increase    |
                    +----------+  +-------------+
                           \          /
                            v        v
                      +----------------+
                      |      STOP      |
                      +----------------+
6. Pseudocode
START

READ number_of_months
CREATE empty monthly_records list

FOR each month:
    READ month_name
    READ units

    energy_charge = 0

    CALCULATE charge for first 100 units at Rs. 1.50
    CALCULATE charge for next 100 units at Rs. 2.50
    CALCULATE charge for next 100 units at Rs. 4.00
    CALCULATE remaining units at Rs. 6.00

    IF units <= 100:
        rebate = 10% of energy_charge
    ELSE:
        rebate = 0

    taxable_amount = energy_charge - rebate + fixed_charge
    surcharge = 5% of taxable_amount
    total_bill = taxable_amount + surcharge

    DISPLAY itemized bill
    STORE month_name, units, total_bill

FOR each stored month:
    IF it is the first month:
        DISPLAY "No previous month"
    ELSE:
        percentage_change =
            (current_bill - previous_bill) / previous_bill * 100

        IF percentage_change > 30:
            DISPLAY "UNUSUAL INCREASE"
        ELSE:
            DISPLAY percentage_change

DISPLAY monthly comparison
STOP
7. Python Source Code
The complete program is in [`electricity_billing.py`](electricity_billing.py).

It uses only Python's standard language features and does not require any
external packages.
8. How to Execute
Requirement: Python 3 installed on your computer.
1. Download or clone this project.
2. Open a terminal or command prompt in the project folder.
3. Run:
python electricity_billing.py
On some systems, use:
python3 electricity_billing.py
4. Enter the number of months.
5. Enter each month name and its electricity consumption in units.
6. Review the itemized bills and monthly comparison.
9. Test Cases
The following expected values use the sample tariff described above.
Test	Units	Energy charge	Rebate	Fixed charge	Surcharge	Total bill
1 - Low usage	50	Rs. 75.00	Rs. 7.50	Rs. 50.00	Rs. 5.88	Rs. 123.38
2 - Slab boundary	100	Rs. 150.00	Rs. 15.00	Rs. 50.00	Rs. 9.25	Rs. 194.25
3 - Second slab	150	Rs. 275.00	Rs. 0.00	Rs. 50.00	Rs. 16.25	Rs. 341.25
4 - Third slab	250	Rs. 600.00	Rs. 0.00	Rs. 50.00	Rs. 32.50	Rs. 682.50
5 - Fourth slab	350	Rs. 1,100.00	Rs. 0.00	Rs. 50.00	Rs. 57.50	Rs. 1,207.50
6 - Zero usage	0	Rs. 0.00	Rs. 0.00	Rs. 50.00	Rs. 2.50	Rs. 52.50


Comparison test: Enter three monthly consumptions: 100, 120, and 200 units.
The program should compare each total bill with the previous month. It should
flag increases greater than 30% (both transitions in this example are flagged).

Input validation tests:
- Entering -10 units should display an error and ask again.
- Entering abc instead of a number should display an error and ask again.
- Entering 0 units should calculate a bill containing the fixed charge and
  applicable surcharge.
10. Sample Output
PROGRESSIVE ELECTRICITY BILLING SYSTEM

How many months do you want to compare? 3

Enter month name: January
Enter electricity units consumed in January: 100

TOTAL BILL: Rs. 194.25

Enter month name: February
Enter electricity units consumed in February: 120

TOTAL BILL: Rs. 262.50

Enter month name: March
Enter electricity units consumed in March: 200

TOTAL BILL: Rs. 472.50

MONTHLY BILL COMPARISON

Month       Units       Bill (Rs.)       Change
January      100          194.25         N/A
February     120          262.50         +35.14%  ** UNUSUAL **
March        200          472.50         +80.00%  ** UNUSUAL **
The sample output is illustrative. Run the program to see the complete
itemized bill and comparison.
11. Conclusion
The Progressive Electricity Billing System calculates household electricity
bills by applying progressive consumption slabs, fixed charges, rebates, and
surcharges. It stores monthly bill details and compares consecutive months to
identify unusual increases greater than 30%. This program demonstrates how
basic Python concepts can be used to solve a practical household billing
problem.
12. Suggested Repository Structure
Python-Activity-Based-Learning/
|
+-- Progressive-Electricity-Billing/
|   |
|   +-- electricity_billing.py
|   +-- README.md
|   +-- sample_output.txt
|
+-- README.md
+-- consolidated_report.pdf
For the full assignment, add your actual execution screenshots and include
this case study in the consolidated PDF report. The main repository should be
named Python-Activity-Based-Learning as specified in the instructions.
