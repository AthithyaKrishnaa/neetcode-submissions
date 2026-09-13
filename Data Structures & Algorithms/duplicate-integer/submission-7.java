class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> hs = new HashSet<>();
        for(int num: nums){
            hs.add(num);
        }
        if(nums.length!=hs.size()){
            return true;
        }else{
            return false;
        }
    }   
}