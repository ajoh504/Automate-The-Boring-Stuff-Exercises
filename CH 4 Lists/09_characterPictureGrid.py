# The following grid is a list of lists.
# Write code that prints the grid as a picture.
#
# Notes: i represents each nested list. j represents
# each string within the nested lists. len(list[i])
# tells the loop to set the range as the length of each
# nested list. print(list[i][j]) where i = 0 and j = 0 
# prints the very top left of the grid. Since j is the 
# nested for loop, j iterates first, thereby printing
# the list at index 0, a.k.a. the first list. When j 
# is finished iterating, i increments from 0 to 1, thereby
# printing all values inside the second list.

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


def printGrid(list):
  for i in range(len(list)):
    for j in range(len(list[i])):
      print(list[i][j] + '  ', end='')
    print('\n')

printGrid(grid)
