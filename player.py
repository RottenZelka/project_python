class Player:
    def __init__(self, name, points):
        self.points = points
        self.name = name

    def type_points(self, mode_list, first_mode_points):
        if mode_list[0] == 1:
            self.points = first_mode_points

    def add_points(self, list_leaderboard, mode_list):
        if mode_list[1] == 1:
            file = open("leaderboard_en.txt", "w")
        else:
            file = open("leaderboard_en.txt", "w")
        for i in range(len(list_leaderboard)):
            name, points = list_leaderboard[i].split()
            points = int(points)
            if points < self.points:
                list_leaderboard[i] = f"{self.name}   {self.points}"
                for idx in range(i, len(list_leaderboard)):
                    file.write(list_leaderboard[idx] + "\n")
                return None
            file.write(list_leaderboard[i] + "\n")


