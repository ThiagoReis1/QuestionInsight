var1 = input("B ou S: ")
var_salgado = int(input("digite quantidade de salgado: "))
var_cappu = int(input("digite quantidade de cappuccino: "))

preco_salgado = (var_salgado * 4.00)
preco_cappu = (var_cappu * 7.50)

total = (preco_salgado + preco_cappu)

print(round(total, 2))