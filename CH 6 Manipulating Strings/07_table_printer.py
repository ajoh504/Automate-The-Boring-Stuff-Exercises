'''
-- table printer --

This function takes a list of lists and prints them in
columns using a right-justified format. The columns must be printed
as rows, left to right. To do this, the function will perform
the following tasks:

1. Determine maximum string length to provide an argument for the
rjust() method. This determines the width of the columns
2. Determine row length as list length, and column length of inner lists
3. Store all strings in a single list, then print them, incrementing by
the length of columns
4. Print each row right justified using the maximum string length.
'''

table_data = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def print_table(table_arg: list) -> str:
    length_of_strings = [] # list for each string length
    longest_str = 0 # Store the longest string length
    all_strings = [] = [] # Final strings to print 
    column_len = len(table_arg[0])
    row_len = len(table_arg)

    
    # Append length of each string to list_of_strings
    # Then sort list_of_lengths to find the longest string length
    for i in range(row_len): 
        for j in range(column_len):
            length_of_strings.append(len(table_arg[i][j]))
            all_strings.append(table_arg[i][j]) # store strings in one list.
    length_of_strings.sort()
    longest_str = length_of_strings[-1]

    #loop through all_strings incrementing by length of columns
    for i in range(column_len):
        for j in range(i, len(all_strings), column_len):
            print(all_strings[j].rjust(longest_str), end='')
        print('\n')
            
print_table(table_data)
