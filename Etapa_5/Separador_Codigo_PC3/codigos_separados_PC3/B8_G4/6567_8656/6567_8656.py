# faça seu código aqui!
vel=int(input("velocidade: "))

if(vel < 50):
	x= 60 + 4.50
	
elif( vel == 50):
	x= 60 + 5.50
	
elif(vel > 50):
	x= 60 + 6.50
	
print("total=", round(x,2))