r = input("Campeao ou Vice-Campeao? ")
n = input("numero de vezes? ")

if(r=="Campeao") and (n=="11-vezes"):
	print("real madrid".upper())
elif(r=="Campeao") and (n=="05-vezes"):
	print("barcelona".upper())
elif(r=="Vice-Campeao") and (n=="01-vez"):
	print("chelsea".upper())
elif(r=="Vice-Campeao") and (n=="04-vezes"):
	print("milan".upper())
else:
	print("time de futebol nao identificado".upper())