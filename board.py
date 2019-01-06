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

