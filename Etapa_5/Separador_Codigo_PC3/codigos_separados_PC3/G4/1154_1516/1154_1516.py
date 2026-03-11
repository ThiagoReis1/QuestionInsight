nci = float(input("Número de cópias iniciais do vírus HIV no sangue:"))
ir = float(input("Taxa de redução de vírus (em %):"))
cis = float(input("Número de cópias introduzidas a cada semana:"))

ri = ir/100

semana = 0
x = nci
while(x<=1000000):
	x = x - (x*ri)
	x = x + cis
	
	semana = semana + 1
	
		
print(semana)
	
	