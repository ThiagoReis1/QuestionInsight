#Entrada de dados
a= float(input("Qual o comprimento da aresta da fazenda, em metros?"))
b= float(input("Qual o custo de aplicacao do fertilizante por metro quadrado?"))

#Calculo interno
c= (2**0.5) + 1
d= a**2
area= 2*d*c
custo= b* area

#saida de dados
print(round(custo,2))