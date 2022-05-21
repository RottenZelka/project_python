import player
import word_guessing
import pygame
import alphabet_printing
import pygame_events
import math

pygame.init()

won_1, won_2 = 0, 0
switch_dict_mode = {
    1: "Race",
    2: "Local multiplayer",
}
switch_dict_language = {
    1: "English",
    2: "Bulgarian",
}
switch_dict_first_mode = {
    1: "Easy",
    2: "Normal",
    3: "Hard",
    4: "Random",
}


def game_mode():
    mode_list = []
    mode_list.append(2)
    mode_list[1] = game_language(mode_list)
    game_mode2(mode_list)
    return mode_list


def game_language(mode_list):
    while True:
        print("Select language of the words:\n1.English\n2.Bulgarian\n")
        mode_list.append(int(input("Enter a Number (1 or 2): ")))
        mode_language = switch_dict_language.get(mode_list[1], f"Selection {mode_list[1]} Not Valid!")

        if mode_language == f"Selection {mode_list[1]} Not Valid!":
            print(f"Selection {mode_list[1]} Not Valid!\n")
            mode_list.pop(1)
            continue

        return mode_list[1]


def game_mode2(mode_list):
    mode_list.append(None)
    while True:
        mode_list.append(int(input("How many rounds would you want  ")))
        if mode_list[3] % 2 == 0:
            print(f"Selection {mode_list[3]} Not Valid!\n")
            continue
        return mode_list[3]


mode_list = game_mode()
player1 = player.Player(input("Enter first player name: "), 0)
player2 = player.Player(input("Enter second player name: "), 0)

fps = 60
gone = 0
clock = pygame.time.Clock()
width = 1500
height = 800
white = (255, 255, 255)
black = (0, 0, 0)
RADIUS = 40


def won_round(turn, player1, player2, window, won_1, won_2):
    letter_x = 500
    letter_y = 250
    font_size = 50
    gap = font_size + 2
    game_font = pygame.font.SysFont('timesnewroman', font_size)
    window.fill(black)
    if turn == 1:
        text = game_font.render(f"{player1.name} won the round", 1, white)
        window.blit(text, (letter_x, letter_y))
    else:
        text = game_font.render(f"{player2.name} won the round", 1, white)
        window.blit(text, (letter_x, letter_y))

    if won_1 == round(mode_list[3]/2) + 1:
        text = game_font.render(f"The winner is {player1}", 1, white)
        window.blit(text, (letter_x, letter_y + gap))
    elif won_2 == round(mode_list[3]/2) + 1:
        text = game_font.render(f"The winner is {player1}", 1, white)
        window.blit(text, (letter_x, letter_y + gap))
    text = game_font.render(f"The result is {won_1} : {won_2}", 1, white)
    window.blit(text, (letter_x, letter_y + gap))
    py_game(2)


def hanged(window, hangman_status, my_word, winner):
    letter_x = 500
    letter_y = 250
    font_size = 50
    if hangman_status == 0:
        return None

    if hangman_status == 7:
        window.fill(black)
        image = pygame.image.load("hangman" + str(hangman_status - 1) + ".png")
        window.blit(image, (0, 0))
        game_font = pygame.font.SysFont('timesnewroman', font_size)
        text = game_font.render(f"You were hanged. The word was {my_word}. The winner is {winner.name}", 1,
                                white)
        window.blit(text, (letter_x, letter_y))
        pygame.quit()

    image = pygame.image.load("hangman" + str(hangman_status - 1) + ".png")
    window.blit(image, (0, 0))

    pygame.display.update()


def guessing_word(my_word, mode_list, window, player1, player2, won_1, won_2):
    font_size = 50
    game_font = pygame.font.SysFont('timesnewroman', font_size)
    word_letters = []
    word_letters.clear()
    word_letters[:0] = my_word
    alphabet_printing.alphabet_making(width, mode_list, window)
    pygame_events.draw_word(word_letters, None, window, 1)
    word_guessed_check = 0
    hangman_status = 0
    turn = 0

    while hangman_status < 7:
        if turn == 1:
            turn = 0
            text = game_font.render(f"{player2.name} turn", 1, white)
            window.blit(text, (500, 10))
        else:
            turn = 1
            text = game_font.render(f"{player1.name} turn", 1, white)
            window.blit(text, (500, 10))
        letter = py_game(1)
        letters = alphabet_printing.letters_return()
        if letter in letters:
            letter[3] = False
        ltr = letter[2].lower()
        pygame_events.draw_alphabet(window, letters)
        word_guessed_check, window = pygame_events.draw_word(word_letters, ltr, window, word_guessed_check)
        if ltr in word_letters[1:-1]:
            if word_guessed_check == len(word_letters) - 2:
                if turn == 1:
                    won_1 += 1
                else:
                    won_2 += 2
                won_round(turn, player1, player2, window, won_1, won_2)
                py_game(0)
            else:
                hanged(window, hangman_status, my_word, None)
            if turn == 1:
                turn = 0
            else:
                turn = 1
        else:
            hangman_status += 1
            if turn == 1:
                hanged(window, hangman_status, my_word, player2)
            else:
                hanged(window, hangman_status, my_word, player1)


def py_game(gone):
    run = True
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if gone == 0:
                window = pygame.display.set_mode((width, height))
                window.fill(black)
                my_word = word_guessing.find_word(mode_list)
                guessing_word(my_word, mode_list, window, player1, player2, won_1, won_2)
            if event.type == pygame.MOUSEBUTTONDOWN and gone == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                letters = alphabet_printing.letters_return()
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        dis = math.sqrt((x - mouse_x) ** 2 + (y - mouse_y) ** 2)
                        if dis < RADIUS:
                            letter[3] = False
                            return letter
            if event.type == pygame.MOUSEBUTTONDOWN and gone == 2:
                return None

        pygame.display.update()


py_game(0)

pygame.quit()
