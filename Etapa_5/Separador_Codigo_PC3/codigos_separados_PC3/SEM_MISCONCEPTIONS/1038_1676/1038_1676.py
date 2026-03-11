quantia = float(input("Qual a quantia que o cliente entrega?"))
taxa_fixa = 8.50
iene = 0.03
valor = round((quantia - taxa_fixa) / iene,2)
print(valor)