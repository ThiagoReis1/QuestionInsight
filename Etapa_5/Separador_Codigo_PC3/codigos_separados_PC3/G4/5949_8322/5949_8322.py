bs=input("B ou C: ")
q= int(input("Quantidade de bolos ou c: "))
c= int(input("Quantidade de cap: "))

if bs=="B":
	v= q*3+c*5.50
	print(v)
else:
	v=q*6+c*5.50
	print(v)
	