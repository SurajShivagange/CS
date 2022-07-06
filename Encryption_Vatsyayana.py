#Vatsyayana Cipher
def Vatsyayana(text, CIPHER_DICT):
    #Creatibg a list to store the CIPHER TEXT
    textC = []

    #using for loop for traverseing through the plain text and convert to Cipher text
    for i in range(len(text)):

        #replacing the message with substitutions
        textC = ''
        for i in text:
            textC = textC + str(CIPHER_DICT.get(i))

    #print("|"+textC+"|")
    return str(textC)
    
    
plain_text = open("path\Filename.txt", "r+")

text = plain_text.read()

text = input("Enter the text to be Encrypted")

#Vatsyayana Cipher dictionary
CIPHER_DICT = {'e': 'u', 'b': 's', 'k': 'x', 'u': 'q', 'y': 'c', 'm': 'w', 'o': 'y', 'g': 'f', 'a': 'm', 'x': 'j', 'l': 'n', 's': 'o', 'r': 'g', 'i': 'i', 'j': 'z', 'c': 'k', 'f': 'p', ' ': 'b', 'q': 'r', 'z': 'e', 'p': 'v', 'v': 'l', 'h': 'h', 'd': 'd', 'n': 'a', 't': ' ', 'w': 't'}

Cipher = Encryption.Vatsyayana(text, CIPHER_DICT)

print("VATSYAYANA Cipher: ", Cipher)