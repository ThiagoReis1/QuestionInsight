tipo=(input("L ou P"))
lanche=int(input())
pizza=int(input())
if tipo=="L":
	conta=(lanche*6.00)+(pizza*3.00)
	print(round(conta,2))
else:
	conta=(lanche*4.50)+(pizza*3.00)
	print(conta)
