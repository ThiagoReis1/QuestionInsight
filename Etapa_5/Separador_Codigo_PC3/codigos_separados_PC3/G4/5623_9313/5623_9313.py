opcao=input("Digite B para bolo ou S pra salgado: ").upper()
q=int(input("Quantidade fatias de bolo/salgado:"))
qcap=int(input("Quantidade de caputinos: "))

if opcao=="B":
	v=q*5+qcap*7.50
	print(round(v,2))
else:
	v2=q*4+qcap*7.50
	print(round(v2,2))