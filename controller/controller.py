from game.states import GameStates as g

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def get_move(self, oops=False):
        msg_data = {"player": self.model.get_current_player_value()}
        move = None
        if oops:
            move = self.view.render(self.model.get_board(), msg_data=msg_data, state=g.INVALID_MOVE)
        else:
            move = self.view.render(self.model.get_board(), msg_data=msg_data, state=g.PLAY)
        return self.handle_move(move)
    
    def show_help(self):
        self.view.render(self.model.valid_moves, state=g.HELP)
        return g.PLAY

    def play_again(self, res):
        if res.lower() == 'y':
            self.model.reset()
            return g.PLAY
        elif res.lower() == 'n':
            return g.EXIT
        elif res.lower() == 'q':
            return g.QUIT
        else:
            return self.model.check_for_win_or_tie()

    def handle_move(self, move_cmd: str):
        if move_cmd.lower() == 'q':
            return g.QUIT
        if move_cmd.lower() == 'h':
            return g.HELP
        if not self.model.is_move_cmd(move_cmd):
            return g.INVALID_INPUT
        row, col = self.model.parse_move(move_cmd)
        if not self.model.is_move_valid(row, col):
            return g.INVALID_MOVE
        self.model.update_board(row, col, self.model.get_current_player())
        result = self.model.check_for_win_or_tie()
        
        if result in [g.WIN, g.TIE]:
            return result
        else:
            self.model.set_current_player(self.model.switch_players())
            return result

    def show_win(self):
        msg_data = {"player": self.model.get_current_player_value()}
        res = self.view.render(self.model.get_board(), msg_data=msg_data, state=g.WIN)
        return self.play_again(res)

    def show_tie(self):
        res = self.view.render(self.model.get_board(), state=g.TIE)
        return self.play_again(res)
    
    def show_quit(self):
        res = self.view.render(self.model.get_board(), state=g.QUIT)
        if res.lower() == 'y':
            return g.EXIT
        elif res.lower() == 'n':
            return g.PLAY
        else:
            return g.QUIT