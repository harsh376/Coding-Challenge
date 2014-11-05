#To be able to read csv formated files, we will first have to import the
#csv module.
import csv
import collections

d1 = collections.defaultdict(list)

def remove_duplicates(values):
    output = []
    seen = set()
    for value in values:
    	if value not in seen:
    		output.append(value)
	    	seen.add(value)
    return output


def getDay(seconds):
	t1 = (int)(seconds) - 1277942400
	t2 = (int)(t1/86400)
	return t2


def printMatrix(Matrix, len):
	for i in range(0,len-1):
		for j in range(0,len):
			print(Matrix[i][j], end='\t')
		print('\n')



def writeToCsv(Matrix, len):
	l1 = []
	for i in range(0,len-1):
		l2 = []
		for j in range(0,len):
			l2.append(Matrix[i][j])
			# print(Matrix[i][j], end='\t')
		# print('\n')
		l1.append(l2)

	with open('test_out_code.csv', 'w', newline='') as fp:
		a = csv.writer(fp, delimiter=',')

		a.writerows(l1)



def populateMatrix(Matrix, MatrixLen, list1, list1_len):
	i=0
	l = list1_len	
	while i<l:
		count = 1
		j=i+1
		while j<l and list1[j]==list1[j-1]+1:
			count = count+1
			j = j+1

		row = list1[i]
		Matrix[row][count]+=1
		i = j


def createMatrix(len1):
	Matrix = [[0 for x in range(len1)] for x in range(len1)] 
	for i in range(0,len1):
		Matrix[i][0] = i+1

	return Matrix


def main():
	with open('test_input.csv', newline='') as f:
		reader = csv.reader(f)

		len1 = 15
		Matrix = createMatrix(len1)

		# create a dict having schema: {userId1:[0,1,2,2,..4], userId2:[3,4,..14]}
		for row in reader:
			timeInSec =  int(row[0])
			userId = int(row[1])
			day = getDay(timeInSec)		# gets the relative day from 7/1/2010

			d1[userId].append(day)		# append the day to the list associated with a userId

		# remove duplicates from the lists associated with each userId
		for item in d1:
			d1[item] = remove_duplicates(d1[item])
			l = len(d1[item])

			populateMatrix(Matrix, len1, d1[item], l)	# populate the matrix for each of the lists


		# printMatrix(Matrix, len1)
		writeToCsv(Matrix, len1)


if __name__ == '__main__':
    main()