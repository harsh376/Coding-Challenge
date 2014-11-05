

def getDay(seconds):
	t1 = seconds - 1277942400
	t2 = (int)(t1/86400)

	return t2


def main():

	# day = getDay(1277942454)
	# day = getDay(1278962058)
	day = getDay(1279151997)
	print("day = " + str(day))


if __name__ == '__main__':
    main()