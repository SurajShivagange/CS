import rsa


#method to generate the private and public keys. The keys will be a tuple of public and private keys, and 
# then write the keys into files.
def generateKeys():
    (publicKey, privateKey) = rsa.newkeys(1024)
    with open('keys/publicKey.pem', 'wb') as p:
        p.write(publicKey.save_pkcs1('PEM'))
    with open('keys/privateKey.pem', 'wb') as p:
        p.write(privateKey.save_pkcs1('PEM'))


#code snippet below opens the files that we created above, and return both the private and public keys
def loadKeys():
    with open('keys/publicKey.pem', 'rb') as p:
        publicKey = rsa.PublicKey.load_pkcs1(p.read())
    with open('keys/privateKey.pem', 'rb') as p:
        privateKey = rsa.PrivateKey.load_pkcs1(p.read())
    return privateKey, publicKey


# encode the message in ASCII and give it the key    
def encrypt(message, key):
    return rsa.encrypt(message.encode('ascii'), key)

#Calling the methods
generateKeys()
publicKey, privateKey =loadKeys()

message = input('Write your message here:')
ciphertext = encrypt(message, publicKey)



print(f'Cipher text: {ciphertext}')

