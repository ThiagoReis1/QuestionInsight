peso= float(input("digite o peso do saco:"))
quantidade= float(input("digite a quantidade diaria de racao:"))
restante= peso - (quantidade * 5)
print(round(restante , 3))