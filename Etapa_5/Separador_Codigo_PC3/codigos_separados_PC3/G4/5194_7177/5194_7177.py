c=input("")
x=float(input("x;"))

if(c=="B"):
	b="Chunin"
	y=x-(x*0.15)
else:
	b="Jounin"
	y=x-(x*0.22)
print("Classe:", b)
print(round(y,2))