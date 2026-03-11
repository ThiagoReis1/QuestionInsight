tempo=float(input("Quantos minutos foram usados:"))

if (100 >= tempo):
	conta= (tempo*1.2)
	
else:
	conta= 25+(tempo*1.4)
	
print(round(conta,2))