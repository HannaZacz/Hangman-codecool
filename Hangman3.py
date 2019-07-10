import random
import time

start_time = time.time()

run = True
while run == True:

# rysunek
    HANGMAN = (
    """
     ------
     |    |
     |
     |
     |
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |
     |
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   -|-
     | 
     |   
     |   
     |   
     |   
    ----------
    """,
    """
     ------
     |    |
     |    O
     |  /-|-
     |   
     |   
     |   
     |   
     |   
    ----------
    """,
    """
     ------
     |    |
     |    O
     |  /-|-|
     |   
     |   
     |   
     |   
     |   
    ----------
    """,
    """
     ------
     |    |
     |    O
     |  /-|-|
     |    |
     |   
     |   
     |   
     |   
    ----------
    """,
    """
     ------
     |    |
     |    O
     |  /-|-|
     |    |
     |    |
     |   | 
     |   | 
     |   
    ----------
    """,
    """
     ------
     |    |
     |    O
     |  /-|-|
     |    |
     |    |
     |   | |
     |   | |
     |  
    ----------
    """)

# maxymalna liczba bledow jest o 1 mniejsza niz liczba rysunkow
    MAX_WRONG = len(HANGMAN) - 1
# slowa
    WORDS = ["DUPA","CODE","COOL","NUDA"]

    word = random.choice(WORDS) # slowo do odgadniecia 


    so_far = "-" * len(word)      # kreska zastępuje nieodgadniętą literę

    wrong = 0 # liczba nietrafionych liter 
    correct = 0 # liczba trafionych liter przy próbie odgadniecia calego wyrazu
    win = 0
    used = [] #  uzyte litery

    print("Hello to Hangman. Let's play!")

    while wrong < MAX_WRONG and so_far != word:
        print(HANGMAN[wrong])
        print("\n These letters you have used:\n", used)
        print("\n Word to guess:\n", so_far)

        guess = input("\n Please enter a letter: ")
        guess = guess.upper()
    #jeśli użytkownik poda jedną literę
        
        if len(guess)==1:
            while guess in used:
                print("You have already tried this letter", guess)
                guess = input("Please enter a letter: ")
                guess = guess.upper()

            used.append(guess)

            if guess in word:
                print("\n",guess,"is in the word!")

        # wersja zmiennej so_far zawierająca odgadniętą literę
                new = ""
                for i in range(len(word)):
                    if guess == word[i]:
                        new += guess
                    else:
                        new += so_far[i]              
                so_far = new
            else:
                print("\n", guess, "n\ is not in word :(")
                wrong += 1
                
        #zgadnięcie całego wyrazu
        elif len(guess) >1:
            correct=0
            #next =''
            guess = guess.upper()
            if len(guess) == len(word): 
               for i in range (len(word)):
                   if guess [i] == word[i]:
                       correct+=1
            if correct == len(word):
                if guess[i] == word[i]:
                    
                    
                    
                    break
                
                
                used.append(guess)
  
   # if win==1:
        print("\n You win!")
        print ("\n You guessed in:", len(used), "tries")
  
  
  
                
#przegrana
    if wrong == MAX_WRONG:
        print(HANGMAN[wrong])
        print("\n You loose!")
    
  
    
    
#wygrana z wylistowana liczba prob       
    else:
        print("\n You win!")
        print ("\n You guessed in:", len(used), "tries")
    
    print("\n The word is:", word)
    
 #timer   
    end_time= time.time() - start_time
    user_time = str(round(end_time, 2))
    print("\n Game time:", user_time, "sek")
    
#rozpoczęcie nowej rozgrywki
    next_game = input("\n\n Do you want to play again (y/n)?")
    if next_game.lower() != 'y':
        run = False
        break