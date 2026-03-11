from numpy import*
x = input("tarefas definidas por letras: ").upper().split(",")
a = zeros(4,dtype=int)

for i in range(size(x)):
	if x[i] == "A":
		a[0] = a[0] + 1
	elif x[i] == "P":
		a[1] = a[1] + 1
	elif x[i] == "D":
		a[2] = a[2] + 1
	elif x[i] ==  "M":
		a[3] = a[3] + 1
print(a)
	
	
	