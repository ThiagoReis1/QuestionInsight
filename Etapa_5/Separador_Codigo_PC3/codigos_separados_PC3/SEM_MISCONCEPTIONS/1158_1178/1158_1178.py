pit = int(input("Populaçao inicial: "))
taxac = float(input("Taxa anual: "))
num= int(input("Roubo: "))
ano1= pit+pit*0.05

anos = ((pit+taxac-num)-13642)
while(anos<num):
print("9")
if (anos == 108):
	print("m")
else:
	print("extincao")