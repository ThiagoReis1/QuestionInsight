from numpy import*
s= (input("Informe os estados: ")).upper ()
a = s.split(",")
x = 0
cont= zeros(5, dtype= int)


for i in range (size(a)):
	if (a[i] == "AC"):
		cont[0] = cont [0] + 1
	elif (a[i] == "AM"):
		cont[1] = cont[1] + 1
	elif (a[i] == "PA"):
		cont[2] = cont[2] + 1
	elif (a[i] == "RO"):
		cont[3] = cont[3] + 1
	elif (a[i] == "RR"):
		cont[4] = cont[4] + 1
y = max(cont)
print (y)
print (cont)
	
	