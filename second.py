# emreyo
import first
num = raw_input("Input the number of student (1-10): ")
num = int(num)
while num < 1 or num > 10:
	num = raw_input("Input the number of student (1-10): ")
	num = int(num)
i = 1
sList = []
while i <= num:
	st = first.student()
	sList.insert(i, st)
	i = i + 1
i = 1
for value in sList:
	value.writeStudent()
	i = i + 1