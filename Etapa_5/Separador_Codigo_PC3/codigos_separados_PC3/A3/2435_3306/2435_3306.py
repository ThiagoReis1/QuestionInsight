#produto sem desconto
produto= float(input("digite o valor do produto:"))
#produto com desconto
desconto= (40/100)*produto
#frete sobre o produto sem desconto
frete= (5/100)*produto
produtodesc= produto - (produto*(40/100))
print(round(produtodesc, 2))
print(round(frete, 2))