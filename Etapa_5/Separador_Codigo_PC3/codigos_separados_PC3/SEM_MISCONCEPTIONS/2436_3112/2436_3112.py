peso = int(input("Peso do produto: "))
distancia = int(input("Distancia: "))

kg = 25	
km = 0.10
ICMS = 12

valor_peso=(peso*kg)
valor_distancia= (distancia*km)
preco = (valor_peso+valor_distancia)

valor_imposto = (preco*(ICMS/100))

print(valor_imposto+preco)

