dep=int(input("deposito inicial: "))
np=int(input("numero de meses: "))
juros=0.01
np=12
while(dep>=0):
	np=np*juros
	dep=np+dep
while(dep==0):
	np=np*juros
	dep=np+dep
print(round(np,2))