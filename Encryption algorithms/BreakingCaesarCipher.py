

def FrequencyAnalysis():
    #Frequency analysis

    #alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    count = {}
    encrypted_string = input('>>> ').upper()

    for s in encrypted_string:
        if s in alphabet:
            if s in count:
                count[s]+=1
            else: 
                count[s] = 1 
            
    most_occured = 1
    last_found = ""
    for key in count:
        if count[key] > most_occured:
            last_found = key
            most_occured = count[key] 

    letter_number = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}
    key = int(letter_number[last_found]) - 5
    print('last_found: ',last_found, 'key: ',key)
    decrypted_string = ""

    for s in encrypted_string:
        if s in alphabet:
            decrypted_string += alphabet[alphabet.index(s)-key]
        else:
            decrypted_string += s
    print(decrypted_string)


def BruteForce():
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    def change_arrey():
        for i in range(number):
            arrey.append(arrey[0])
            arrey.remove(arrey[0])

    encrypted_string = input('>>> ').upper()
    
    print("""
    All posible variants of decoding: 
    """)

    for number in range(len(alphabet)):
        arrey = list(map(lambda x:x,alphabet))
        change_arrey()
        decrypted_string = ""
        for i in encrypted_string:
            if i == " ":
                decrypted_string += " "
            else:
                for j in range(len(alphabet)):
                    if i == arrey[j]:
                        decrypted_string += alphabet[j]
        print(f"[{str(number)}] {str(decrypted_string)}")

while True:
    print("""
        If you want use FrequencyAnalysis: 'FA'
        If you want use BruteForce: input 'BF'
    """)
    method_type = input()

    if method_type == 'FA':
        FrequencyAnalysis()
        break
    elif method_type == 'BF':
        BruteForce()
        break
    else:
        print('Invalid input')