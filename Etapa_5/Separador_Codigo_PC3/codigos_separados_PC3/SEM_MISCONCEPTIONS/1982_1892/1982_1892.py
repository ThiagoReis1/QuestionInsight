pais = input("Digite o pais: ").upper()
cidade = input("Digite a cidade:").upper()
if(pais == "ITALIA" and cidade == "ROMA"):
	resultado = "LATINA"
	print(resultado)
elif(pais == "ITALIA" and cidade =="FLORENCA"):
	resultado = "SIENA"
	print(resultado)
elif(pais == "ESPANHA" and cidade == "FRIGILIANA"):
	resultado ="MALAGA"
	print(resultado)
elif(pais == "ESPANHA" and cidade== "MADRID"):
	resultado = "MADRID"
	print(resultado)
else:
	resultado = "PROVINCIA NAO IDENTIFICADA"
	print(resultado)
	