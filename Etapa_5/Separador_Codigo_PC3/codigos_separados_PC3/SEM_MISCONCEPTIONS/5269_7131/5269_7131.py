num= int(input("digite o numero:  "))
total=0
md3=0
while num!=0:
	total=total+1
	if num%3==0:
		md3=md3+1
	num= int(input("digite o numero:  "))	
print(total)
porcentagem=(md3*100)/total
print(round(porcentagem, 2))

	