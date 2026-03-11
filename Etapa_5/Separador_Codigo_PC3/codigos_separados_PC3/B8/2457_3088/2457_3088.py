b = int(input("Insira a quantidade de bilhetes desejados:"))
t = input("Insira o tipo de acomodacao:")
if (t=="rede") or (t=="camarote") or (t=="suite"): 
	if t=="rede":	
		result =round(b*500.00,2)
	elif t=="camarote":
		result =round(b*1200.00,2)
	elif t=="suite":
		result = round(b*1500.00,2)
else:
	result = "acomodacao invalida"
print(result)