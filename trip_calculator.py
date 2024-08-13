print("Welcome to the trip calculator!")
total_bill = input("What was the total bill? $ ")
tip_percentage = input("How much tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

total_bill = int(total_bill)
tip_percentage = int(tip_percentage)
people = int(people)

bill_after_tip = total_bill * (1 + tip_percentage / 100)
bill_per_person = bill_after_tip / people
# final_bill_per_person = round(bill_per_person, 2)
final_bill_per_person = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: $ {final_bill_per_person}")
