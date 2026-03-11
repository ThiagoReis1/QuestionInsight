preco = 2.86
servico = 50.00
gasol = float(input("quantidade de litros:"))

x=(((preco * gasol)+ (servico) )*34/100)

valor=((preco * gasol) + (servico) + x)
print(round(valor,2))


