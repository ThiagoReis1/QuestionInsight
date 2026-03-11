nb = int(input("numero de bacterias: "))
nh = int(input("numero horas: "))

cont = 0
soma = 0

while(nb>0): 
	cont = cont + (cont ** 0.02)
	soma = soma + cont
	t = cont + soma
	
print(t)