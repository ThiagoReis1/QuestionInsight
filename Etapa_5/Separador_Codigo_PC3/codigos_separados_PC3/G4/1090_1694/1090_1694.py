#UNIVERSIDADE FEDERAL DO AMAZONAS
#ICC  ---- 30/06/2016
#AVALIAÇÃO 2 ----- exercicio 1
#MATHEUS GABRIEL PEREIRA DE CAMPOS

c1=float(input("Digite o valor da compra 1:"))
c2=float(input("Digite o valor da compra 2:"))
c3=float(input("Digite o valor da compra 3:"))
c4=float(input("Digite o valor da compra 4:"))
lim=float(input("Digite o valor do limite do cartao:"))

c11=round(c1,2)
c22=round(c2,2)
c33=round(c3,2)
c44=round(c4,2)
lim1=round(lim,2)
s=c11+c22+c33+c44
ss=round(s,2)
if lim1>=ss:
	print(ss)
	print("Sim")
else:
	print(ss)
	print("Nao")