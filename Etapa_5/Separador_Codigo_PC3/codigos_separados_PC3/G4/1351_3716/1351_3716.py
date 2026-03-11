est= float(input("estimativa de macas por metro quadrado: "))
are= float(input("comprimento da aresta: "))

area= 3 * ((3 * are**2)**0.5)/2

quant= est*area

print(int(quant))