def fact(num):
	if (num!=0):
		return num*fact(num-1)
	else:
		return 1

x=int(input("Enter num: "))
print(fact(x))
	
