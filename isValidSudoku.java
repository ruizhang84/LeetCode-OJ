public class Solution {
    public boolean isValidSudoku(char[][] board) {
        
        for (int i = 0; i< board.length; i++){
            HashMap row = new HashMap();
            HashMap col = new HashMap();
            for (int j = 0; j< board.length; j++){
                //row
                if (!row.containsKey(board[i][j]))
                    row.put(board[i][j], 1);
                else if(board[i][j] != '.')
                    return false;
                
                //column
                if (!col.containsKey(board[j][i]))
                    col.put(board[j][i], 1);
                else if (board[j][i] != '.')
                    return false;
            }
        }
        
        
        for (int i = 0; i < board.length/3; i++){
            for (int j = 0; j < board.length/3; j++){
                HashMap sq = new HashMap();
                
                for (int m = 0; m < 3; m++){
                    for (int n = 0; n < 3; n++){
                        if (!sq.containsKey(board[3*i+m][3*j+n]))
                            sq.put(board[3*i+m][3*j+n], 1);
                        else if (board[3*i+m][3*j+n] != '.')
                            return false;
                        
                        
                    }
                }
            }
        }
        
        return true;
        
        
        
        
        
    }
}
