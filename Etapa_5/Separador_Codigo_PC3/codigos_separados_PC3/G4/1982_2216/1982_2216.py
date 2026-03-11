P=input("nome do pais")
C=input("nome da cidade")
p=(P).upper()
c=(C).upper()
if((p =="ITALIA")and(c =="ROMA")):
	print("LATINA")
elif((p =="ITALIA") and (c =="FLORENCA")):
	print("SIENA")
elif((p =="ESPANHA")and(c =="FRIGILIANA")):
	print("MALAGA")
elif((p =="ESPANHA")and(c =="MADRID")):
	print("MADRID")
else:
	print("PROVINCIA NAO IDENTIFICADA")