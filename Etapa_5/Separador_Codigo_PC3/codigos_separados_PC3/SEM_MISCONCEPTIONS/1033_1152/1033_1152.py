kilo = int(input("Kilos:"))
preco_fixo = 43.21*kilo
taxa_fixa = 25
icms = float(((preco_fixo+taxa_fixa)/100)*62)
total = preco_fixo+taxa_fixa+icms
resultado = round((total),1)
print(resultado)