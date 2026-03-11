from numpy import *

n = array(eval(input("valores: ")))
i = 0
total = 10000

while i < size(n) :
	if n[i]== 1 :
		total = total * 2
	elif n[i]== 2 :
		total = total * 1
	elif n[i]== 3 :
		total = total / 2
	elif n[i] ==4 :
		total = total / 4
	i = i + 1
print(round(total, 2))
		

		