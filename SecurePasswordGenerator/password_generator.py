import random
import string
from os import system

PW_MIN = 8
PW_MAX = 20

SAVE_PATH = ""

##Clears the Console Screen And Prints Desired Error Message
def print_error(message:str):
    system("cls")
    print(message)

## Continues To Prompt User For A Value Between Min & Max Until Validation Success.
def get_valid_int(prompt:str, min:int, max:int):
    isValid = False
    while (not isValid):
        user_in = input(prompt+"\n>")
        if (user_in.isnumeric()):
            user_in = int(user_in)
            if (user_in > min-1 and user_in < max+1):
                system("cls")
                isValid = True
                return user_in
            else: print_error(f"Invalid Number: Number Out Of Bounds")
        else: print_error("Invalid Input: Value Must Be Numeric")

## Main Function Used To Collect Input From User While Validating.
def get_user_input():
    system("cls")
    isValid = False
    pw_size = get_valid_int("Select A Password Size Between 8-20", PW_MIN, PW_MAX)

    while (not isValid):
        remaining = pw_size
        letters = get_valid_int(f"How Many Letters To Use?\nRemaining: {remaining}", 0, remaining)
        remaining -= letters
        digits = get_valid_int(f"How Many Numbers To Use?\nRemaining: {remaining}", 0, remaining)
        remaining -= digits
        retards = get_valid_int(f"How Many Characters to Use?\nRemaining: {remaining}", 0, remaining)
        remaining -= retards
        if (remaining != 0): 
           print_error("Combined Values Must Equal Password Size. Please Try Again.")
        else: 
            pw = generate_password(letters, digits, retards)
            log_password(pw, letters, digits, retards)
            save_password(SAVE_PATH, pw)
            isValid = True

## Returns A String of Random Letter, Numbers, and Characters Based on Parameters.
def generate_password(chars:int, numbers:int, special:int):
    out = ""
    contents = []
    for x in range(chars):
        contents.append(get_random_char())
    for y in range(numbers):
        contents.append(get_random_digit())
    for z in range(special):
        contents.append(get_random_retard())
    random.shuffle(contents)
    for n in range(len(contents)):
        out += contents[n]
    return out

## Logs Password and Values to Console For Debugging?
def log_password(pw:str, chars:int, numbers:int, special:int):
    print("Generated Password: " + pw)
    print("------------------")
    print(f"Letters: {chars}\nDigits: {numbers}\nCharacters: {special}\n")

## Saves Password To Desired Path As A Text Document, Appends If File Exsists.
def save_password(path:str, password:str):
    if (len(path) > 0):
        with open(path+"/password.txt", "a") as file:
            file.write(f"Generated Password: {password}\n")

def get_random_char(): return random.choice(string.ascii_letters)
def get_random_digit(): return random.choice(string.digits)
def get_random_retard(): return random.choice(string.punctuation)

system("cls")
get_user_input()