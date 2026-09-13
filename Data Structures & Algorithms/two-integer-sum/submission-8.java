class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hm = new HashMap<>();

        for(int i=0; i<nums.length; i++){
            int x = target-nums[i];
            if(hm.containsKey(x)){
                return new int[]{hm.get(x),i};
            }
            hm.put(nums[i],i);
        }
        return new int[]{};
    }
}
