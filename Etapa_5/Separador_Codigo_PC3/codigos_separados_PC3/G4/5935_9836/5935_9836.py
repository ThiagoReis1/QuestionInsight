v1=float(input("peso da mercadoria:"))

v2= v1 * 43.21 + 25.00
icms= v2*(62/100)

total=v2+icms

print(round(total,2))