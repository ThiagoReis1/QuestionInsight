peso = int(input("peso:  "))
distancia = int(input("distancia:  "))
kilo = 25.00 
km =  0.10  
preco = (peso * kilo) + (distancia * km)
icms = preco * (12/100)
total =preco + icms
print(float(round(total, 2)))