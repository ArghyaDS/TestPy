#Write a program which can compute the factorial of a given numbers. The results should be printed in a comma-separated sequence on a single line. Suppose the following input is supplied to the program:
#8
#Then, the output should be:
#40320


def fact(num):
	if (num!=0):
		return num*fact(num-1)
	else:
		return 1

x=int(input("Enter num: "))
print(fact(x))
	
