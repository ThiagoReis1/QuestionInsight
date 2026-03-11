c= float(input("combustivel: "))

if c<17.5:
	x= c+10.5
elif 17.5<c<35:
	x= c+14
elif 35<c<50:
	x= c+18.6
else:
	x= c+24.5
print(x)