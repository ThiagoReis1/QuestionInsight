na=input("nome do aminoacido: ").lower()
if(not(na == "aspartato" or na == "fenilalanina" or na == "tirosina")):
	print("Entrada: ",na)
	print("Dado Invalido")
elif(na == "aspartato"):
	pm = (12.011* 4)+(1.0079*6)+(14.0067*1)+(15.9994* 4)
	print(round(pm,2))
elif(na == "fenilalanina"):
	pm1 = (12.011*9)+(1.0079* 11)+(15.9994*2)+(32.066*1)
	print(round(pm1,2))
elif(na == "tirosina"):
	pm2 = (12.011* 9)+ (1.0079*11)+(14.0067*1)+(15.9994*3)
	print(round(pm2,2))