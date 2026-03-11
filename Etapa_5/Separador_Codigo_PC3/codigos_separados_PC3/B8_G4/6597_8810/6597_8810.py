# faça seu código aqui!
n = int(input("Digite o numero de funcionarios: "))

i = 0 
a = 0
b = 0
c = 0

while(i < n):
	v = input("Seu voto: ").upper()
	if(v == "A"):
		a = a + 1
	elif(v == "B"):
		b = b + 1
	elif(v == "C"):
		c = c + 1
	i = i + 1
	

print("A=", a)
print("B=", b)
print("C=", c)