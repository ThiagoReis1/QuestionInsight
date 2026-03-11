aresta= float(input("insira a aresta"))
custo= float(input("digite o custo"))
area= 2 * (aresta**2) *((2**0.5)+1)
custototal= custo * area
print(round(custototal, 2))