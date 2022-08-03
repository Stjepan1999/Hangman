import random


print('----------WELCOME TO HANGMAN GAME!----------')

def lines(word):
    display = '_' * len(word)
    print(display)
    
def images(tries):
    HANGMAN_PICS = ['''
   +---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\  |
  / \  |
      ===''']
    HANGMAN_PICS = sorted(HANGMAN_PICS, reverse=True)
    print(HANGMAN_PICS[tries])
            
croatian = ['auto', 'mobitel', 'čovjek', 'zagreb', 'novac', 'vatrogasac', 'bolnica', 'nogomet', 'košarka', 'more', 'printer', 'tipkonica', 'kompjuter', 'monitor', 'televizor', 'ormar', 'proteza', 'motor']
english = ['car', 'phone', 'human', 'city', 'country', 'baby', 'book', 'money', 'desk', 'computer', 'software', 'keyboard', 'street', 'guitar', 'piano', 'house', 'beach', 'ocean', 'printer', 'football', 'basketball']
guessed_letters = []
guessed_words = []
user_wins = 0
user_losts = 0

        
while True:
    izbornik = input('Do you want to play hangman? Y/N: ').upper()
    if izbornik == 'Y':
        language = input('Do you want to play in Croatian or English? C/E: ').upper()
        if language == 'C':
            words = croatian
        elif language == 'E':
            words = english
        else:
            print('Please enter valid choice.')
            continue
    if izbornik == 'N':
        break
    if not izbornik in 'YN':
        print('Enter valid choice.')
        continue
    while izbornik == 'Y':
        random.shuffle(words)
        word = words.pop().upper()
        word_2 = word
        display = '_' * len(word)
        length = len(word)
        tries = 6
        while tries > 0:
            images(tries)
            print(display)
            guess = str(input('Enter letter/word: ')).upper()
            if len(guess) == 1:
                if not guess in word:
                    if not guess in guessed_letters:
                        print(f'Letter {guess} is not in word')
                        guessed_letters.append(guess)
                        tries -= 1
                    else:
                        print(f'You already entered "{guess}" letter!')
                    
                if guess in word:
                    guessed_letters.extend([guess])
                    index = word.find(guess)
                    word = word[:index] + " " + word[index + 1:]
                    display = display[:index] + guess + display[index + 1:]
                    print(display + '\n')
                
                    
                if not '_' in display:
                    print(f'Congrats, you guessed the word {display}!')
                    user_wins += 1
                    guessed_letters = []
                    print(f'You have {user_wins} WINS and {user_losts} LOSES!')
                    break
                
                if tries == 0:
                    images(0)
                    print('You lost!')
                    guessed_letters = []
                    user_losts += 1
                    print(f'You have {user_wins} WINS and {user_losts} LOSES!')
                    break
            
            if len(guess) > 1:
                if guess != word_2:
                    if not guess in guessed_words:
                        print(f'Word {guess} is not answer!')
                        guessed_words.append(guess)
                        tries -= 1
                    else:
                        print(f'You already entered "{guess} word!')
                
                if guess == word_2:
                    print(f'Congrats, you guessed the word {word_2}!')
                    user_wins += 1
                    guessed_words = []
                    guessed_letters = []
                    print(f'You have {user_wins} WINS and {user_losts} LOSES!')
                    break
                
                if tries == 0:
                    images(0)
                    print('You lost!')
                    user_losts += 1
                    guessed_words = []
                    guessed_letters = []
                    print(f'You have {user_wins} WINS and {user_losts} LOSES!')
                    break
        



        




