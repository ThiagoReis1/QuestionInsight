a = input("Digite o nome do aminoacido: ")

o = 15.9994
c = 12.011
n = 14.0067
s = 32.0067
h = 1.00794

cis = round(((c * 3) + (h * 7) + n + (o * 2) + s), 2)
iso = round(((c * 6) + (h * 13) + n + (o *2)), 2)
met = round(((c * 5) + (h * 11) + n + (o * 2) + s), 2)

if(a.lower() == "cisteina" or a.lower() == "isoleucina" or a.lower() == "metionina"):
	if(a.lower() == "cisteina"):
		print(cis)
	elif(a.lower() == "isoleucina"):
		print(iso)
	elif(a.lower() == "metionina"):
		print(met)
	else:
		print("Entrada:",a)
		print("Dado Invalido")
	
	