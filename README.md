**Essentially an application to solve sudoku using probability and data frames**

Here is the SudoKode: 


        1. Make the whole data structure 
        2. Take in input of a number x in a cell y
        3. Make the probability of number x in cell y 100% and 0% for all numbers  other than x. Chnage the corresponding box, row and column such that the probability of x being in them becomes 0. 
        4. If a cell has the probability of one number in it being 100 and others being 0, mark it dead.
        5. Change the probability of all cells where the the probability of a number being in that cell has become 0 using a queue. At all times the total probability of a cll having a number should be 100. 
        6. If the probability of a cell containing a particular number becomes 100, add it to the queue and redo steps 2 - 6
        7. Redo steps 2 - 6 until each cell has a probability for sure.


Input type: 

Input type has been assumed to be 