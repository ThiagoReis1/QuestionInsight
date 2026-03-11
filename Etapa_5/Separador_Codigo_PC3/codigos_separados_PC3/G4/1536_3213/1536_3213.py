x = float(input("valor de x: "))
k = int(input("valor de k: "))

cont = 1
soma = x
vc = k
ex = 1

#if ((-1 < ac <= 1) and (vc > 0)):
while (cont < vc):
		soma = soma + (-1)*(-1)**(cont+1)*((x**(ex+1))/(ex+1))
		cont = cont + 1
		ex = ex + 1
		
print(round(soma,10))