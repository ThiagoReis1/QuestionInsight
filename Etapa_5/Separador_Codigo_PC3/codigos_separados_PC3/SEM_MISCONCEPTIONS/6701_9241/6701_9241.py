produto= float(input("total dos produtos: "))

icms= produto+ 15.00
compra= icms+icms*(30/100)
print(round(compra, 2))