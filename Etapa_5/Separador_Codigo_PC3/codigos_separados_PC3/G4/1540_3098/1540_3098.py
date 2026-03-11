from math import*
ang=eval(input("angulo: "))#angulo de entrada
k=int(input("n. termos: "))#numero de termos
#contadores#
eq=0 #para a equaçao
b=0 #(((esse é para debaixo))))colocamos 1 porque nao pode divisao por zero.tambem somaremos 1 no final
i=0#(vai servir para o d cima)
cont=0#serve para contar o numero
sinal=1 #sinal para mudar
#(((formula)))verificar depois
while(k>=0 and ang>0 and cont<k ):
	eq = eq +((ang**i)/(factorial(2*b)))*sinal
	cont = cont + 1
	b = b + 1
	sinal = - sinal
	i = i + 1
print(round(eq,6))
