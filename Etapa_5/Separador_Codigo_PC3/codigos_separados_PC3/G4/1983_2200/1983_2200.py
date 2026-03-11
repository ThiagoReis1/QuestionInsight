c = input().lower()
p = input().lower()
if((c == "asia") or (c == "america-do-sul")):
	if((c == "asia") and (p == "jordania")):
		print("AS RUÍNAS DE PETRA")
	elif((c == "asia") and (p == "india")):
		print("TAJ MAHAL")
	elif((c == "america-do-sul") and (p == "peru")):
		print("MACHU PICCHU")
	elif((c == "america-do-sul") and (p == "brasil")):
		print("CRISTO REDENTOR")
	else:
		print("INFORMACAO NAO IDENTIFICADA")
else:
	print("INFORMACAO NAO IDENTIFICADA")
