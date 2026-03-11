kwh = float(input("qtda:"))
kwhm = 0.43
taxa = 10 

soma = kwh * kwhm + taxa

icms = soma * 0.25

soma2 = icms + soma

print(round(soma2, 2))


