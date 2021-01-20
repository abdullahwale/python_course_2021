#if-elif
#take marks display grade 
marks=int(input("Enter Your marks in a Programming Subject!"))
if marks>=90:
  print("A Grade")
elif marks>80:
  print("B Grade")
elif marks>70:
  print("C Grade")
elif marks>60:
  print("D Grade")
else:
  print("F Grade")