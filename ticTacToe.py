class TicTacToe:
    board_empty = [
        [" 1 ", "║", " 2 ", "║", " 3 ",],
        ["═══", "╬", "═══", "╬", "═══",],
        [" 4 ", "║", " 5 ", "║", " 6 ",],
        ["═══", "╬", "═══", "╬", "═══",],
        [" 7 ","║", " 8 ", "║", " 9 ",]
    ]

    def __init__(self):
        self.board = TicTacToe.board_empty
        self.draw_title()
        self.p1 = input("enter name player one: ")
        self.p2 = input("enter name player two: ")

    def draw_title(self):
        print("""

 ______   __     ______        ______   ______     ______        ______   ______     ______       
/\__  _\ /\ \   /\  ___\      /\__  _\ /\  __ \   /\  ___\      /\__  _\ /\  __ \   /\  ___\      
\/_/\ \/ \ \ \  \ \ \____     \/_/\ \/ \ \  __ \  \ \ \____     \/_/\ \/ \ \ \/\ \  \ \  __\      
   \ \_\  \ \_\  \ \_____\       \ \_\  \ \_\ \_\  \ \_____\       \ \_\  \ \_____\  \ \_____\    
    \/_/   \/_/   \/_____/        \/_/   \/_/\/_/   \/_____/        \/_/   \/_____/   \/_____/    
                                                                                                  

""")
    