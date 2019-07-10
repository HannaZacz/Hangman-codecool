import os

#def add_highscore(text):                                                                                                
#    fo = open('highscores.txt','a')
#    fo.write(text+'\n')
#    fo.close()


def add_highscore(text):                                                                                              
    fo = open('highscores.txt','r+')
    highscores_list = fo.readlines()

    if len(highscores_list) > 9:
        fo.seek(0, os.SEEK_SET)
        fo.truncate(0)
        scores = []
        for i in range(len(highscores_list)):
            temp = highscores_list[i].split()
            for element in temp:
                if '.' in element:
                    scores.append(float(element))
        worst_score = max(scores)

        for record in highscores_list:
            if str(worst_score) not in record:
                fo.write(record)

    fo.seek(0, os.SEEK_END)
    fo.write(text+'\n')
    fo.close()


def read_highscore():
    fo = open('highscores.txt','r')
    highscores = fo.read().split('\n')
    fo.close()
    highscores.pop()
    return highscores


def sort_highscores(highscores):
    scores = []
    for i in range(len(highscores)):
        temp = highscores[i].split()
        for element in temp:
            if '.' in element:
                scores.append(float(element))
    return sorted(scores)


def print_highscores(highscores,sorted_scores):
    index = 1
    fo = open('trophy.txt','r')
    trophy = fo.read()
    fo.close()
    print('\n=== Hall of Fame ===')
    print(trophy)
    final_highscores_list = []
    for i in range(len(sorted_scores)):
        for element in highscores:
            if str(sorted_scores[i]) in element:
                final_highscores_list.append(element)

    for element in final_highscores_list:
        print(f'{index}. {element}')
        index += 1


def show_hangman(position):
    fo = open('hangman.txt','r')
    image = fo.read(position)
    return image


def check_game_result(lives,guessing_count,user_time):
    if lives > 0:
        print('\nYou won!')
        print(f'\nIt took only {str(guessing_count)} guesses')        
    else:
        print('\nYou Lost!')

    print(f'\nGame took: {user_time} seconds')


def generate_hidden_word(city):
    hidden_message =''
    for i in range(len(city)):
        hidden_message += '_'
    return hidden_message
    