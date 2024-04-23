import sys
rollNo = int(input("Roll No.: "))
Name = input("Name: ")
marks = {"physics": "", "chemistry": "", "maths": ""}
total = 0
Status = True
for i in marks:
	a = int(input(f"Marks of {i}: "))
	if a < 40:
		Status = False
	total += a
	marks[i] = a
if not Status:
	print("Fail")
	sys.exit()
	
percentage = (total/300)*100
if percentage >= 70:
	print("Grade is DISTINCTION")
elif percentage >= 60:
	print("Grade is FIRST CLASS") 
elif percentage >= 50:
		print("Grade is SECOND CLASS")
else:
		print("Grade is PASS CLASS")