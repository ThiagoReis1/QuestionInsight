ambrosio = int(input("votos"))
demel = int(input("votos"))

tot = demel+ambrosio
vambrosio = float(ambrosio/tot)*100
vdemel = float(demel/tot)*100
if (vambrosio>vdemel):
	print("Ambrosio Rutra")
   print(round(vambrosio,2))
else:
   print("Demelza Olecram")
   print(round(vdemel,2))




