C = input("S.I,U: ").upper()
soma = 0
cont = 0
while(C != "X"):
	if(C == "S"):
		soma = soma + 1
	C = input("S,I,U: ")
print(soma)