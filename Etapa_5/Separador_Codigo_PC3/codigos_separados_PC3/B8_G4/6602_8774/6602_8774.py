# faça seu código aqui!
N= int(input("qtde de alunos: "))
l= 0
c= 0
p= 0
cont= 0

while cont < N:
	prato= input().upper()
	if prato == "C":
		c= c + 1
	elif prato == "L":
		l= l + 1
	elif prato == "P":
		p= p + 1
	cont+=1
		
print("L=", l)
print("C=", c)
print("P=", p)
	
		

