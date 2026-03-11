from numpy import*

a = input("Insira a Cor do Olho do Cliente: ").split(",")
n = zeros(5, dtype=int)

for i in range(size(a)):
	if(a[i] == "P"):
		n[0] += 1
	elif a[i] == "C":
		n[1] += 1
	elif a[i] == "M":
		n[2] += 1
	elif a[i] == "V":
		n[3] += 1
	elif a[i] == "A":
		n[4] += 1
	
print(max(n))
print(n)