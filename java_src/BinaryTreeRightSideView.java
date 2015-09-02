/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> ret = new ArrayList<Integer>();
        recursivePro(root,ret,0);
        return ret;
    }
    
    public void recursivePro(TreeNode root, List<Integer> ret, int depth){
        if(root == null) return;
        if(ret.size() == depth) ret.add(root.val);
        recursivePro(root.right,ret,depth+1);
        recursivePro(root.left,ret,depth+1);
    }
}