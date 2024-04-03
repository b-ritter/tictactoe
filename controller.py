from states import GameStates as g

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def get_move(self, oops=False):
        msg = ""
        if oops:
            msg = f"Oops, that space is  occupied. "
        msg += f"Player {self.model.get_current_player_value()}'s move: "
        move = self.view.render(self.model.get_board(),msg)
        return self.model.hanlde_move(move)
    
    def show_help(self):
        self.view.render(self.model.valid_moves, "Valid moves. Press any key to continue.")
        return g.PLAY

    def play_again(self, res):
        if res.lower() == 'y':
            self.model.reset()
            return g.PLAY
        elif res.lower() == 'n':
            return g.EXIT

    def show_win(self):
        msg = f"Player {self.model.get_current_player_value()} wins. Play again? Type y/n "
        res = self.view.render(self.model.get_board(), msg)
        return self.play_again(res)

    def show_tie(self):
        res = self.view.render(self.model.get_board(), "It's a tie. Play again? Type y/n ")
        return self.play_again(res)