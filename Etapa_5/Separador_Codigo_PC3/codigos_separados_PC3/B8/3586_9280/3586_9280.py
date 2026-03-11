from numpy import*

v = array(eval(input("  ")))
i = 0 

while(i < size(v)):
	if(v[i] == 1):
		pont_total += 100
	elif(v[i] == 2):
		pont_total += 60
	elif(v[i] == 3):
		pont_total += 20
	elif(v[i] == 4):
		pont_total = 0
	i += 1
print(round(pont_total, 2))
		