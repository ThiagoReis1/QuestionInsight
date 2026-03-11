ba= int(input("valor a: "))
bb= int(input("valor b: "))
ja= float(input("juros a: "))
jb= float(input("juros b: "))
d=0
while(ba> 0 and bb >0 and ja> 0 and jb> 0and ba>bb and ja<jb):
	ba= ba+(ba*(ja/100))
	bb= bb+(bb*(jb/100))
	d=d+1
	print(round(d,2))
	if(ba> 0 and bb >0 and ja> 0 and jb> 0and ba>bb and ja<jb):
		print(round(d,2))
	elif(bb<ba and ja>jb):
		print("Dados incorretos"