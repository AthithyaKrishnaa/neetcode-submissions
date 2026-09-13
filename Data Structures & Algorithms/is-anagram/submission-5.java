class Solution {
    public boolean isAnagram(String s, String t) {
        int[] count = new int[26];
        System.out.println(Arrays.toString(count));
        for(char c:s.toCharArray()){
            count[c-97]++;
        }
        for(char c:t.toCharArray()){
            count[c-97]--;
        }
        for(int n: count){
            if(n!=0){
                return false;
            }
        }
        return true;
    }
}
