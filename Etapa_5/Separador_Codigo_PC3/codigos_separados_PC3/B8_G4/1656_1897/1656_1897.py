from numpy import*

x = input("String: ").split(',')
BE = 0
ES = 0
FR = 0
IT = 0
PT = 0

for i in x:
	if(i.upper()=="BE"):
		BE=BE+1
	elif(i.upper()=="ES"):
		ES=ES+1
	elif(i.upper()=="FR"):
		FR=FR+1
	elif(i.upper()=="IT"):
		IT=IT+1
	elif(i.upper()=="PT"):
		PT=PT+1
	x=array([BE,ES,FR,IT,PT])
print(max(x))
print(x)