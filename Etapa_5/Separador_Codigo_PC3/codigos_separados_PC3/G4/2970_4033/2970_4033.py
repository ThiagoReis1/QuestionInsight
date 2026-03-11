from math import*
tempo=int(input(" quantos meses de investimento: "))
Qo=1500
Qf=(1042000)
x=Qf/Qo
i=((x**(1/tempo)))-1
print(round(i,5))

if(i<=0.01):
	print("Real")
else:
	print("Irreal")
