
opcaoprincipal = 6.9
guarnicoes = 2.5
bebida = 3.0

qguarnicoes = float(input("quantidade da guarnicao: "))
bebidas = float(input("quantidade de bebidas: "))

custototal = (bebidas*bebida) + (qguarnicoes*guarnicoes) + opcaoprincipal
print(round(custototal, 2))
