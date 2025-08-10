class Board():
    def __init__(self):
        self.board = []
        for i in range(8):
            row = []
            for j in range(8):
                row.append('')
            self.board.append(row)


        for j in range(8):
            self.board[1][j] = 'Pblk'
            self.board[6][j] = 'Pwht'

        self.board[0][0] = self.board[0][7] = 'Rblk'
        self.board[7][0] = self.board[7][7] = 'Rwht'

        self.board[0][1] = self.board[0][6] = 'Knblk'
        self.board[7][1] = self.board[7][6] = 'Knwht'

        self.board[0][2] = self.board[0][5] = 'Bblk'
        self.board[7][2] = self.board[7][5] = 'Bwht'

        self.board[0][3] = 'Qblk'
        self.board[7][3]  = 'Qwht'

        self.board[0][4] = 'Kiwht'
        self.board[7][4] = 'Kiwht'




