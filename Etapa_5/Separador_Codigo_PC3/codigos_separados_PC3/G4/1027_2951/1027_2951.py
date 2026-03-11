kwh=float(input())
conta=(kwh*0.43)+10.00
icms= 25/100*conta
vt=conta+icms
print(round(vt,2))