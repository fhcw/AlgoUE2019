import sys
input_file = sys.argv[1]


####FUNCTIONS####

def optimize_grid(grid_list):
    new_grid_list = []
    for i in grid_list:
        line = i.split()
        line = list(map(float, line))
        new_grid_list.append(line)
    return new_grid_list


def manhattan(v, h, d, rows, columns):        # v = down grid, h = right grid, d = diagonal grid
    grid = []
    for i in range(0, rows):                  # fill empty grid with correct size
        grid.append([0] * columns)

    grid[0][0] = 0                            # fill first row and first column
    for i in range(1, rows):
        grid[i][0] = grid[i - 1][0] + v[i - 1][0]
    for j in range(1, columns):
        grid[0][j] = grid[0][j - 1] + h[0][j - 1]

    for i in range(1, rows):                  # fill rest
        for j in range(1, columns):
            grid[i][j] = max(grid[i - 1][j] + v[i - 1][j], grid[i][j - 1] + h[i][j - 1], grid[i - 1][j - 1] + d[i - 1][j - 1])

    print(grid[rows - 1][columns - 1])


####MAIN_FUNCTION####

def extract_and_calc_grid(user_file):
    with open(user_file, 'r') as input:        # open file
        content = input.read()                 # read file
        file = content.rstrip('\n')            # remove new lines in file
        file = file.split('\n')                # split at new lines
        down = []                              # make empty lists
        right = []
        diag = []
        for line in file:                      # iterate until you reach ---, this is now down grid
            down.append(line)
            if line == '---':
                break

        size_down = len(down)                          # save length of gdown
        for line in file[size_down:len(file)]:         # iterate from end of down to get right grid
            right.append(line)
            if line == '---':
                break

        size = len(down) + len(right)

        for line in file[size:len(file)]:
            diag.append(line)
            if line == '---':
                break

    g_down = down[1:len(down)-1]               # save g_down but cut out header and ---
    g_right = right[1:len(right)-1]            # save g_right but cut out header and ---
    g_diag = diag[1:len(diag)-1]

    size_of_grid = len(g_right)                # length of g_right gives correct size of grid

    g_down = optimize_grid(g_down)
    g_right = optimize_grid(g_right)
    g_diag = optimize_grid(g_diag)

    manhattan(g_down, g_right, g_diag, size_of_grid, size_of_grid)

    return 0


if __name__ == '__main__':
    extract_and_calc_grid(input_file)



