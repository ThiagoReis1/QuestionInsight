preco_area = float(input("Informe o preço da aera por metro quadrado :"))
area_privativa = float(input("Informe a aera privativa :"))
area_comum = float(input("Informe a area comum :"))
area_garagem = float(input("Informe a area da garagem :"))

preco_total = ((area_privativa+area_comum+area_garagem) * preco_area)
print(preco_total)