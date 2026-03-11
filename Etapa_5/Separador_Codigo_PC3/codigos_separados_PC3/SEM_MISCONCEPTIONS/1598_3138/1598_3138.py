from numpy import*
vector_price=array(eval(input("")))

i=0
new=0

while(i<size(vector_price)):
	if(vector_price[i]>80.00):
		new=new+vector_price[i]- 5
	else:
		new=new+vector_price[i]
	i=i+1
print(round(new,2))
