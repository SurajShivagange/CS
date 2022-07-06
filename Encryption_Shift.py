def Shift(text,s):
	result = ""

	# traverse text
	for i in range(len(text)):
		char = text[i]

		# Encrypt uppercase characters
		if (char.isupper()):
			result += chr((ord(char) + s-65) % 26 + 65)

		# Encrypt lowercase characters
		else:
			result += chr((ord(char) + s - 97) % 26 + 97)

	return result
    
    
plain_text = open("path\Filename.txt", "r+")

text = plain_text.read()

text = input("Enter the text to be Encrypted")

    
#______________________________
#Caesar Cipher
#key size 
s = 3
#print ("Shift : " + str(s))

Cipher = Encryption.Shift(text,s)

print("Caesar Cipher: ", Cipher)


#______________________________
#Shift Cipher 
#key size
s = int (input("Enter the key size from 1 to 25."))

Cipher = Encryption.Shift(text, s)

print("Shift Cipher: ", Cipher)


#______________________________
#ROT13
#key size
s = 13

Cipher = Encryption.Shift(text, s)

print("ROt 13 Cipher: ", Cipher)
    
