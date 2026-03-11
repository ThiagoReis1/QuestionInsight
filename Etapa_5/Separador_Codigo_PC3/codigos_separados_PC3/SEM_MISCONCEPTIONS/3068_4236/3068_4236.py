nome = input("nome? (CIMITARRA/KATANA/SABRE)").upper()
d = int(input("num: "))
n1 = int(input("valor: "))
n2 = int(input("valor: "))
S = n1 + n2
SA = "SABRE"
KA = "KATANA"
CI= "CIMITARRA"

if ((1>n1>10) or (1>n2>10) or (d<0) or (nome"" != SA) or (nome != KA) or (nome!= CI)) :
	print("Entrada invalida")
elif (nome == "CIMITARRA"):
	print(2 * S + 2 * d)
elif (nome == "KATANA"):
	print(2 * S + d)
elif (nome == "SABRE"):
	print(S + 2 * d)

