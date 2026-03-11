s = input("SETOR?: ").upper()

cont = 0 
while ( s != "X"):
	if ( s == "FT"):
		cont = cont + 1
	s = input("SETOR?: ").upper()
print(cont)