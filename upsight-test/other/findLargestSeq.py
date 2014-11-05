


def printMatrix(Matrix, len):
	for i in range(0,len):
		for j in range(0,len):
			print(Matrix[i][j], end='\t')
		print('\n')


def populateMatrix(Matrix, MatrixLen, list1, list1_len):
	i=0
	l = list1_len
	while i<l:
		print(list1[i], end=" : ")
		count = 1
		j=i+1
		while j<l and list1[j]==list1[j-1]+1:
			# print(j, end=",")
			count = count+1
			j = j+1

		row = list1[i]
		Matrix[row][count]+=1
		i = j
		print(count)



def main():
	len1 = 15
	Matrix = [[0 for x in range(len1)] for x in range(len1)]
	# printMatrix(Matrix, len1)

	list1 = [0,1,2,3,5,6,8,9,10,14,15]
	l = len(list1)

	populateMatrix(Matrix, len1, list1, l)


	printMatrix(Matrix, len1)



if __name__ == '__main__':
    main()
