import pygame_events

RADIUS = 40
GAP = 30
white = (255, 255, 255)


starty = 500
letters = []


def alphabet_making(width, mode_list, window):
    letters.clear()
    startx = round((width - (RADIUS * 2 + GAP) * 13) / 2)

    if mode_list[1] == 1:
        file = open("alphabet_en.txt", "r").read().splitlines()
    elif mode_list[1] == 2:
        file = open("alphabet_bg.txt", "r").read().splitlines()

    for i in range(len(file)):
        x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
        y = starty + ((i // 13) * (GAP + RADIUS * 2))
        letters.append([x, y, file[i], True])

    pygame_events.draw_alphabet(window, letters)


def letters_return():
    return letters

