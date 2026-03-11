from numpy import*
tri = array(eval(input("Trincas:")))
z = zeros(10, dtype = int)



p = 0
while(p<10):
	for i in range(0,size(tri),3):
			if(tri[i]  ==  p  ):
				if(tri[i+1] == tri[i] ):
					if(tri[i+2] == tri[i]):
						z[p]=z[p]+1
	p += 1
		
print(z)

		

					
			
			
		
	
		