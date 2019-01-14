import sys
import string

serial = None
parallel = None
batteries = None
on = 1

def intro():
    print("Welcome to the Bomb Defusal Manual\n")
    input("To continue, press Enter\n")
    menu()

def menu():
    serial = int(input("Enter the last digit of the serial number: "))
    serialVowel = input("Does the serial number contain a vowel[Y/N]: ")
    parallel = input("Is there a parallel port? (Y/N): ").upper()
    batteries = int(input("Enter the number of batteries: "))
    while on == 1:
        print("1: Simple Wires")
        print("2: Button")
        print("3: Simon Says")
        print("4: Word Panel")
        print("5: Morse Code")
        print("6: Complicated Wires")
        print("7: Wire Sequence")
        print("8: Passwords")
        print("0: Reset")
        print("10: Exit")
        choice = int(input("Please select a module: "))
        if choice == 10:
            return
        elif choice == 1: #done
            simpleWires()
        elif choice == 2: #done
            pressButton()
        elif choice == 3: #done
            simonSays()
        elif choice == 4: #TODO
            wordPanel()
        elif choice == 5: #TODO
            morseCode()
        elif choice == 6: #TODO
            complicatedWires()
        elif choice == 7: #TODO
            wireSequence()
        elif choice == 8: #done
            passwords()
        elif choice == 0:
            resetData()

#Tested with success
def simpleWires():
    numWires = int(input("Enter the number of wires: "))

    if(numWires == 3):
        redWire = int(input("Red wires: "))
        if  redWire == 0:
            input("Cut 2nd wire\n")
            return
        lastWire = input("Last wire color: ")
        if lastWire == "white" or lastWire == "White":
            input("Cut last wire\n")
            return
        blueWire = int(input("Blue wires: "))
        if blueWire > 1:
            input("Cut last blue")
            return
        else:
            input("Cut last wire")
            return
    elif numWires == 4:
        redWire = int(input("Red wires: "))
        if redWire == 0:
            lastWire = input("Last wire color: ")
            if lastWire == "yellow" or lastWire == "Yellow":
                input("Cut the first wire")
                return
        else:
            if serial%2 == 1:
                input("Cut last red")
                return
        blueWire = int(input("Blue Wires: "))
        if blueWire == 1:
            input("Cut the first wire")
            return
        yellowWire = int(input("Yellow Wires: "))
        if yellowWire < 2:
            input("Cut the second wire")
            return
        else:
            input("Cut the last wire")
            return

    elif numWires == 5:
        lastWire = input("Last wire color: ")
        if lastWire == "Black" or lastWire == "black":
            if serial%2 == odd:
                input("Cut the 4th wire")
                return
            else:
                input("Cut the 1st wire")
                return
        redWire = int(input("Red Wires: "))
        if redWire == 1:
            yellowWire = int(input("Yellow Wires: "))
            if yellowWire >= 2:
                input("Cut the 1st wire")
                return
        blackWire = int(input("Black Wires: "))
        if blackWire == 0:
            input("Cut second wire")
            return
        else:
            input("Cut first wire")
            return
    elif numWires == 6:
        yellowWire = int(input("Yellow Wires: "))
        if yellowWire == 0:
            if serial%2 == 1:
                input("Cut 3rd wire")
                return
        elif yellowWire == 1:
            whiteWire = int(input("White wires: "))
            if whiteWire >= 2:
                input("Cut the 4th wire")
                return
        redWire = int(input("Red Wires: "))
        if redWire == 0:
            input("Cut the last wire")
            return
        else:
            input("Cut the 4th wire")
            return

def pressButton():
    buttonColor = input("Button color: ").lower()
    buttonWord = input("Button: ").lower()
    if buttonWord == "detonate":
        if batteries > 1:
            input("Tap the button")
            return
    if batteries >= 3 and (buttonColor == "blue" or buttonColor == "Blue"):
        if buttonWord == "abort":
            heldButton()
            return
        elif buttonWord == "frk":
            input("Tap the button")
            return
        else:
            heldButton()
            return

def heldButton():
    stripColor = input("Strip Color").lower()
    if stripColor == "Blue" or stripColor == "blue":
        input("Release on a 4")
        return
    elif stripColor == "Yellow" or stripColor == "yellow":
        input("Release on a 5")
        return
    else:
        input("Release on a 1")
        return

def wordPanel():
    switch = 1
    locList = [
        ["Bottom Right Word: ","cee", "display", "hold on", "lead", "no", "says", "see", "there", "you are"],
        ["Bottom Left Word: ","", "leed", "reed", "they're"],
        ["Middle Right Word: ","blank", "read", "red", "their", "you", "your", "you're"],
        ["Middle Left Word: ","led", "nothing", "yes", "they are"],
        ["Top Right Word: ","c", "first", "okay"],["Top Left Word: ","ur"]
    ]

    wordDict = {"blank":"wait, right, okay, middle, blank",
                "done":"sure, uh huh, next, what?, your, ur, you're, hold, like, you, u, you are, uh uh, done",
                "first":"left, okay, yes, middle, no, right, nothing, uhhh, wait, ready, blank, what, press, first",
                "hold":"you are, u, done, uh uh, you, ur, sure, what?, you're, next, hold",
                "left":"right, left",
                "like":"you're, next, u, ur, hold, done, uh uh, what?, uh huh, you, like",
                "middle":"blank, ready, okay, what, nothing, press, no, wait, left, middle",
                "next":"what?, uh huh, uh uh, your, hold, sure, next"}

    while switch == 1:
        topWord = input("Enter word on top (for blank just press Enter): ").lower()
        foundL = []
        for l in locList:
            if topWord in l:
                foundL = l
        keyWord = input(foundL[0]).lower()
        while keyWord not in wordDict.keys():
            keyWord = input("Error: Word spelled incorrectly, input again: ")
        input(wordDict[keyWord])
        done = input("Done?[Y/N]: ")
        if done == "Y":
            switch = 0
    return

def morseCode():
    morseDict = {"-":"3.532","....":"3.515","...-":"3.595","..-.":"3.555",
                 ".-..":"3.542","-....":"3.600","-....-..":"3.572","-....-...":"3.575",
                 "-.....": "3.552"}

def complicatedWires():
    pass

def wireSequence():
    pass

#done
def passwords():
    password = ["about","after","again","below","could",
                "every","first","found","great","house",
                "large","learn","never","other","place",
                "plant","point","right","small","sound",
                "spell","still","study","their","there",
                "these","thing","think","three","water",
                "where","which","world","would","write"]
    temp = []
    firstLetters = input("Enter the first set of letters: ").lower()
    for letters in firstLetters:
        for word in password:
            if word[0] == letters:
                temp.append(word)
    password = temp
    temp = []
    if len(password) == 1:
        str = password[0]
        input(str)
        return
    secondLetters = input("Enter the second set of letters: ").lower()
    for letters in secondLetters:
        for word in password:
            if word[1] == letters:
                temp.append(word)
    password = temp
    temp = []
    if len(password) == 1:
        str = password[0]
        input(str)
        return
    thirdLetters = input("Enter the third set of letters: ").lower()
    for letters in thirdLetters:
        for word in password:
            if word[2] == letters:
                temp.append(word)
    password = temp
    temp = []
    if len(password) == 1:
        str = password[0]
        input(str)
        return
    fourthLetters = input("Enter the fourth set of letters: ").lower()
    for letters in fourthLetters:
        for word in password:
            if word[3] == letters:
                temp.append(word)
    password = temp
    temp = []
    if len(password) == 1:
        str = password[0]
        input(str)
        return
    fifthLetters = input("Enter the fifth set of letters: ").lower()
    for letters in fifthLetters:
        for word in password:
            if word[4] == letters:
                temp.append(word)
    password = temp
    temp = []
    if len(password) == 1:
        str = password[0]
        input(str)
        return
    input("Clearly something went wrong. Let's try that again.")
    passwords()

def simonSays():
    rbgyOdd = {"red":["blue", "yellow", "green"], "blue":["red", "green", "red"],
            "green":["yellow", "blue", "yellow"], "yellow":["green", "red", "blue"]}
    rbgyEven = {"red": ["blue", "red", "yellow"], "blue": ["yellow", "blue", "green"],
               "green": ["green", "yellow", "blue"], "yellow": ["red", "green", "red"]}
    strikes = 0
    strike = ""
    getIn = ""
    solution = ""
    done = True
    while(done):
        if serialVowel == "Y":
            sequence = input("Enter color sequence: ").lower()
            sequence = sequence.split(" ")
            for word in sequence:
                solution += rbgyOdd[word][strikes]
            print(solution)
            strike = input("Any errors in input?{Y/N}: ").lower()
            if strike == "Y":
                strikes += 1
            getIn = input("Done?[Y/N]: ")
            if getIn == "Y":
                done = False
        else:
            sequence = input("Enter color sequence: ").lower()
            sequence = sequence.split(" ")
            for word in sequence:
                solution += rbgyEven[word][strikes]
            print(solution)
            strike = input("Any errors in input?{Y/N}: ")
            if strike == "Y":
                strikes += 1
            getIn = input("Done?[Y/N]: ")
            if getIn == "Y":
                done = False
    return

def resetData():
    serial = None
    parallel = None
    serial = int(input("Enter the last digit of the serial number: "))
    parallel = input("Is there a parallel port? (Y/N): ")
    parallel = parallel.upper()
    batteries = int(input("Enter the number of batteries: "))

if __name__ == '__main__':
    intro()