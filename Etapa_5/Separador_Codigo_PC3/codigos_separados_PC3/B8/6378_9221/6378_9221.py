from numpy import*

caixa= input ("digite:").upper()
count = zeros(4, dtype= int)

for i in caixa:
	if (i == "C"):
		count[0] = count[0] +1
	elif(i == "D"):
		count[1] = count[1] +1
	elif(i== "V"):
		count[2] = count[2] +1
	elif(i== "U"):
		count[3] = count[3] +1
print(count)