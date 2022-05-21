import points_summer
import alphabet_printing
import pygame_events
import random

width = 1500


def guessing_word(my_word, mode_list, first_mode_points, window, guessed, player):
    word_letters = []
    word_letters.clear()
    word_letters[:0] = my_word
    alphabet_printing.alphabet_making(width, mode_list, window)
    pygame_events.draw_word(word_letters, None, window, 1)
    word_guessed_check = 0
    hangman_status = 0

    while hangman_status < 7:
        letter = pygame_events.pygame_events(mode_list, my_word, window, 2, first_mode_points, guessed, player)
        letters = alphabet_printing.letters_return()
        if letter in letters:
            letter[3] = False
        ltr = letter[2].lower()
        pygame_events.draw_alphabet(window, letters)
        word_guessed_check, window = pygame_events.draw_word(word_letters, ltr, window, word_guessed_check)
        if ltr in word_letters[1:-1]:
            if word_guessed_check == len(word_letters) - 2:
                guessed += 1
                first_mode_points = points_summer.first_mode_points_summer(mode_list, first_mode_points, my_word,
                                                                           hangman_status, guessed)
                pygame_events.guessed_word(window, first_mode_points)
                pygame_events.pygame_events(mode_list, find_word(mode_list), window, 1, first_mode_points, guessed,
                                            player)
            else:
                pygame_events.hanged(window, hangman_status, first_mode_points, mode_list, player, my_word)
        else:
            hangman_status += 1
            print(hangman_status)
            pygame_events.hanged(window, hangman_status, first_mode_points, mode_list, player, my_word)


def find_word(mode_list):
    my_word = ""
    if int(mode_list[1]) == 1:
        file = open("eng_words.txt", "r").read().splitlines()
    elif mode_list[1] == 2:
        pass  # STILL DIDN'T FIND A LIST OF ALL BULGARIAN WORDS
        file = open("bg_words.txt", "r").read().splitlines()
    if mode_list[0] == 1:
        if mode_list[2] == 1:
            while 3 > len(my_word) or len(my_word) > 5:
                my_word = random.choice(file)
        elif mode_list[2] == 2:
            while 10 > len(my_word) or len(my_word) < 5:
                my_word = random.choice(file)
        elif mode_list[2] == 3:
            while len(my_word) < 10:
                my_word = random.choice(file)
        else:
            my_word = random.choice(file)

    else:
        my_word = random.choice(file)
    print(my_word)
    return my_word
