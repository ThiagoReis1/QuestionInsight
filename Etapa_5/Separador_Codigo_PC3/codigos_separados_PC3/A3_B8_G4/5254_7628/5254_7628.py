p=float(input())
c=int(input())

x=c=="1" or c=="2" or c=="3" or c=="4"

if c=="1":
	f=0.1
	venda=(p-p * 0.4)+p*(f/100)
	print(round(venda, 2))
elif c=="2":
	f=0.8
	venda=(p-p * 0.4)+p*(f/100)
	print(round(venda, 2))
elif c=="3":
	venda=(p-p*0.4)+p
	print(round(venda, 2))
elif c=="4":
	f=0.02
	venda=(p-p * 0.4)+p*(f/100)
	print(round(venda, 2))