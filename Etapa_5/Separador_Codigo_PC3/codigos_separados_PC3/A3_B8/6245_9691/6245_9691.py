p = input("S (satisfeitos), I (insatisfeitos) , N (neutro) ou X para encerrar o programa:  ").upper()
contador = 0
while p!=p:
	if p == "S":
		contador += 1
		p = input("S (satisfeito), I (insatis), N (neutro): ")
	elif p == "I":
		p = int(input("S (satisfeito), I(insatisfeito), N (neutro) ou "))
	 

