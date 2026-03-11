pc = float(input("preco de custo: "))
if(pc<=50):
	x = pc*2
	print(round(x,2))
elif(pc>50) and (pc<100):
	y = pc/2 + pc
	print(round(y,2))
elif(pc>100) and (pc=500):
	z = pc*0.4 + pc
	print(round(z,2))
elif(pc>=500):
	a = pc*0.3 + pc
	print(round(a,2))