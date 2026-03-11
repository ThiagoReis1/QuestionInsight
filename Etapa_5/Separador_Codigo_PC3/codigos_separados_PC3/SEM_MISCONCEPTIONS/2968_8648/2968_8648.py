#Variávei de entrada:
LS = input("Digite (L) para lanche e (S) para salgado: ")
quantidade_LS = int(input("Digite a quantidade de lanches ou salgados: "))
quantidade_R = int(input("Digite a quantidade de refrigerante: "))
#Cálculo e Condições: 
if LS == "L":
 valor_total = (5 * quantidade_LS) + (4 * quantidade_R)
 print(round(valor_total, 2))
if LS == "S":
 valor_total = (3.50 * quantidade_LS) + (4 * quantidade_R)
 print(round(valor_total, 2))