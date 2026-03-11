var = input("digite a variavel: ")
q_lanche = int(input("quantos lanches: "))
q_refri =int(input("quantos refri: "))
lanche= 5
salgado = 3.5
refri = 4
if var == "L":
	mensagem = (5*q_lanche)+(4*q_refri)
if var == "S":
	mensagem = (3.5*q_lanche)+(4*q_refri)
print(round(mensagem , 2))
	