consumido = float(input("volume consumido por mes: "))
custo = float(0.37)
taxa = float(15.00)
icms = float(0.35)


valori = (consumido*custo+taxa)*icms
valor= valori + (consumido*custo+taxa)

print(round(valor, 2))


