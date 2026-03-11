DA = int(input(""))
DB = int(input(""))
jA=float(input(""))
jB=float(input(""))
DA = DA
DB = DB
t = 0

while (DA and DB and jA and jB >0 and DA>DB and jA<jB):
	DA = DA + (DA*(jA/100))
	DB = DB + (DB*(jB/100))
	t= t+1
print(t)


				 
