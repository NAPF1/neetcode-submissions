class Solution {
    // HashMap {k = n in nums: v = count of n}
    // Sort nums
    // iterate n in nums, count ++ for each
    // add to map
    // reset count
    // return k number of sorted map.values()
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> map = new HashMap<>();
        Arrays.sort(nums);
        
        int count = 1;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i-1] == nums[i]) {
                count++;
            }
            else {
                map.put(nums[i-1], count);
                count = 1;
            }
        }
        map.put(nums[nums.length - 1], count);

        List<Integer> list = new ArrayList<>(map.keySet());
        list.sort((a, b) -> map.get(b) - map.get(a));

        int[] result = new int[k];
        for (int i = 0; i < k; i++) {
            result[i] = list.get(i);
        }
        return result;
    }
}
