#Emanuel Batany
#Lab 01 - AV-01
aresta=float(input("Digite o valor da aresta: "))
preco=float(input("Digite o preco do metro quadrado: "))
a=float(3*aresta**2*3**0.5)
area=a/2.0
valor_final=area*preco
print(round(valor_final,2))