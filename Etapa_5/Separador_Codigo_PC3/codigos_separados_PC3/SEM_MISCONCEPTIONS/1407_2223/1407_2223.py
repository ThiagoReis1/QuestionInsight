quan_inicial = int(input("Informe a quantidade de vida do personagem: "))
Dado1 = int(input("Informe o valor do D1: "))
Dado2 = int(input("Informe o valor do D2: "))
Dado3 = int(input("Informe o valor do D3: "))

dados = Dado1+Dado2+Dado3
dano_reb = 10*dados

if(quan_inicial - dano_reb > 0):
	vida = quan_inicial - dano_reb
	mensagem = "vivo"
	
else:
	vida = 0
	mensagem = "morto"

print(vida)
print(mensagem.upper())