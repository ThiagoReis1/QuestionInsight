x= int(input("digite o valor:"))
x1= x//1000000
rest_x1= x % 1000000
x2= rest_x1//100000
rest_x2 = rest_x1 %100000
x3= rest_x2 // 10000
rest_x3 = rest_x2 % 10000
x4= rest_x3 // 1000
rest_x4 = rest_x3 % 1000
x5= rest_x4 // 100
rest_x5 = rest_x4 % 100
x6= rest_x5 // 10
rest_x6 = rest_x5 % 10
e= ((x1*100)+(x2*10)+(x3*1));
z= ((x4*100)+(x5*10)+(x6*1));
if((e + z)**2 >=x):
	print("X atende a propriedade")
else:
	print(z)
