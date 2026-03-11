from numpy import*
x= input("estados:").upper().split(',')
a = zeros(5, dtype=int)
for i in x:
	if(i == "AM"):
		a[0] = a[0] + 1
	elif(i == "PE"):
		a[1] = a[1] + 1
	elif(i == "MG"):
		a[2] = a[2] + 1
	elif(i == "SP"):
		a[3] = a[3] + 1
	elif(i == "RS"):
		a[4] = a[4] + 1
print(max(a))
print(a)