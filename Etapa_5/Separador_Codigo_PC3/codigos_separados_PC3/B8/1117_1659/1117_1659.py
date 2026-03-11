preco = float(input("Digite o preço normal da entrada:"))
dia = int(input("Digite o dia da semana: "))
music = input("É dia de música ao vivo? ")

desconto = preco * 0.25
acres = 20.00

print("Entradas:", preco, ",", dia, ",", music)

if(music == "N"):
	if(dia == 1 or dia == 2 or dia == 4):
		valor_total = desconto
elif(music == "S"):
	valor_total = preco + acres
		
print("Valor a pagar: R$", round(valor_total, 2))