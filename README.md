# 🏢 Corporate Payroll System

A simple and interactive Python command-line application designed to calculate employee payroll details, including performance-based bonuses and tax deductions based on Egyptian Pound (EGP) brackets.

## 🚀 Features

* **Dynamic Bonus Calculation:** Automatically applies a 20% or 10% bonus based on the employee's performance rating (1 to 5).
* **Tax Deduction System:** Calculates taxes automatically using salary brackets (10% or 15%).
* **Input Validation:** Restricts invalid entries such as negative salaries or ratings outside the 1-5 range.
* **Clean Invoice Output:** Generates a neat, formatted text-based payroll statement.

## 🛠️ How It Works

The system calculates net payable cash using the following logic:
1. **Gross Salary** = Base Salary + Bonus
2. **Tax Deductions** = Applied based on Gross Salary brackets
3. **Net Payable Cash** = Gross Salary - Tax

## 💻 Technical Stack

* **Language:** Python 3.x
* **Core File:** `main.py`

## 🏃 How to Run the Project

1. Make sure you have Python installed on your machine.
2. Clone this repository or download the `main.py` file.
3. Open your terminal/command prompt, navigate to the file directory, and run:

```bash
python main.py
