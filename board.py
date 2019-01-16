'''
The sudoku board
'''

from objs import *

class SudokuBoard(object):

    def __init__(self):
        self.rows = {"row_{0}".format(i) : Row() for i in range(1,10)}
        self.columns = {"col_{0}".format(i) : Column() for i in range(1,10)}
        self.squares = {"square_{0}".format(i) : Square() for i in range(1,10)}

    def __repr__(self):
        for row in self.rows:
            for number in self.rows[row]:
                print(number, sep=' | ')
            print('-'*27)

    def fill_starting_numbers(self, starting_numbers):
        '''
            takes in a list of starting numbers that are read as a top-left to bottom right 
            read through.  like how you would read a comic book!

            Empty spaces must be zero!

            returns: None
        '''
        row = -1
        col = 0
        square = -1
        for i, number in enumerate(starting_numbers):
            if i // 9 > row:
                row += 1
            col = i % 9
            if col % 3 == 0 and row % 3 == 0:
                square += 1
            print((row, col, square))
                


if __name__ == "__main__":
    # unit tests

    ############
    # test board prints
    ############

