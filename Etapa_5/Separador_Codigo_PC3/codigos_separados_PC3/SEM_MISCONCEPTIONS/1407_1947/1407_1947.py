vida=int(input("Qtd inicial de vida:"))
dado1=int(input("Valor sorteado do dado 1:"))
dado2=int(input("Valor sorteado do dado 2:"))
dado3=int(input("Valor sorteado do dado 3:"))
N= dado1 + dado2 + dado3
dano_causado = 10 * N
if N >= 3 and N <= 36:
	if vida - dano_causado > 0:
		print(vida - dano_causado)
		print("VIVO")
	else:
		print(0)
		print("MORTO")
	
		
		
	
		