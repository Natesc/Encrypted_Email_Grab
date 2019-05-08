import Reader
import Decipher
import os

# Define login details & server
from_email = 'example@gmail.com'
from_pwd = 'passforgmailaccount'
smtp_server = 'imap.gmail.com'
smtp_port = 993

# Ask the user who the message is from
coming = input("Who is the message from: ")

# Call the function to check the inbox for messages
body = (Reader.readmail(from_email, from_pwd, smtp_server, coming))

# If they are out of attempts and there are no messages quit the program
if not body:
    print("There are no messages from users you've tried.")
    quit()

# Decipher the base message
message = [i for i in body if i == i.capitalize()]
string = ' '.join(message)

# Ask if the message has further encryption
answer = input("Is the text encrypted? (Yes or No): ")

# Make sure the input is yes or no
while answer.lower() not in ("yes", "no"):
     answer = input("Invalid Input, Try Again: ")

# If the answer is yes ask for the key and then call for the decipher function
if answer.lower() == "yes":
    shift = int(input("Key: "))
    shift = shift*-1
    string = (Decipher.encrypt(string, shift))
else:
    pass

# print the message
print("\nThe message is: " + "'" + string + "'")

# Ask if they would like to save the message
answer = input("\nWould you like to save the message? (Yes or No): ")

# Make sure the answer is yes or no
while answer.lower() not in ("yes", "no"):
    answer = input("Invalid input try again: ")

# if the answer is yes save the message to the users desktop else quit
if answer.lower() == "yes":
    # Try for the OneDrive Desktop if there isn't one use regular desktop
    try:
        with open(os.path.expanduser('~\\OneDrive\\Desktop\\Decoded.txt'), 'a+') as file:
            file.write(string + '\n')
    except IOError:
        with open(os.path.expanduser('~\\Desktop\\Decoded.txt'), 'a+') as file:
            file.write(string + '\n')
else:
    quit()