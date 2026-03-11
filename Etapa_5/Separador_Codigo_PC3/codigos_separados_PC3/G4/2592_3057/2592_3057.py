from numpy import* 
ubs = array(eval(input("Indices de vacinacao: ")))

x = 0
  
for i in range(size(ubs)): 	
	if (ubs[i] >= ubs[0]/100): 
		x = x+1
print(x)


	