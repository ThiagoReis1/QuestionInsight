p = input(":").upper()
c = input(":").upper()
if((p=="ITALIA") or (p=="ESPANHA")) and ((c=="ROMA") or(c=="FLORENCA")or(c=="MADRID")or(c=="FRIGILIANA")):
	if (p=="ITALIA") and (c=="ROMA"):
		print("LATINA")
	elif(p=="ITALIA") and (c=="FLORENCA"):
		print("SIENA")
	elif(p=="ESPANHA") and (c=="FRIGILIANA"):
		print("MALAGA")
	elif(p=="ESPANHA") and (c=="MADRID"):
		print("MADRID")
else:
	print("PROVINCIA NAO IDENTIFICADA")
	