men=float(input("qual o valor da sua mensalidade:"))
qua=int(input("numero de crianca:"))

if qua==1:
	f1=(men/100)*90*qua
	print(round(f1,2))
elif qua==2:
	f2=(men/100)*70*qua
	print(round(f2,2))
elif qua >=3:
	f3=(men/100)*60*qua
	print(round(f3,2))