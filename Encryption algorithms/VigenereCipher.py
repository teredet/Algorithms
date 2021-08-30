def vigenere_cipher(mode, message, key):
	'''
    mode - 'E' if you want to encrypt and 'D' if you want to decrypt\n
    message - the string to encode or decore\n
    key - codeword\n
    \n
    The function encodes or decodes the message.\n
    Returns a string.\n
	
	'''
	key *= len(message) // len(key) + 1  
	finalMessage = ""
	for i, j in enumerate(message):
		if mode == 'E':
			temp = ord(j) + ord(key[i])
		else:
			temp = ord(j) - ord(key[i])
		finalMessage += chr(temp % 26 + ord('A'))
	return finalMessage


if __name__ == "__main__":
    while True:
        print('Enter E to encrypt the message, D to decrypt and EXIT to exit')
        cryptMode = input('>>> ').upper()

        if cryptMode == 'EXIT':
            break
        elif cryptMode in ['E','D']:
            message = input('Enter the string: ').upper()
            key = input('Enter key: ').upper()
            print("Final message: ",vigenere_cipher(cryptMode, message, key))
        else:
            continue
