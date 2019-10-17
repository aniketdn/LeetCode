#  A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.
#  
#  Given an grid of integers, how many 3 x 3 "magic square" subgrids are there?  (Each subgrid is contiguous).
#  
#   
#  
#  Example 1:
#  
#  Input: [[4,3,8,4],
#          [9,5,1,9],
#          [2,7,6,2]]
#  Output: 1
#  Explanation: 
#  The following subgrid is a 3 x 3 magic square:
#  438
#  951
#  276
#  
#  while this one is not:
#  384
#  519
#  762
#  
#  In total, there is only one magic square inside the given grid.





class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        final=0
        flag=1
        for i in range(0,len(grid)-2):
            for j in range(0,len(grid[i])-2):
                if(grid[i][j]!=5):
                    flag=1
                    for r in range(0,3):
                        for c in range(0,3):
                            if(1<=grid[i+r][j+c]<=9):
                                continue
                            else:
                                flag=-99
                                break
                    if flag!=-99:
                        if(grid[i][j]+grid[i][j+1]+grid[i][j+2]==15):
                            if(grid[i+1][j]+grid[i+1][j+1]+grid[i+1][j+2]==15):
                                if(grid[i+2][j]+grid[i+2][j+1]+grid[i+2][j+2]==15):
                                    if(grid[i][j]+grid[i+1][j]+grid[i+2][j]==15):
                                        if(grid[i][j+1]+grid[i+1][j+1]+grid[i+2][j+1]==15):
                                            if(grid[i][j+2]+grid[i+1][j+2]+grid[i+2][j+2]==15):
                                                if(grid[i][j]+grid[i+1][j+1]+grid[i+2][j+2]==15):
                                                    if(grid[i][j+2]+grid[i+1][j+1]+grid[i+2][j]==15):
                                                        final=final+1
        return final
