def fun1():
	print('5')

def fun2():
	print('6')

def main():
	
	new_list = [fun1, fun2]
	new_list[0]()


if __name__ == "__main__":
	main()

