from numpy import*

vetor = array(eval(input("Digite a face do dado: ")))

i = 0 
total = 0

while i < size(vetor) :
	
	if vetor[i] == 1 :
		
		total = total + 10
	
	elif vetor[i] == 2 :
		
		total = total + 5
		
	elif vetor[i] == 3 :
		
		total = total + 10
		
	elif vetor[i] == 4 :
		
		total = total + 5
		
	elif vetor[i] == 5 :
		
		total = total + 10
		
	elif vetor[i] == 6:
		
		total = total + 5
	
	i = i + 1
	
print(total)