

def isPresentInList(list1, list2):
	for item in list2:
		if item in list1:
			print(str(item)+" : present")
		else:
			print(str(item)+" : absent")

def main():
	list1 = [1,2,3,5,7,8,9]
	list2 = [4,2,6,8,12]
	isPresentInList(list1, list2)


if __name__ == '__main__':
    main()