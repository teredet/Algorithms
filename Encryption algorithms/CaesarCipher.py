alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

while True:
    print('Enter E to encrypt the message, D to decrypt and EXIT to exit')
    menu = input('>>> ').upper()
    if menu == 'EXIT':
        break
    elif not (menu == 'E' or menu == 'D'):
        continue
    output = ''
    message = input('Enter the string: ').upper()
    key = int(input('Enter key: '))
    if menu == 'D':
        key *= -1
    for letter in message:
        if letter in alphabet:
            t = alphabet.find(letter)
            new_key = (t + key) % len(alphabet)
            output += alphabet[new_key]
        else:
            output += letter
    print('Результат: ' + output)