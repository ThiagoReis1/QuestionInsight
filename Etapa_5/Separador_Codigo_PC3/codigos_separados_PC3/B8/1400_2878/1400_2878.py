tipo_de_ataque = input("Digite o tipo de ataque- (constricao) ou (polen): ")
numero_de_rodadas = int(input("Digite o numero de rodadas: "))
D1 = int(input("Digite o primeiro valor de D1: "))
D2 = int(input("Digite o segundo valor de D2: "))

if(tipo_de_ataque.lower() == "constricao"):
   N = 2*(D1 + D2)
   dano_cons = N + 1
   dt = dano_cons + numero_de_rodadas
   print(dt)

elif(tipo_de_ataque.lower() == "polen"):
	dano_polen  = D1 * D2
	print(dano_polen)