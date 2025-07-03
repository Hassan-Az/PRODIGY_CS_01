import string

def encrypt(textMSG, sh):
    # taking out the index nymbers of characters
    msgIndex = []
    for char in textMSG:
        if char != " ":
            if char in alphabet:
                index = int(alphabet.index(char))
                msgIndex.append(index)
        else:
            msgIndex.append(88)

    # shifting the character
    for i in range(len(msgIndex)):
        if msgIndex[i] != 88:
            msgIndex[i] += sh
            if msgIndex[i] > 25:
                msgIndex[i] -= 26
        else:
            continue
    
    # converting number into characters
    msg = ""
    for i in msgIndex:
        if i != 88:
            msg = msg + alphabet[i]
        else:
            msg = msg + " "
    return msg

def decrypt(encMSG, sh):   
    # taking out the index nymbers of characters
    msgIndex = []
    for char in encMSG:
        if char != " ":
            if char in alphabet:
                index = int(alphabet.index(char))
                msgIndex.append(index)
        else:
            msgIndex.append(88)

    # shifting the character
    for i in range(len(msgIndex)):
        if msgIndex[i] != 88:
            msgIndex[i] -= sh
            if msgIndex[i] < 0:
                msgIndex[i] += 26
        else:
            continue
    
    # converting number into characters
    msg = ""
    for i in msgIndex:
        if i != 88:
            msg = msg + alphabet[i]
        else:
            msg = msg + " "
    return msg

alphabet = list(string.ascii_lowercase)

print("""
 _____                              _____ _       _               
/  __ \                            /  __ (_)     | |              
| /  \/ __ _  ___  ___  __ _ _ __  | /  \/_ _ __ | |__   ___ _ __ 
| |    / _` |/ _ \/ __|/ _` | '__| | |   | | '_ \| '_ \ / _ \ '__|
| \__/\ (_| |  __/\__ \ (_| | |    | \__/\ | |_) | | | |  __/ |   
 \____/\__,_|\___||___/\__,_|_|     \____/_| .__/|_| |_|\___|_|   
                                           | |                    
                                           |_|                                                                                                                                                     
""")

encrypted_msg = ""
decrypted_msg = ""
option = 9
while option != 0:
    print("""__________________________________
1. encrypt with Caesar cipher
2. decrypt with Caesar cipher
0. exit          
""")
    option = int(input("Select option: "))

    if option == 1:
        msg = input('Enter your text: ')
        shift = int(input("Enter number of shifts to perform: "))
        encrypted_msg = encrypt(msg, shift)
        print("\nencrypted message is ", encrypted_msg)
    if option == 2:
        msg = input('Enter your text: ')
        shift = int(input("Enter number of shifts to perform: "))        
        decrypted_msg = decrypt(msg, shift)
        print("\ndecrypted message is ", decrypted_msg)