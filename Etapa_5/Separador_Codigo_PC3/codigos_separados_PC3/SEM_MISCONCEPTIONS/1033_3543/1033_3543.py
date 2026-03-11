peso = float(input("peso em kg"))
frete = (peso*43.21)+25
imposto = frete*62/100
vt = frete+imposto
print(round(vt,2))