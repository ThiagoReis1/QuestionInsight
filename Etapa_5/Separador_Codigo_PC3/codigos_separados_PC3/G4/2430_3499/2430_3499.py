a = float(input("qual o valor total da compra a prazo?"))
b = float(input("quantas parcelas ao mes?"))
x = 300/100

juros = (a*x*b)/100
m = a + juros

print(round(m, 2))
