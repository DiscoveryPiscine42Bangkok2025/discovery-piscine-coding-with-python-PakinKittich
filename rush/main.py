from checkmate import checkmate

def main():
    board1 = """\
R...
.K..
....
...B"""
    checkmate(board1)  # Expected: Success

    board2 = """\
P.
.K"""
    checkmate(board2)  # Expected: Fail


if __name__ == "__main__":
    main()
