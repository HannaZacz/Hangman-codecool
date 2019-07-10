import random
import time
import datetime
from hangman_functions import *


fo = open('countries-and-capitals.txt','r')
city_list = (fo.read()).split('\n')
fo.close()
supported_commands = ['yes','no']


cont = 'yes'
while cont == 'yes':
    random_country_city_pair = random.choice(city_list)
    country = random_country_city_pair.split(' | ')[0]
    city = random_country_city_pair.split(' | ')[1].upper()
    hidden_message = generate_hidden_word(city)

    guessing_count = 0
    lives = 10
    max_lives = 10

    hidden_message_as_list = list(hidden_message)
    start_time = time.time()

    print(city)
    print((' ').join(hidden_message_as_list))
    print('\nLives left: ' + str(lives))

    while '_' in hidden_message_as_list and lives != 0:
        is_game_won = False
        guess_correct = False
        guessed_character = input('\nWpisz litere: ').upper()
        if len(guessed_character) == len(hidden_message_as_list):
            if guessed_character == city:
                is_game_won = True
            else:
                lives -= 1
        else:
            if guessed_character in city : guess_correct = True
            index_list = []
            for i in range(len(city)):
                if city[i] == guessed_character:
                    index_list.append(i)

            for index in index_list:
                hidden_message_as_list[index] = guessed_character
            


        if not guess_correct:
            lives -= 1
            percent_of_hangman = (round((lives / max_lives - 1) * -1,2))
            print(show_hangman(int(round(percent_of_hangman * 500))))
        
        
        
        if is_game_won:
            print('\n' + (' ').join(list(city)) + '\n')
            break


        guessing_count += 1

        print('\nLives left: ' + str(lives))
        hidden_message_temp = (' ').join(hidden_message_as_list)

        if lives <=5:
            print(f'Tip: Capital of {country} is {hidden_message_temp}')
        else:
            print(hidden_message_temp)


    end_time = time.time() - start_time
    user_time = str(round(end_time,3))

    #Inform the user about his result
    check_game_result(lives, guessing_count, user_time)
    

    highscores = read_highscore()
    sorted_scores = sort_highscores(highscores)
    worst_score = sorted_scores[-1]

    if lives > 0 and (end_time < worst_score or len(highscores) < 10):
        print('\nCongratulations, New Highscore!')
        playername = input('\nWrite your name to save your score: ')   

        while not playername.isalnum():
            print('Names can only contain letters and numbers')
            playername = input('\nWrite your name to save your score: ')

        current_date = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
        #highscore = playername + ' | ' + current_date + ' | ' + 'Game took: ' + user_time + ' seconds | ' + str(guessing_count) + ' | ' + city.lower().capitalize()
        highscore = f'{playername} | {current_date} | Game took: {user_time} seconds | {str(guessing_count)} | {city.lower().capitalize()}'        
        add_highscore(highscore)

    highscores = read_highscore()
    sorted_scores = sort_highscores(highscores)
    print_highscores(highscores,sorted_scores)


    answer = input('\nDo you want to play again?(yes/no): ')    
    while answer not in supported_commands:
        print('\nUnknown command')
        answer = input('\nDo you want to play again?(yes/no): ')

    cont = answer