nb = int(input("numero de bacterias"))
qt = int(input("horas"))
soma=0

while(qt!=0):
	qt = qt-1
	soma=soma+nb*0.15	
	
print(soma)
	