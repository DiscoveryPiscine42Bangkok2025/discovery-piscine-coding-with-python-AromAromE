def main():
    # Fixed the spacing issue in your board
    test = """\
....
.K..
....
....\
"""
    test = test.strip().split('\n')
    
    # Add some debug prints to see what's happening
    print("Raw board after split:")
    for i, line in enumerate(test):
        print(f"Line {i}: '{line}' (length: {len(line)})")
    
    # Convert to list of lists like a proper 2D board
    board = [list(line) for line in test]
    print(board)
    print(f"\nKing position: {find_king(board)}")

def find_king(board):
    print("Searching for King...")
    for row in range(len(board)):
        for col in range(len(board[row])):
            print(f"Checking position ({row}, {col}): '{board[row][col]}'")
            if board[row][col] == 'K':
                print(f"Found King at ({row}, {col})!")
                return (row, col)
    print("No King found!")
    return None

if __name__ == "__main__":
    main()