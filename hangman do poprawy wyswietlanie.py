import random
import time
import csv

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

    txt_open = open("cac.txt", "r") #open file read mode

    list_of_countries = [] #create list of countries
    list_of_cities = [] #create list of cities


    for line in txt_open:
        country_and_city = txt_open.readline() #read line from file
        country_and_city = country_and_city.upper()
        separate = country_and_city.rstrip("\n").split(" | ") # split - separate countries form cities
        #rstrip usuwa zadane znaki (tu \n) po prawej stronie

        list_of_countries.append(separate[0])
        list_of_cities.append(separate[-1])

    index = random.randrange(0, len(list_of_cities))



    word = (list_of_cities[index]) # slowo do odgadniecia 


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
        #podpowiedz jesli zostalo ostatnie zycie
        
        if wrong == MAX_WRONG - 1:
            print("\nWARNING! I have a tip for you ;-)")
            print("\nCapital City of " + list_of_countries[index])

        guess = input("\n Please enter a letter or try to guess the word: ")
        guess = guess.upper()
    #jeśli użytkownik poda jedną literę
        
        if len(guess)==1:
            while guess in used:
                print("You have already tried this letter", guess)
                guess = input("Please enter a letter or try to guess the word: ")
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
                print("\n", guess, "is not in word :(")
                wrong += 1
                
        #zgadnięcie całego wyrazu
        elif len(guess) >1:
            correct=0
            
            guess = guess.upper()
            if len(guess) == len(word): 
               for i in range (len(word)):
                   if guess [i] == word[i]:
                       correct+=1
                  
            
            if correct == len(word):
                if guess[i] == word[i]:
                    
                    break
            else:
                    print("\n", guess, "it is not this word :( Be careful! Entering wrong word kills 2 times faster! ")
                    wrong += 2
                
                    used.append(guess)

                
#przegrana
    if wrong >= MAX_WRONG:
        print(HANGMAN[wrong])
        print("\n You loose! :(")

    
#wygrana z wylistowana liczba prob       
    else:
        win=1
        print("\n You win!")
        print ("\n You guessed in:", len(used), "tries")
    
    print("\n The word is:", word)
    
 #timer   
    end_time= time.time() - start_time
    user_time = str(round(end_time, 2))
    print("\n Game time:", user_time, "sek")
    
    if win==1:
        name = input ("\n What is your name? ")
        print("\n")
    
#zapisanie wyniku do pliku
        with open('high_scores.csv', mode='a+') as high_scores:
            high_scores = csv.writer(high_scores, delimiter='|')
            row = name.capitalize(), user_time+" sec", len(used), word
            high_scores.writerow(row)
    
    #odczytanie wyników w konsoli
        with open('high_scores.csv', 'r+') as high_scores:
            high_scores = high_scores.readlines() 
            count=0
            print("High scores:")
            print('ID |','Name    |', 'Time  |', 'Tries |', 'Word |')
            print("--------------------------------------")
            for row in high_scores:
                count +=1    
                print ("{}"".  ""{}".format(count,row)) 
                print("--------------------------------------")
    
    
#rozpoczęcie nowej rozgrywki
    next_game = input("\n\n Do you want to play again (y/n)?")
    if next_game.lower() != 'y':
        run = False
        break