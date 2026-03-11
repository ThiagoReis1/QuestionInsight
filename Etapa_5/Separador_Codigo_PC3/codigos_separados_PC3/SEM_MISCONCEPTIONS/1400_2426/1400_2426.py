tipo = input()
rodadas = int(input())
D1 = int(input())
D2 = int(input())
#constrição
dado1 = (D1 + D2)
dano1 = dado1 + 1
#Pólen venenoso
dano2 = (D1 * D2)
#condição
if(tipo == 'constricao'):
	a = (rodadas * dano1)
	print(a)
else:
	print(dano2)