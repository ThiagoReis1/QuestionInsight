s = input("Informe a unidade academica: ").upper()
cont = 0

while (s != "X"):
	if (s == "FT"):
		cont += 1
	
	s = input("Informe a unidade academica: ").upper()
		
print(cont)