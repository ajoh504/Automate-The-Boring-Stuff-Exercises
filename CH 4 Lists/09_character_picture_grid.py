# The following grid is a list of lists.
# Write code that prints the grid as a picture.
# The arrow must be pointing down.


def print_arrow_down():
  grid =[['.', '.', '.', '.', '.', '.'],
         ['.', 'O', 'O', '.', '.', '.'],
         ['O', 'O', 'O', 'O', '.', '.'],
         ['O', 'O', 'O', 'O', 'O', '.'],
         ['.', 'O', 'O', 'O', 'O', 'O'],
         ['O', 'O', 'O', 'O', 'O', '.'],
         ['O', 'O', 'O', 'O', '.', '.'],
         ['.', 'O', 'O', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.']]

  for i in range(6):
    for j in range(9):
      print(grid[j][i], end='')
    print('\n')

print_arrow_down()
