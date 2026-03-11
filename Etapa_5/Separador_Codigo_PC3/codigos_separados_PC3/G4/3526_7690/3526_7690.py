x = float(input("numero inteiro maior que 0: "))
k = int(input("quantidade de termos: "))

ex = 1 
div = 1
ack = 0
soma = 0
while(ack < k ):
	son = (x**ex)/div
	ex = ex + 2
	div = div + 2
	ack = ack + 1
	soma = son + soma
print(round(soma,7))
	