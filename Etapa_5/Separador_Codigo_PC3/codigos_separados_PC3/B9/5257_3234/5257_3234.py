p=float(input("preco de custo "))

if((p<=50)):
	total=p+1*p
	print(round(total,2))
elif((p>50) and (p<=100)):
	total= 1.5*p
	print(round(total,2))
elif((p>100) and(p<=500)):
	total=1.4*p
	print(round(total,2))
else:
	total=1.3*p

	print(round(total,2))