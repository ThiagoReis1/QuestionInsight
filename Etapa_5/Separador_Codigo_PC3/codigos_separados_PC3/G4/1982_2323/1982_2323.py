C = input("País")
P = input("Cidade")

if C == "ITALIA" and P == "ROMA":
	R= "LATINA"
	print(R.upper())
elif C == "ITALIA" and P == "FLORENCA":
	R= "SIENA"
	print(R.upper())

elif C == "ESPANHA" and P == "FRIGILIANA":
	R= "MALAGA"
elif C == "ESPANHA" and P == "MADRID":
	R= "MADRID"
	print(R.upper())
else:
	print("PROVINCIA NAO IDENTIFICADA")
	
