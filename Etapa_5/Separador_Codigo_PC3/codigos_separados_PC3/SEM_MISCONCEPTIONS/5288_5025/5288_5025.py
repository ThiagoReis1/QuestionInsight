idade = int(input("Idade do participante:"))
cont = 0
mi = 0
while (idade != -1):
	cont = cont + 1
	if (idade < 18 and idade != -1):
		mi = mi + 1 
	idade = int(input("Idade do participante:"))
print(cont)
print(round((mi * 100 / cont),2))
	
	
	