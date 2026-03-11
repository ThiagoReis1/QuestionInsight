# faça seu código aqui!
n = int(input("Quantidade de funcionarios do setor: "))
cont = 0
a = 0
b = 0
c = 0
while(cont < n):
	vt = input("Informe a tecnica desejada: ").upper()
	if(vt == "A"):
		a = a + 1
	elif(vt == "B"):
		b = b + 1
	elif(vt == "C"):
		c = c + 1
	
	cont = cont + 1
	
print("A= ", a)
print("B= ", b)
print("C= ", c)