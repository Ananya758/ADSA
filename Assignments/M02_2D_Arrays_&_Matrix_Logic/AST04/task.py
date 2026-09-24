def diagonalSort(mat):
    rows = len(mat)
    cols = len(mat[0])

    # Sort diagonals starting from the first column
    for start_row in range(rows):
        r, c = start_row, 0
        values = []

        while r < rows and c < cols:
            values.append(mat[r][c])
            r += 1
            c += 1

        values.sort()

        r, c = start_row, 0
        for value in values:
            mat[r][c] = value
            r += 1
            c += 1

    # Sort diagonals starting from the top row
    for start_col in range(1, cols):
        r, c = 0, start_col
        values = []

        while r < rows and c < cols:
            values.append(mat[r][c])
            r += 1
            c += 1

        values.sort()

        r, c = 0, start_col
        for value in values:
            mat[r][c] = value
            r += 1
            c += 1

    return mat


if __name__ == '__main__':
    m, n = map(int, input().split())
    mat = []

    for i in range(m):
        mat.append(list(map(int, input().split())))

    print(diagonalSort(mat))
