from tkinter import *
from tkinter import messagebox
from python_chess_game import *
import pygame

def show_chess_board(start_screen):
    global current_turn
    current_turn = 'white'
    buttons = []
    selected_piece=None
    selected_old_piece=[]

    chess_board = Toplevel()
    chess_board.geometry('800x800')
    chess_board.title('Chess Game')
    pygame.mixer.init()
    game_sound_aa = pygame.mixer.Sound("click_soundd.wav")


    label = Label(chess_board, text="Welcome to Chess!", font=("Arial", 24))
    label.grid(row=0, column=0, columnspan=8, pady=10)

    def restart_game():
        chess_board.destroy()
        show_chess_board(None)

    restart_button = Button(chess_board,bg= "steelblue", text="Restart", font=("Arial", 12),foreground="white", command=restart_game)
    restart_button.grid(row=9, column=3, columnspan=2, pady=10)

    turn_label = Label(chess_board,text="Turn : "+ current_turn, font=("Arial", 12 ),foreground="white", bg="steelblue")
    turn_label.grid(row=10, column=3, columnspan=2)

    pawns_white = PhotoImage(file='pawnswhite.png').subsample(25)
    pawns_black = PhotoImage(file='pawnsblack.png').subsample(25)

    rook_white = PhotoImage(file='rookwhite.png').subsample(25)
    rook_black = PhotoImage(file='rookblack.png').subsample(25)

    knight_white = PhotoImage(file='knightwhite.png').subsample(25)
    knight_black = PhotoImage(file='knightblack.png').subsample(25)

    bishops_white = PhotoImage(file='bishopwhite.png').subsample(25)
    bishops_black = PhotoImage(file='bishopblack.png').subsample(25)

    queen_white = PhotoImage(file='queenwhite.png').subsample(25)
    queen_black = PhotoImage(file='queenblack.png').subsample(25)

    king_white = PhotoImage(file='kingwhite.png').subsample(25)
    king_black = PhotoImage(file='kingblack.png').subsample(25)

    for i in range(8):
        chess_board.rowconfigure(i, weight=1)
        chess_board.columnconfigure(i, weight=1)

    class Board():
        def __init__(self):
            self.board = []
            for i in range(8):
                row = []
                for j in range(8):
                    row.append(None)
                self.board.append(row)

            for j in range(8):
                self.board[1][j] = Pawn('black', (1, j), has_moved=False)
                self.board[6][j] = Pawn('white', (6, j), has_moved=False)

            self.board[0][0] = Rook('black', (0, 0), has_moved=False)
            self.board[0][7] = Rook('black', (0, 7), has_moved=False)
            self.board[7][0] = Rook('white', (7, 0), has_moved=False)
            self.board[7][7] = Rook('white', (7, 7), has_moved=False)

            self.board[0][1] = Knight('black', (0, 1), has_moved=False)
            self.board[0][6] = Knight('black', (0, 6), has_moved=False)
            self.board[7][1] = Knight('white', (7, 1), has_moved=False)
            self.board[7][6] = Knight('white', (7, 6), has_moved=False)

            self.board[0][2] = Bishop('black', (0, 2), has_moved=False)
            self.board[0][5] = Bishop('black', (0, 5), has_moved=False)
            self.board[7][2] = Bishop('white', (7, 2), has_moved=False)
            self.board[7][5] = Bishop('white', (7, 5), has_moved=False)

            self.board[0][3] = Queen('black', (0, 3), has_moved=False)
            self.board[7][3] = Queen('white', (7, 3), has_moved=False)

            self.board[0][4] = King('black', (0, 4), has_moved=False)
            self.board[7][4] = King('white', (7, 4), has_moved=False)

    chess = Board()
    buttons = []
    def check_game_over(row, col):
        target_piece = chess.board[row][col]
        if isinstance(target_piece, King):
            winner = "black" if target_piece.color == "white" else "white"
            messagebox.showinfo("Game Over\n King was captured Game Over \n","the Winner is : "+winner)
            chess_board.destroy()

    selected_piece = None
    selected_coord_piece = None

    def click(row, col):
        nonlocal selected_piece , selected_coord_piece , turn_label
        global current_turn
        cell = chess.board[row][col]

        if selected_coord_piece is not None:
            old_row, old_col = selected_coord_piece
            original_color = "WhiteSmoke" if (old_row + old_col) % 2 == 0 else "#42473d"
            buttons[old_row][old_col].config(bg=original_color)

        if selected_piece is None and cell:
            if cell.color == current_turn:
              selected_piece = cell
              selected_coord_piece = (row, col)
              buttons[row][col].config(bg="lightblue")
        elif selected_piece is not None:
            from_row, from_col = selected_coord_piece

            if is_valid_move(selected_piece, from_row, from_col, row, col):
                check_game_over(row, col)

                chess.board[row][col] = selected_piece
                chess.board[from_row][from_col] = None

                buttons[row][col].config(image=get_piece_image(selected_piece))
                buttons[from_row][from_col].config(image='')
                game_sound_aa.play()

                current_turn = 'black' if current_turn == 'white' else 'white'
                turn_label.config(text="Turn : "+current_turn)

            original_color = "WhiteSmoke" if (from_row + from_col) % 2 == 0 else "#42473d"
            buttons[from_row][from_col].config(bg=original_color)
            selected_piece = None
            selected_coord_piece = None


    def is_valid_move(piece, from_row, from_col, to_row, to_col):
        if isinstance(piece, Pawn):
            direction = -1 if piece.color == 'white' else 1
            start_row = 6 if piece.color == 'white' else 1

            if to_row == from_row + direction and to_col == from_col:
                if chess.board[to_row][to_col] is None:
                    return True

            if from_row == start_row and to_row == from_row + 3 * direction and to_col == from_col:
                if (chess.board[from_row + direction][to_col] is None and
                        chess.board[to_row][to_col] is None):
                    return True

            if to_row == from_row + direction and abs(to_col - from_col) == 1:
                target = chess.board[to_row][to_col]
                if target is not None and target.color != piece.color:
                    return True

        if isinstance(piece, Rook):

            if from_row == to_row or from_col == to_col:
                step_row = 0 if from_row == to_row else (1 if to_row > from_row else -1)
                step_col = 0 if from_col == to_col else (1 if to_col > from_col else -1)

                r, c = from_row + step_row, from_col + step_col
                while (r, c) != (to_row, to_col):
                    if chess.board[r][c] is not None:
                        return False
                    r += step_row
                    c += step_col

                target = chess.board[to_row][to_col]
                return target is None or target.color != piece.color
        if isinstance(piece, Knight):
            target = chess.board[from_row][from_col]
            row_k = abs(to_row - from_row)
            col_k = abs(to_col - from_col)
            if (row_k, col_k) in [(2, 1), (1, 2)]:
                if target is None or target.color != piece.color:
                    return True
        if isinstance(piece, Bishop):
            target = chess.board[to_row][to_col]
            if abs(to_row - from_row) == abs(to_col - from_col):
                step_row = 1 if to_row > from_row else -1
                step_col = 1 if to_col > from_col else -1

                r, c = from_row + step_row, from_col + step_col
                while (r, c) != (to_row, to_col):
                    if chess.board[r][c] is not None:
                        return False
                    r += step_row
                    c += step_col

                target = chess.board[to_row][to_col]
                return target is None or target.color != piece.color
        if isinstance(piece, Queen):
            target = chess.board[to_row][to_col]
            if from_row == to_row or from_col == to_col or abs(to_row - from_row) == abs(to_col - from_col):
                step_row = 0 if from_row == to_row else (1 if to_row > from_row else -1)
                step_col = 0 if from_col == to_col else (1 if to_col > from_col else -1)

                r, c = from_row + step_row, from_col + step_col
                while (r, c) != (to_row, to_col):
                    if chess.board[r][c] is not None:
                        return False
                    r += step_row
                    c += step_col

                target = chess.board[to_row][to_col]
                return target is None or target.color != piece.color
        if isinstance(piece, King):
            target = chess.board[to_row][to_col]
            if abs(to_row - from_row) <= 1 and abs(to_col - from_col) <= 1:
                if target is None or target.color != piece.color:
                    return True

            return False


    def get_piece_image(cell):
        if cell is None:
            return None

        if isinstance(cell, Pawn):
            return pawns_white if cell.color == 'white' else pawns_black
        elif isinstance(cell, Rook):
            return rook_white if cell.color == 'white' else rook_black
        elif isinstance(cell, Knight):
            return knight_white if cell.color == 'white' else knight_black
        elif isinstance(cell, Bishop):
            return bishops_white if cell.color == 'white' else bishops_black
        elif isinstance(cell, Queen):
            return queen_white if cell.color == 'white' else queen_black
        elif isinstance(cell, King):
            return king_white if cell.color == 'white' else king_black
        else:
            return None

    for i in range(8):
        row_button = []
        for j in range(8):
            if (i + j) % 2 == 0:
                color = "WhiteSmoke"
            else:
                color = "#42473d"
            cell = chess.board[i][j]
            image = get_piece_image(cell)

            if image:
                piece = Button(chess_board, image=image, bg=color, command=lambda r=i, c=j: click(r, c))
                piece.image = image
            else:
                piece = Button(chess_board, bg=color, command=lambda r=i, c=j: click(r, c))
            piece.grid(row=i, column=j, padx=0, pady=0, sticky=NSEW)
            row_button.append(piece)
        buttons.append(row_button)


