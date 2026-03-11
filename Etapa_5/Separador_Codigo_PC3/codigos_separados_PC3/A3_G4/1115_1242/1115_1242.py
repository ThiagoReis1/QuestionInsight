sa = float(input("Digite o salario:")) 
co = int(input("Digite o codigo:"))
print("Entradas: R$", sa ,"e codigo", co)
r = ((sa+0.80+10.20) or (sa+0.65+10.20) or (sa+17.80+17.20) or (sa+0.55+14.20))
if co == "101":
	r = sa+0.80+10.120
	print("Novo salario: R$", r)
elif co == "102":
	r = sa+0.65+10.20
	print("Novo salario: R$", r)
elif co == "103":
	r = sa+17.80+17.20
	print("Novo salario: R$", r)
elif co == "104":
	r = sa+0.55+10.20
	print("Novo salario: R$", r)
else:
	print("Entradas: R$", r,"e codigo", co)