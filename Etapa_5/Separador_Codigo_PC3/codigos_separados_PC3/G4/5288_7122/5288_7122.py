idade = int(input(""))

cont = 0
soma = 0

while(idade != -1):
	if(idade < 18):
		soma = soma + 1
	cont = cont + 1
	idade = int(input(""))
	
print(cont)
c = (soma*100)/cont
print(round(c,2))
	