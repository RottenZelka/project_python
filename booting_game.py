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
    mode_list = []  # 0 element - game mode 1 element - game language 2 element(optional) - mode for first mode
    # 3  element mode for second mode

    while True:
        mode_list.clear()
        print("Select Game mode:\n1.Race\n2.Local multiplayer\n")
        mode_list.append(int(input("Enter a Number (1 or 2): ")))
        mode_name = switch_dict_mode.get(mode_list[0], f"Selection {mode_list[0]} Not Valid!")

        if mode_name == f"Selection {mode_list[0]} Not Valid!":
            print(f"Selection {mode_list[0]} Not Valid!\n")
            continue

        if mode_list[0] == 2:
            return mode_list

        mode_list[1] = game_language(mode_list)

        print(f"\nAre you sure you want to play {mode_name} in {switch_dict_language.get(mode_list[1])}\n")
        i = str(input("Enter answer (y for yes and other for no): "))
        if i == "y":
            print("Rules:\n")  # WRITE RULES IN FILE. THEN PRINT THEM + LEADERBOARD FOR 1 MODE
            if mode_list[0] == 1:
                game_mode1(mode_list)
            else:
                game_mode2(mode_list)
            break
        else:
            print("Changing mode...\n")
    return mode_list


def game_mode1(mode_list):
    while True:
        print("This mode requires you to say with how long words would you like to start:\n"
              "1.Less than 5 letters\n2.Less than 10 letters\n3.More than 10 letters\n4.Random words")
        mode_list.append(int(input("Enter a Number (1, 2, 3 or 4): ")))
        f_mode_name = switch_dict_first_mode.get(mode_list[2], f"Selection {mode_list[2]} Not Valid!\n")
        if f_mode_name != f"Selection {mode_list[2]} Not Valid!\n":
            print(f"You would start the game with {f_mode_name} words")
            return mode_list[2]
        else:
            print(f"Selection {mode_list[2]} Not Valid!\n")


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
