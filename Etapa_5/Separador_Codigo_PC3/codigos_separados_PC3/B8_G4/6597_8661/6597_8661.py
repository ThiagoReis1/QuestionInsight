# faça seu código aqui!
n = float(input(""))

con = 0

A = 0
B = 0
C = 0

while n >= 0:
	x = float(input())
	if x.upper() == "A":
		A = A + 1
		con = con +1
	elif x.upper() == "B":
		B = B+1
		con = con + 1
	elif x.upper() == "C":
		C = C+1
		con = con + 1
		
print("A=", A)
print("B=", B)
print("C=", C)
		
		