a = int(input())

x = a%5
y = a%3

if( x == 0 and y !=0):
	print("Tac")
elif( y == 0 and x != 0):
	print("Tic")
elif( x == 0 and y == 0):
	print("TicTac")
else:
	print(a)
