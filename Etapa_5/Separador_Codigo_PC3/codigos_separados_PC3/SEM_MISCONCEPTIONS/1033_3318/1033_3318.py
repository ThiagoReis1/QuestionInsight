taxacobrada = 25.0
valordoquilo = 43.21

mercadoria = float(input("peso da mercadoria: "))
custo = (mercadoria*valordoquilo)+taxacobrada
imposto = (custo*(62/100))
custototal = custo+imposto
print(round(custototal, 2))