import pygame
import word_guessing
import math
import alphabet_printing

#This file is used for functions using pygame
pygame.init()

RADIUS = 40
fps = 60
clock = pygame.time.Clock()
width = 1500
height = 800
white = (255, 255, 255)
black = (0, 0, 0)
leaderboard_start_x = 10
first_mode_points = 0
guessed_letters = []
guessed_letters.clear()


def pygame_events(mode_list, my_word, window, gone, first_mode_points, guessed, player):
    run = True
    button_x = 600
    button_y = 500
    button_width = 250
    button_height = 70
    pygame.init()

    if gone == 0 and mode_list[0] == 1:
        window = pygame.display.set_mode((width, height))
        window = leaderboard_printing(mode_list, window, 0, player)

    if gone == 3 and mode_list[0] == 1:
        game_font = pygame.font.SysFont('timesnewroman', 50)
        pygame.draw.rect(window, white, pygame.Rect(button_x, button_y, button_width, button_height), 2)
        text = game_font.render(f"New Game", 1, white)
        window.blit(text, (button_x + 5, button_y + 5))
        button_x += button_width + 10
        pygame.draw.rect(window, white, pygame.Rect(button_x, button_y, button_width, button_height), 2)
        text = game_font.render(f"Exit Game", 1, white)
        window.blit(text, (button_x + 5, button_y + 5))

    while run:
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and (gone == 1 or gone == 0):
                window.fill(black)
                word_guessing.guessing_word(my_word, mode_list, first_mode_points, window, guessed, player)
            if event.type == pygame.MOUSEBUTTONDOWN and gone == 2:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                letters = alphabet_printing.letters_return()
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        dis = math.sqrt((x - mouse_x) ** 2 + (y - mouse_y) ** 2)
                        if dis < RADIUS:
                            letter[3] = False
                            return letter
            if event.type == pygame.MOUSEBUTTONDOWN and gone == 3:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if button_x <= mouse_x <= button_x + button_width and button_y <= mouse_y <= button_y + button_height:
                    pygame.quit()
                button_x -= button_width - 10
                if button_x <= mouse_x <= button_x + button_width and button_y <= mouse_y <= button_y + button_height:
                    pygame.quit()
                    exec(open("main.py").read())
        pygame.display.update()


def draw_alphabet(window, letters):
    game_font = pygame.font.SysFont('timesnewroman', 50)
    window.fill(black)
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(window, white, (x, y), RADIUS, 3)
            text = game_font.render(ltr, 1, white)
            window.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))


def draw_word(word_letters, ltr, window, word_guessed_check):
    font_size = 50
    game_font = pygame.font.SysFont('timesnewroman', font_size)
    gap = font_size + 10
    letter_x = 500
    letter_y = 250
    for i in range(1, len(word_letters) - 1):
        if ltr == word_letters[i]:
            guessed_letters.append(ltr)
            word_guessed_check += 1
    print(guessed_letters)
    for i in range(len(word_letters)):
        if i == len(word_letters) - 1 or i == 0:
            letter = game_font.render(f"{word_letters[i]}", 1, white)
            window.blit(letter, ((letter_x + gap), letter_y))
        else:
            letter = game_font.render(f"_", 1, white)
            window.blit(letter, ((letter_x + gap), letter_y))
        letter_x += gap
    for i in range(len(guessed_letters)):
        letter_x = 500 + gap
        for j in range(1, len(word_letters) - 1):
            if guessed_letters[i] == word_letters[j]:
                letter = game_font.render(f"{word_letters[j]}", 1, white)
                window.blit(letter, ((letter_x + gap), letter_y))
            letter_x += gap
    if len(guessed_letters) == len(word_letters) - 2:
        guessed_letters.clear()
    pygame.display.update()
    return word_guessed_check, window


def guessed_word(window, first_mode_points):
    letter_x = 500
    letter_y = 250
    font_size = 50
    gap = font_size + 2
    window.fill(black)
    game_font = pygame.font.SysFont('timesnewroman', font_size)
    text = game_font.render(f"Guessed word. Your points are {first_mode_points}.", 1, white)
    window.blit(text, ((letter_x + gap), letter_y))
    letter_y += gap
    text = game_font.render(f"Press to continue", 1, white)
    window.blit(text, ((letter_x + gap), letter_y))
    pygame.display.update()


def hanged(window, hangman_status, first_mode_points, mode_list, player, my_word):
    letter_x = 500
    letter_y = 250
    font_size = 50
    if hangman_status == 0:
        return None

    if hangman_status == 7:
        window.fill(black)
        image = pygame.image.load("hangman" + str(hangman_status - 1) + ".png")
        window.blit(image, (0, 0))
        player.type_points(mode_list, first_mode_points)
        game_font = pygame.font.SysFont('timesnewroman', font_size)
        text = game_font.render(f"You were hanged. The word was {my_word} Your points are {first_mode_points}.", 1, white)
        leaderboard_printing(mode_list, window, 1, player)
        window.blit(text, (letter_x, letter_y))
        pygame_events(None, None, window, 3, 0, 0, player)

    image = pygame.image.load("hangman" + str(hangman_status - 1) + ".png")
    window.blit(image, (0, 0))

    pygame.display.update()


def leaderboard_printing(mode_list, window, flag, player):
    leaderboard_start_y = 0
    font_size = 30
    font = pygame.font.SysFont('timesnewroman', font_size)
    gap = font_size + 2
    if mode_list[1] == 1:
        # making list from leaderboard file
        with open("leaderboard_en.txt") as leaderboard:
            list_leaderboard = []
            for line in leaderboard:
                list_leaderboard.append(line.strip())
    elif mode_list[1] == 2:
        with open("leaderboard_bg.txt") as leaderboard:
            list_leaderboard = []
            for line in leaderboard:
                list_leaderboard.append(line.strip())
    if flag == 0:
        if mode_list[0] == 1:
            pygame.display.set_caption("HANGMAN RACE")
            text = font.render(f"LEADERBOARD", 1, white)
            window.blit(text, (leaderboard_start_x, leaderboard_start_y))
            leaderboard_start_y += gap
            for i in range(0, len(list_leaderboard)):
                leaderboard_string = list_leaderboard[i]
                text = font.render(f"{leaderboard_string}", 1, white)
                window.blit(text, (leaderboard_start_x, leaderboard_start_y))
                leaderboard_start_y += gap
            text = font.render(f"PRESS ANYWHERE TO START GAME", 1, white)
            window.blit(text, (leaderboard_start_x, leaderboard_start_y))
    else:
        player.add_points(list_leaderboard, mode_list)

    pygame.display.update()
    return window


pygame.quit()
