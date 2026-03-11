# Luiz Inácio
# Av.01 - Ex.02 16/06/2016


kwh=float(input("Digite o seu consumo de energia:"))

valor=(kwh*0.43)+10
icms=0.25*valor
total=valor+icms

print(round(total,2))