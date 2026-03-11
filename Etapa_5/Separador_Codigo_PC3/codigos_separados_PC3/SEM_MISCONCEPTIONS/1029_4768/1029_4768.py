consumo = (float(input("quantos minutos?")))
tfm = 23.00
vm = 0.28
icms = (consumo*vm+tfm)/100*31
sub_t = (consumo*vm+tfm)
print(round(icms+sub_t, 2))