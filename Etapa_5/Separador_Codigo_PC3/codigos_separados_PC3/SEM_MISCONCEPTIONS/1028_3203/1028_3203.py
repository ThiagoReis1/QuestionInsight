#x = volume
x = float(input())
preco = 0.37 * x + 15
#calculo do imposto
imp = float(preco * (35/100))
total = imp + preco
print(float(round(total,2)))