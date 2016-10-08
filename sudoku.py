from copy import deepcopy
from sys import argv


class Board:
    """
    represents sudoku board
    """
    
    def __init__(self, config=None):
        if config == None:
            config = [['.' for i in range(9)] for i in range(9)]
            
        self.config = config
        
        vert = [['.' for i in range(9)] for i in range(9)]
        for i in range(9):
            for j in range(9):
                vert[i][j] = self.config[j][i]
                
        self.vert = vert
        
        boxes = [['.' for i in range(9)] for i in range(9)]
        for i in range(9):
            for j in range(9):
                box_coords = configToBoxes([i,j])
                boxes[box_coords[0]][box_coords[1]] = self.config[i][j]
                
        self.boxes = boxes
        
    def updateNumbers(self):
        vert = [['.' for i in range(9)] for i in range(9)]
        for i in range(9):
            for j in range(9):
                vert[i][j] = self.config[j][i]
                
        self.vert = vert
        
        boxes = [['.' for i in range(9)] for i in range(9)]
        for i in range(9):
            for j in range(9):
                box_coords = configToBoxes([i,j])
                boxes[box_coords[0]][box_coords[1]] = self.config[i][j]
                
        self.boxes = boxes
        
        
        
    def __str__(self):
        s = ("{0[0]} {0[1]} {0[2]} | {0[3]} {0[4]} {0[5]} | {0[6]} {0[7]} {0[8]} \n" +
            "{1[0]} {1[1]} {1[2]} | {1[3]} {1[4]} {1[5]} | {1[6]} {1[7]} {1[8]} \n" +
            "{2[0]} {2[1]} {2[2]} | {2[3]} {2[4]} {2[5]} | {2[6]} {2[7]} {2[8]} \n" +
            "= = = + = = = + = = = \n" +
            "{3[0]} {3[1]} {3[2]} | {3[3]} {3[4]} {3[5]} | {3[6]} {3[7]} {3[8]} \n" +
            "{4[0]} {4[1]} {4[2]} | {4[3]} {4[4]} {4[5]} | {4[6]} {4[7]} {4[8]} \n" +
            "{5[0]} {5[1]} {5[2]} | {5[3]} {5[4]} {5[5]} | {5[6]} {5[7]} {5[8]} \n" +
            "= = = + = = = + = = = \n" + 
            "{6[0]} {6[1]} {6[2]} | {6[3]} {6[4]} {6[5]} | {6[6]} {6[7]} {6[8]} \n" + 
            "{7[0]} {7[1]} {7[2]} | {7[3]} {7[4]} {7[5]} | {7[6]} {7[7]} {7[8]} \n" + 
            "{8[0]} {8[1]} {8[2]} | {8[3]} {8[4]} {8[5]} | {8[6]} {8[7]} {8[8]} \n").format(*(self.config))
            
        return s
    
def placeNumber(board, number, coordinates):
    
    board.config[coordinates[0]][coordinates[1]] = number
    board.updateNumbers()
    
    
def configToBoxes(lst):
    """
    Takes in a list of one coordinate from the original
    'horizontal' board config and returns the coordinates in 'box'
    coordinates
    """
    i = lst[0]
    j = lst[1]
    if i == 0:
        if j == 0:
            return [0,0]
        if j == 1:
            return [0,1]
        if j == 2:
            return [0,2]
        if j == 3:
            return [1,0]
        if j == 4:
            return [1,1]
        if j == 5:
            return [1,2]
        if j == 6:
            return [2,0]
        if j == 7:
            return [2,1]
        if j == 8:
            return [2,2]
    if i == 1:
        if j == 0:
            return [0,3]
        if j == 1:
            return [0,4]
        if j == 2:
            return [0,5]
        if j == 3:
            return [1,3]
        if j == 4:
            return [1,4]
        if j == 5:
            return [1,5]
        if j == 6:
            return [2,3]
        if j == 7:
            return [2,4]
        if j == 8:
            return [2,5]
    if i == 2:
        if j == 0:
            return [0,6]
        if j == 1:
            return [0,7]
        if j == 2:
            return [0,8]
        if j == 3:
            return [1,6]
        if j == 4:
            return [1,7]
        if j == 5:
            return [1,8]
        if j == 6:
            return [2,6]
        if j == 7:
            return [2,7]
        if j == 8:
            return [2,8]
        
    if i == 3:
        if j == 0:
            return [3,0]
        if j == 1:
            return [3,1]
        if j == 2:
            return [3,2]
        if j == 3:
            return [4,0]
        if j == 4:
            return [4,1]
        if j == 5:
            return [4,2]
        if j == 6:
            return [5,0]
        if j == 7:
            return [5,1]
        if j == 8:
            return [5,2]
    if i == 4:
        if j == 0:
            return [3,3]
        if j == 1:
            return [3,4]
        if j == 2:
            return [3,5]
        if j == 3:
            return [4,3]
        if j == 4:
            return [4,4]
        if j == 5:
            return [4,5]
        if j == 6:
            return [5,3]
        if j == 7:
            return [5,4]
        if j == 8:
            return [5,5]
    if i == 5:
        if j == 0:
            return [3,6]
        if j == 1:
            return [3,7]
        if j == 2:
            return [3,8]
        if j == 3:
            return [4,6]
        if j == 4:
            return [4,7]
        if j == 5:
            return [4,8]
        if j == 6:
            return [5,6]
        if j == 7:
            return [5,7]
        if j == 8:
            return [5,8]
    if i == 6:
        if j == 0:
            return [6,0]
        if j == 1:
            return [6,1]
        if j == 2:
            return [6,2]
        if j == 3:
            return [7,0]
        if j == 4:
            return [7,1]
        if j == 5:
            return [7,2]
        if j == 6:
            return [8,0]
        if j == 7:
            return [8,1]
        if j == 8:
            return [8,2]
    if i == 7:
        if j == 0:
            return [6,3]
        if j == 1:
            return [6,4]
        if j == 2:
            return [6,5]
        if j == 3:
            return [7,3]
        if j == 4:
            return [7,4]
        if j == 5:
            return [7,5]
        if j == 6:
            return [8,3]
        if j == 7:
            return [8,4]
        if j == 8:
            return [8,5]
        
    if i == 8:
        if j == 0:
            return [6,6]
        if j == 1:
            return [6,7]
        if j == 2:
            return [6,8]
        if j == 3:
            return [7,6]
        if j == 4:
            return [7,7]
        if j == 5:
            return [7,8]
        if j == 6:
            return [8,6]
        if j == 7:
            return [8,7]
        if j == 8:
            return [8,8]
    
def isFull(board):
    for x in board.config:
        for y in x:
            if y == '.':
                return False
        
    return True

def isGoal(board):
    return isFull(board) and isValid(board)

def isValid(board):
    for row in board.config:
        for i in range(9):
            if row.count(i) > 1:
                return False
            
    for col in board.vert:
        for i in range(9):
            if col.count(i) > 1:
                return False
    
    for box in board.boxes:
        for i in range(i):
            if box.count(i) > 1:
                return False
        
        
    
    return True
        

def getSuccessors(board):
    successors = []
    for i in range(9):
        for j in range(9):
            if board.config[i][j] == '.':
                for k in range(1,10):
                    boxes_coords = configToBoxes([i,j])
                    if k not in board.config[i] and k not in board.vert[j] and k not in board.boxes[boxes_coords[0]]:
                        newBoard = deepcopy(board)
                        newBoard.config[i][j] = k
                        newBoard.vert[j][i] = k
                        newBoard.boxes[boxes_coords[0]][boxes_coords[1]] = k
                        successors.append(newBoard)
                        
                return successors     
                
    

def solve(config):
    """
    Generic backtracking solver.
        config: the current config
    Returns:  A config, if valid, None otherwise
    """
    
    if isGoal(config):
        return config
    else:
        for successor in getSuccessors(config):
            if isValid(successor):
                #if debug: print('Valid Successor:\n' + str(successor))
                solution = solve(successor)
                if solution != None:
                    return solution
        
def main():
    
    # example puzzle
    """
    d = [['.' for i in range(9)] for i in range(9)]
    d[0][4] = 5
    d[0][7] = 9
    d[1][2] = 6
    d[1][5] = 2
    d[1][6] = 5
    d[2][1] = 7
    d[2][5] = 9
    d[2][7] = 6
    d[3][1] = 9
    d[3][6] = 3
    d[4][1] = 4
    d[4][2] = 5
    d[4][4] = 3
    d[4][6] = 9
    d[4][7] = 1
    d[5][2] = 1
    d[5][7] = 2
    d[6][1] = 1
    d[6][3] = 8
    d[6][7] = 4
    d[7][2] = 2
    d[7][3] = 9
    d[7][6] = 1
    d[8][2] = 3
    d[8][4] = 7
    """
    
    b = Board()
    print('Initial Config:\n' + str(b))
    ans = input("Would you like to create your own sudoku board? (y/n)")
    while (ans.lower() != "y" and ans.lower() != "n"):
        ans = input("Would you like to create your own sudoku board? (y/n)")
        
    if ans.lower() == "y":
        ans=input('Enter the coordinates of a square like "3,2" without the quotes ("q" to quit): ').lower()
        num = ""
        while(ans != "q" and num != "q"):
            nums = ans.split(',')
            if nums[0].isdigit() == False or nums[1].isdigit() == False:
                print('The coordinates must be numbers and of the form "digit,digit"')
            elif int(nums[0]) < 0 or int(nums[0]) > 8 or int(nums[1]) < 0 or int(nums[0]) > 8:
                print('The coordinates must be within the range 0-8')
            nums[0] = int(nums[0])
            nums[1] = int(nums[1])
            num=input('Enter a number for ' +str(nums) + ' ("q" to quit): ' ).lower()
            if num == 'q':
                break
            num = int(num)
            placeNumber(b, num, nums)
            print('Initial Config:\n' + str(b))
            ans=input('Enter the coordinates of a square like "3,2" without the quotes ("q" to quit):').lower()
            nums = ans.split(',')
            
    # read and display the initial board
    
    initConfig = b
    print('Initial Config:\n' + str(initConfig))
    
    
    # solve the puzzle
    solution = solve(initConfig)
    
    # display the solution, if one exists
    if solution != None:
        print('Solution:\n' + str(solution))
    else:
        print('No solution.')
        
    
    
main()
    
