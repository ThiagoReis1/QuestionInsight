from numpy import *
p=array(eval( input("peso dos alunos:")))
a=array(eval( input("altura dos alunos:")))
v=array(zeros(size(a),dtype=float))

for x in range(size(a)):	
	icm=p[x]/a[x]**2
	v[x]=icm
print(v)
print("O MAIOR ICM DA TURMA EH: ", round(max(v),2))
if max(v)<17:
		print("MUITO ABAIXO DO PESO")
elif 17<=max(v)<=18.49:
		print("ABAIXO DO PESO")
elif 18.50<= max(v)<=24.99:
		print("PESO NORMAL")
elif 25<=max(v)<=29.99:
		print("ACIMA DO PESO")
elif 30<=max(v)<=34.99:
		print("OBESIDADE")
elif 30<=max(v)<=39.99:
		print("OBESIDADE SEVERA")
else:
		print("OBESIDADE MORBIDA")