lambaris=int(input("qual o numero de lambaris: "))
tucunares=int(input("qual o numero de tucunares: "))
taxalambaris=float(input("taxa mensal de lambaris: "))
taxatucunares=float(input("taxa mensal de tucunares: "))
meses=1
i=1
while (lambaris==tucunares):
	lambaris = lambaris*taxalambaris + lambaris
	tucunares = tucunares*taxatucunares + tucunares 
	meses=meses+1
print(meses)
	
	