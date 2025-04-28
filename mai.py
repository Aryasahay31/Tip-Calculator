print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip_bill = (tip/100) * bill + bill
each_pay =  tip_bill/people
final_each_pay = round(each_pay, 2)
print(f"Each person has to pay: $ {final_each_pay}.")