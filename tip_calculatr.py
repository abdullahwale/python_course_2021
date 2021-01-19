#Tip calculaytor
people=int(input("Total number of People's"))
bill=int(input("Total bill"))
tip=int(input("How much tip  you want to give?"))
tip_percent=tip/100
total_bill=bill+tip_percent
per_person_bill=total_bill/people
final_amount=round(per_person_bill,2)
print(f"Each Person should have to pay: {final_amount} rupees")

