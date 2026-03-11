t= float(input("tempo de voo?"))
x= 200
if(t<=200):
	custo= 5000/100*t
else:
	custo= 8000+100
	
print(round(custo,2))