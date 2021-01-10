# Write a program that calculates the Body 
# Mass Index (BMI) from a user's weight and height.
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
#print(type(height))
new_height=float(height)
new_wight=int(weight)
bmi=new_wight // new_height ** 2
#bmi = new_wight / (new_height * new_height)
#print(int(bmi))
print(bmi)
