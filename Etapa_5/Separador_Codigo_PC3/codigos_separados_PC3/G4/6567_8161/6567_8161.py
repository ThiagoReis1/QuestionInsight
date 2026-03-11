# faça seu código aqui!
v = int(input("banda larga:"))
if(v<50):
	x= 4.50 + 60
elif(v==50):
	x = 5.50 + 60
else:
	x = 6.50 + 60
print("total=",round(x, 2))
