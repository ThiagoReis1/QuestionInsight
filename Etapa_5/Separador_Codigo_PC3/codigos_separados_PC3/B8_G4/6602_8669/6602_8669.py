# faça seu código aqui!
n= int(input("numero de alunos: "))
c= 0
L= 0
C= 0
P= 0
while c < n:
	prato= input("escolha um prato (L, C ou P): ").upper()
	c = c+1
	if prato == "L":
		L= L+1
	elif prato == "C": 
		C= C+1
	elif prato == "P":
		P= P+1
print("L=", L)
print("C=", C)
print("P=", P)
	
	