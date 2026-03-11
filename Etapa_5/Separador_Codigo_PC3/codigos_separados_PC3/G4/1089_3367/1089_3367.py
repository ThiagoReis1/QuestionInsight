vc1=float(input("valor da compra1"))
vc2=float(input("valor da compra2"))
vc3=float(input("valor da compra3"))
lc=float(input("limete do cartao"))
vt=vc1+vc2+vc3
if (vt<=lc):
	mensagem= "Nao ultrapassou"
else:
	mensagem= "Ultrapassou"
print(round(vt, 2))
print(mensagem)