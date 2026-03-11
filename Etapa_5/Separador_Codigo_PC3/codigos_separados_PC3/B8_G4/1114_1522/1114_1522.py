# Universidade Federal do Amazonas - UFAM
# Ana Regina dos Santos da Silva - Mat. 21603561
# Exercicio 1
# 21/07/16

# Leitura da Velocidade do trem (v) em km/h e do tempo (t) em h
v = float(input("Digite a velocidade do trem:"))
t = float (input("Digite o tempo de viagem do trem:"))
print("Entradas:",v,"km/h e",t,"h")

if (t<1800):
	if (v<=0 or t<0):
		print("Entradas:",v,"km/h e",t,"h")	
		print("Dados invalidos")
		if (v*t == 200):
			print("Próxima parada: Bravos")
		elif (v*t == 400):
			print("Próxima parada: Castamere")
		elif(v*t == 600):
			print("Próxima parada: Doriath")
		elif(v*t == 750):
			print("Próxima parada: Edoras")
		elif(v*t == 1150):
			print("Próxima parada: Fangorn")
		elif(v*t == 1550):
			print("Próxima parada: Gondor")
		elif(v*t == 1800):
			print("Próxima parada: Hogsmead")
	else:
		print("Entradas:",v,"km/h e",t,"h")	
		print("Próxima parada: Hogsmead")
else: 
	print ()
		
		
		
		


	

	
	
