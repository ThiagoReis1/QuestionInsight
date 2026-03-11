#escolhas provincias

pais = input("Digite o pais: ").upper()
cidade = input ("Digite a cidade:").upper()

if(pais!="ITALIA") and (pais!="ESPANHA"):
	print("PROVINCIA NAO IDENTIFICADA")
	
elif(pais=="ITALIA") and (cidade=="ROMA"):
	print("LATINA")
elif(pais=="ITALIA") and (cidade=="FLORENCA"):
	print("SIENA")
elif(pais=="ESPANHA") and (cidade=="FRIGILIANA"):
	print("MALAGA")
elif(pais=="ESPANHA") and (cidade=="MADRID"):
	print("MADRID")
else: 
	print("PROVINCIA NAO IDENTIFICADA")