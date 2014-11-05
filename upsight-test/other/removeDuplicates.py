
def remove_duplicates(values):
    output = []
    seen = set()
    for value in values:
    	if value not in seen:
    		output.append(value)
	    	seen.add(value)
    return output



def main():


	d1 = {'0':[0,1,2,0,2,1,5,6], '1':[4,5,6,6,5]}

	for item in d1:
		d1[item] = remove_duplicates(d1[item])

	print(d1.items())




if __name__ == '__main__':
    main()