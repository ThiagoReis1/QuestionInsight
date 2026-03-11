from numpy import*
peso=array(eval(input("peso: ")))
altura=array(eval(input("altura: ")))
t=0
w=size(peso)
imc=zeros(w,dtype=float)
while(t<=size(peso)):
	for i in peso:
		x=i
	for j in altura:
		y=j
	imc[t]=array(eval(round(x/(y**2)),2))
for k in imc:
	if(k<17):
		situacao="MUITO ABAIXO DO PESO"
	elif(k>=17 and k<=18.49):
		situacao="ABAIXO DO PESO"
	elif(k>=18.5 and k<=24.99):
		situacao="PESO NORMAL"
	elif(k>=25 and k<=29.99):
		situacao="ACIMA DO PESO"
	elif(k>=30 and k<=34.99):
		situacao="OBESIDADE"
	elif(k>=35 and k<=39.99):
		situacao="OBESIDADE SEVERA"
	elif(k>=40):
		situacao="OBESIDADE MORBIDA"
print(imc)
print("O MAIOR IMC DA TURMA EH:",max(imc),situacao)