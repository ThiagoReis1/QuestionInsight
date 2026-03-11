peso = float(input())
distancia = float(input())
kg = 25*peso
km = 0.10*distancia
icms = 0.12*kg + 0.12*km
preco = kg + km + icms
valordoimposto = preco * (icms/100)
print(float(round(preco, 2)))
