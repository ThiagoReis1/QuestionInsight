# faça seu código aqui!
n = int(input("n > "))
c = 0
L = 0
C = 0
P = 0

while c < n:
	c = c+1
	o = input("o > ").upper()
	if o == "L":
		L = L +1
	elif o == "C":
		C = C +1
	elif o == "P":
		P = P +1
	
print("L= "+str(L))
print("C= "+str(C))
print("P= "+str(P))
