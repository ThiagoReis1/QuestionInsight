from math import*
ang=eval(input("angulo: "))#angulo de entrada
k=int(input("n. termos: "))#numeros de termos
#contadores#
eq=0 #para a equacao
b=0 #(((esse e para debaixo))))colocamos 1 porque nao poder divisao por zero. tambem somaremos 
i=0 
cont=0#serve para o d cima
sinal=1 #sinal para mudar
#(((formula)))verificar depois
while(k>i):
	eq = eq + ((ang**i)/(factorial(2*i)))*sinal
	cont = cont + 1 
	b = b + 1
	sinal = - sinal
	i = i +1
	
print(round(eq,6))
	
