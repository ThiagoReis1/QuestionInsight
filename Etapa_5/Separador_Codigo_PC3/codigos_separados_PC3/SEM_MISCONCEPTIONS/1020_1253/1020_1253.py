# avaliaçao 01
# Leonardo Fernandes Auzier
# 16 - 6 - 2016

base_maior= float(input("o valor da base maior: "))
base_menor= float(input("o valor da base menor: "))
altura= float(input("o valor da altura: "))
custo_m2= float(input("custo por metro quadrado: "))

area=altura*(base_maior+base_menor)/2
custo_total=area*custo_m2 

print(round(custo_total,2))

