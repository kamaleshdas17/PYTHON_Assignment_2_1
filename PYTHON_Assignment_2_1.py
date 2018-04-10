##Write a program which accepts a sequence of comma-separated numbers from console
##and generate a list.

input_lst = input('Please enter a sequence of comma-separated numbers: ')

output_lst=[]

for i in input_lst.split(','):
	output_lst.append(int(i))
	
print ('Newly generated list is: ',output_lst)
	
