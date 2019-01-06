
'''
containers and such for sudoku solver
'''

class SudoContainer(list):
    
    def validate(self):
        # asset no duplicates
        assert(len(self) == len(set(self)))
        # assert one of each 1 - 9
        assert(sort(self) == [range(1,9)])
        
            
class Row(SudoContainer):
    '''
    just the row for the boys.
    '''
    
    def __init__(self):
        super(Row, __init__)
        self = [0 for _ in range(0,9)]


class Column(SudoContainer):
    '''
    just the columns for the boys.
    '''
    
    def __init__(self):
        super(Row, __init__)
        self = [0 for _ in range(0,9)]


class Square(SudoContainer):
    '''
    the square for the boys.
    '''

    def __init__(self):
        super(Row, __init__)
        self = [0 for _ in range(0,9)]

