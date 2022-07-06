import math

def encryptMessageWithoutKey(msg, size):
	
	#Blank string to store the encrypted text
	cipher = ""
	
	# track key indices
	k_indx = 0

	#Length of the key to find the size of the columns
	msg_len = float(len(msg))
	
	#converting the message into lists for handling 
	msg_lst = list(msg)
	
	#sorting the list of keys to identify the order of transposition
	key_lst = [item for item in range(0, size)]
	# calculate column of the matrix
	col = size
	#can take user input for the number of columns if key is not required

	# calculate maximum row of the matrix
	row = int(math.ceil(msg_len / col))

	# add the padding character '_' in the empty cell of the matrix
	fill_null = int((row * col) - msg_len)
	msg_lst.extend('_' * fill_null)

	# create Matrix and insert message and padding characters row-wise
	matrix = [msg_lst[i: i + col] for i in range(0, len(msg_lst), col)]

	# read matrix column-wise using key
	for _ in range(col):
		#current index
		curr_idx = key_lst.index(k_indx)
		#adding the required alphabet from the matrix into the string called cipher
		cipher += ''.join([row[curr_idx] for row in matrix])
		#incrementing the index
		k_indx += 1
		#end for

	#print(cipher)
	return cipher


	
msg = input ("_____\nEnter the message to be encrypted: ")
size = int(input ("Enter the column: "))

#First transposition of the message
cipher = encryptMessageWithoutKey(msg, size)

#Displaying the intermediate stage
print(f"\nTranspotion Cipher of message '{msg}' with key size '{size}':\t", cipher)

#Second transposition of the message
cipher2 = encryptMessageWithoutKey(cipher, size)

#Displaying the final stage
print(f"\nDouble Transpotion Cipher of message '{msg}' with key size '{size}':\t", cipher2)