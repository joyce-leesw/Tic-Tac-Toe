class tictactoe:
    def __init__ (self, render= True):
        self.board = [[0,0,0] for i in range(3)]
        self.render = render
        self.player = 1
        self.repr = {0: ".", 1: "X", -1: "O"}

    def get_player(self):
        player = ''
        key = ''
        while player not in ('Y' or 'N'):
            player = input("Would you like to go first? Y/N?: ")
            player = player.upper()
            if player not in ('Y' or 'N'):
                print("Invalid Key")

        key = input("Please select your key. X or O?: ")
        key = key.upper()

        if key == 'O':
            self.player *= -1
        print(f"Your key is {key}")
        return key
    
    def is_winner(self):
        win = None
        # rows
        for row in range(3):
            if abs(sum(self.board[row])) == 3:
                win = self.board[row][0]

        # # columns    
        for column in range(3):
            if abs(sum([row[column] for row in self.board]))  == 3:
                win = self.board[0][column]

        # diagonals
        if abs(sum([self.board[row][row] for row in range(3)])) == 3:
            win = self.board[0][0]

        if abs(sum([self.board[row][2- row] for row in range(3)])) == 3:
            win = self.board[0][2]

        return win
    
    def state(self):
        return str(self.board)

    def valid_moves(self):
        move = []
        for row in range(3):
            for column in range(3):
                if self.board[row][column] == 0:
                    move.append((row, column))
        return move

    def get_end(self):
        for row in range(3):
            for column in range(3):
                if self.board[row][column] == 0:
                    return False
        return True
    
    def show_board(self):
        for row in self.board:
            for column in row:
                print(self.repr[column], end="\t")
            print("\n")

    def play(self):
        key = self.get_player()
        while True:
            if self.render:
                self.show_board()
                print(f"Player {self.repr[self.player]} turn")

            
            flag = 1
            while flag == 1:
            # # select a position
                x, y = list(map(int, input("Choose a position: ").split()))
                if self.board[x][y] != 0:
                    print("You can't go there. Go again.")
                else:
                    flag = 0
            self.board[x][y] = self.player

            # checking whether current player is won or not
            if self.is_winner():
                # show final board
                self.show_board()
                print(f"Player {self.repr[self.player]} wins the game!")
                return self.is_winner()

            # checking whether the game is draw or not
            if self.get_end():
                self.show_board()
                print("It's a tie!")
                break

            self.player *= -1
        return None

# starting the game
tic_tac_toe = tictactoe()
tic_tac_toe.play()

