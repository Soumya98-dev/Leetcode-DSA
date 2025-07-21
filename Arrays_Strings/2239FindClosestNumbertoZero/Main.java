/*
 * Algorithm
 * Initialize res to Integer.MAX
 * for i to nums.length
 *  take the abs value of nums[i]
 *  calc the diff with 0
 *  store in res if it is lower than the current value
 * return res
 */

public class Main {
    public static void main(String[] args) {
        // int[] nums = { -4, -2, 1, 4, 8 };
        int[] nums = { -100000, -100000 };
        System.out.println(findClosestNumber(nums));
    }

    public static int findClosestNumber(int[] nums) {
        int result = Integer.MAX_VALUE;
        int pos = -1;
        for (int i = 0; i < nums.length; i++) {
            int diff = Math.abs(nums[i]) - 0;
            if (diff < result) {
                pos = i;
                result = diff;
            } else if (diff == result) {
                if (nums[pos] < nums[i]) {
                    pos = i;
                }
            }
        }

        return nums[pos];

    }
}