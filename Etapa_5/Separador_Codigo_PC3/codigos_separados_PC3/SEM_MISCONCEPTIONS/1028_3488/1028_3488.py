#conta de agua + taxa
conta = 0.37  
taxa = 15

#icms
icms = 0.35

volume =  float(input("volume por mes: "))
var1 = volume * conta + taxa
valor = var1 * icms
total = var1 + valor
print(round(total, 2))