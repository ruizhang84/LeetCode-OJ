public class Solution {
    public void solveSudoku(char[][] board) {
        ArrayList<Set<Integer>> row = new ArrayList<Set<Integer>>();
        ArrayList<Set<Integer>> col = new ArrayList<Set<Integer>>();
        ArrayList<Set<Integer>> sub = new ArrayList<Set<Integer>>();
        ArrayList<Integer> unfill = new ArrayList<Integer>();      //i and j "."
        
        int idx = 0;
        for (int i = 0; i < 9; i++){
            Set<Integer> temp_row = new HashSet<Integer>();
            Set<Integer> temp_col = new HashSet<Integer>();
            //add 1-9
            for (int j = 1; j < 10; j++){
                temp_row.add(j);
                temp_col.add(j);
            }
            //remove exist, and add '.' position
            for (int j = 0; j < 9; j++){
                if(board[i][j] != '.'){
                    temp_row.remove(board[i][j] - '0');
                }else{
                    unfill.add(i);  //initial guess
                    unfill.add(j);
                    unfill.add(0);
                    idx++;
                }
                if(board[j][i] != '.')
                    temp_col.remove(board[j][i] - '0');
            }
            //System.out.print(temp_row);
            //System.out.print(temp_col);
            row.add(temp_row);
            col.add(temp_col);
        }
        
        // sub matrix
        for(int i = 0; i<9; i+= 3){
            for(int j = 0; j<9; j+= 3){
                Set<Integer> temp_sub = new HashSet<Integer>();
                //add 1-9
                for(int k = 1; k<10; k++)
                    temp_sub.add(k);
                //remove exist
                for(int k = 0; k<9; k++){
                    if(board[i + k/3][ j + k%3] != '.')
                        temp_sub.remove(board[i + k/3][ j + k%3] - '0');
                }
                //System.out.println(temp_sub);
                sub.add(temp_sub);
            }
        }
        
        //DFS fill out '.'
        while (idx > 0){
            idx--;
            int i = unfill.get(idx*3);
            int j = unfill.get(idx*3+1);
            int k = unfill.get(idx*3+2);
            
            //restore k
            if (k != 0){
                row.get(i).add(k);
                col.get(j).add(k);
                sub.get(i/3*3+j/3).add(k);
            }
            
            //try to set choice next avail k
            int update = 0;
            for (int l = k+1; l < 10; l++){
                if (row.get(i).contains(l)
                    && col.get(j).contains(l)
                    && sub.get(i/3*3+j/3).contains(l) ){
                    board[i][j] = (char) (l + 48);
                    
                    row.get(i).remove(l);
                    col.get(j).remove(l);
                    sub.get(i/3*3+j/3).remove(l);
                    
                    unfill.set(idx*3+2, l);
                    update = 1;
                    break;
                }
            }
            
            
            //backtrack
            if (update == 0){
                unfill.set(idx*3+2, 0);
                board[i][j] = '.';
                idx += 2;
            }
            
        }
        
        
        
        
        
        
        
        
        
    }
}
