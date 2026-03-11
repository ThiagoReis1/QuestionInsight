from numpy import*
v = str(input("Estados: "))
v = v.split(',')
x = zeros(5, dtype = int)
pb = 0
ppa = 0
ppr = 0
pa = 0
pi = 0
for i in v:
	if(i == "B"):
		pb = pb + 1
	elif(i == "PA"):
		ppa = ppa + 1
	elif(i == "PR"):
		ppr = ppr + 1
	elif(i == "A"):
		pa = pa + 1
	elif(i == "I"):
		pi = pi + 1
x[0] = pb
x[1] = ppa
x[2] = ppr
x[3] = pa
x[4] = pi
print(max(x))
print(x)