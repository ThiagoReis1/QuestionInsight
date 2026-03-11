precoc = float(input("qual o preco custo?"))
if(precoc <= 50):
	x = precoc 
	l = x
	vf = x + l
	vfr = round(vf, 2)
	print(vfr)
elif(precoc >= 50.01) and (precoc <= 100):
	x = precoc / 2	
	vf = x + precoc
	vfr = round(vf, 2)
	print(vfr)
elif(precoc >= 100.01) and (precoc <= 500):
	x = precoc * 0.4
	vf = x + precoc
	vfr = round(vf, 2)
	print(vfr)
elif(precoc > 500):
	x =  precoc * 0.3
	vf = x + precoc
	vfr = round(vf,2)
	print(vfr)