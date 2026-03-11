mercadoria=float(input("mercadoria: "))
peso=43.21
taxa=25.00
icms=0.62
total=(mercadoria*peso+taxa)
imposto=total*icms
print(round(total+imposto,2))