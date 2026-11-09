from gameparts import Board


def main():
    game: Board = Board()

    # При использовании метода make_move напрямую в коде нет защиты от некорректных координат!
    # В целом использование методов класса Board в неожиданных местах
    # может вызывать различные ошибки и некорректное поведение, это будет доработано в следующей версии.
    # В этом случае также к строкам и столбцам необходимо обращаться по индексам (0, 1, 2).
    # game.make_move(0, 2, 'X')
    # game.make_move(0, 0, 'X')
    # game.make_move(2, 0, 'X')
    # game.make_move(1, 1, 'O')
    # game.print_board()
    # game.make_move(0, 2, 'O')
    # game.make_move(2, 2, 'Z')
    # game.make_move(0, 2, 'Z')

    move: int = 0
    while game.game_is_going:
        if move == 9:
            print('Ничья!')
            break

        if move % 2 == 0:
            print('Ходят крестики...')
            player: str = 'X'
        else:
            print('Ходят нолики...')
            player: str = 'O'

        try:
            row: int = int(input('Введите ряд (1, 2, 3): '))
            if row < 1 or row > 3:
                raise ValueError

            col: int = int(input('Введите столбец (1, 2, 3): '))
            if col < 1 or col > 3:
                raise ValueError

        except ValueError:
            print('Неверный формат данных! Только целые числа, от 1 до 3 включительно!')
            continue

        row -= 1
        col -= 1

        game.make_move(row, col, player)

        if not game.return_move:
            move += 1
        else:
            game.return_move = False


if __name__ == '__main__':
    main()
