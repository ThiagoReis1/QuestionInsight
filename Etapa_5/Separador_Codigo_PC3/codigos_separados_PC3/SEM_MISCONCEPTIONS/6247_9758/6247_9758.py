monit = input("unidade academica:").upper()

cont = 0

while (monit != "X"):
	if (monit == "FT"):
		cont = cont + 1
	monit = input("unidade academica:").upper()
		
		
print(cont)