a = int(input("valor da casa: "))
b = int(input("valor inicial: "))
c = int(input("deposito: "))
d = float(input("juros: "))
soma = b
t = 0
if(a<=0)or(b<=0)or(c<=0)or(d<=0):
	print("Dados incorretos")
else:
	while(soma<a):
		ren = soma*(d/100)
		soma = soma + ren + c
		t= t+1
	print(t)
		
		