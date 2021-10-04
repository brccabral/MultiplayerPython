class Game:
    def __init__(self, id) -> None:
        self.p1Went = False
        self.p2Went = False
        self.ready = False
        self.id = id
        self.moves = [None, None]
        self.wins = [0,0]
        self.ties = 0
    def get_player_move(self, p):
        """
        :param p: [0,1]
        :return: Move
        """
        return self.moves[p]
    
    def player_controller(self, player, move):
        self.moves[player]= move
        if player == 0:
            self.p1Went = True
        else:
            self.p2Went = True
    
