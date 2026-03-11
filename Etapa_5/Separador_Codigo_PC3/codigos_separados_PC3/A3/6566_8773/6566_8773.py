qtdp= int(input())
valor= 30 
total=0
if qtdp<10: 
	total= valor+3.25
elif qtdp==10:
	total= valor+4.50
else:
	total= valor+6.00
print("total=",round(total, 2))
