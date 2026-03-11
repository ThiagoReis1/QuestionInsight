# guilherme da silva almeida 
base_maior = float(input("comprimento da base maior:"))
base_menor = float(input("comprimento da base menor:"))
altura = float(input("altura:"))
metro = float(input("metro quadrado:"))
custo = altura*(base_maior+base_menor)/2 * metro

print(round(custo,2))