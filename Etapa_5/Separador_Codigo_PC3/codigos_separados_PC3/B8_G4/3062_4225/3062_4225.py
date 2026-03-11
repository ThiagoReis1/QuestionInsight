po = int(input( ))
a = input( )
d = int(input( ))
e = 100
m = 30
n = 50
if(d<1)or(d>10)or(a!="ESPADA")and(a!="MARRETA")and(a!="MACHADO"):
	print("Entrada invalida")
elif(a=="ESPADA")and(po>=100):
	dano = d*10
	print(dano)
elif(a=="MACHADO")and(po>=30):
	dano = d+3
	print(dano)
elif(a=="MARRETA")and(po>=50):
	dano = d+5
	print(dano)
elif(po<e)or(po<m)or(po<n):
	print("PO insuficiente")