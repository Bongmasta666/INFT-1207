import random
import string
from os import system

PW_MIN = 8
PW_MAX = 20

##Clears the Console Screen And Prints Desired Error Message
def printError(message:str):
    system("cls")
    print(message)

## Continues To Prompt User For A Value Between Min & Max Until Validation Success.
def getValidInt(prompt:str, min:int, max:int):
    isValid = False
    while (not isValid):
        user_in = input(prompt+"\n>")
        if (user_in.isnumeric()):
            user_in = int(user_in)
            if (user_in > min-1 and user_in < max+1):
                system("cls")
                isValid = True
                return user_in
            else: printError(f"Invalid Number: Number Out Of Bounds")
        else: printError("Invalid Input: Value Must Be Numeric")

## Main Function Used To Collect Input From User While Validating.
def getUserValues():
    system("cls")
    isValid = False
    pw_size = getValidInt("Select A Password Size Between 8-20", PW_MIN, PW_MAX)

    while (not isValid):
        remaining = pw_size
        letters = getValidInt(f"How Many Letters To Use?\nRemaining: {remaining}", 0, remaining)
        remaining -= letters
        digits = getValidInt(f"How Many Numbers To Use?\nRemaining: {remaining}", 0, remaining)
        remaining -= digits
        retards = getValidInt(f"How Many Retarded Characters to Use?\nRemaining: {remaining}", 0, remaining)
        remaining -= retards
        if (remaining != 0): 
           printError("Combined Values Must Equal Password Size. Please Try Again.")
        else: 
            pw = genPW(letters, digits, retards)
            logPw(pw, letters, digits, retards)
            isValid = True

## Returns A String of Random Letter, Numbers, and Characters Based on Parameters.
def genPW(chars:int, numbers:int, special:int):
    out = ""
    contents = []
    for x in range(chars):
        contents.append(getRandomChar())
    for y in range(numbers):
        contents.append(getRandomDigit())
    for z in range(special):
        contents.append(getRandomRetard())
    random.shuffle(contents)
    for n in range(len(contents)):
        out += contents[n]
    return out

## Logs Password and Values to Console For Debugging?
def logPw(pw:str, chars:int, numbers:int, special:int):
    print("Generated Password: " + pw)
    print("------------------")
    print(f"Letters: {chars}\nDigits: {numbers}\nRetarded Characters: {special}\n")

def getRandomChar(): return random.choice(string.ascii_letters)
def getRandomDigit(): return random.choice(string.digits)
def getRandomRetard(): return random.choice(string.punctuation)

system("cls")
getUserValues()