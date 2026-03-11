preco_da_area= float(input())
area_privada=float(input())
area_comum = float(input())
area_garagem =float(input())

preco=((area_privada+area_comum+area_garagem)*preco_da_area)
print(round(preco,2))