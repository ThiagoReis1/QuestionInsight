from numpy import*
vet = input()
a = vet.split(",")
c = 0
B = 0
PA = 0
PR = 0
A = 0
I = 0
while(c < size(a)):
	if(a[c] == "B"):
		B = B + 1
	elif(a[c] == "PA"):
		PA = PA + 1
	elif(a[c] == "PR"):
		PR = PR + 1
	elif(a[c] == "A"):
		A = A + 1
	elif(a[c] == "I"):
		I = I + 1
	c = c + 1
vet1 = array([B, PA, PR, A, I])
print(max(vet1))
print(vet1)
