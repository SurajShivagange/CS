def Shift(text,s):
	result = ""

	# traverse text
	for i in range(len(text)):
		char = text[i]

		# Encrypt uppercase characters
		if (char.isupper()):
			result += chr((ord(char) - s-65) % 26 + 65)

		# Encrypt lowercase characters
		else:
			result += chr((ord(char) - s - 97) % 26 + 97)

	return result
    
    
#reading from file

plain_text = open("path\Filename.txt", "r+")

text = plain_text.read()

text = input("Enter the text to be Encrypted")


#______________________________________
#CAESAR CIPHER

#key size 
s = 3
#print ("Shift : " + str(s))

Cipher = Decryption.Shift(text,s)

print("Cipher: ", Cipher)



#______________________________________
#Shift Cipher with user defined key from 1 to 25 
#key size
s = int (input("Enter the key size from 1 to 25."))

Cipher = Decryption.Shift(text, s)

print("Cipher: ", Cipher)




#______________________________________
#ROT 13
s = 13

Cipher = Decryption.Shift(text, s)

print("Cipher: ", Cipher)
