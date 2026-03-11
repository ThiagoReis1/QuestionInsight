abre = float(input())
fecha = float(input())

variacao = fecha - abre

variacao = (variacao * 100) / abre

print(round(variacao,1))  

