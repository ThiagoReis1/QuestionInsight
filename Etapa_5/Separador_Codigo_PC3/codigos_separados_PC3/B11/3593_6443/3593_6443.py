pontos = 200
vet=eval(input())


for i in vet:
	if i==1:
		pontos= pontos / 2
	if i==2:
		pontos= pontos *3
	if i==3:
		pontos= pontos / 2
	if i==4:
		pontos= pontos * 3
	if i==5:
		pontos= pontos / 2
	if i==6:
		pontos= pontos *3
	
	
print(round(pontos,2))