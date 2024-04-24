
import pandas as pd
import numpy as np
import re
import math
import string




class Sudoku_str():

      def __init__(self):
            self.sudoku_dim = int(input())
            self.dict_df = {}
            self.change = int(math.sqrt(self.sudoku_dim))
            self.letters = list(string.ascii_uppercase[0:self.sudoku_dim])
            self.blocks = list(string.ascii_lowercase[0:self.sudoku_dim])
            self.block_letters = np.array(self.blocks).reshape(-1, self.change)
            print(self.block_letters)
            self.start_list = []
            base_points = 1
            self.a = 0
            self.b = 0
            self.row_tracker = 0
            self.col_tracker = 0

            for i in range(0, self.sudoku_dim):
                  self.start_list.append(base_points)


            for let_num in range(0, self.sudoku_dim):
                  self.col_tracker = self.col_tracker + 1
                  self.b = 0
                  self.row_tracker = 0
                  if self.col_tracker == self.change + 1:
                        self.a = self.a + 1
                        self.col_tracker = 1
                  for num in range(1, self.sudoku_dim + 1):
                        self.row_tracker = self.row_tracker + 1
                        if self.row_tracker == self.change + 1:
                              self.row_tracker = 1
                              self.b = self.b + 1
                        col_name = self.letters[let_num] + str(num) + self.block_letters[self.a][self.b] + 'y'
                        self.dict_df[col_name] = self.start_list

            self.str = pd.DataFrame(self.dict_df)

      def give_cols(self):
            return self.str.columns 


      def print_df(self):
            print(self.str)

      def change_val(self, row, col, val):
            self.str.loc[row, col] = val

      def get_current_value(self, row, col):
            return self.str[col].iloc[row]

class Queue:
     
    def __init__(self) -> None:
            self.array = []

    def add(self, cell):
            self.array.append(cell)


    def delete(self):
            self.array = self.array[1:]

    def print_queue(self):
          for each in self.array:
                print(each)

    def is_empty(self):
          return len(self) == 0


class Solve_Sudoku():
      
        '''   

        Algorithm Sudokode

        1. Make the whole data structure 
        2. Take in input of a number x in a cell y
        3. Make the probability of number x in cell y 100% and 0% for all numbers  other than x. Chnage the corresponding box, row and column such that the probability of x being in them becomes 0. 
        4. If a cell has the probability of one number in it being 100 and others being 0, mark it dead.
        5. Change the probability of all cells where the the probability of a number being in that cell has become 0 using a queue. At all times the total probability of a cll having a number should be 100. 
        6. If the probability of a cell containing a particular number becomes 100, add it to the queue and redo steps 2 - 6
        7. Redo steps 2 - 6 until each cell has a probability for sure. 



        '''

        def __init__(self):
              self.table = Sudoku_str()
              self.cells_solved = 0
              self.cells_tobe_solved = self.table.sudoku_dim * self.table.sudoku_dim
              self.puzzle = pd.DataFrame()
              self.solution = pd.DataFrame()
              self.make_puzzle()
              self.operating_queue = Queue()
              self.all_cols = self.table.give_cols()
              self.size = self.table.sudoku_dim
        

        def make_puzzle(self):
              letters = list(string.ascii_uppercase[0:self.table.sudoku_dim])
              for letter in letters:
                    self.puzzle[letter] = list(np.zeros((self.table.sudoku_dim, 1)))
                    self.solution[letter] = [] 

        def get_input(self):
              
              '''
              - Takes input
              - Splits it into row, column and number 
              - adds the input to operating queue
              - adds it to puzzle or problem 
              - adds it to puzzle solution 
              - changes the number of cells solved 
              - adds it to the dataframe and marks the cell as dead by using regex to search the columns using row and col number 
              '''
              a = input("Enter the info:").split(' ')
              col = a[0][0]
              row = int(a[0][1]) - 1
              number = int(a[1])
              self.operating_queue.add(a)
              self.operating_queue.print_queue()
              self.puzzle.loc[row, col] = number
              self.solution.loc[row, col] = number
              self.cells_solved = self.cells_solved + 1
              col_df = ''
              for col_name in self.all_cols:
                  pattern = col + str(row + 1) + '..'
                  match = re.match(pattern, col_name)
                  if match:
                        col_df = match.group()  # Change 0 to specify a different group if needed
                        self.change_to_max(col_df, number)
                        break
      
        def change_to_max(self, cell, number):
             row_index = number - 1
             self.table.change_val(row_index, cell, self.size)
             all_cells = self.find_associated(cell)
             traverse = 0
             while all_cells.is_empty() == False:
                   self.change_to_min(all_cells[traverse], number)
                   traverse = traverse + 1             

        
        def change_to_min(self, cell, number):
             row_index = list(cell)[1]
             current_val = self.table.get_current_value(row_index, cell)
             self.table.change_val(row_index, cell, 0)
             for i in range[0:self.table.sudoku_dim]:
                   if i!=row_index:
                         self.table.change_val(i, cell, current_val + 1 )

        def find_associated(self, cell):
            associated_cells = Queue()
            temp = list(cell)
            column = temp[0]
            row = temp[1]
            block = temp[2]
            notcol = '[^' + column + ']'
            notrow = '[^' + row + ']'
            pattern1 = re.compile(column + notrow + '.' + 'y')
            pattern2 = re.compile(notcol + row + '.' + 'y')
            pattern3 = re.compile(notcol + notrow + block + 'y')

            #Efficiency Point: Can we reconstruct the names of all associated cells? Yes we can ... ugh hard algo to code 

            for col_name in self.all_cols:
                  match1 = re.match(pattern1, col_name)
                  match2 = re.match(pattern2, col_name)
                  match3 = re.match(pattern3, col_name)
                  if match1:
                        associated_cells.add(match1.group(0))
                  elif match2:
                         associated_cells.add(match2.group(0))
                  elif match3:
                         associated_cells.add(match3.group(0))
            return associated_cells
        
        def change_status(self, cell):
              #changes the status of cell from alive to dead
              pass      

        def solve():
              pass

obj1 = Solve_Sudoku()
obj1.get_input()
obj1.get_input()




        








