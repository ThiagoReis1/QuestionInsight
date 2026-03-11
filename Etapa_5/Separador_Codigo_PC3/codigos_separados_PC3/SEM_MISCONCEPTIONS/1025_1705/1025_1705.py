# Luiz Inácio
# Av01 - Ex.01


comprimento=float(input("Insira o comprimento do terreno:"))
largura=float(input("Insira a largura do terreno:"))
custo=float(input("Digite o valor do custo:"))

p=2*(comprimento+largura)

valor=p*custo

print(round(valor,2))