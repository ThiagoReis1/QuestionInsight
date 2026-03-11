#pede a entrada da largura em m
l= float(input(""))
c=float(input(""))
custo=float(input(""))
#perimetro do terreno
perimetro= 2 * (c+l)
#valor total da construção
custo_total=  custo * perimetro

print(round(custo_total, 2))