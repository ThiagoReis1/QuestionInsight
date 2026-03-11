v=input("time vecedor ou empate:").upper()
cont=0
while (v!="X"):
	if(v=="A"):
		cont=cont+1
		v=input("time verncedor ou empate:").upper()
	else:
		v=input("time vencedor ou empate:").upper()
print(cont)