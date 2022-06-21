import random

class tictac:
    def __init__(self):
        #initializing the empty board and variables for turns
        self.board = [" " for i in range(10)]
        self.playerTurn = "O"
        self.cpuTurn = "X"
        self.currentTurn = random.choice(["X", "O"])

    def getBoard(self):
        #returns a formatted version of the board
        joined = []
        for i in range(3):
            joined.append(f"⠀{self.board[1+3*i]}⠀|⠀{self.board[2+3*i]}⠀|⠀{self.board[3+3*i]}⠀")
        return "\n---------------\n".join(joined)

    def move(self, pos):
        #accepts commands to place a symbol on the board, switches between turns, calls on the ai after player turn
        self.board[int(pos)] = self.currentTurn
        self.currentTurn = "X" if self.currentTurn=="O" else "O"
        if self.currentTurn == "X":
            self.cpuInput()

    def cpuInput(self):
        '''
        the "ai" for the game
        it works in 4 steps, according to the priority:
        1. check whether the ai can make a winning move on this turn, if so, do it
        2. check whether the player can make a winning move on the next turn, if so, prevent it
        3. check whether the center if empty, if so, take it
        4. check whether a corner is empty, if so, take a random one
        if none of the above are possible, take a random square
        every step has a chance to be missed (the ai will instead pick a random square) to add a little spice
        '''
        possibleMoves = [x for x, letter in enumerate(self.board) if letter == " " and x != 0] #creates a list of empty squares

        if not self.isBoardFull():
            #double checks whether the board is full
            for turn in [self.cpuTurn, self.playerTurn]:
                #checks first whether the computer can win on this turn and secondly whether the player can win on the next
                for pos in possibleMoves:
                    boardCopy = self.board[:] #non-referential copy of the board
                    boardCopy[pos] = turn
                    if self.winCheck(boardCopy, turn):
                        if random.randint(1, 8) == 8: #1 in 8 chance the computer will not notice a winning turn
                            self.move(random.choice(possibleMoves))
                        else:
                            self.move(pos)
                            return

            openCorners = [x for x in possibleMoves if x in [1, 3, 7, 9]] #list of empty corners

            if 5 in possibleMoves:
                if random.randint(1, 4) == 4: #1 in 4 chance the computer will not take the center if it can
                    self.move(random.choice(possibleMoves))
                    return
                else:
                    self.move(5)
                    return

            if len(openCorners) > 0:
                if random.randint(1, 4) == 4: #1 in 4 chance the computer will not take the corner if it can
                    self.move(random.choice(possibleMoves))
                    return
                else:
                    self.move(random.choice(openCorners))
                    return
            else:
                self.move(random.choice(possibleMoves))
                return

    def winCheck(self, board, turn):
        #Checking whether the win condition is met
        return ((board[1] == board[2] == board[3] == turn) or
        (board[4] == board[5] == board[6] == turn) or
        (board[7] == board[8] == board[9] == turn) or
        (board[1] == board[4] == board[7] == turn) or
        (board[2] == board[5] == board[8] == turn) or
        (board[3] == board[6] == board[9] == turn) or
        (board[1] == board[5] == board[9] == turn) or
        (board[3] == board[5] == board[7] == turn))

    def isFree(self, pos):
        #checking whether the given square is empty
        return self.board[pos] == " "

    def isBoardFull(self):
        #checking whether the board is full
        return all(field != " " for field in self.board[1:])
