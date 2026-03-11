ano = int(input(" "))
pais = input("B/E:").upper()

ano_2= 2023-ano

if ano_2 >= 18 and pais== "B":
   print("sim")
   total= ano_2-18
   print(total)
	
elif ano_2 < 18 and pais == "B":
   print("nao")	
   total= 18-ano_2
   print(total)
	
elif ano_2 >=16 and pais== "E":
   print("sim")
   total= ano_2 -16
	
else: 
   print("nao")
   total= 16- ano_2
   print(total)