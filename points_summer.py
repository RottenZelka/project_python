def first_mode_points_summer(mode_list, first_mode_points, my_word, hangman_status, guessed):
    letters_guessed = 0
    if mode_list[2] != 4:
        if hangman_status != 7:
            first_mode_points += len(my_word)
        else:
            first_mode_points += letters_guessed
    else:
        if hangman_status != 7:
            first_mode_points += len(my_word)
            first_mode_points -= hangman_status
        else:
            first_mode_points += letters_guessed

    if guessed % 5 == 0 and mode_list[2] < 4:
        mode_list[2] += 1
    return first_mode_points
