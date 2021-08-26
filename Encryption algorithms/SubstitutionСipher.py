def SubstitutionСipher(message, keys):
    '''
    message - the string to encode or decore\n
    keys - Dictionary with character ratios. When encoding: sign - key. When decoded: key - sign.\n
    \n
    The function encodes or decodes the message.\n
    Returns a string.\n    
    '''

    modified_string = ""

    for i in message:
        if i in keys:
            modified_string += keys[i]
        else:
            modified_string += i
    
    return modified_string


if __name__ == "__main__":
    while True:
        print('Enter E to encrypt the message, D to decrypt and EXIT to exit')
        cryptMode = input('>>> ').upper()

        if cryptMode == 'EXIT':
            break
        elif cryptMode in ['E','D']:
            message = input('Enter the string: ').upper()

            symbolsAlpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            symbolsCrypt = ['!','@','#','$','%','^','&','*','(',')','-','=', '+','?',':',';','<','>','/','[',']','{','}','|','.',',','~']

            if cryptMode == 'E':
                keys = dict(zip(symbolsAlpha,symbolsCrypt))
                print(f"Encrypted text: {SubstitutionСipher(message, keys)}")
            elif cryptMode == 'D':
                keys = dict(zip(symbolsCrypt, symbolsAlpha))
                print(f"Decrypted text: {SubstitutionСipher(message, keys)}")
        else:
            continue