def crypt(input_string, keys):

    modified_string = ""

    for i in input_string:
        if i in keys:
            modified_string += keys[i]
        else:
            modified_string += i
    
    return modified_string


cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
if cryptMode not in ['E','D']:
	print("Error: mode is not Found!"); raise SystemExit

input_string = input('>>> ').upper()

symbolsAlpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbolsCrypt = ['!','@','#','$','%','^','&','*','(',')','-','=', '+','?',':',';','<','>','/','[',']','{','}','|','.',',','~']

if cryptMode == 'E':
    keys = dict(zip(symbolsAlpha,symbolsCrypt))
    print(f"Encrypted text: {crypt(input_string, keys)}")
elif cryptMode == 'D':
    keys = dict(zip(symbolsCrypt, symbolsAlpha))
    print(f"Decrypted text: {crypt(input_string, keys)}")




#symbolsAlpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#symbolsCrypt = ['!','@','#','$','%','^','&','*','(',')','-','=', '+','?',':',';','<','>','/','[',']','{','}','|','.',',','~']

#cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
#if cryptMode not in ['E','D']:
#	print("Error: mode is not Found!"); raise SystemExit
#startMessage = input("Write the message: ").upper()
#keys = dict(zip(symbolsAlpha,symbolsCrypt))

#def encryptDecrypt(mode, message, final = ""):
#	if mode == 'E':
#		for symbol in message:
#			if symbol in keys: final += keys[symbol]
#	else:
#		for symbol in message:
#			for key in keys:
#				if symbol == keys[key]: final += key
#	return final
#print("Final message:",encryptDecrypt(cryptMode, startMessage))