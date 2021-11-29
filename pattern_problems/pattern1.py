# note:the inner loop will be  running the same as 'n'
# the outer loop can be the number of times the n value





# Pattern problem 1
# def pattern1():
# 	for i in range (1,n) :
# 		for j in range(i) :
			
# 			print ('*',end = ' ')
# 		print('\r')
# n = 5
# pattern1()
 



#  # Pattern problem 2
# def pattern2():
# 	for row in range (0, n):
# 		for col in range (0,n-row):
# 			print ('*', end =" ")
# 		print('\r')
# n = 4
# pattern2()



# Pattern problem 3

# def pattern3():
# 	for row in range(1, n):
# 		for col in range(1, row+1):
# 			# col<=row
# 			print(col, end=' ')
# 		print('\r')
# n= 6
# pattern3()

# Pattern problem 4

# def pattern4():
# 	for row in range(0,n*2-1):
# 		if row<n:
# 			for col in range(0,row+1):
# 				print("*",end="")
# 			print('\r')
# 		else:
# 			for col in range(0,2*n-1-row):
# 				print("*",end="")
# 			print('\r')
# n=5
# pattern4()

# Pattern problem 5
def pattern5():
	for row in range (0,n*2-1):
		if row<=n :
			for col in range(1,6):
				for col in range(n-col,n-col+1):
					print(' ', end="")
				print("*", end="")
			print('\r')
		else:
			space = int (row-n)
			for col in range(0,2*n-1-row):
				for col in space:
					print(' ')
				print("*", end="")
			print('\r')
n=5
pattern5()

#     *
#    * *
#   * * *
#  * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *

# We need the outer loop running nine times
# 	for row in range (1,n*2):
# 	Were n =5

# We need the column running in range of 5 times in every row

# 	for col in range(0,5):
	
# If n-row>5
#  Print space






	