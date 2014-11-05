

len = 14
# Creates a list containing 5 lists initialized to 0
Matrix = [[0 for x in range(len)] for x in range(len)] 

for i in range(0,len):
	for j in range(0,len):
		print(Matrix[i][j], end='\t')
	print('\n')
