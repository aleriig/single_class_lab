class Team:
    def __init__(self, name, players, coach):
        self.name = name
        self.players = players
        self.coach = coach
        self.points = 0

    # There is a given list of players in the team
    # In that list, include a new player
    def add_player(self, new_player):
        self.players.append(new_player)

    def has_player(self, player):
        # return player in self.players
        if player in self.players:
            return True
        else:
            return False

    # Method to play a game
    # Two possibilities: Win or lose
    # if win:
    #   add three to points
    # if lose:
    #   add zero to points
    #
    # win = True & lose = False
    def play_game(self, winning_game):
        if winning_game:
            self.points += 3