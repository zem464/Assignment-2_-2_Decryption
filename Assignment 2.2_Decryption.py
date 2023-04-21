# Zemerelin Iris M. Membrere
# BSCPE 1-4
# Assignment 2

# Problem 2 - Decryption

# Get an encrypted input from the user
encrypted_input = input("\033[33m\033[1mInput the encrypted text: \033[35m\033[0m").lower()
decrypted_output = ""

# Check for the corresponding symbol to substitute
for i in range(len(encrypted_input)):
# If there is '*', change to 'a'
    if encrypted_input[i] == '*':
        decrypted_output += 'a'
# If there is '&', change to 'e'
    elif encrypted_input[i] == '&':
        decrypted_output += 'e'
# If there is '#', change to 'i'
    elif encrypted_input[i] == '#':
        decrypted_output += 'i'
# If there is '+', change to 'o'
    elif encrypted_input[i] == '+':
        decrypted_output += 'o'
# If there is '!', change to 'u'
    elif encrypted_input[i] == '!':
        decrypted_output += 'u'
    else:
        decrypted_output += encrypted_input[i]
# Print the decrypted input
print("\033[33m\033[1mDecryption: \033[35m\033[0m", decrypted_output)