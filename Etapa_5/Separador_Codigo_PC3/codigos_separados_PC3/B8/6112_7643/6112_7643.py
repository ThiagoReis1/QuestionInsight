combu = float(input("Quantidade de combustivel: "))

if (combu < 17.5):
	c = combu + 10.5
elif(combu > 17.5) and (combu <= 35.0):
	c = combu + 14.0
elif(combu > 35.0) and (combu <= 50.0):
	c = combu + 18.6
elif(combu > 50.0):
	c = combu + 24.5
print(round(c,1))