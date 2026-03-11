pv=int(input("pontos de vida: "))
d1=int(input("valor 1 :"))
d2=int(input("valor 2 :"))
d3=int(input("valor 3 :"))
N=(d1)+(d2)+(d3)
danos=10*N

if(pv>0):
	print(pv-danos)
	mensagem=VIVO
	
else:
	pv=0
	mensagem=MORTO
	
print(pv)
print(mensagem)