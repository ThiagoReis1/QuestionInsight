ataque = input("(maritimo/terrestre): ")
q = float(input("quantidade de baforadas: "))


if(ataque == "maritimo"):
	m = "Viserion"
	s = q * 40
	
else:	
	m = "Drogon"
	s = q * 150
	
print(str(m))
print(int(s))