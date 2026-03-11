nn = int(input("Digite: "))
cont = 0
cont1 = 0
contt = 0
conta = 0
while(cont < nn):
	cont = cont + 1
	n = input("nome: ").lower()
	if(n == "tais"):
		contt = contt + 1
	elif(n == ("edgar")):
		cont1 = cont1 + 1
	elif(n == "ana"):
		conta = conta + 1
print("tais= ", contt)
print("edgar= ", cont1)
print("ana= ", conta)

