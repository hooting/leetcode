public class Solution {
    class Pos{
        public int x,y;
        public Pos(int x,int y){
            this.x = x;
            this.y = y;
        }
    }
    public int numIslands(char[][] grid) {
        if(grid == null) return 0;
        int row = grid.length;
        if(row == 0 || grid[0] == null) return 0;
        int column = grid[0].length;
        if(column == 0) return 0;
        int islandNum = 0;
        for(int i = 0; i < row; i++){
            for(int j = 0; j < column; j++){
                if(grid[i][j] == '1'){
                    islandNum++;
                    disappear(i,j,grid);
                }
            }
        }
        return islandNum;
    }
    
    //Use for disapearing an island
    public void disappear(int i, int j, char[][] grid){
        //array edge detect
        if(i < 0 || i >= grid.length){
            return;
        }
        if(j < 0 || j >= grid[i].length){
            return;
        }
        //island edge detect
        if(grid[i][j] == '0'){
            return;
        }

        //disapear this cell
        grid[i][j] = '0';
        //disapear other cell in the same island
        disappear(i + 1, j, grid);
        disappear(i - 1, j, grid);
        disappear(i, j + 1, grid);
        disappear(i, j - 1, grid);
    }
}