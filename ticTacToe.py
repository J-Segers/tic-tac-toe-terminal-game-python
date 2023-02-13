from os import system, name
from time import sleep

class TicTacToe:
    draw_board_empty = [
        ["         ", "║", "         ", "║", "         "],
        ["    1    ", "║", "    2    ", "║", "    3    ",],
        ["         ", "║", "         ", "║", "         "],
        ["═════════", "╬", "═════════", "╬", "═════════"],
        ["         ", "║", "         ", "║", "         "],
        ["    4    ", "║", "    5    ", "║", "    6    ",],
        ["         ", "║", "         ", "║", "         "],
        ["═════════", "╬", "═════════", "╬", "═════════"],
        ["         ", "║", "         ", "║", "         "],
        ["    7    ", "║", "    8    ", "║", "    9    ",],
        ["         ", "║", "         ", "║", "         "]
    ]

    empty_board = [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""]
    ]

    p1 = dict()
    p2 = dict()

    def __init__(self):
        self.board_drawing = TicTacToe.draw_board_empty
        self.board = TicTacToe.empty_board
        self.draw_title()
        self.p1["name"] = input("enter name player one: ")
        if self.p1["name"] is "":
            self.p1["name"] = 'x'
        self.p1["mark"] = "x"
        self.p2["name"] = input("enter name player two: ")
        if self.p2["name"] is "":
            self.p2["name"] = 'o'
        self.p2["mark"] = "o"
        self.current_player = self.p1
        print(self.current_player)


    def draw_title(self):
        print("""

 ______   __     ______        ______   ______     ______        ______   ______     ______       
/\__  _\ /\ \   /\  ___\      /\__  _\ /\  __ \   /\  ___\      /\__  _\ /\  __ \   /\  ___\      
\/_/\ \/ \ \ \  \ \ \____     \/_/\ \/ \ \  __ \  \ \ \____     \/_/\ \/ \ \ \/\ \  \ \  __\      
   \ \_\  \ \_\  \ \_____\       \ \_\  \ \_\ \_\  \ \_____\       \ \_\  \ \_____\  \ \_____\    
    \/_/   \/_/   \/_____/        \/_/   \/_/\/_/   \/_____/        \/_/   \/_____/   \/_____/    
                                                                                                  

""")

    def draw_board(self):
        current_board = ""

        for row in self.board_drawing:
            # spacing centers game board under title
            current_board += "\t\t\t\t" + ''.join(row)
            current_board += '\n'
        
        print(current_board)

    def play_turn(self):
        valid_choice = False
        new_turn = True
        while valid_choice == False:
            if new_turn == False:
                print("please enter a valid choice")

            choice = input("{} please choose one of the available positions: ".format(self.current_player['name'].title()))
            
            if(self.__check_choice(choice) == True):
                self.__update_board(choice)
                valid_choice = True
    
    def swap_player(self):
        if self.current_player == self.p1:
            self.current_player = self.p2
        else:
            self.current_player = self.p1
    
    def __check_choice(self, choice):
        if not choice.isdigit():
            print("entry is not a digit please enter a number ranging 1 - 9")
            sleep(3)
            return False
        
        choice_number = int(choice)

        if choice_number < 1 or choice_number > 9:
            print("given input is not a number ranging 1 - 9")
            sleep(3)
            return False
        
        row, col = self.__translate_choice_to_board_location(choice_number)
        
        if self.board[row][col] != "x" and self.board[row][col] != "o":
            return True
        else:
            print("Position already taken!")
            sleep(3)
            return False

    def __update_board(self, choice):
        choice_number = int(choice)
        row, col = self.__translate_choice_to_board_location(choice_number)
        self.board[row][col] = self.current_player['mark']
        self.__update_board_to_draw(row, col)
    
    def __update_board_to_draw(self, row, col): 
        x = ["   ╲ ╱   ", "    ╳    ", "   ╱ ╲   "]
        o = ["  ▕▔▔▔▏  ", "  ▕ ▯ ▏  ", "  ▕▁▁▁▏  "]
        if row == 0 and col == 0:
            if self.board[row][col] == 'x':
                self.board_drawing[0][0] = x[0]
                self.board_drawing[1][0] = x[1]
                self.board_drawing[2][0] = x[2]
            else:
                self.board_drawing[0][0] = o[0]
                self.board_drawing[1][0] = o[1]
                self.board_drawing[2][0] = o[2]
        elif row == 0 and col == 1:
            if self.board[row][col] == 'x':
                self.board_drawing[0][2] = x[0]
                self.board_drawing[1][2] = x[1]
                self.board_drawing[2][2] = x[2]
            else:
                self.board_drawing[0][2] = o[0]
                self.board_drawing[1][2] = o[1]
                self.board_drawing[2][2] = o[2]
        elif row == 0 and col == 2:
            if self.board[row][col] == 'x':
                self.board_drawing[0][4] = x[0]
                self.board_drawing[1][4] = x[1]
                self.board_drawing[2][4] = x[2]
            else:
                self.board_drawing[0][4] = o[0]
                self.board_drawing[1][4] = o[1]
                self.board_drawing[2][4] = o[2]
        elif row == 1 and col == 0:
            if self.board[row][col] == 'x':
                self.board_drawing[4][0] = x[0]
                self.board_drawing[5][0] = x[1]
                self.board_drawing[6][0] = x[2]
            else:
                self.board_drawing[4][0] = o[0]
                self.board_drawing[5][0] = o[1]
                self.board_drawing[6][0] = o[2]
        elif row == 1 and col == 1:
            if self.board[row][col] == 'x':
                self.board_drawing[4][2] = x[0]
                self.board_drawing[5][2] = x[1]
                self.board_drawing[6][2] = x[2]
            else:
                self.board_drawing[4][2] = o[0]
                self.board_drawing[5][2] = o[1]
                self.board_drawing[6][2] = o[2]
        elif row == 1 and col == 2:
            if self.board[row][col] == 'x':
                self.board_drawing[4][4] = x[0]
                self.board_drawing[5][4] = x[1]
                self.board_drawing[6][4] = x[2]
            else:
                self.board_drawing[4][4] = o[0]
                self.board_drawing[5][4] = o[1]
                self.board_drawing[6][4] = o[2]
        elif row == 2 and col == 0:
            if self.board[row][col] == 'x':
                self.board_drawing[8][0] = x[0]
                self.board_drawing[9][0] = x[1]
                self.board_drawing[10][0] = x[2]
            else:
                self.board_drawing[8][0] = o[0]
                self.board_drawing[9][0] = o[1]
                self.board_drawing[10][0] = o[2]
        elif row == 2 and col == 1:
            if self.board[row][col] == 'x':
                self.board_drawing[8][2] = x[0]
                self.board_drawing[9][2] = x[1]
                self.board_drawing[10][2] = x[2]
            else:
                self.board_drawing[8][2] = o[0]
                self.board_drawing[9][2] = o[1]
                self.board_drawing[10][2] = o[2]
        elif row == 2 and col == 2:
            if self.board[row][col] == 'x':
                self.board_drawing[8][4] = x[0]
                self.board_drawing[9][4] = x[1]
                self.board_drawing[10][4] = x[2]
            else:
                self.board_drawing[8][4] = o[0]
                self.board_drawing[9][4] = o[1]
                self.board_drawing[10][4] = o[2]

    def __translate_choice_to_board_location(self, choice):
        row = 0
        col = 0

        if choice >= 1 and choice <= 3:
            row = 0
        elif choice >= 4 and choice <= 6:
            row = 1
        elif choice >= 7 and choice <= 9:
            row = 2

        if choice % 3 == 1:
            col = 0
        elif choice % 3 == 2:
            col = 1
        elif choice % 3 == 0:
            col = 2

        return row, col
    
    def check_win(self):
        board = self.board

        h_line1 = ''.join(board[0])
        h_line2 = ''.join(board[1])
        h_line3 = ''.join(board[2])

        v_line1 = board[0][0] + board[1][0] + board[2][0]
        v_line2 = board[0][1] + board[1][1] + board[2][1]
        v_line3 = board[0][2] + board[1][2] + board[2][2]

        d_line1 = board[0][0] + board[1][1] + board[2][2]
        d_line2 = board[2][0] + board[1][1] + board[0][2]

        if h_line1 == 'xxx' or h_line1 == 'ooo':
            return True
        elif h_line2 == 'xxx' or h_line2 == 'ooo':
            return True
        elif h_line3 == 'xxx' or h_line3 == 'ooo':
            return True
        elif v_line1 == 'xxx' or v_line1 == 'ooo':
            return True
        elif v_line2 == 'xxx' or v_line2 == 'ooo':
            return True
        elif v_line3 == 'xxx' or v_line3 == 'ooo':
            return True
        elif d_line1 == 'xxx' or d_line1 == 'ooo':
            return True
        elif d_line2 == 'xxx' or d_line2 == 'ooo':
            return True
        else:
            return False
    
    def check_board_full(self):
        for row in self.board:
            for col in row:
                if col == "":
                    return False
        return True

def clear():
    if name != "posix":
        system("cls")
    else:
        system("clear")

#clear screen at initiation game
clear()

# initiate game
ttt = TicTacToe()

# game flow
while True:
    clear()
    ttt.draw_title()
    ttt.draw_board()
    ttt.play_turn()
    clear()
    ttt.draw_title()
    ttt.draw_board()
    if ttt.check_win():
        print('Congratulations ' + ttt.current_player['name'] + ' has won the game')
        break
    elif ttt.check_win() == False and ttt.check_board_full() == True:
        print('nobody won')
        break

    ttt.swap_player()

