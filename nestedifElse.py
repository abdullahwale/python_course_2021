#Nested if else
#Program to Take Admission in University
#First You got 50 or above marks from the Univesity Test
#After that you should Got 20 marks or above in Department Test
#After that you got 10 marks or above in Interview
#if you pass all then you got Admission in MS Computer Science 
u_test_marks=int(input("Enter your university test Marks!"))

if u_test_marks>=50:
  d_test_marks=int(input("Enter your departmental test Marks!"))
  if d_test_marks>=20:
    interview_marks=int(input("Enter your Interview Markss Marks!"))
    if interview_marks>=10:
        print("You Got Admission")
    else:
      print("Please Try Again")
  else:
    print("Please Try Again")
else:
  print("Please Try Again")









#  print("You Got Admission")