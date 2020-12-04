import random


def draw_board(board):
    print("  %s | %s | %s" % (board[7], board[8], board[9]))
    print("-------------")
    print("  %s | %s | %s" % (board[4], board[5], board[6]))
    print("-------------")
    print("  %s | %s | %s" % (board[1], board[2], board[3]))


def input_player_letter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def play_again():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


def how_many_players():
    if a == 1:
        return "Player v/s Computer"
    elif a == 2:
        return "Player1 v/s Player2"


def who_goes_first():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


def who_goes_first2():
    if random.randint(0, 1) == 0:
        return 'player2'
    else:
        return 'player1'


def make_move(board, letter, move):
    board[move] = letter


def is_winner(board, letter):
    return ((board[1] == letter and board[2] == letter and board[3] == letter)
            or (board[4] == letter and board[5] == letter and board[6] == letter)
            or (board[7] == letter and board[8] == letter and board[9] == letter)
            or (board[1] == letter and board[5] == letter and board[9] == letter)
            or (board[3] == letter and board[5] == letter and board[7] == letter)
            or (board[7] == letter and board[4] == letter and board[1] == letter)
            or (board[8] == letter and board[5] == letter and board[2] == letter)
            or (board[9] == letter and board[6] == letter and board[3] == letter))


def get_board_copy(board):
    dupe_board = []
    for i in board:
        dupe_board.append(i)
    return dupe_board


def is_space_free(board, move):
    return board[move] == ' '


def get_player_move(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not is_space_free(board, int(move)):
        move = input()
    return int(move)


def choose_random_move_from_list(board, move_list):
    possible_moves = []
    for i in move_list:
        if is_space_free(board, i):
            possible_moves.append(i)
    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return None


def get_computer_move(board, computer_letter):
    if computer_letter == 'X':
        player_letter == 'O'
    else:
        player_letter == 'X'

    for i in range(1, 10):
        copy = get_board_copy(board)
        if is_space_free(copy, i):
            make_move(copy, computer_letter, i)
            if is_winner(copy, computer_letter):
                return i
    for i in range(1, 10):
        copy = get_board_copy(board)
        if is_space_free(copy, i):
            make_move(copy, player_letter, i)
            if is_winner(copy, player_letter):
                return i

    move = choose_random_move_from_list(board, [1, 3, 7, 9])
    if move not in None:
        return move

    if is_space_free(board, 5):
        return 5

    return choose_random_move_from_list(board, [2, 4, 6, 8])


def is_board_full(board):
    for i in range(1, 10):
        if is_space_free(board, i):
            return False
    return True


while True:
    print("WELCOME TO TIC-TAC-TOE")
    print("Press 1 for Single Player\nPress 2 for Two Player")
    theBoard = [' '] * 10
    a = int(input())
    players = how_many_players()
    if a == 1:
        player_letter, computer_letter = input_player_letter()
        turn = who_goes_first()
        print('The ' + turn + ' will go first.')
    elif a == 2:
        player_letter, player2Letter = input_player_letter()
        turn2 = who_goes_first2()
        print('The ' + turn2 + ' will go first.')
    gameIsPlaying = True

    if a == 1:
        while gameIsPlaying:
            if turn == 'player':
                draw_board(theBoard)
                move = get_player_move(theBoard)
                make_move(theBoard, player_letter, move)

                if is_winner(theBoard, player_letter):
                    draw_board(theBoard)
                    print('Hooray! You have won the game!')
                    gameIsPlaying = False
                else:
                    if is_board_full(theBoard):
                        draw_board(theBoard)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'computer'

            else:
                move = get_computer_move(theBoard, computer_letter)
                make_move(theBoard, computer_letter, move)

                if is_winner(theBoard, computer_letter):
                    draw_board(theBoard)
                    print('The computer has beaten you! You lose.')
                    gameIsPlaying = False
                else:
                    if is_board_full(theBoard):
                        draw_board(theBoard)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'player'

    if not play_again():
        break

    elif a == 2:
        while gameIsPlaying:
            if turn2 == 'player':
                draw_board(theBoard)
                move = get_player_move(theBoard)
                make_move(theBoard, player_letter, move)

                if is_winner(theBoard, player_letter):
                    draw_board(theBoard)
                    print('Hooray!Player1 won the game!')
                    gameIsPlaying = False
                else:
                    if is_board_full(theBoard):
                        draw_board(theBoard)
                        print('The game is a tie!')
                        break
                    else:
                        turn2 = 'player2'
            else:
                turn2 == 'player2'
                draw_board(theBoard)
                move = get_player_move(theBoard)
                make_move(theBoard, player2Letter, move)

                if is_winner(theBoard, player2Letter):
                    draw_board(theBoard)
                    print('Hooray!Player2 won the game!')
                    gameIsPlaying = False
                else:
                    if is_board_full(theBoard):
                        draw_board(theBoard)
                        print('The game is a tie!')
                        break
                    else:
                        turn2 = 'player'

    if not play_again():
        break
