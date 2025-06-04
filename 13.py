#project on tip caluclator
print("Welcome to the tip caluclator\n")
bill=float(input("what was the total bill? $\n"))
people=int(input("how many people would like to split"))
tip=int(input("what is the percentage would you like to give? 10,15,20,25,30\n"))
total_tip_with_bill=tip/100*bill+bill
bill_per_person = total_tip_with_bill/people
final_amount = round(bill_per_person,2)
print(final_amount)