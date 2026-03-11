#ravalona compra produtos em site estrangeiro, o alibaba
#as encomendas sao retidas pelos correios e pega um imposto de 81% sobre o valor da encomenda
#mais taxa fixa de 12 reais

a=float(input("qual o valor da encomenda?"))

b=0.81*a
c=12.0
valortotal=(a)+(b)+(c)
print(round(valortotal,2))