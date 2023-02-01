class TicTacToe:
    board_empty = [
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

    p1 = dict()
    p2 = dict()

    def __init__(self):
        self.board = TicTacToe.board_empty
        self.draw_title()
        self.p1["name"] = input("enter name player one: ")
        self.p1["mark"] = "x"
        self.p2["name"] = input("enter name player two: ")
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

        for row in self.board:
            # spacing centers game board under title
            current_board += "\t\t\t\t" + ''.join(row)
            current_board += '\n'
        
        print(current_board)