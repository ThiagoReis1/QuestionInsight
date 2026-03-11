x = float(input())
d = float(input())
preco = (x*25.00)+(d*0.10)
imposto = preco*(12/100)
total = preco+imposto

print(round(total,2))