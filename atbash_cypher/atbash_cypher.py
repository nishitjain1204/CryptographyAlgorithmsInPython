letter_table = {'A' : 'Z', 'B' : 'Y', 'C' : 'X', 'D' : 'W', 'E' : 'V',     # Letter to table to refer to for corresponding letter
        'F' : 'U', 'G' : 'T', 'H' : 'S', 'I' : 'R', 'J' : 'Q', 
        'K' : 'P', 'L' : 'O', 'M' : 'N', 'N' : 'M', 'O' : 'L', 
        'P' : 'K', 'Q' : 'J', 'R' : 'I', 'S' : 'H', 'T' : 'G', 
        'U' : 'F', 'V' : 'E', 'W' : 'D', 'X' : 'C', 'Y' : 'B', 'Z' : 'A'} 

def atbash(message):
        cipher = ""
        for letter in message:
                if letter != " ":  # Checks if letter is a space or not
                        cipher += letter_table[letter]
                else:
                        cipher += " "
        return cipher

message = input("Enter your message: ")
cipher = atbash(message.upper())
print(cipher)