comida = input ("digite (B) para fatia de bolo e (S) para  salgado: ")
qtde = int (input("qtde de ambos: "))
q_cappuccino = int(input("digite a qtde de cappuccino:"))

fatiadebolo = 5.00
salgado = 4.00
cappuccino = 7.50

if comida == "B":
	v = (qtde * 5.00) + (q_cappuccino * 7.50)
	print (round(v, 2))

else:
	v = (qtde * 4.00) + (q_cappuccino * 7.50)
	print (round(v, 2))