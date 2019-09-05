class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_row=[]
        max_col=[]
        for i in range(0,len(grid)):
            max_row.append(max(grid[i]))
            temp=[]
            for j in range(0,len(grid[i])):
                temp.append(grid[j][i])
            max_col.append(max(temp))

        sum=0
        for i in range(0,len(grid)):
            for j in range(0,len(grid[j])):
                val=min(max_row[i],max_col[j])
                sum=sum+(val-grid[i][j])

        return (sum)
