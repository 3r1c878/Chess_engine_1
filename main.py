from board.board import Board

def main():
    board = Board()
    while True:
        board.print_board()
        move = input("Enter your move (e.g. e2 e4): ").strip()
        if move.lower() in {"quit", "exit"}:
            break
        try:
            board.make_move(move)
        except ValueError as e:
            print("Invalid move:", e)

if __name__ == "__main__":
    main()
