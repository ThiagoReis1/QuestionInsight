tipoAtaque = input()
numRodadas = int(input())
dado1 = int(input())
dado2 = int(input())

#Constrição
if(tipoAtaque == 'constricao'):
	N = dado1 + dado2
	pts_deVida = numRodadas * (N + 1)
	print(pts_deVida)
#polen
else:
   N = dado1*dado2
   print(N)