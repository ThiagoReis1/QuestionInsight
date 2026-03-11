from numpy import*
ven = array(eval(input("vendas: ")))
som = 0
i = 0
for i in range(size(ven)):
	som = som + ven[i]
	if(som>=55):
		som = 0 
print(som)