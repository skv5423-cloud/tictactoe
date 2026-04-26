class Point:
    def __init__(self, row, col):
        self.row = row
        self.col = col

class TicTacToe:
    """
    Gives users two options:
        - a regular game that can have ties or win by 3 diagonal, across a row, or down a column
        - an advanced game where player's can only have 3 marks on a board at a time
            - the first mark made will be removed when a fourth mark is added
            - same rules apply in order to win
            - game will continue and there are no ties
    """

    def __init__(self, mode):
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.x_turn = True
        self.hardMode = mode
        self.xPoints = []
        self.oPoints = []

    def __str__(self):
        return f"    0    1    2\n0 {self.board[0]}\n1 {self.board[1]}\n2 {self.board[2]}"
    
    __repr__ = __str__

    def tie(self):
        # check if there is a tie
        for row in self.board:
            if " " in row:
                return False
        
        print("Tie!")
        return True

    def checkWinner(self):
        """
        This function checks whether a player has won using the current marks on the board.
        Returns True if a player has won or there is a tie, False otherwise.
        """
        board = self.board
        # check for 3 in a row
        for row in board:
            if row[0] == row[1] == row[2] and row[0] != ' ':
                print(f'Player {row[0]} wins!')
                return True
            
        # check for 3 in a column
        for i in range(3):
            if board[0][i] == board[1][i] == board[2][i] and board[0][i] != ' ':
                print(f'Player {board[0][i]} wins!')
                return True
            
        # check diagonals
        if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
            print(f'Player {board[0][0]} wins!')
            return True
        
        if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
            print(f'Player {board[0][2]} wins!')
            return True
        
        return False
        
        
    
    def playerMove(self):
        """
        This function will obtain user input and verify whether they can place a mark on the designated spot.
        The function checks if the input is out of bounds or not a number.
        The function also checks if the spot is already taken.
        Once verified, it will call markBoard, to place a mark or delete one according to game rules.
        No returns
        """
        player = 'O'
        if self.x_turn:
            player = 'X'

        valid = False
        
        while not valid:
            try:
                row = int(input(f"Player {player}: Enter a row: "))

                col = int(input(f"Player {player}: Enter a column: "))

                # checks if row is not between 0 and 2
                if (row < 0 or row > 2):
                    print('Index for row out of bounds!')

                # checks if col is not between 0 and 2
                if (col < 0 or col > 2):
                    print('Index for column out of bounds!')

                # checks if spot is already taken
                elif self.board[row][col] != ' ':
                    print('Spot is alredy taken, try another one.')
                
                else:
                    # mark the board with player's mark
                    point = Point(row, col)
                    self.markBoard(point, player)

                    # switch player's turn
                    self.x_turn = not self.x_turn

                    valid = True

            except ValueError:
                print('Invalid input! Please enter a number 0 - 2!')



    def markBoard(self, point, player):
        """
        This function will mark the board with the player's mark given a Point object.
        If hard mode is on, and there are currently 3 of the player's marks on the board, one will be removed when the new one is added.
        No returns
        """

        # marks the board
        self.board[point.row][[point.col]] = player

        # for hard mode
        if self.hardMode:
            # point is added to memory
            if player == 'X':
                lst = self.xPoints
            else:
                lst = self.oPoints
            lst.append(point)

            # point is removed from the board and reset to a space
            if len(lst) == 4:
                del_point = lst.pop(0)
                self.board[del_point.row][del_point.col] = ' '



    def playGame(self):
        """
        This function keeps the game going until there is a winner.
        """
        has_won = False
        while not has_won and not self.tie():
            print(self)
            self.playerMove()
            has_won = self.checkWinner()

        print(f'Results:\n{self}')




def main():
    t = TicTacToe(False)
    t.playGame()

if __name__ == "__main__":
    main()