#Bremer Augusto de Brito Cuesta - 21452666
#Lab de codificacao
#Avaliacao 1
#16/06/2016

a = float(input())
b = float(input())
c = float(input())
s = (a+b+c)
custo_construcao = float(input("qual o custo de construcao da cerca?")) 
perimetro_terreno = a+b+c
custo_total = custo_construcao * perimetro_terreno
print(round(custo_total,2))
