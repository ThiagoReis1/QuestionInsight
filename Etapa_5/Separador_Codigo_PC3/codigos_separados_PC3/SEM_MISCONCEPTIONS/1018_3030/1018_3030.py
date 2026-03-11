#lado do retângulo
cateto1 = float(input("Qual o tamanho de um lado?"))
cateto2 = float(input("Qual a medida do segundo lado?"))
Aplicacao = float(input("Qual valor da aplicacao po m2? "))

area = (cateto1 * cateto2) / 2

total = area * Aplicacao 

print(round(total, 2))