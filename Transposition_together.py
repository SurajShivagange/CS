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



# Decryption
def decryptMessage(stage_1):
	msg = ""

	# track key indices
	k_indx = 0

	# track msg indices
	msg_indx = 0
	msg_len = float(len(stage_1))
	msg_lst = list(stage_1)

	# calculate column of the matrix
	col = len(key)
	
	# calculate maximum row of the matrix
	row = int(math.ceil(msg_len / col))

	# convert key into list and sort
	# alphabetically so we can access
	# each character by its alphabetical position.
	key_lst = sorted(list(key))

	# create an empty matrix to
	# store deciphered message
	dec_cipher = []
	for _ in range(row):
		dec_cipher += [[None] * col]

	# Arrange the matrix column wise according
	# to permutation order by adding into new matrix
	for _ in range(col):
		curr_idx = key.index(key_lst[k_indx])

		for j in range(row):
			dec_cipher[j][curr_idx] = msg_lst[msg_indx]
			msg_indx += 1
		k_indx += 1

	# convert decrypted msg matrix into a string
	try:
		msg = ''.join(sum(dec_cipher, []))
	except TypeError:
		raise TypeError("This program cannot",
						"handle repeating words.")

	null_count = msg.count('_')

	if null_count > 0:
		return msg[: -null_count]

	return msg

print("Decryped Message: {}".format(decryptMessage(stage_1)))