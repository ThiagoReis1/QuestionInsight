comida = input("digite (L) para lanche e (S) para salgado: ")
qtde = int(input("qtde de ambos: "))
q_refri = int(input("digite a qtde de refri: "))

lanche = 5.00
salgado = 3.50
refrigerante = 4.00

if comida == "L":
	v = (qtde  * 5.00) + (q_refri * 4.00)
	print(round(v, 2))
else: 
	v2 = (qtde * 3.50) + (q_refri * 4.00)
	print(round(v2, 2))
   
