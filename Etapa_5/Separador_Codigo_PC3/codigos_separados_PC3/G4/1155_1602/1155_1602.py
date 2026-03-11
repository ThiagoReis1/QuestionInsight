vs=float(input("viros no sangue:"))
nl=float(input("numero de leucocitos:"))
mv=float(input("taxa de mutiplicação do viros:"))
md=float(input("taxa de mutiplicaçãodos leucocitos:"))
i=1

while(nl*2>vs):
	nl=nl*md
	vs=vs*mv
	i=i+1
	print(nl)