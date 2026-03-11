m=1
consumo=0.37*m**3
esgoto=15
conta=consumo+esgoto
icms=35/100*(consumo+esgoto)
print(round(icms+conta,2))