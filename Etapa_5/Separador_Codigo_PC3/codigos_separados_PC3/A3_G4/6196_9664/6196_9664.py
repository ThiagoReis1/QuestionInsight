at= float(input("al: "))
tx= float (input("tx: "))

alt= 1.5
ta= 0.02
c= 0
ano= 0

while at < alt:
	at= at + tx
	alt= alt + ta
	ano= ano + 1
	
print(ano)
	
	