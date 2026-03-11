time = input("")
vez = input("")

if( (time == "Campeao") and (vez =="06-vezes")):
	print("corinthians".upper())	
elif(	(time == "Campeao") and (vez =="03-vezes")):
	print("santos".upper())
elif( (time == "Vice-Campeao") and (vez =="01-vez")):
	print("flamengo".upper())
elif( (time == "Vice-Campeao") and (vez =="06-vezes")):
	print("internacional".upper())
else:
	print("time de futebol nao identificado".upper())	
