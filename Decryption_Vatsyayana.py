def Vatsyayana(text, CIPHER_DICT):

	#Creating lists of keys and values of the dictionary for retreaval of the the message
	CDKlist = list(CIPHER_DICT.keys())
	CDVlist = list(CIPHER_DICT.values())



	#Creatibg a list to store the CIPHER TEXT
	#textP = []

	#using for loop for traverseing through the plain text and convert to Cipher text
	for i in range(len(text)):

		#replacing the Cipher text with the dictionary values
		textP = ''
		for i in text:

			#finding the index of the value in the list
			index = CDVlist.index(i)
			#print(CDKlist.index(i))
			#print(CDVlist[char])

			#getting the key for the index of the value
			textP = textP + str( CDKlist[index] )

	#print("|"+textC+"|")
	return str(textP)



plain_text = open("path\Filename.txt", "r+")

text = plain_text.read()

text = input("Enter the text to be Encrypted")

#Vatsyayana Cipher dictionary
CIPHER_DICT = {'e': 'u', 'b': 's', 'k': 'x', 'u': 'q', 'y': 'c', 'm': 'w', 'o': 'y', 'g': 'f', 'a': 'm', 'x': 'j', 'l': 'n', 's': 'o', 'r': 'g', 'i': 'i', 'j': 'z', 'c': 'k', 'f': 'p', ' ': 'b', 'q': 'r', 'z': 'e', 'p': 'v', 'v': 'l', 'h': 'h', 'd': 'd', 'n': 'a', 't': ' ', 'w': 't'}


Cipher = Decryption.Vatsyayana(text, CIPHER_DICT)

print(f"Plain Text: {Cipher}")