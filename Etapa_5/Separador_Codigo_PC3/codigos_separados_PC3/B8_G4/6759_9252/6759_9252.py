# faça seu código aqui!
dist = int(input("distancia: "))
tax = 50

if(dist < 10):
	tax += 5.5
elif(dist == 10):
	tax += 7.75
elif(dist > 10):
	tax += 10

print(tax)	
