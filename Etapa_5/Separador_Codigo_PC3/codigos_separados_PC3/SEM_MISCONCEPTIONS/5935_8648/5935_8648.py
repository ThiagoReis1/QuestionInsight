#Peso da Mercadoria (Kg)
peso = float(input("Digite o valor: "))
#Cálculo mercadoria 
mercadoria = peso * (43.21) + 25.00
#Total
total = mercadoria * 0.62
total_2 = mercadoria + total
#resultado
print(round(total_2, 2))