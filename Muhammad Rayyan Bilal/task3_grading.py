marks = int(input("Enter your Marks:"))
grade ="H"
if marks>=90 and marks<=100:
   grade="A"
elif marks>=75 and marks<90:
   grade="B"
elif marks>=60 and marks<75:
   grade="C"
elif marks>50 and marks<60:
   grade="D"
elif marks<=50:
   grade="F"
else:
   print("Invalid")

print("Grade:", grade)