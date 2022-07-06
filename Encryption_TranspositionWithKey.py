import math

def encryptMessagewithKey(msg, key):
	#Blank string to store the encrypted text
	cipher = ""
	
	# track key indices
	k_indx = 0

	#Length of the key to find the size of the columns
	msg_len = float(len(msg))
	
	#converting the message into lists for handling 
	msg_lst = list(msg)
	
	#sorting the list of keys to identify the order of transposition
	key_lst = sorted(list(key))

	# calculate column of the matrix
	col = len(key)
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
		curr_idx = key.index(key_lst[k_indx])
		#adding the required alphabet from the matrix into the string called cipher
		cipher += ''.join([row[curr_idx] for row in matrix])
		#incrementing the index
		k_indx += 1
		#end for

	#print(cipher)
	return cipher
    
msg = input ("_____\nEnter the message to be encrypted: ")
key = input ("Enter the key for encryption: ")

#First transposition of the message
stage_1 = encryptMessagewithKey(msg, key)

#Displaying the intermediate stage
print(f"\nSingle Transpotion Cipher of message '{msg}' with key '{key}':\t", stage_1)

#Second transposition of the message i.e transposition of the cipher of stage 1
cipher = encryptMessagewithKey(stage_1, key)

#Printing the final cipher text
print(f"\nDouble transposed message '{msg}' with key '{key}' is\n\t'",cipher,"'")