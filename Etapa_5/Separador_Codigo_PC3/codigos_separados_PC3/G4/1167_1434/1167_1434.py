#Gabriel Felipe
#28/07/16

N = int(input("qual o numero N de termos"))

cont = 1
div = 1
sinal = -1
S = 0

while(cont <= N):
	S = S - sinal * (cont**2)/(7+div)
	sinal = - sinal
	cont = cont + 1	
	div = div + 2
print(round(S,11))	