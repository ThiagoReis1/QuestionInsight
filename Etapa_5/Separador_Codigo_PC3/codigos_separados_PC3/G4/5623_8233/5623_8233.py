a=input("bolo ou salgado:")
v=int(input("quantidade de alimento:"))
c=int(input("cappuccinos:"))
if a.upper()=="B":
	t=(v*5)+(c*7.5)
else:
	t=(v*4)+(c*7.5)
print(round(t,2))