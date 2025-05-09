for i in range(5):
	for j in range(7):
		if i+j==7 or i-j==1:
			print("*",end=" ")
		elif i==0 and(j==1 or j==2 or j==4 or j==5):
			print("*",end=" ")
		elif i==1 and j==3:
			print("*",end=" ")
		else:
			print(" ",end=" ")
	print()		
		
	