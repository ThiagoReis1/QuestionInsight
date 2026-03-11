Peso =float(input("Peso da encomenda:"))
Distancia =float(input("Distancia a viajar:"))
valor_kilo =25
valor_km =0.10
icms =12/100
preco =(Peso*valor_kilo)+(Distancia*valor_km)
valor_icms = preco*icms
total =valor_icms+preco
print(round(total,2))
