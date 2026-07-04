# ==================================
# ========= Payroll System =========
# ==================================

def calculate_bonus(base_salary, performance_rating):
    
    if performance_rating == 5:
         bonus_percentage = .20
    elif performance_rating in (3, 4) :
         bonus_percentage = .10
    else:
         bonus_percentage = 0.0 

    return base_salary * bonus_percentage   

def calculate_tax(gross_salary):
     
    if gross_salary > 7000:
         tax_percentage = .15
    elif gross_salary >= 3000:
         tax_percentage = .10
    else:
         tax_percentage = 0.0
    return gross_salary * tax_percentage

def  main_hr_app():
     
      print("--- 🏢 Corporate Payroll System 🏢 ---")

      emp_name = input("Enter Employee Name: ")
      base_salary = float(input("Enter Base Salary (EGP): "))
      rating = int(input("Enter Performance Rating"))

      if ( rating < 1 or rating > 5) or base_salary < 0 :
         return "❌ Invalid data entered. Please restart and check your inputs."
      
      bonus = calculate_bonus(base_salary, rating)
      gross_salary = base_salary + bonus
      tax = calculate_tax(gross_salary)
      net_salary = gross_salary - tax

      print("\n" + "="*40)
      print(f"📄 PAYROLL STATEMENT FOR: {emp_name}")
      print("="*40)
      print(f"• Base Salary:       {base_salary:.2f} EGP")
      print(f"• Earned Bonus:      {bonus:.2f} EGP")
      print(f"• Tax Deductions:    {tax:.2f} EGP")
      print("-" * 40)
      print(f"💰 NET PAYABLE CASH: {net_salary:.2f} EGP")
      print("="*40)

main_hr_app()