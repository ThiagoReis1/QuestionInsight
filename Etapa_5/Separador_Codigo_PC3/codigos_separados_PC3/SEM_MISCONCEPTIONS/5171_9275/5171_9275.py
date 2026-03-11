# peso da ração

peso_racao =float(input("digite o kg: "))

#quantidade necessaria

quantidade_racao  = float(input("digite a quantidade: "))

soma=(quantidade_racao*peso_racao)-7


restara = soma%7

print(round(restara, 2 ))