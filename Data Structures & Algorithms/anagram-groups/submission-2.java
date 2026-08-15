class Solution {
    // HashMap 
    // For each word
    // Iterate through chars
    // Store occurence in array
    // Add occurence as key
    // add word as value
    // return values

    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> map = new HashMap<>(); // all strings {(a:1, c:1, t:1) : ["act"]} return values

        for (String s : strs) {
            int[] count = new int[26];
            for (char c : s.toCharArray()) {
                count[c - 'a']++; // distance from a == order in alphabet
            }
            String key = Arrays.toString(count); // count is now string key
            map.putIfAbsent(key, new ArrayList<>()); // add key to map if absent, requires value also
            map.get(key).add(s); // get key and add current word
        }
        return new ArrayList<>(map.values()); //list instead of collection obj
    }
}
