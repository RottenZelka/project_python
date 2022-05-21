import booting_game
import word_guessing
import pygame_events
import player

print("-------HANGMAN-------\n\n\n\n")

guessed_words = 0
first_mode_points = 0


mode_list = booting_game.game_mode()

if mode_list[0] == 2:
    exec(open("multy_player.py").read())
else:
    player = player.Player(input("Enter name: "), 0)
    my_word = word_guessing.find_word(mode_list)
    pygame_events.pygame_events(mode_list, my_word, None, 0, 0, 0, player)
