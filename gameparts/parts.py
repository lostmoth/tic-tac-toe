class Board:
    def __init__(self):
        self.board: list[list[str]] = [[' ' for _ in range(3)] for _ in range(3)]
        self.game_is_going: bool = True
        self.return_move: bool = False

    @staticmethod
    def __check_player(player: str) -> str:
        if player == 'X':
            return 'крестики'
        elif player == 'O':
            return 'нолики'
        return 'Ошибка'

    def make_move(self, row: int, col: int, player: str) -> None:
        if player != 'X' and player != 'O':
            print('В игре участвуют только крестики и нолики!')
            return

        if self.board[row][col] == ' ':
            self.board[row][col] = player
            self.print_board()
            self.__check_win()
        else:
            print('Данная клетка уже занята!')
            self.return_move = True

    def __check_win(self) -> None:
        for row in self.board:
            if len(set(row)) == 1 and row[0] != ' ':
                print(f'Победили {Board.__check_player(row[0])}!')
                self.game_is_going = False
                return

        if self.board[0][0] == self.board[1][0] == self.board[2][0] and self.board[0][0] != ' ':
            print(f'Победили {Board.__check_player(self.board[0][0])}!')
            self.game_is_going = False
            return
        elif self.board[0][1] == self.board[1][1] == self.board[2][1] and self.board[0][1] != ' ':
            print(f'Победили {Board.__check_player(self.board[0][1])}!')
            self.game_is_going = False
            return
        elif self.board[0][2] == self.board[1][2] == self.board[2][2] and self.board[0][2] != ' ':
            print(f'Победили {Board.__check_player(self.board[0][2])}!')
            self.game_is_going = False
            return
        elif self.board[1][1] == self.board[0][0] == self.board[2][2] and self.board[1][1] != ' ':
            print(f'Победили {Board.__check_player(self.board[1][1])}!')
            self.game_is_going = False
            return
        elif self.board[1][1] == self.board[0][2] == self.board[2][0] and self.board[1][1] != ' ':
            print(f'Победили {Board.__check_player(self.board[1][1])}!')
            self.game_is_going = False
            return

    def print_board(self) -> None:
        print('----------')
        for row in self.board:
            print(' | '.join(row))
        print('----------')

