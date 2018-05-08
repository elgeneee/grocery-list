def entry():
	print('Welcome to our login page')
	print('Press Y to start and N to quit')
	yn = input('==>')
	while True:
		if yn.lower() == 'y':
			test()
			break
		elif yn.lower() == 'n':
			break
		else:
			print('Only accept Y/N')
			print('Try Again?')
			try_again = input('Press Y to try again and N to quit:')
		if try_again.lower() == 'y':
			entry()
		elif try_again.lower() == 'n':
			break
		else:
			break

def test():
    lists = []
    print('Hit space and click ENTER to quit adding to list.')
    while True:
        items = input('Items to buy:')
        lists.append(items)
        if items == " ":
            lists.remove(" ")
            break
    print('You have: {}.'.format(', '.join (lists)))
    print('Enjoy Shopping!')

entry()
