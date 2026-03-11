a=float(input())
c1=float(0.28*a)
consumo= c1+ float(23.00)
icms= (consumo*100)%31
consumo_total= consumo + icms
print(round(consumo_total,2))
