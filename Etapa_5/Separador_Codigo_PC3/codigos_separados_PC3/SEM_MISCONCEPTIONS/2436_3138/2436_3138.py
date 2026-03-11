peso=int(input("quanto q pesa o jaburu"))
distancia=int(input("e pro Acre e,bisho?"))

kg=25.00
km=0.10
ICMS=12

valor_peso=(peso*kg)
valor_distancia=(distancia*km)
preco=(valor_peso+valor_distancia)

Valor_imposto = (preco*(ICMS/100))

print(Valor_imposto+preco)



