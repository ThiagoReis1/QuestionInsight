a = float(input("comprimento da aresta "))
custo = float(input("custo de aplicacao "))


area = 2*(a**2)*(2**0.5+1)
total = (area*custo)

print(round(total,2))