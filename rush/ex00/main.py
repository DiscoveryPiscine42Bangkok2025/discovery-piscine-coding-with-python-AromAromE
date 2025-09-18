from checkmate import checkmate

def main():

    board1 = """\
R...
.K..
..P.
....\
"""
    checkmate(board1)

    board2 = """\
..
.K\
"""
    checkmate(board2)

    board3 = """\
....
.PK.
....
....\
"""
    checkmate(board3)
    
    board4 = """\
B...
.K..
....
....\
"""
    checkmate(board4)

    board5 = """\
Q...
....
..K.
....\
"""
    checkmate(board5)

    board6 = """\
R...
P...
K...
....\
"""
    checkmate(board6)

    board7 = """\
...K...
...P...
...R...
.......\
"""
    checkmate(board7) 

    board8 = """\
....
.K..
P...
....\
"""
    checkmate(board8)

if __name__ == "__main__":
    main()