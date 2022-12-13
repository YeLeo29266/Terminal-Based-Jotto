import random as r
from datetime import datetime as dt

# function to display hall of fame 
def getHoF():
    # opening file and getting list 
    filename = open('hall_of_fame.txt')
    scores = filename.readlines()

    # list to store values
    HoF = []

    # getting names and score to put into HoF
    for i in range(len(scores)):
        currentIndex = scores[i].split(', ')
        currentScore = currentIndex[0].strip().replace(',', '')
        names = currentIndex[1].strip()
        HoF.append([int(currentScore), names])

    sortHoF(HoF)

    # getting the format for Hall of Fame
    HoFString = ''
    print('\n--- Hall of Fame ---')
    print(' ## : Score : Player')
    for i in range(len(HoF)):
        currentString = f'{i + 1: 3} : {HoF[i][0]: 5} : {HoF[i][1]}'
        print(currentString)

    filename.close()

# function to get lowest value from HoF
def getMin():
    filename = open('hall_of_fame.txt')
    scores = filename.readlines()

    scoreList = []

    # checks to see if the file has values
    if len(scores) > 0:
        # getting scores to put into HoF
        for i in range(len(scores)):
            currentIndex = scores[i].split()
            currentScore = currentIndex[0].strip().replace(',', '')
            scoreList.append([int(currentScore)])
        
        # sorting HoF from least to greatest
        scoreList = sorted(scoreList)

        filename.close()

        return scoreList[0][0]
    else:
        return 0

# gets HoF length
def HoFLen():

    filename = open('hall_of_fame.txt')
    HoF = filename.readlines()

    return len(HoF)

# function to sort HoF file
def sortHoF(list):
    filename = open('hall_of_fame.txt', 'w')
    for i in range(len(list)):
        if i != len(list) - 1:
            filename.writelines(f'{list[i][0]}, {list[i][1]}\n')
        else:
            filename.writelines(f'{list[i][0]}, {list[i][1]}')
    filename.close()

# removes the lowest score from HoF file, code from pynative
def removeScore():
    lines = []
    with open('hall_of_fame.txt', 'r') as fp:
        lines = fp.readlines()

    with open('hall_of_fame.txt', 'w') as fp:
        for number, line in enumerate(lines):
            if number not in [9]:
                fp.write(line)

# function to update HoF
def updateHoF(name, score):
    # compares current score to new score
    if score > getMin() or HoFLen() < 10:
        # checks current length of HoF
        if HoFLen() < 10:
            filename = open('hall_of_fame.txt', 'a')
            file2 = open('hall_of_fame.txt', 'r')
            length = len(file2.readlines())
            if length > 0:
                filename.write(f'\n{score}, {name}')
                filename.close()
                file2.close()
                print(f'\nWay to go {name}!')
                print(f'You earned a total of {score} points and made it into the Hall of Fame!')
                getHoF()
            else:
                filename.write(f'{score}, {name}\n')
                file2.close()
                filename.close()
                print(f'\nWay to go {name}!')
                print(f'You earned a total of {score} points and made it into the Hall of Fame!')
                getHoF()
        else:
            removeScore()
            filename = open('hall_of_fame.txt', 'a')
            filename.write(f'\n{score}, {name}')
            filename.close()
            print(f'\nWay to go {name}!')
            print(f'You earned a total of {score} points and made it into the Hall of Fame!')
            getHoF()
    else:
        return  

# function to check score, returns points and the message to display
def check_score(check, turns, currentWord):
    # variables to store returns 
    message = ''
    points = 0
    # match case to return proper score
    match turns:
        case 6:
            message = 'Impossible! You earned 64 points this round.'
            points += 64
            return message, points
        case 5:
            message = 'Genius! You earned 32 points this round.'
            points += 32
            return message, points
        case 4:
            message = ('Magnificent! You earned 16 points this round.') 
            points += 16
            return message, points
        case 3:
            message = ('Impressive! You earned 8 points this round.')
            points += 8
            return message, points
        case 2:
            message = ('Splendid! You earned 4 points this round.')
            points += 4
            return message, points
        case 1:
            message = ('Great! You earned 2 points this round.')
            points += 2
            return message, points
        case 0:
            if (check == '!!!!!'):
                message = ('Phew! You earned 1 points this round.')
                points += 1
                return message, points
            else: 
                message = (f'You ran out of tries.\nThe word was {currentWord}.')
                return message, points
        case _:
            message = (f'You ran out of tries.\nThe word was {currentWord}')
            return message, points

# gets list of words from file
def get_list(file):
    words = file.readlines()
    for i in range(len(words)):
        words[i] = words[i].strip()
    # closing file 
    file.close()

    return words

# function to pick words to use within a game, returns a list of three words
def pick_game_words(words):
    # creating list to hold words
    randWords = []

    # getting random words
    for i in range(3):
        random = r.randint(0, len(words) - 1)
        randWords.append(words[random])

    # returns three words
    return randWords

# function to check validity of words, returns X's, ?'s, and !'s
def check_words(guess, currentWord, alphabet): 
    # variables to store returns
    current = ''

    # array to check repeating letters
    currentWordArray = []
    for i in range(len(currentWord)):
        currentWordArray.append(currentWord[i])

    # loop to check each character of words 
    for i in range(5):
        if guess[i].lower() == currentWord[i]:
            current += '!'
            # checks off alphabet 
            alphabet[ord(guess[i].lower()) - 97] = '!'

        elif guess[i].lower() in currentWordArray:
            current += '?'
            # makes sure it does not override
            if (alphabet[ord(guess[i].lower()) - 97] != '!'):
                alphabet[ord(guess[i].lower()) - 97] = '?'
                # ensures no repeating letters
                currentWordArray.remove(guess[i].lower())

        else:
            current += 'X'
            if (alphabet[ord(guess[i].lower()) - 97] != '?'):
                alphabet[ord(guess[i].lower()) - 97] = 'X'

    # turns alphabet list into a string 
    alphabetString = ''
    for i in range(len(alphabet)):
        alphabetString += alphabet[i]

    return current, alphabetString, alphabet

# checks validity of guess
def check_valid(guess):
    proceed = False
    while proceed == False:
        # checks length of guess
        if (len(guess) == 5):
            # checking to see each character is valid
            characters = []
            for k in range(len(guess)):
                if guess[k].isalpha() == True:
                    characters.append(guess[k])
            if (len(characters) == 5):
                proceed = True
                return proceed
            else:
                # error for special characters
                print('\nInvalid guess. Please only enter letters.\n')
                return proceed
        else:
            # error for invalid length
            print('\nInvalid guess. Please enter exactly 5 characters.\n')
            return proceed
    
# function to start game 
def start_game():
    # alphabet string for later
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # gets the random words
    file = open('words.txt')

    list = get_list(file)

    words = pick_game_words(list)

    # keeps track of points
    points = 0

    # filling alphabet with empty spaces
    updatedAlph = []
    for i in range(26):
        updatedAlph.append(' ')

    # loop for each round 
    for i in range(3):
        print(f'\nRound {i + 1}:')
        print(words[i]) # for debugging
        # variables to keep track of turns and points
        turns = 0
        turnsLeft = 6
        end = False
        guesses = [] # list to track the guesses during round 
        while end == False and turnsLeft > 0:
            valid = False
            # validity check
            while valid != True:
                guess = input(f'{turns + 1}? ')
                valid = check_valid(guess)

            # checks words 
            current, alphString, updatedAlph = check_words(guess, words[i], updatedAlph)

            # printing the checks
            print('  ', current, '   ', alphString)
            print('  ', guess.lower(), '   ', alphabet)
            # appends current guess thing 
            guesses.append(current)

            # ends loop if the word is right
            if (current == '!!!!!'):
                turns += 1
                turnsLeft -= 1
                end = True
            else:
                turns += 1
                turnsLeft -= 1

        # prints current round results
        message, add = check_score(current, turnsLeft, words[i])
        points += add
        print(message)

        # round summary
        print(f'Round {i + 1} summary:')
        for j in range(turns):
            print(f'   {guesses[j]}')

        # resetting alph
        updatedAlph = []
        for i in range(26):
            updatedAlph.append(' ')

    # generating end message
    return points

def main():
    """Write your mainline logic below this line (then delete this line)."""
    print('Welcome to PyWord.')

    # variable to decide whether or not user selected correct input
    proceed = False
    while proceed == False:
        choice = input('\n----- Main Menu -----\n1. New Game\n2. See Hall of Fame\n3. Quit\n\nWhat would you like to do? ')
        # decision tree
        if (choice == '1'):
            # gets player name 
            name = input('Enter your player name: ')

            # starts game
            points = start_game()

            updateHoF(name, points)

        elif (choice == '2'):
            # prints header
            getHoF()

        elif (choice == '3'):
            print('Goodbye.')

            proceed = True
        else:
            print('\nInvalid choice. Please try again.')

if __name__ == "__main__":
    main()
