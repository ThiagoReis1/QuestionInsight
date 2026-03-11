tempo=float(input("digite o tempo de chamadas em minutos:"))
#plano de telefonia por minuto consumido
custo= (0.28)*tempo
#valor fixo
fixo= 23.00
#total
total= custo+fixo
#icms
icms=(total)*(31/100)
#custo total
custototal= total+ icms
print(round(custototal, 2))
