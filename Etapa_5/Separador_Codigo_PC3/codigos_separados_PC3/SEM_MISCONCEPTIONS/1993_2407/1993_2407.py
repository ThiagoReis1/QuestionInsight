am = input("Nome do aminoácido: ").lower()

if (am == "cisteina"):
	cisteina = (3*12.011)+(7*1.00794)+(1*14.0067)+(2*15.9994)+(1*32.066)
	print(round(cisteina, 2))
elif (am == "isoleucina"):
	isoleucina = (6*12.011)+(13*1.00794)+(1*14.0067)+(2*15.9994)
	print(round(isoleucina, 2))
elif (am == "metionina"):
	metionina =	(5*12.011)+(11*1.00794)+(1*14.0067)+(2*15.9994)+(1*32.066)
	print(round(metionina, 2))
else: 
	print("Entrada:", am)
	print("Dado Invalido")