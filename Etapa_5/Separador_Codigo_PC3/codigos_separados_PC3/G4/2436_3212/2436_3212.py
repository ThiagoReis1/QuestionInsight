peso=float(input("peso do produto:"))
d=float(input("distancia entre o ponto de origem e destino:"))

x=peso*25

y=d*0.10

preco=x+y

imposto=(preco*12)/100

#calculando o valor total
vt=preco+imposto

print(round(vt,2))
