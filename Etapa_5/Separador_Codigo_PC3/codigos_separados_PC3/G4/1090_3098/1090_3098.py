lim=float(input("qual o limite do cartao?  "))
c1=float(input("qual o valor da compra 1?   "))
c2=float(input("qual o valor da compra 2?   "))
c3=float(input("qual o valor da compra 3?   "))
c4=float(input("qual o valor da compra 4?   "))
total=c1+c2+c3+c4
if (total<=lim):
	print(round(total,2))
	print("Dentro do limite")
else:
	print(round(total,2))
	print("Estourou o limite")
