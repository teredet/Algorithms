def сaesar_сiplet(menu, message, key):
    '''
    menu - 'E' if you want to encrypt and 'D' if you want to decrypt\n
    message - the string to encode or decore\n
    key - the number to shift\n
    \n
    The function encodes or decodes the message.\n
    Returns a string.\n
    
    '''
    
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    output = ''
    if menu == 'D':
        key *= -1
    for letter in message:
        if letter in alphabet:
            t = alphabet.find(letter)
            new_key = (t + key) % len(alphabet)
            output += alphabet[new_key]
        else:
            output += letter
    return output



if __name__ == "__main__":
    while True:
        print('Enter E to encrypt the message, D to decrypt and EXIT to exit')
        menu = input('>>> ').upper()
        if menu == 'EXIT':
            break
        elif menu == 'E' or menu == 'D':
            message = input('Enter the string: ').upper()
            key = int(input('Enter key: '))
            print('Result: ' + сaesar_сiplet(menu, message, key))
        else:
            continue