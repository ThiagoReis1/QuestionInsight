from math import*
vm=float(input("qual o valor da mensalidade: "))
n=int(input("qual  o numero: "))


if(n==1):
	vt=((vm*n)*10/100)
	t=(vm*n)-vt
	print(round(t,2))
elif(n==2):
	vt1=((vm*n)*30)/100
	t1=(vm*n)-vt1
	print(round(t1,2))
else:
	vt2=((vm*n)*40)/100
	t2=(vm*n)-vt2
	print(round(t2,2))