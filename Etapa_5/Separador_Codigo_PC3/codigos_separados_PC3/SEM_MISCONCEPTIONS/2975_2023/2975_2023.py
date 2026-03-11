# Restaurante do Zezinho.

q_suco = int(input("digite a quantidade de suco:"))
q_salgado = int(input("digite a quantidade de salgado:"))
valor = float(input("digite o valor:"))

v_lanche = ((q_suco*3)+(q_salgado*3.50))

if (valor>=v_lanche):
	mens = "Sim"
	
else:
	mens = "Nao"
	
print(round(v_lanche,2))
print(mens)